import hashlib

def calculate_md5(input_string):
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode('utf-8'))
    return md5_hash.hexdigest()

input_string = input("Enter a string to hash: ")
md5_hash = calculate_md5(input_string)  

print(f"MD5 hash of '{input_string}' is: {md5_hash}")   