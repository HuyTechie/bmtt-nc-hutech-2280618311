from .alphabet import ALPHABET

class CaesarCipher:
    def __init__(self, shift: int):
        """
        Initialize Caesar cipher with a shift value.
        
        Args:
            shift (int): The number of positions to shift each character
        """
        self.shift = shift
        self.alphabet = ALPHABET
        
    def encrypt(self, text: str) -> str:
        """
        Encrypt the given text using Caesar cipher.
        
        Args:
            text (str): The text to encrypt
            
        Returns:
            str: The encrypted text
        """
        result = []
        for char in text.upper():
            if char in self.alphabet:
                # Get position of character in alphabet
                pos = self.alphabet.index(char)
                # Shift position and wrap around if needed
                new_pos = (pos + self.shift) % len(self.alphabet)
                # Get new character
                result.append(self.alphabet[new_pos])
            else:
                # Keep non-alphabetic characters unchanged
                result.append(char)
        return ''.join(result)
    
    def decrypt(self, text: str) -> str:
        """
        Decrypt the given text using Caesar cipher.
        
        Args:
            text (str): The text to decrypt
            
        Returns:
            str: The decrypted text
        """
        # Decryption is just encryption with negative shift
        return self.encrypt(text, -self.shift) 