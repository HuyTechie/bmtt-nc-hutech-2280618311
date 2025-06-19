import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from PIL import Image
import os

# --- LỚP CHÍNH CỦA ỨNG DỤNG GIAO DIỆN ---
class SteganographyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Công cụ giấu tin trong ảnh (Steganography)")
        self.geometry("700x500")

        # Tạo các tab (Mã hóa, Giải mã)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, padx=10, fill="both", expand=True)

        # Frame cho mỗi tab
        self.encode_frame = ttk.Frame(self.notebook, padding="10")
        self.decode_frame = ttk.Frame(self.notebook, padding="10")

        self.notebook.add(self.encode_frame, text="Mã hóa (Giấu tin)")
        self.notebook.add(self.decode_frame, text="Giải mã (Lấy tin)")

        # Các biến lưu đường dẫn file
        self.source_image_path = tk.StringVar()
        self.encoded_image_path = tk.StringVar()

        # Tạo các thành phần trên từng tab
        self.create_encode_widgets()
        self.create_decode_widgets()

    # --- TAB MÃ HÓA ---
    def create_encode_widgets(self):
        # --- Chọn ảnh gốc ---
        ttk.Label(self.encode_frame, text="Bước 1: Chọn ảnh gốc").grid(row=0, column=0, columnspan=2, sticky="w")
        ttk.Button(self.encode_frame, text="Duyệt file...", command=self.select_source_image).grid(row=1, column=0, sticky="w", pady=5)
        ttk.Label(self.encode_frame, textvariable=self.source_image_path, foreground="blue").grid(row=1, column=1, sticky="w", padx=5)

        # --- Nhập thông điệp ---
        ttk.Label(self.encode_frame, text="Bước 2: Nhập thông điệp cần giấu").grid(row=2, column=0, columnspan=2, sticky="w", pady=(10, 0))
        self.message_text = scrolledtext.ScrolledText(self.encode_frame, height=8, wrap="word")
        self.message_text.grid(row=3, column=0, columnspan=2, sticky="ew", pady=5)
        
        # --- Đặt tên file output ---
        ttk.Label(self.encode_frame, text="Bước 3: Đặt tên file ảnh đầu ra").grid(row=4, column=0, sticky="w", pady=(10,0))
        self.output_filename_entry = ttk.Entry(self.encode_frame)
        self.output_filename_entry.insert(0, "encoded_image.png")
        self.output_filename_entry.grid(row=5, column=0, columnspan=2, sticky="ew", pady=5)

        # --- Nút thực thi ---
        ttk.Button(self.encode_frame, text="Bắt đầu mã hóa", command=self.run_encode, style="Accent.TButton").grid(row=6, column=0, columnspan=2, pady=20)
        
        self.encode_status_label = ttk.Label(self.encode_frame, text="")
        self.encode_status_label.grid(row=7, column=0, columnspan=2)

        # Cấu hình cho grid co giãn
        self.encode_frame.columnconfigure(1, weight=1)

    # --- TAB GIẢI MÃ ---
    def create_decode_widgets(self):
        # --- Chọn ảnh đã mã hóa ---
        ttk.Label(self.decode_frame, text="Bước 1: Chọn ảnh đã được giấu tin").grid(row=0, column=0, columnspan=2, sticky="w")
        ttk.Button(self.decode_frame, text="Duyệt file...", command=self.select_encoded_image).grid(row=1, column=0, sticky="w", pady=5)
        ttk.Label(self.decode_frame, textvariable=self.encoded_image_path, foreground="blue").grid(row=1, column=1, sticky="w", padx=5)
        
        # --- Nút thực thi ---
        ttk.Button(self.decode_frame, text="Bắt đầu giải mã", command=self.run_decode, style="Accent.TButton").grid(row=2, column=0, columnspan=2, pady=20)

        # --- Hiển thị kết quả ---
        ttk.Label(self.decode_frame, text="Thông điệp được giải mã:").grid(row=3, column=0, columnspan=2, sticky="w", pady=(10, 0))
        self.decoded_message_text = scrolledtext.ScrolledText(self.decode_frame, height=10, wrap="word", state="disabled")
        self.decoded_message_text.grid(row=4, column=0, columnspan=2, sticky="ew", pady=5)
        
        self.decode_status_label = ttk.Label(self.decode_frame, text="")
        self.decode_status_label.grid(row=5, column=0, columnspan=2)
        
        # Cấu hình cho grid co giãn
        self.decode_frame.columnconfigure(1, weight=1)


    # --- CÁC HÀM XỬ LÝ SỰ KIỆN VÀ LOGIC ---
    def select_source_image(self):
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.bmp"), ("All files", "*.*")])
        if path:
            self.source_image_path.set(os.path.basename(path))
            self._full_source_path = path

    def select_encoded_image(self):
        path = filedialog.askopenfilename(filetypes=[("Encoded PNG", "*.png"), ("All files", "*.*")])
        if path:
            self.encoded_image_path.set(os.path.basename(path))
            self._full_encoded_path = path

    def run_encode(self):
        if not hasattr(self, '_full_source_path'):
            messagebox.showwarning("Thiếu thông tin", "Vui lòng chọn ảnh gốc.")
            return

        message = self.message_text.get("1.0", tk.END).strip()
        if not message:
            messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập thông điệp cần giấu.")
            return
            
        output_filename = self.output_filename_entry.get().strip()
        if not output_filename:
            messagebox.showwarning("Thiếu thông tin", "Vui lòng đặt tên cho file ảnh đầu ra.")
            return

        try:
            self.encode_status_label.config(text="Đang xử lý, vui lòng chờ...", foreground="orange")
            self.update_idletasks() # Cập nhật giao diện
            
            self.encode_image(self._full_source_path, message, output_filename)
            
            self.encode_status_label.config(text="") # Xóa status
            messagebox.showinfo("Thành công", f"Đã giấu tin thành công!\nẢnh đã được lưu với tên: {output_filename}")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Đã xảy ra lỗi trong quá trình mã hóa: {e}")
        finally:
            self.encode_status_label.config(text="")
            
    def run_decode(self):
        if not hasattr(self, '_full_encoded_path'):
            messagebox.showwarning("Thiếu thông tin", "Vui lòng chọn ảnh đã mã hóa.")
            return
            
        try:
            self.decode_status_label.config(text="Đang giải mã, vui lòng chờ...", foreground="orange")
            self.update_idletasks() # Cập nhật giao diện
            
            decoded_message = self.decode_image(self._full_encoded_path)
            
            self.decoded_message_text.config(state="normal")
            self.decoded_message_text.delete("1.0", tk.END)
            self.decoded_message_text.insert("1.0", decoded_message)
            self.decoded_message_text.config(state="disabled")

            messagebox.showinfo("Hoàn tất", "Đã giải mã xong. Kết quả được hiển thị bên dưới.")

        except Exception as e:
            messagebox.showerror("Lỗi", f"Đã xảy ra lỗi trong quá trình giải mã: {e}")
        finally:
            self.decode_status_label.config(text="")

    # --- LOGIC STEGANOGRAPHY (ĐÃ SỬA LỖI) ---
    def encode_image(self, image_path, message, output_filename):
        img = Image.open(image_path).convert('RGB')
        
        # Thêm ký tự null để đánh dấu kết thúc thông điệp
        binary_message = ''.join(format(ord(char), '08b') for char in message)
        binary_message += '00000000' 
        
        if len(binary_message) > img.width * img.height * 3:
            raise ValueError("Thông điệp quá dài để giấu trong ảnh này.")

        data_index = 0
        pixels = list(img.getdata())
        new_pixels = []

        for pixel in pixels:
            new_pixel = list(pixel)
            for color_channel in range(3):
                if data_index < len(binary_message):
                    # Thay đổi bit cuối cùng (LSB) của kênh màu
                    new_pixel[color_channel] = pixel[color_channel] & ~1 | int(binary_message[data_index])
                    data_index += 1
            new_pixels.append(tuple(new_pixel))

        new_img = Image.new(img.mode, img.size)
        new_img.putdata(new_pixels)
        new_img.save(output_filename, 'PNG')


    def decode_image(self, encoded_image_path):
        img = Image.open(encoded_image_path)
        binary_message = ""
        
        pixels = img.getdata()
        for pixel in pixels:
            for color_channel in range(3):
                binary_message += str(pixel[color_channel] & 1)

        message = ""
        for i in range(0, len(binary_message), 8):
            byte = binary_message[i:i+8]
            if byte == '00000000':  # Dừng khi gặp ký tự null
                break
            try:
                message += chr(int(byte, 2))
            except ValueError:
                # Bỏ qua byte không hợp lệ có thể xuất hiện ở cuối
                pass
        
        return message

if __name__ == "__main__":
    app = SteganographyApp()
    # Thêm style cho nút bấm
    style = ttk.Style(app)
    style.configure("Accent.TButton", foreground="white", background="dodgerblue", font=('Helvetica', 10, 'bold'))
    app.mainloop()