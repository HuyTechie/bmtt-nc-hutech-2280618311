from flask import Flask, render_template, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.playfair import PlayfairCipher
from cipher.railfence import RailFenceCipher
from cipher.transposition import TranspositionCipher
from cipher.vigenere import VigenereCipher

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')



@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/caesar/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    caesar_cipher = CaesarCipher()

    encrypted_text = caesar_cipher.encrypt_text(text, key)
    return f"encrypted text: {encrypted_text}"

@app.route("/caesar/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    caesar_cipher = CaesarCipher()

    decrypted_text = caesar_cipher.decrypt_text(text, key)
    return f"decrypted text: {decrypted_text}"



@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    playfair_cipher = PlayfairCipher()
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)

    encrypted_text = playfair_cipher.playfair_encrypt(text, playfair_matrix)
    return f"encrypted text: {encrypted_text}"

@app.route("/playfair/decrypt", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    playfair_cipher = PlayfairCipher()
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(text, playfair_matrix)
    return f"decrypted text: {decrypted_text}"



@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    railfence_cipher = RailFenceCipher()

    encrypted_text = railfence_cipher.rail_fence_encrypt(text, key)
    return f"encrypted text: {encrypted_text}"

@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    railfence_cipher = RailFenceCipher()

    decrypted_text = railfence_cipher.rail_fence_decrypt(text, key)
    return f"decrypted text: {decrypted_text}"



@app.route("/transposition")
def transposition():
    return render_template('transposition.html')

@app.route("/transposition/encrypt", methods=['POST'])
def transposition_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    transposition_cipher = TranspositionCipher()

    encrypted_text = transposition_cipher.encrypt(text, key)
    return f"encrypted text: {encrypted_text}"

@app.route("/transposition/decrypt", methods=['POST'])
def transposition_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    transposition_cipher = TranspositionCipher()

    decrypted_text = transposition_cipher.decrypt(text, key)
    return f"decrypted text: {decrypted_text}"


@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    vigenere_cipher = VigenereCipher()

    encrypted_text = vigenere_cipher.vigenere_encrypt(text, key)
    return f"encrypted text: {encrypted_text}"

@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    vigenere_cipher = VigenereCipher()

    decrypted_text = vigenere_cipher.vigenere_decrypt(text, key)
    return f"decrypted text: {decrypted_text}"

# Main function to run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
