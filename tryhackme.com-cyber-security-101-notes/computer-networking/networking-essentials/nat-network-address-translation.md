---
description: One public IP address to provide Internet access to many private IP addresses
---

# NAT (Network Address Translation)

The idea behind NAT lies in using **one public IP address** to provide Internet access to **many private IP addresses**. In other words, if you are connecting a company with twenty computers, you can provide Internet access to all twenty computers by using a single public IP address instead of twenty public IP addresses

Router that support NAT keep track of ongoing connections. They keep a table translating network addresses between internal and external networks. As seen in picture bellow:

<figure><img src="../../../.gitbook/assets/5f04259cf9bf5b57aed2c476-1719849362861.svg" alt=""><figcaption><p>An example of how a router with NAT can connect many devices with single public IP</p></figcaption></figure>

Assuming that the router has infinite processing power, it can maintain \~65k simultaneous TCP connections.
