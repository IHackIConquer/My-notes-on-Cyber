---
description: >-
  How TLS, SSH, and VPN can secure your network traffic.
  https://tryhackme.com/r/room/networkingsecureprotocols
---

# Networking Secure Protocols

## TLS (Transport Layer Security)

TLS is a cryptographic protocol operating at the OSI model’s transport layer. It allows secure communication between a client and a server over an insecure network. TLS ensures that no one can read or modify the exchanged data

Tens of protocols have received security upgrades with the simple addition of TLS. Examples include HTTP, DNS, MQTT, and SIP, which have become HTTPS, DoT (DNS over TLS), MQTTS, and SIPS, where the appended “S” stands for Secure due to the use of SSL/TLS.

#### How TLS works:

The first step for every server (or client) that needs to identify itself is to get a signed TLS certificate. Generally, the server administrator creates a Certificate Signing Request (CSR) and submits it to a Certificate Authority (CA); the CA verifies the CSR and issues a digital certificate. Once the (signed) certificate is received, it can be used to identify the server (or the client) to others, who can confirm the validity of the signature. For a host to confirm the validity of a signed certificate, the certificates of the signing authorities need to be installed on the host. In the non-digital world, this is similar to recognising the stamps of various authorities.

## HTTP Over TLS, (instead of TCP)

(Hypertext Transfer Protocol Secure)

Requesting a page over HTTPS will require the following three steps (after resolving the domain name):

1. Establish a TCP three-way handshake with the target server
2. Establish a TLS session
3. Communicate using the HTTP protocol; for example, issue HTTP requests, such as `GET / HTTP/1.1`

The key takeaway is that TLS offered security for HTTP without requiring any changes in the lower or higher layer protocols. In other words, TCP and IP were not modified, while HTTP was sent over TLS the way it would be sent over TCP.

## SMTPS, POP3S, IMAPS

Adding TLS to SMTP, POP3, and IMAP is no different than adding TLS to HTTP.

The insecure versions use the default TCP port numbers shown in the table below:

| Protocol | Default Port Number |
| -------- | ------------------- |
| HTTP     | 80                  |
| SMTP     | 25                  |
| POP3     | 110                 |
| IMAP     | 143                 |

The secure versions, i.e., over TLS, use the following TCP port numbers by default:

| Protocol | Default Port Number    |
| -------- | ---------------------- |
| HTTPS    | 443                    |
| SMTPS    | <p>465 and 587<br></p> |
| POP3S    | 995                    |
| IMAPS    | 993                    |

## SSH (Secure SHell)

Secure Shell (SSH) refers to a cryptographic network protocol used in secure communication between devices. SSH encrypts data using cryptographic algorithms, such as Advanced Encryption System (AES) and is often used when logging in remotely to a computer or server.

When you use an SSH client, it is most likely based on OpenSSH libraries and source code.

OpenSSH few key points:

* **Secure authentication**: Besides password-based authentication, SSH supports public key and two-factor authentication.
* **Confidentiality**: OpenSSH provides end-to-end encryption, protecting against eavesdropping. Furthermore, it notifies you of new server keys to protect against man-in-the-middle attacks.
* **Integrity**: In addition to protecting the confidentiality of the exchanged data, cryptography also protects the integrity of the traffic.
* **Tunneling**: SSH can create a secure “tunnel” to route other protocols through SSH. This setup leads to a VPN-like connection.
* **X11 Forwarding**: If you connect to a Unix-like system with a graphical user interface, SSH allows you to use the graphical application over the network.

&#x20;`ssh username@hostname` to connect to an SSH server. If the username is the same as your logged-in username, you only need `ssh hostname`. Then, you will be asked for a password; however, if public-key authentication is used, you will be logged in immediately.

the SSH server listens on port 22

## SFTP and FTPS

SFTP stands for SSH File Transfer Protocol

FTPS stands for File Transfer Protocol Secure

SFTP and SSH share the same port number 22

FPT uses port 21, FTPS port 990

If enabled in the OpenSSH server configuration, you can connect using a command such as `sftp username@hostname`. Once logged in, you can issue commands such as `get filename` and `put filename` to download and upload files, respectively. Generally speaking, SFTP commands are Unix-like and can differ from FTP commands

## VPN

A Virtual Private Network is a way to create a secure "tunnel" between two networks. For example, you use a VPN on TryHackMe to access the private network on which the machines operate. VPNs are also commonly used for an employee to log into their workplace when they are not on site (such as working from home or travelling for business matters). VPNs are also used where networks (such as coffee shops) do not provide encryption, and are a great way of preventing others from reading your network traffic.

For the image bellow:

the VPN client will encrypt the traffic and pass it to the main branch via the established VPN tunnel (shown in blue). The VPN traffic is limited to the blue lines; the green lines would carry the decrypted VPN traffic.

<figure><img src="../../.gitbook/assets/5f04259cf9bf5b57aed2c476-1721903538365.svg" alt=""><figcaption></figcaption></figure>



In the network diagram below, we see two remote users using VPN clients to connect to the VPN server in the main branch. In this case, the VPN client connects a single device.

<figure><img src="../../.gitbook/assets/5f04259cf9bf5b57aed2c476-1721903568757 (2).svg" alt=""><figcaption></figcaption></figure>

The VPN server may be configured to give you access to a private network but not to route your traffic. Furthermore, some VPN servers leak your actual IP address, although they are expected to route all your traffic over the VPN. Depending on why you are using a VPN connection, you might need to run a few more tests, such as a DNS leak test.

### Where are VPNs illegal? <a href="#id-where-are-vpns-illegal-1" id="id-where-are-vpns-illegal-1"></a>

VPNs are illegal, or will get you in trouble in North Korea, Belarus, Oman, Iraq, and Turkmenistan. In some other countries, including China, Russia, Türkiye, UAE, India, Iran, Egypt, and Uganda, only government-approved VPNs are legal

source nordvpn.com 30/11/2024







&#x20;
