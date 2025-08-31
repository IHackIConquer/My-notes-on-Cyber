---
description: Transmission Control Protocol/Internet Protocol
---

# TCP/IP Model

TCP/IP was developed in the 1970s by the Department of Defense (DoD). One of the strengths of this model is that it allows a network to continue to function as parts of it are out of service, for instance, due to a military attack. This capability is possible in part due to the design of the routing protocols to adapt as the network topology changes.

* **Application Layer**: The OSI model application, presentation and session layers, i.e., layers 5, 6, and 7, are grouped into the application layer in the TCP/IP model.
* **Transport Layer**: This is layer 4.
* **Internet Layer**: This is layer 3. The OSI model’s network layer is called the Internet layer in the TCP/IP model.
* **Link Layer**: This is layer 2.

This table below shows how the TCP/IP model layers map to the ISO/OSI model layers.

| **Layer Number** | **ISO OSI Model**  | **TCP/IP Model (RFC 1122)** | **Protocols**                                    |
| ---------------- | ------------------ | --------------------------- | ------------------------------------------------ |
| 7                | Application Layer  | Application Layer           | HTTP, HTTPS, FTP, POP3, SMTP, IMAP, Telnet, SSH, |
| 6                | Presentation Layer |                             |                                                  |
| 5                | Session Layer      |                             |                                                  |
| 4                | Transport Layer    | Transport Layer             | TCP, UDP                                         |
| 3                | Network Layer      | Internet Layer              | IP, ICMP, IPSec                                  |
| 2                | Data Link Layer    | Link Layer                  | Ethernet 802.3, WiFi 802.11                      |
| 1                | Physical Layer     |                             |                                                  |



"Suppose that you were sending a novel to someone and the only way you could send it was by sending postcards so you cut the pages of the novel up, put them on postcards and then you realise that you have to number the postcards in order to let the party at the other end put them in the right order. Then you wonder you know if some of them got lost you'd have to re-transmit them so you keep copies to send. Then you realise that you need to find out whether you need to send any copies and you have acknowledgements coming back in the form of post cards, some of which might get lost. And so you have time outs that say if I haven't heard anything I'll start sending copies. It's basically the way the TCP works. It essentially allows us to send novels in sequenced order on top of postcards except of course we do it electronically and much faster."  - VINTON CERF\


