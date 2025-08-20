---
description: >-
  Internet Control Message Protocol (ICMP) is mainly used for network
  diagnostics and error reporting.
---

# ICMP: Troubleshooting Networks

Two popular commands rely on ICMP, and they are instrumental in network troubleshooting and network security. The commands are:

* `ping`: This command uses ICMP to test connectivity to a target system and measures the round-trip time (RTT). In other words, it can be used to learn that the target is alive and that its reply can reach our system.
* `traceroute`: This command is called `traceroute` on Linux and UNIX-like systems and `tracert` on MS Windows systems. It uses ICMP to discover the route from your host to the target.

## Ping

Many things might prevent us from getting a reply. In addition to the possibility of the target system being offline or shut down, a firewall along the path might block the necessary packets for `ping` to work.

<figure><img src="../../../.gitbook/assets/Capture1.PNG" alt=""><figcaption><p>The output shows no packet loss; moreover, it calculates the minimum, average, maximum, and standard deviation (mdev) of the round-trip time (RTT).im</p></figcaption></figure>



```bash
ping 192.168.11.1 -c 4
```

-c to tell the ping to stop after sending four packets

## Traceroute

The Internet protocol has a field called Time-to-Live (TTL) that indicates the maximum number of routers a packet can travel through before it is dropped.

When the TTL reaches zero, the router drops the packet and sends an ICMP Time Exceeded message (ICMP Type `11`)&#x20;

For all the ICMP types: [https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml](https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml)

<figure><img src="../../../.gitbook/assets/2.PNG" alt=""><figcaption><p>The traversed route might change as we rerun the command.</p></figcaption></figure>

{% embed url="https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml" %}

AI's lame effort at visualising why ICMP don't use ports...

<div><figure><img src="../../../.gitbook/assets/85f5c37b-dade-4aaa-a737-4348df16218a.webp" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/2d076dc0-73c7-43f6-ad2e-f010f97651ac (1).webp" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/9b3a0529-c916-49c2-aed4-64f3ca4a2244 (1).webp" alt=""><figcaption></figcaption></figure></div>
