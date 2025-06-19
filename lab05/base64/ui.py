import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import base64
import os

# --- Phần logic xử lý mã hóa và giải mã (từ file của bạn) ---

def encrypt_data(input_string):
    """Mã hóa một chuỗi sử dụng Base64 và ghi vào file."""
    try:
        encoded_bytes = base64.b64encode(input_string.encode("utf-8"))
        encoded_string = encoded_bytes.decode("utf-8")
        with open("data.txt", "w") as file:
            file.write(encoded_string)
        return encoded_string, None
    except Exception as e:
        return None, str(e)

def decrypt_data():
    """Đọc file data.txt và giải mã chuỗi Base64."""
    try:
        if not os.path.exists("data.txt"):
            return None, "Tệp 'data.txt' không tồn tại. Vui lòng mã hóa trước."
            
        with open("data.txt", "r") as file:
            encoded_string = file.read().strip()
        
        if not encoded_string:
             return None, "Tệp 'data.txt' trống rỗng."

        decoded_bytes = base64.b64decode(encoded_string)
        decoded_string = decoded_bytes.decode("utf-8")
        return decoded_string, None
    except Exception as e:
        return None, f"Lỗi giải mã: {e}"

# --- Phần giao diện người dùng (UI) ---

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Công cụ Mã hóa & Giải mã Base64")
        self.geometry("600x450")
        self.resizable(False, False)

        # Cấu hình grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # Style
        style = ttk.Style(self)
        style.configure("TLabel", font=("Helvetica", 11))
        style.configure("TButton", font=("Helvetica", 11, "bold"))
        style.configure("TEntry", font=("Helvetica", 11))

        self.create_widgets()

    def create_widgets(self):
        # --- Khung nhập liệu ---
        input_frame = ttk.Frame(self, padding="10")
        input_frame.grid(row=0, column=0, columnspan=2, sticky="ew")
        input_frame.columnconfigure(0, weight=1)

        ttk.Label(input_frame, text="Nhập thông tin cần mã hóa:").grid(row=0, column=0, sticky="w")
        
        self.entry_input = ttk.Entry(input_frame, width=80)
        self.entry_input.grid(row=1, column=0, sticky="ew", pady=5)

        # --- Khung các nút chức năng ---
        button_frame = ttk.Frame(self, padding="10")
        button_frame.grid(row=1, column=0, columnspan=2)

        self.encrypt_button = ttk.Button(button_frame, text="Mã hóa và Lưu", command=self.run_encrypt)
        self.encrypt_button.pack(side="left", padx=10)

        self.decrypt_button = ttk.Button(button_frame, text="Đọc và Giải mã", command=self.run_decrypt)
        self.decrypt_button.pack(side="left", padx=10)
        
        self.clear_button = ttk.Button(button_frame, text="Xóa", command=self.clear_fields)
        self.clear_button.pack(side="left", padx=10)

        # --- Khung hiển thị kết quả ---
        result_frame = ttk.Frame(self, padding="10")
        result_frame.grid(row=2, column=0, columnspan=2, sticky="nsew")
        result_frame.columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1) # Cho phép khung này mở rộng

        ttk.Label(result_frame, text="Kết quả (đã mã hóa):").grid(row=0, column=0, sticky="w")
        self.text_encrypted = tk.Text(result_frame, height=5, state="disabled", background="#f0f0f0")
        self.text_encrypted.grid(row=1, column=0, sticky="ew", pady=5)

        ttk.Label(result_frame, text="Kết quả (đã giải mã):").grid(row=2, column=0, sticky="w", pady=(10, 0))
        self.text_decrypted = tk.Text(result_frame, height=5, state="disabled", background="#f0f0f0")
        self.text_decrypted.grid(row=3, column=0, sticky="ew", pady=5)

    def set_text_widget(self, widget, text):
        """Hàm helper để cập nhật nội dung cho Text widget."""
        widget.config(state="normal")
        widget.delete("1.0", tk.END)
        widget.insert("1.0", text)
        widget.config(state="disabled")

    def run_encrypt(self):
        input_string = self.entry_input.get()
        if not input_string:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập thông tin cần mã hóa.")
            return
        
        encoded_string, error = encrypt_data(input_string)
        
        if error:
            messagebox.showerror("Lỗi", f"Lỗi khi mã hóa: {error}")
        else:
            self.set_text_widget(self.text_encrypted, encoded_string)
            self.set_text_widget(self.text_decrypted, "") # Xóa kết quả giải mã cũ
            messagebox.showinfo("Thành công", "Đã mã hóa thành công và ghi vào tệp data.txt")

    def run_decrypt(self):
        decoded_string, error = decrypt_data()

        if error:
            messagebox.showerror("Lỗi", error)
            self.set_text_widget(self.text_decrypted, "")
        else:
            self.set_text_widget(self.text_decrypted, decoded_string)
            # Bạn cũng có thể hiển thị nội dung được mã hóa từ file
            with open("data.txt", "r") as file:
                encoded_content = file.read().strip()
                self.set_text_widget(self.text_encrypted, encoded_content)


    def clear_fields(self):
        """Xóa tất cả các trường nhập liệu và kết quả."""
        self.entry_input.delete(0, tk.END)
        self.set_text_widget(self.text_encrypted, "")
        self.set_text_widget(self.text_decrypted, "")


if __name__ == "__main__":
    app = App()
    app.mainloop()