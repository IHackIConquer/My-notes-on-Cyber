# Using Hashing for Secure Password Storage

What if **2 users have the same password**? The hash will produce the **same output** and threat actor could use that to their advantage by only cracking 1 hash, gaining access to more than 1 account. It also means someone could create a **Rainbow Table** to break the hashes

Rainbow Table is lookup table of hashes to plaintexts&#x20;

| Hash                             | Password       |
| -------------------------------- | -------------- |
| 02c75fb22c75b23dc963c7eb91a062cc | zxcvbnm        |
| b0baee9d279d34fa1dfd71aadb908c3f | 11111          |
| c44a471bd78cc6c2fea32b9fe028d30a | asdfghjkl      |
| d0199f51d2728db6011945145a1b607a | basketball     |
| dcddb75469b4b4875094e14561e573d8 | 000000         |
| e10adc3949ba59abbe56e057f20f883e | 123456         |
| e19d5cd5af0378da05f63f891c7467af | abcd1234       |
| e99a18c428cb38d5f260853678922e03 | abc123         |
| fcea920f7412b5da7be0cf42b8c93759 | 1234567        |
| 4c5923b6a6fac7b7355f53bfe2b8f8c1 | inS3CyourP4\$$ |

Websites like [**CrackStation**](https://crackstation.net/) and [**Hashes.com**](https://hashes.com/en/decrypt/hash) internally use massive rainbow tables to provide fast password cracking for **hashes without salts**. Doing a lookup in a sorted list of hashes is quicker than trying to crack the hash.

## Protecting Against Rainbow Tables with salt

Salt is added to the start or the end of the password and this means no password will be the same

Hash functions like Bcrypt and Scrypt handle this automatically. Salts don’t need to be kept private.

## Example of Securely Storing Passwords

1. We select a secure hashing function, such as Argon2, Scrypt, Bcrypt, or PBKDF2.
2. We add a unique salt to the password, such as `Y4UV*^(=go_!`
3. Concatenate the password with the unique salt. For example, if the password is `AL4RMc10k`, the result string would be `AL4RMc10kY4UV*^(=go_!`
4. Calculate the hash value of the combined password and salt. In this example, using the chosen algorithm, you need to calculate the hash value of `AL4RMc10kY4UV*^(=go_!`.
5. Store the hash value and the unique salt used (`Y4UV*^(=go_!`).
