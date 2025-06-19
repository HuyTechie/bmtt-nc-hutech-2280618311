import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import json
from blockchain import Blockchain

# --- Giao diện người dùng ---

class BlockchainApp(tk.Tk):
    def __init__(self, blockchain):
        super().__init__()
        self.blockchain = blockchain
        self.miner_address = "Miner_Node_1"  # Địa chỉ ví của thợ mỏ

        self.title("Trình khám phá Blockchain")
        self.geometry("1100x700")

        # --- Cấu trúc giao diện ---
        main_frame = ttk.Frame(self, padding="10")
        main_frame.pack(fill="both", expand=True)

        # Chia giao diện thành 2 phần chính (trái và phải)
        pane = ttk.PanedWindow(main_frame, orient="horizontal")
        pane.pack(fill="both", expand=True)

        # Phần bên trái: Bảng điều khiển (thêm giao dịch, mine,...)
        controls_frame = ttk.Frame(pane, width=350, height=600)
        pane.add(controls_frame, weight=1)

        # Phần bên phải: Hiển thị chuỗi khối
        chain_frame = ttk.Frame(pane, width=750, height=600)
        pane.add(chain_frame, weight=3)

        # --- Xây dựng các thành phần con ---
        self.create_controls_widgets(controls_frame)
        self.create_chain_widgets(chain_frame)

        # Cập nhật giao diện lần đầu
        self.update_chain_display()

    def create_controls_widgets(self, parent):
        """Tạo các widget cho khung điều khiển bên trái."""
        # --- Khung thêm giao dịch ---
        tx_frame = ttk.LabelFrame(parent, text="Thêm giao dịch mới", padding="10")
        tx_frame.pack(fill="x", padx=5, pady=5)

        ttk.Label(tx_frame, text="Người gửi:").grid(row=0, column=0, sticky="w", padx=5, pady=2)
        self.sender_entry = ttk.Entry(tx_frame)
        self.sender_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=2)

        ttk.Label(tx_frame, text="Người nhận:").grid(row=1, column=0, sticky="w", padx=5, pady=2)
        self.receiver_entry = ttk.Entry(tx_frame)
        self.receiver_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=2)

        ttk.Label(tx_frame, text="Số lượng:").grid(row=2, column=0, sticky="w", padx=5, pady=2)
        self.amount_entry = ttk.Entry(tx_frame)
        self.amount_entry.grid(row=2, column=1, sticky="ew", padx=5, pady=2)
        
        tx_frame.columnconfigure(1, weight=1)

        add_tx_button = ttk.Button(tx_frame, text="Thêm vào danh sách chờ", command=self.add_transaction_ui)
        add_tx_button.grid(row=3, column=0, columnspan=2, pady=10)

        # --- Khung các giao dịch đang chờ ---
        pending_tx_frame = ttk.LabelFrame(parent, text="Các giao dịch đang chờ được khai thác", padding="10")
        pending_tx_frame.pack(fill="both", expand=True, padx=5, pady=5)

        self.pending_tx_text = scrolledtext.ScrolledText(pending_tx_frame, height=10, state="disabled")
        self.pending_tx_text.pack(fill="both", expand=True)

        # --- Khung hành động ---
        action_frame = ttk.LabelFrame(parent, text="Hành động", padding="10")
        action_frame.pack(fill="x", padx=5, pady=5)

        mine_button = ttk.Button(action_frame, text="Khai thác khối mới (Mine)", command=self.mine_block_ui)
        mine_button.pack(fill="x", pady=5)

        validate_button = ttk.Button(action_frame, text="Kiểm tra tính hợp lệ của chuỗi", command=self.validate_chain_ui)
        validate_button.pack(fill="x", pady=5)
        
        self.status_label = ttk.Label(parent, text="Sẵn sàng", font=("Helvetica", 10, "italic"))
        self.status_label.pack(side="bottom", fill="x", padx=5, pady=5)


    def create_chain_widgets(self, parent):
        """Tạo widget hiển thị chuỗi khối bên phải."""
        chain_display_frame = ttk.LabelFrame(parent, text="Toàn bộ chuỗi khối (Blockchain)", padding="10")
        chain_display_frame.pack(fill="both", expand=True, padx=5, pady=5)

        self.chain_text = scrolledtext.ScrolledText(chain_display_frame, wrap="word", state="disabled")
        self.chain_text.pack(fill="both", expand=True)

    def add_transaction_ui(self):
        """Xử lý sự kiện nhấn nút thêm giao dịch."""
        sender = self.sender_entry.get()
        receiver = self.receiver_entry.get()
        amount = self.amount_entry.get()

        if not sender or not receiver or not amount:
            messagebox.showwarning("Thiếu thông tin", "Vui lòng điền đầy đủ thông tin giao dịch.")
            return
        
        try:
            amount_val = float(amount)
        except ValueError:
            messagebox.showerror("Lỗi dữ liệu", "Số lượng phải là một con số.")
            return

        self.blockchain.add_transaction(sender, receiver, amount_val)
        self.update_pending_tx_display()
        
        # Xóa các trường nhập
        self.sender_entry.delete(0, tk.END)
        self.receiver_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        
        self.status_label.config(text=f"Đã thêm giao dịch: {sender} -> {receiver}")

    def mine_block_ui(self):
        """Xử lý sự kiện nhấn nút khai thác."""
        self.status_label.config(text="Đang khai thác khối mới... Vui lòng chờ.")
        self.update() # Cập nhật giao diện ngay lập tức

        previous_block = self.blockchain.get_previous_block()
        previous_proof = previous_block.proof
        
        # Thêm giao dịch thưởng cho thợ mỏ
        self.blockchain.add_transaction(sender="network", receiver=self.miner_address, amount=1.0)
        
        # Bắt đầu quá trình khai thác (Proof of Work)
        new_proof = self.blockchain.proof_of_work(previous_proof)
        previous_hash = previous_block.hash
        
        # Tạo khối mới
        new_block = self.blockchain.create_block(new_proof, previous_hash)
        
        self.update_chain_display()
        self.update_pending_tx_display()
        
        self.status_label.config(text="Sẵn sàng")
        messagebox.showinfo("Khai thác thành công!", f"Một khối mới #{new_block.index} đã được thêm vào chuỗi!")

    def validate_chain_ui(self):
        """Xử lý sự kiện nhấn nút kiểm tra chuỗi."""
        is_valid = self.blockchain.is_chain_valid(self.blockchain.chain)
        if is_valid:
            messagebox.showinfo("Kết quả", "Chuỗi khối hợp lệ.")
            self.status_label.config(text="Kiểm tra hoàn tất: Chuỗi hợp lệ.")
        else:
            messagebox.showerror("Kết quả", "CẢNH BÁO: Chuỗi khối không hợp lệ!")
            self.status_label.config(text="Kiểm tra hoàn tất: Chuỗi KHÔNG hợp lệ!")

    def update_chain_display(self):
        """Cập nhật toàn bộ chuỗi khối lên giao diện."""
        self.chain_text.config(state="normal")
        self.chain_text.delete("1.0", tk.END)
        
        display_text = ""
        for block in self.blockchain.chain:
            display_text += "="*30 + f" Khối #{block.index} " + "="*30 + "\n"
            block_dict = {
                "Timestamp": block.timestamp,
                "Transactions": block.transactions,
                "Proof": block.proof,
                "Previous Hash": block.previous_hash,
                "Hash": block.hash
            }
            # Dùng json.dumps để định dạng đẹp hơn
            display_text += json.dumps(block_dict, indent=4)
            display_text += "\n\n"
        
        self.chain_text.insert("1.0", display_text)
        self.chain_text.config(state="disabled")

    def update_pending_tx_display(self):
        """Cập nhật các giao dịch đang chờ."""
        self.pending_tx_text.config(state="normal")
        self.pending_tx_text.delete("1.0", tk.END)
        if not self.blockchain.current_transactions:
            self.pending_tx_text.insert("1.0", "Không có giao dịch nào đang chờ.")
        else:
            tx_text = json.dumps(self.blockchain.current_transactions, indent=4)
            self.pending_tx_text.insert("1.0", tx_text)
        self.pending_tx_text.config(state="disabled")


if __name__ == "__main__":
    # Khởi tạo blockchain
    my_blockchain = Blockchain()
    
    # Khởi tạo và chạy ứng dụng UI
    app = BlockchainApp(my_blockchain)
    app.mainloop()