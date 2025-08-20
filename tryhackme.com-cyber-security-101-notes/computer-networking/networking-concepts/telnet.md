---
description: TELetype NETwork protocol is a network protocol for remote terminal connection
---

# TELNET

Telnet server is **not encrypted**, making it an easy target for attackers.

TELNET client, allows you to connect to and communicate with a remote system and issue text commands. Although initially it was used for remote administration, we can use `telnet` to connect to any server listening on a TCP port number.

`quit` to close connection

`GET / HTTP/1.1` and `Host: anything`&#x20;

`Host: telnet`&#x20;

&#x20;On some servers, you might get the file without sending `Host: anything`

To get `file.html`, you would send `GET /file.html HTTP/1.1`,

&#x20;Or just `GET /file.html` might work depending on the web server in use. This approach is efficient for troubleshooting as you would be “talking HTTP” with the server.
