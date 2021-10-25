
import hashlib


s2 = hashlib.sha1(b'Hello, World').hexdigest()


s1 = hashlib.sha1(b'Hello, World').hexdigest()


print(s1==s2)




