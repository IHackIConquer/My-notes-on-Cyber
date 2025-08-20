---
description: >-
  Defines how your web browser communicates with the web servers.
  https://tryhackme.com/r/room/protocolsandservers
---

# HTTP(S) (Hypertext Transfer Protocol (Secure))

Some of the commands or methods that your web browser commonly issues to the web server are:

* `GET` retrieves data from a server, such as an HTML file or an image.
* `POST` allows us to submit new data to the server, such as submitting a form or uploading a file.
* `PUT` is used to create a new resource on the server and to update and overwrite existing information.
* `DELETE`, as the name suggests, is used to delete a specified file or resource on the server.

HTTP and HTTPS commonly use TCP ports 80 and 443, respectively, and less commonly other ports such as 8080 and 8443.



Some examples with`telnet`

`GET / HTTP/1.1` and `Host: anything`&#x20;

&#x20;On some servers, you might get the file without sending `Host: anything`

To get `file.html`, you would send `GET /file.html HTTP/1.1`,

&#x20;Or just `GET /file.html` might work depending on the web server in use. This approach is efficient for troubleshooting as you would be “talking HTTP” with the server.

<figure><img src="../../../.gitbook/assets/a23a13cef49ae7fff87bfd94f6a175dc.png" alt=""><figcaption></figcaption></figure>
