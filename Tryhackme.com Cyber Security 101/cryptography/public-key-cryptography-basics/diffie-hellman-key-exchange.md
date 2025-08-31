---
description: >-
  Allows parties to share secrets thanks to maths. Calculator:
  https://www.irongeek.com/diffie-hellman.php?
---

# Diffie-Hellman Key Exchange

[https://tryhackme.com/r/room/publickeycrypto](https://tryhackme.com/r/room/publickeycrypto)

#### Imagine:

* Alice and Bob want to agree on a secret number (the "key") to send each other secret messages, but they don't want anyone else to know it.
* They both have a **special number** (let's call it the "key") that they want to use, but they don't want to send it directly. Instead, they’ll create the key **together** without revealing it.

#### Here's how they do it:

1. **Pick a public number**:
   * Alice and Bob agree on two numbers ahead of time:
     * A **big number** (called p) that everyone knows(prime number)
     * A **smaller number** (called g), also called the "generator," that is used to make their private keys.
2. **Both choose their secret numbers**:
   * Alice picks a **secret number** (let's call it a)—she keeps this number to herself.
   * Bob picks his own **secret number** (let's call it b)—he also keeps this number to himself.
3. **Exchange public values**:
   * Alice calculates a number A using her secret number a and the public numbers p and g, then sends A to Bob.
   * Bob does the same with his secret number b, calculates a number B, and sends it to Alice.
   * Now, Alice has B, and Bob has A, but **they don’t know each other’s secret numbers**.
4. **Use the numbers to create a shared key**:
   * Alice uses the number B (which Bob sent her) and her own secret number a to calculate the secret shared key. This is her version of the "secret key."
   * Bob uses the number A (which Alice sent him) and his own secret number b to calculate the same shared key.

#### Why does this work?

* The trick is that even though they both exchanged numbers, only they can calculate the shared key because they know their secret numbers. **No one else can figure out the key, even if they know the public numbers and what Alice and Bob sent to each other.**
* The result is that both Alice and Bob now have the same key, and they can use it to **encrypt** their messages to each other.

#### In short:

* Alice and Bob each pick a secret number.
* They send "mixed-up" numbers to each other based on their secret numbers.
* Using the numbers they receive and their own secret number, they **magically** both end up with the same secret key to send encrypted messages, but no one else can figure out what it is.



<figure><img src="../../../.gitbook/assets/5f04259cf9bf5b57aed2c476-1728439878360.svg" alt=""><figcaption></figcaption></figure>

RSA are incorporated into many security protocols and standards to provide a comprehensive security solution.
