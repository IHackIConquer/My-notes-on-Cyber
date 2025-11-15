---
description: >-
  RSA is a public-key encryption algorithm that enables secure data transmission
  over insecure channels. With an insecure channel, we expect adversaries to
  eavesdrop on it.
---

# RSA

Calculator: [https://www.cs.drexel.edu/\~popyack/IntroCS/HW/RSAWorksheet.html](https://www.cs.drexel.edu/~popyack/IntroCS/HW/RSAWorksheet.html)

RSA is based on the mathematically difficult problem of **factoring a large number**. Multiplying two large prime numbers is a straightforward operation; however, finding the factors of a huge number takes much more computing power.

* Prime number 1: $$982451653031$$
* Prime number 2: $$169743212279$$
* Their product: $$982451653031 × 169743212279 = 166764499494295486767649$$

On the other hand, it’s pretty tricky to determine what two prime numbers multiply together to make $$14351$$ and even more challenging to find the factors of $$166764499494295486767649$$.

In real-world examples, the prime numbers would be much bigger than the ones in this example. A computer can easily factorise $$166764499494295486767649$$; however, it cannot factorise a number with more than 600 digits. And you would agree that the multiplication of the two huge prime numbers, each around 300 digits, would be easier than the factorisation of their product.

<figure><img src="../../../.gitbook/assets/5f04259cf9bf5b57aed2c476-1725294065881.svg" alt=""><figcaption></figcaption></figure>

1. Bob chooses two prime numbers: $$p = 157$$ and $$q = 199$$. He calculates $$n = p × q = 31243$$.
2. With $$ϕ(n) = n − p − q + 1 = 31243 − 157 − 199 + 1 = 30888$$, Bob selects $$e = 163$$ such that $$e$$ is relatively prime to $$ϕ(n)$$; moreover, he selects $$d = 379$$, where $$e × d = 1$$ mod $$ϕ(n)$$, i.e., $$e × d = 163 × 379 = 61777$$ and $$61777$$ mod $$30888 = 1$$. The public key is $$(n,e)$$, i.e., $$(31243,163)$$ and the private key is $(n,d), i.e., $$(31243,379)$$.
3. Let’s say that the value they want to encrypt is $$x = 13$$, then Alice would calculate and send $$y = xe$$ mod $$n = 13163$$ mod $$31243 = 16341$$.
4. Bob will decrypt the received value by calculating $$x = yd$$ mod $$n = 16341379$$ mod $$31243 = 13$$. This way, Bob recovers the value that Alice sent.

* p and q are large prime numbers
* n is the product of p and q
* The public key is n and e
* The private key is n and d
* m is used to represent the original message, i.e., plaintext
* c represents the encrypted text, i.e., ciphertext

IRL this would be done with much bigger numbers
