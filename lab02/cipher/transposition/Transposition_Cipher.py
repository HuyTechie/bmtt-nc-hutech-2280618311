class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        encrypted_text = ""
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text

    def decrypt(self, text, key):
        # Xác định số hàng cần thiết
        num_rows = len(text) // key
        if len(text) % key:
            num_rows += 1  # Nếu không chia hết, cần thêm một hàng

        # Khởi tạo lưới rỗng
        grid = [''] * num_rows

        # Xác định vị trí từng ký tự trên lưới
        index = 0
        for col in range(key):
            row = 0
            while row < num_rows and index < len(text):
                grid[row] += text[index]
                index += 1
                row += 1

        # Ghép các hàng lại để tạo văn bản giải mã
        decrypted_text = ''.join(grid)
        return decrypted_text
