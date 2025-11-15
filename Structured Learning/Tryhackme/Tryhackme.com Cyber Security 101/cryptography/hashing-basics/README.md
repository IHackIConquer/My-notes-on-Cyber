---
description: >-
  Hash function takes data of any size and creates a fixed sized summary/digest
  of that data.
---

# Hashing Basics

Any slight change in the input data will completely change the output. Even the change of one letter

[https://pypi.org/project/hashID/](https://pypi.org/project/hashID/) Identify the different types of hashes used to encrypt data and especially passwords.

The output of a hash function is typically raw bytes, which are then encoded. Common encodings are base64 or hexadecimal. `md5sum`, `sha1sum`, `sha256sum`, and `sha512sum` produce their outputs in hexadecimal format. Remember that hexadecimal format prints each raw byte as two hexadecimal digits.

## Hash Collision

Hash collision is when 2 different inputs give the same output. Hash functions are designed to avoid this problem and from exploitation. MD5 and SHA1 are considered insecure due to the ability to engineer hash collision .

Hash Collision how to:&#x20;

MD5 collision example: [https://www.mscs.dal.ca/\~selinger/md5collision/](https://www.mscs.dal.ca/~selinger/md5collision/)&#x20;

SHA1 example: [https://shattered.io/](https://shattered.io/)







