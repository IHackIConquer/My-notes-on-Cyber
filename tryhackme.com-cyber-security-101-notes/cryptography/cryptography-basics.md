---
description: >-
  The practice and study of techniques for secure communication and data
  protection where we expect the presence of adversaries and third parties
---

# Cryptography Basics

[https://tryhackme.com/r/room/cryptographybasics](https://tryhackme.com/r/room/cryptographybasics)

[https://gchq.github.io/CyberChef/](https://gchq.github.io/CyberChef/) to decode anything

[https://cryptii.com/](https://cryptii.com/) To decode anything else

<figure><img src="../../.gitbook/assets/5f04259cf9bf5b57aed2c476-1725293744539.svg" alt=""><figcaption><p>Encryption</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/5f04259cf9bf5b57aed2c476-1725293763258.svg" alt=""><figcaption><p>Decryption</p></figcaption></figure>

* **Plaintext** is the original, readable message or data before it’s encrypted. It can be a document, an image, a multimedia file, or any other binary data.
* **Ciphertext** is the scrambled, unreadable version of the message after encryption. Ideally, we cannot get any information about the original plaintext except its approximate size.
* **Cipher** is an algorithm or method to convert plaintext into ciphertext and back again. A cipher is usually developed by a mathematician.
* **Key** is a string of bits the cipher uses to encrypt or decrypt data. In general, the used cipher is public knowledge; however, the key must remain secret unless it is the public key in asymmetric encryption. We will visit asymmetric encryption in a later task.
* **Encryption** is the process of converting plaintext into ciphertext using a cipher and a key. Unlike the key, the choice of the cipher is disclosed.
* **Decryption** is the reverse process of encryption, converting ciphertext back into plaintext using a cipher and a key. Although the cipher would be public knowledge, recovering the plaintext without knowledge of the key should be impossible (infeasible).

### Historical Ciphers

Caesar Cipher

* Plaintext: `TRYHACKME`
* Key: 3 (Assume it is a right shift of 3.)
* Cipher: Caesar Cipher

<figure><img src="../../.gitbook/assets/5f04259cf9bf5b57aed2c476-1725293808044.svg" alt=""><figcaption><p>Tryhackme becomes WUBKDFNPH</p></figcaption></figure>

Other notable historical Ciphers:

* The Vigenère cipher from the 16th century
* The Enigma machine from World War II
* The one-time pad from the Cold War

## Types of Encryption

### Symmetric Encryption

Uses the same key to encrypt and decrypt the data

Keeping the key secret is a must!

<figure><img src="../../.gitbook/assets/5f04259cf9bf5b57aed2c476-1725293928434 (1).svg" alt=""><figcaption><p>DES, 3DES and AES are examples of Symmetric Encription</p></figcaption></figure>

AES is the adopted standard. Its key size can be 128, 192, or 256 bits.

### Asymmetric Encryption ( also called **public key cryptography**)

<figure><img src="../../.gitbook/assets/5f04259cf9bf5b57aed2c476-1725293946043.svg" alt=""><figcaption></figcaption></figure>

Asymmetric encryption tends to be slower, and many asymmetric encryption ciphers use larger keys than symmetric encryption. For example, RSA uses 2048-bit, 3072-bit, and 4096-bit keys; 2048-bit is the recommended minimum key size. Diffie-Hellman also has a recommended minimum key size of 2048 bits but uses 3072-bit and 4096-bit keys for enhanced security. On the other hand, ECC can achieve equivalent security with shorter keys. For example, with a 256-bit key, ECC provides a level of security comparable to a 3072-bit RSA key.

Asymmetric encryption is based on a particular group of mathematical problems that are easy to compute in one direction but extremely difficult to reverse. In this context, extremely difficult means practically infeasible

Real life example of asymmetric encryption:&#x20;

**Sending a Secret Message (Mailbox & Key)**

* **Public Key**: Think of the **public key** as a **mailbox** where anyone can drop a letter (message). It’s open to the public, so anyone can send you a letter (encrypt the message).
* **Private Key**: The **private key** is like the **key to your mailbox**. Only you have it, so only you can open the mailbox (decrypt the message) and read what was inside.

**Example**: If your friend wants to send you a secret letter, they put it in your public mailbox (use your public key to encrypt). Only you can open that mailbox and read the letter using your private key.

This is "**asymmetric**" because the keys are different **(one for locking, one for unlocking)**. It’s super secure because your private key stays private, and the public key can’t be used to unlock anything—it’s only for locking!

## Basic Math

### XOR Operation (exclusive OR)

is a logical operation in binary arithmetic

**compares two bits and returns 1 if the bits are different and 0 if they are the same**

| A | B | A ⊕ B |
| - | - | ----- |
| 0 | 0 | 0     |
| 0 | 1 | 1     |
| 1 | 0 | 1     |
| 1 | 1 | 0     |

### Modulo Operation

Another mathematical operation we often encounter in cryptography is the modulo operator, commonly written as %$$%$$ or as $$mod$$. The modulo operator, $$X%Y$$, is the **remainder** when X is divided by Y. In our daily life calculations, we focus more on the result of division than on the remainder. The remainder plays a significant role in cryptography.

Let’s consider a few examples.

* $$25%5 = 0$$ because 25 divided by 5 is 5, with a remainder of 0, i.e., $$25 = 5 × 5 + 0$$
* $$23%6 = 5$$ because 23 divided by 6 is 3, with a remainder of 5, i.e., $$23 = 3 × 6 + 5$$
* $$23%7 = 2$$ because 23 divided by 7 is 3 with a remainder of 2, i.e., $$23 = 3 × 7 + 2$$

An important thing to remember about modulo is that it’s not reversible. If we are given the equation $$x%5 = 4$$, infinite values of $$x$$ would satisfy this equation.
