---
description: >-
  The Open System Interconnection (OSI) model is a conceptual model that
  describes how communications should occur in a computer network.
---

# OSI Model

<figure><img src="../../../.gitbook/assets/5f04259cf9bf5b57aed2c476-1719848845717.svg" alt=""><figcaption><p>“Please Do Not Throw Spinach Pizza Away.” - Acronym</p></figcaption></figure>

## 1. Physical

The first layer deals with the physical connection between devices. This includes cables as well as wireless.

## 2. Data Link

The second layer represents the protocol than enables data transfer between nodes on the same network segment. (A Network segment e.g. company office with 10 computer connected to a network switch.)

Examples of layer 2 include Ethernet, i.e., 802.3, and WiFi, i.e., 802.11. Ethernet and WiFi addresses are six bytes. Their address is called a MAC address, where MAC stands for Media Access Control. They are usually expressed in hexadecimal format with a colon separating each two bytes

## 3. Network

The 3rd layer's job is to send data between different networks, finding a path to transfer the network packets between the diverse networks - also called the  logical addressing and routing.

Examples of the network layer include Internet Protocol (IP), Internet Control Message Protocol (ICMP), and Virtual Private Network (VPN) protocols such as IPSec and SSL/TLS VPN.

## 4. Transport

Layer 4, the transport layer, enables end-to-end communication between running applications on different hosts. Your web browser is connected to the TryHackMe web server over the transport layer, which can support various functions like flow control, segmentation, and error correction.

Examples of layer 4 are Transmission Control Protocol (TCP) and User Datagram Protocol (UDP).

## 5. Session

The session layer is responsible for establishing, maintaining, and synchronising communication between applications running on different hosts. Establishing a session means initiating communication between applications and negotiating the necessary parameters for the session. Data synchronisation ensures that data is transmitted in the correct order and provides mechanisms for recovery in case of transmission failures.

Examples of the session layer are Network File System (NFS) and Remote Procedure Call (RPC).

## 6. Presentation

The presentation layer ensures the data is delivered in a form the application layer can understand. Layer 6 handles data encoding, compression, and encryption. An example of encoding is character encoding, such as ASCII or Unicode.

Various standards are used at the presentation layer. Consider the scenario where we want to send an image via email. First, we use JPEG, GIF, and PNG to save our images; furthermore, although hidden from the user by the email client, we use MIME (Multipurpose Internet Mail Extensions) to attach the file to our email. MIME encodes a binary file using 7-bit ASCII characters.

## 7. Application

The application layer provides network services directly to end-user applications. Your web browser would use the HTTP protocol to request a file, submit a form, or upload a file.

The application layer is the top layer, and you might have encountered many of its protocols as you use different applications. Examples of Layer 7 protocols are HTTP, FTP, DNS, POP3, SMTP, and IMAP.&#x20;
