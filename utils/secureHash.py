from Crypto.Hash import SHA256

def encodeHash(text):
    hash_object = SHA256.new()
    hash_object.update(text.encode('utf-8'))
    return hash_object.hexdigest()

