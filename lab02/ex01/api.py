from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.Playfair import PlayfairCipher
from cipher.Transposition import TranspositionCipher

app = Flask(__name__)

# ====================== CIPHER INSTANCES ======================
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
railfence_cipher = RailFenceCipher()
playfair_cipher = PlayfairCipher()
transposition_cipher = TranspositionCipher()


# ====================== CAESAR CIPHER ENDPOINTS ======================
@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])

    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})


@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])

    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

# ====================== VIGENERE CIPHER ENDPOINTS ======================
@app.route("/api/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    """
    Encrypt text using Vigenere cipher
    Request body:
    {
        "plain_text": "text to encrypt",
        "key": "keyword"
    }
    """
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})


@app.route("/api/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    """
    Decrypt text using Vigenere cipher
    Request body:
    {
        "cipher_text": "text to decrypt",
        "key": "keyword"
    }
    """
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# ====================== RAIL FENCE CIPHER ENDPOINTS ======================
@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    """
    Encrypt text using Rail Fence cipher
    Request body:
    {
        "plain_text": "text to encrypt",
        "key": number_of_rails (integer)
    }
    """
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])

    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/railfence/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])

    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)

    return jsonify({'decrypted_text': decrypted_text})

# ====================== PLAYFAIR CIPHER ENDPOINTS ======================
@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    """
    Create Playfair cipher matrix
    Request body:
    {
        "key": "keyword"
    }
    """
    data = request.json
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({"playfair_matrix": playfair_matrix})

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    """
    Encrypt text using Playfair cipher
    Request body:
    {
        "plain_text": "text to encrypt",
        "key": "keyword"
    }
    """
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, playfair_matrix)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    """
    Decrypt text using Playfair cipher
    Request body:
    {
        "cipher_text": "text to decrypt",
        "key": "keyword"
    }
    """
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, playfair_matrix)
    return jsonify({'decrypted_text': decrypted_text})

# ====================== TRANSPOSITION CIPHER ENDPOINTS ======================
@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    """
    Encrypt text using Transposition cipher
    Request body:
    {
        "plain_text": "text to encrypt",
        "key": number_of_columns (integer)
    }
    """
    data = request.get_json()
    plain_text = data.get('plain_text')
    key = int(data.get('key'))
    encrypted_text = transposition_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    """
    Decrypt text using Transposition cipher
    Request body:
    {
        "cipher_text": "text to decrypt",
        "key": number_of_columns (integer)
    }
    """
    data = request.get_json()
    cipher_text = data.get('cipher_text')
    key = int(data.get('key'))
    decrypted_text = transposition_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# ====================== MAIN ======================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
