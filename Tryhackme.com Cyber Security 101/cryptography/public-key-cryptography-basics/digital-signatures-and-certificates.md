---
description: >-
  Not to be confused with actual hand written signatures using a tablet or
  whatever
---

# Digital Signatures and Certificates

In many modern countries, digital and physical signatures have the same legal value.

The simplest form of digital signature is encrypting the document with your private key. If someone wants to verify this signature, they would decrypt it with your public key and check if the files match. This process is shown in the image below.

### Reminder of how asymmetric keys work:

Because the keys are different (one for locking, one for unlocking). It’s super secure because your private key stays private, and the public key can’t be used to unlock anything—it’s only for locking!

<figure><img src="../../../.gitbook/assets/5f04259cf9bf5b57aed2c476-1725294344472 (1).svg" alt=""><figcaption></figcaption></figure>

Pasting an image of a signature on top of a document doesn't constitute as secure as anyone can copy  and paste an image.&#x20;

We use the term _digital signature_ to refer to signing a document using a private key or a certificate. This process is similar to the image shown above, where Bob encrypts a hash of his document and shares it with Alice, along with the original document. Alice can decrypt the encrypted hash and compare it with the hash of the file she received. This approach proves the document’s integrity, unlike pasting a fancy image of a signature.

## Certificates

Digital certificates can be used to secure websites, devices, web servers, signatures, code, software, email and more

### How they work:

#### Step-by-Step:

1. **The Website Shows Its ID**: When you visit a website (like your bank), it shows you its digital ID card, called a **certificate**. This certificate includes:
   * The website’s name (e.g., "yourbank.com").
   * Its public key (used for encryption).
   * The name of a trusted organization that issued it (called a **Certificate Authority** or **CA**).
   * A digital signature from the CA proving the certificate is real.
2. **The CA Is Trusted**: Your browser has a list of **trusted CAs** built into it, like a guest list at the party. These are well-known and highly secure organizations.
3. **Chains of Trust**: Sometimes, the CA on the certificate isn’t on your browser’s trusted list directly. Instead, it was vouched for by another CA higher up in the trust chain. For example:
   * The website’s certificate is signed by an **Intermediate CA**.
   * The Intermediate CA is signed by a **Root CA**, which is on your browser’s trusted list. This chain of trust links back to a Root CA, which ensures everything is legit.
4. **Browser Checks Everything**: Your browser follows the chain:
   * It verifies each signature, starting from the website's certificate.
   * It climbs the chain until it reaches a Root CA.
   * If all links in the chain are valid, the certificate (and the website) are trusted.
5. **The Website Proves Itself**: The website also has a secret (its private key) that matches the public key in the certificate. It uses this during a handshake with your browser to prove it’s the real owner.
6. **Secure Connection Established**: If all checks pass, your browser says, "This is legit!" and sets up a secure, encrypted connection with the website.

***

#### Why Chains of Trust?

Chains make it easier to manage trust. Instead of every website needing to get a certificate directly from a Root CA, they can get one from an Intermediate CA, which makes the process faster and more scalable. The Root CA still indirectly vouches for the website through this chain.

***

If anything in the chain is broken (e.g., a signature doesn’t match, or the certificate is expired), your browser will throw a warning, saying, "Something’s wrong—don’t trust this site!"



