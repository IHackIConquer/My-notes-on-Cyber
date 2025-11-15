---
description: >-
  FTP server listens on TCP port 21 by default. Very efficient for file
  transfer. Can be faster than HTTP
---

# FTP (File Transfer Protocol)

<figure><img src="../../../.gitbook/assets/da71a52fddfbb268dc6c5857daf07f18.png" alt=""><figcaption></figcaption></figure>

Example commands defined by the FTP protocol are:

* `USER` is used to input the username
* `PASS` is used to enter the password
* `RETR` (retrieve) is used to download a file from the FTP server to the client.
* `STOR` (store) is used to upload a file from the client to the FTP server.



In the terminal below we executed the command `ftp 10.10.240.137` to connect to the remote FTP server using the local `ftp` client. Then we went through the following steps:

* We used the username `anonymous` to log in
* We didn’t need to provide any password
* Issuing `ls` returned a list of files available for download
* `type ascii` switched to ASCII mode as this is a text file
* `get coffee.txt` allowed us to retrieve the file we want

<figure><img src="../../../.gitbook/assets/Capture4.PNG" alt=""><figcaption><p>What happens in the terminal</p></figcaption></figure>

With Wireshark we can see the exchange more closely. The client’s messages are in **red**, while the server’s responses are in **blue**

<figure><img src="../../../.gitbook/assets/5f04259cf9bf5b57aed2c476-1719849609513.png" alt=""><figcaption><p>What happens between the client and the server</p></figcaption></figure>
