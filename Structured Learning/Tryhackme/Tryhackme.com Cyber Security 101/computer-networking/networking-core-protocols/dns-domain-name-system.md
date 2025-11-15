# DNS (Domain Name System)

DNS operates at the Application Layer, i.e., Layer 7 of the ISO OSI model. DNS traffic uses UDP port 53 by default and TCP port 53 as a default fallback

* **A record**: The A (Address) record maps a hostname to one or more IPv4 addresses. For example, you can set `example.com` to resolve to `172.17.2.172`.
* **AAAA Record**: The AAAA record is similar to the A Record, but it is for IPv6. Remember that it is AAAA (quad-A)
* **CNAME Record**: The CNAME (Canonical Name) record maps a domain name to another domain name. For example, `www.example.com` can be mapped to `example.com` or even to `example.org`.
* **MX Record**: The MX (Mail Exchange) record specifies the mail server responsible for handling emails for a domain.

When you type an address.com your browser will query the DNS server for the **A record.**&#x20;

When you try to send an email to zade@test.cz the mail server will query DNS server for **MX record**

