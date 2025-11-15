---
description: I've got expressed permission to try hack  advis-marketing.cz
---

# Web enum of advis-marketing.cz



<figure><img src="../.gitbook/assets/nikt.JPG" alt=""><figcaption><p>First scan</p></figcaption></figure>

With simple nikto commands

IP 91.239.201.14

Server the target is using

OSVDB-877  (Open Source Vulnerability Database

host is vulnerable to XST - Cross-Site Tracing, a vulnerability that exploits the HTTP TRACE method to potentially steal sensitive data, including authentication data and cookies, from a web application.

some info about OSVDB-877

&#x20;: [https://medium.com/@tushar\_rs\_/cross-site-tracing-attack-xst-5aa519658b7a](https://medium.com/@tushar_rs_/cross-site-tracing-attack-xst-5aa519658b7a) ???

Can't find anything too specific on osvdb-877

<figure><img src="../.gitbook/assets/ssssss.JPG" alt=""><figcaption><p>Second scan, same results, just wanted to output it to a file</p></figcaption></figure>

The txt output file no longer mentions the server information

## Trying Gobuster now - Directory enumeration mode

<figure><img src="../.gitbook/assets/123.JPG" alt=""><figcaption><p>First attempt unsuccesful</p></figcaption></figure>

It wouldn't let me procced because of 301 status code

Second attempt with this command:

`gobuster dir -k -u advis-marketing.cz -t50 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -b 301,403,404 -e -f --timeout 60s -o buster_advis.txt`

<figure><img src="../.gitbook/assets/1234.JPG" alt=""><figcaption></figcaption></figure>

## Nmap

nmap -sC -sV -A -O -vv -p- -T5 91.239.201.14 -oN nmap\_scan.txt

<figure><img src="../.gitbook/assets/nmap (1).JPG" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/ssadad.JPG" alt=""><figcaption></figcaption></figure>

## Metasploit on postgresqle

Tried few exploits with no success

msf6 auxiliary(scanner/postgres/postgres\_hashdump)

msf6 auxiliary(scanner/postgres/postgres\_version)

msf6 exploit(linux/http/acronis\_cyber\_infra\_cve\_2023\_45249)

msf6 exploit(linux/http/acronis\_cyber\_infra\_cve\_2023\_45249)

msf6 auxiliary(scanner/postgres/postgres\_dbname\_flag\_injection)

msf6 auxiliary(scanner/postgres/postgres\_login)

msf6 auxiliary(scanner/postgres/postgres\_hashdump)

## hydra&#x20;

hydra -l /usr/share/wordlists/SecLists/Usernames/top-usernames-shortlist.txt -P /usr/share/wordlists/rockyou.txt ftp://91.239.201.14

<figure><img src="../.gitbook/assets/sydara.JPG" alt=""><figcaption><p>only a year to complete this brute force...</p></figcaption></figure>

huh, i cant seem to access advis-marketing.cz from the thm vm but i can access it from my own browser? Everything else seems to be working fine, just advis-marketing.cz not working. How could it be? Did it block my access from my ip lol? I've turn off hydra, nmap scans and everyting but to no avail.



