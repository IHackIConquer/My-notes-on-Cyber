---
description: Nmap network scanner https://tryhackme.com/r/room/nmap
---

# Nmap

<figure><img src="../../.gitbook/assets/sitelogo.png" alt=""><figcaption></figcaption></figure>

[https://www.stationx.net/nmap-cheat-sheet/](https://www.stationx.net/nmap-cheat-sheet/)

* Discover live hosts
* Find running services on the live hosts
* Distinguish the different types of port scans
* Detect the versions of the running services
* Control the timing
* Format the output

It is best to run Nmap with `sudo` privileges. Running Nmap with local user privileges will still work; however, you should expect many features to be unavailable. You get a minimal portion of Nmap’s power when running it as a local user. For instance, Nmap would automatically use SYN scan (`-sS`) if you are running it with `sudo` privileges and will default to connect scan (`-sT`) if run as a local user. The reason is that crafting certain packets, such as sending a TCP SYN packet, requires root privileges.

### How to specify targets:

* IP range using `-`: If you want to scan all the IP addresses from 10.10.186.1 to 10.10.186.10, you can write `10.10.186.1-10`
* ![](<../../.gitbook/assets/nmap ip range.PNG>)
* IP subnet using `/`: If you want to scan a subnet, you can express it as `192.168.0.1/24`, and this would be equivalent to `192.168.0.0-255`
* Hostname: You can also specify your target by hostname, for example, `example.thm`



* `-p[range]` allows you to specify a range of ports to scan. For example, `-p10-1024` scans from&#x20;
* `-F` is for Fast mode, which scans the 100 most common ports (instead of the default 1000).
* `-p[range]` allows you to specify a range of ports to scan. For example, `-p10-1024` scans from port 10 to port 1024, while `-p-25` will scan all the ports between 1 and 25. Note that `-p-` scans all the ports and is equivalent to `-p1-65535` and is the best option if you want to be as thorough as possible.

&#x20;`-sn` Disable port scanning. Host discovery only.

`-sL`  No Scan. List targets only



When scanning a directly connected network, Nmap starts by sending ARP requests. When a device responds to the ARP request, Nmap labels it with “Host is up”.

Address Resolution Protocol (ARP) is responsible for finding the MAC (hardware) address related to a specific IP address. It works by broadcasting an ARP query, "Who has this IP address? Tell me." And the response is of the form, "The IP address is at this MAC address." This doesn't work when&#x20;



## Scanning TCP Ports

### The Connect scan

`-sT` Tries to complete the TCP three-way handshake with every target TCP port. If the TCP port turns out to be open and Nmap connects successfully, Nmap will tear down the established connection.

### SYN scan (stealth)

`-sS` Unlike the Connect scan, it only sends the TCP SYN Packet and never completes the three-way handshake . As connection is never established this leads to fewer logs. Hence it's considered stealthy.&#x20;

## Scanning UDP ports

DNS, DHCP, NTP (Network Time Protocol), SNMP (Simple Network Management Protocol), and VoIP (Voice over IP). UDP does not require establishing a connection and tearing it down afterwards. Furthermore, it is very suitable for real-time communication, such as live broadcasts.

`-sU` To scan for UDP services

## Other useful commands:

`-sV` enables Service and Version Detection

`-O` enables OS detection

## Timing&#x20;

Running your scan at its normal speed might trigger an IDS or other security solutions.

Intrusion Detection System (IDS) is a system that detects unauthorised network and system intrusions. Examples include detecting unauthorised devices connected to the local network and unauthorised users accessing a system or modifying a file.

Table showing approximate times

| Timing          | Total Duration |
| --------------- | -------------- |
| T0 (paranoid)   | 9.8 hours      |
| T1 (sneaky)     | 27.53 minutes  |
| T2 (polite)     | 40.56 seconds  |
| T3 (normal)     | 0.15 seconds   |
| T4 (aggressive) | 0.13 seconds   |

More on timing on : [https://nmap.org/book/performance-timing-templates.html](https://nmap.org/book/performance-timing-templates.html)

A second helpful option is the number of parallel service probes. The number of parallel probes can be controlled with `--min-parallelism <numprobes>` and `--max-parallelism <numprobes>`.

A similar helpful option is the `--min-rate <number>` and `--max-rate <number>`. As the names indicate, they can control the minimum and maximum rates at which `nmap` sends packets. The rate is provided as the _number of packets per second_. It is worth mentioning that the specified rate applies to the whole scan and not to a single host.

&#x20;`--host-timeout <time>`. This option specifies the maximum time you are willing to wait, and it is suitable for slow hosts or hosts with slow network connections.

More on this on [https://nmap.org/book/man-performance.html](https://nmap.org/book/man-performance.html)

## Output: Controlling What You See

Most likely, the `-v` option is more than enough for verbose output; however, if you are still unsatisfied, you can increase the verbosity level by adding another “v” such as `-vv` or even `-vvvv`. You can also specify the verbosity level directly, for example, `-v2` and `-v4`. You can even increase the verbosity level by pressing “v” after the scan already started.\


If all this verbosity does not satisfy your needs, you must consider the `-d` for debugging-level output. Similarly, you can increase the debugging level by adding one or more “d” or by specifying the debugging level directly. The maximum level is `-d9`; before choosing that, make sure you are ready for thousands of information and debugging lines.

#### Saving Scan Report

In many cases, we would need to save the scan results. Nmap gives us various formats. The three most useful are normal (human-friendly) output, XML output, and grepable output, in reference to the `grep` command. You can select the scan report format as follows:

* `-oN <filename>` - Normal output
* `-oX <filename>` - XML output
* `-oG <filename>` - `grep`-able output (useful for `grep` and `awk`)
* `-oA <basename>` - Output in all major formats



