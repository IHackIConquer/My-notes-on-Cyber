---
description: User Datagram Protocol and Transmission Control Protocol
---

# UPD and TCP

## UDP

User Datagram Protocol is a connectionless protocol; UDP does not require a connection to be established. UDP is suitable for protocols that rely on fast queries, such as DNS, and for protocols that prioritise real-time communications, such as audio/video conferencing and broadcast.

UDP is a simple connectionless protocol that operates at the transport layer 4

UDP does not even provide a mechanism to know that the packet has been delivered.

A real life example would be sending a letter with not confirmation of delivery

## TCP

Transmission Control Protocol is a connection-oriented transport protocol. It requires the establishment of a TCP connection before any data can be sent.

In TCP, each data octet has a sequence number; this makes it easy for the receiver to identify lost or duplicated packets. The receiver, on the other hand, acknowledges the reception of data with an acknowledgement number specifying the last received octet.

A TCP connection is established using what’s called a three-way handshake. Two flags are used: SYN (Synchronise) and ACK (Acknowledgment). The packets are sent as follows:

1. SYN Packet: The client initiates the connection by sending a SYN packet to the server. This packet contains the client’s randomly chosen initial sequence number.
2. SYN-ACK Packet: The server responds to the SYN packet with a SYN-ACK packet, which adds the initial sequence number randomly chosen by the server.
3. ACK Packet: The three-way handshake is completed as the client sends an ACK packet to acknowledge the reception of the SYN-ACK packet.

<figure><img src="../../../.gitbook/assets/5f04259cf9bf5b57aed2c476-1719849036216 (1).svg" alt=""><figcaption><p>A three-way handshake</p></figcaption></figure>

