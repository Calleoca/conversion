import hashlib
import base64

word = raw_input("Please insert something here to encode: ")

ascii = ' '.join(str(ord(letter)) for letter in word)

print "ASCII: ", ascii
print "Hex: ", "word".encode("hex")
print "Base64: ", base64.b64encode(word)
print "MD5: ", hashlib.md5(word).hexdigest()
print "SHA-1: ", hashlib.sha1(word).hexdigest()
print "SHA-224: ", hashlib.sha224(word).hexdigest()
print "SHA-256: ", hashlib.sha256(word).hexdigest()
print "SHA-384: ", hashlib.sha384(word).hexdigest()
print "SHA-512: ", hashlib.sha512(word).hexdigest()
