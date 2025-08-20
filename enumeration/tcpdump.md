---
description: >-
  TCPdump is like a spy for your computer's network traffic. It listens to all
  the messages (data packets) going in and out of your computer and shows you
  what’s happening behind the scenes.
---

# TCPDump

[https://tryhackme.com/r/room/tcpdump](https://tryhackme.com/r/room/tcpdump)

Imagine you're at a party, and everyone is talking to each other. TCPdump is like someone standing quietly in the corner, writing down who’s talking to whom, what they’re saying, and how long they’re chatting. It doesn’t change the conversations; it just observes and takes notes.

Here’s what TCPdump does in simple terms:

1. **Captures Traffic**: It grabs packets (tiny pieces of data) moving through your network. These could be things like emails, web pages, or file downloads.
2. **Shows Details**: It tells you where the packet is going, where it came from, and what kind of data it is carrying.
3. **Filters Traffic**: If you’re only interested in certain conversations (like messages to a specific website), you can tell TCPdump to focus only on those.

It’s super useful for troubleshooting network problems, checking for security issues, or learning how networks work. But, just like spying at a party, you need permission to use it in most case

## Basic Packet Capture

### Specify the Network Interface

The first thing to decide is which network interface to listen to using `-i INTERFACE`. You can choose to listen on all available interfaces using `-i any`; alternatively, you can specify an interface you want to listen on, such as `-i eth0`.

A command such as `ip address show` (or merely `ip a s`) would list the available network interfaces. In the terminal below, we see one network card, `ens5`, in addition to the loopback address.

<figure><img src="../.gitbook/assets/sss (1).PNG" alt=""><figcaption></figcaption></figure>

### Save the Captured Packets

To save the packets into a file use command `-w filename`

### Read Captured Packets from a File

To read packets from a file use `-r filename`

### Limit the Number of Captured Packets

To specify the nmber of packets to capture use `-c 666`

### Don't Resolve IP Addresses and Port Numbers

To avoid DNS lookups use `-n`&#x20;

To avoid port numbers being resolved use `-nn`

<figure><img src="../.gitbook/assets/Captusasasare.PNG" alt=""><figcaption><p>The difference between using the -n command and not using it</p></figcaption></figure>

### Summary and Examples

The table below provides a summary of the command line options that we covered.

<table><thead><tr><th width="257">Command</th><th>Explanation</th></tr></thead><tbody><tr><td><code>tcpdump -i INTERFACE</code></td><td>Captures packets on a specific network interface</td></tr><tr><td><code>tcpdump -w FILE</code></td><td>Writes captured packets to a file</td></tr><tr><td><code>tcpdump -r FILE</code></td><td>Reads captured packets from a file</td></tr><tr><td><code>tcpdump -c COUNT</code></td><td>Captures a specific number of packets</td></tr><tr><td><code>tcpdump -n</code></td><td>Don’t resolve IP addresses</td></tr><tr><td><code>tcpdump -nn</code></td><td>Don’t resolve IP addresses and don’t resolve protocol numbers</td></tr><tr><td><code>tcpdump -v</code></td><td>Verbose display; verbosity can be increased with <code>-vv</code> and <code>-vvv</code></td></tr></tbody></table>

Consider the following examples:

* `tcpdump -i eth0 -c 50 -v` captures and displays 50 packets by listening on the `eth0` interface, which is a wired Ethernet, and displays them verbosely.
* `tcpdump -i wlo1 -w data.pcap` captures packets by listening on the `wlo1` interface (the WiFi interface) and writes the packets to `data.pcap`. It will continue till the user interrupts the capture by pressing CTRL-C.
* `tcpdump -i any -nn` captures packets on all interfaces and displays them on screen without domain name or protocol resolution

## Filtering Expressions

<figure><img src="../.gitbook/assets/5f04259cf9bf5b57aed2c476-1723125963214.svg" alt=""><figcaption><p>Filtering</p></figcaption></figure>

#### Filtering by Host

Let’s say you are only interested in IP packets exchanged with your network printer or a specific game server. You can easily limit the captured packets to this host using `host IP` or `host HOSTNAME`

&#x20;It is **important** to note that capturing packets requires you to be logged-in as **`root` or to use `sudo`**.

If you want to limit the packets to those from a particular source IP address or hostname, you must use `src host IP` or `src host HOSTNAME`. Similarly, you can limit packets to those sent to a specific destination using `dst host IP` or `dst host HOSTNAME`.

#### Filtering by Port

`port #`

example: `sudo tcpdump -i ens5`` `**`port 53`**` ``-n`

This will capture all the packets sent to or from a specific number

You can limit the packets to those from a particular source port number or to a particular destination port number using `src port PORT_NUMBER` and `dst port PORT_NUMBER`, respectively.

#### Filtering by Procol

examples include: `ip`, `ip6`, `udp`, `tcp`, and `icmp`

example command line: `sudo tcpdump -i ens5 icmp -n`

#### Logical Operators

* `and`: Captures packets where both conditions are true. For example, `tcpdump host 1.1.1.1 and tcp` captures `tcp` traffic with `host 1.1.1.1`.
* `or`: Captures packets when either one of the conditions is true. For instance, `tcpdump udp or icmp` captures UDP or ICMP traffic.
* `not`: Captures packets when the condition is not true. For example, `tcpdump not tcp` captures all packets except TCP segments; we expect to find UDP, ICMP, and ARP packets among the results.

#### Summary and Examples

The table below offers a summary of the command line options that we covered.

<table><thead><tr><th width="333">Command</th><th>Explanation</th></tr></thead><tbody><tr><td><code>tcpdump host IP</code> or <code>tcpdump host HOSTNAME</code></td><td>Filters packets by IP address or hostname</td></tr><tr><td><code>tcpdump src host IP</code> or</td><td>Filters packets by a specific source host</td></tr><tr><td><code>tcpdump dst host IP</code></td><td>Filters packets by a specific destination host</td></tr><tr><td><code>tcpdump port PORT_NUMBER</code></td><td>Filters packets by port number</td></tr><tr><td><code>tcpdump src port PORT_NUMBER</code></td><td>Filters packets by the specified source port number</td></tr><tr><td><code>tcpdump dst port PORT_NUMBER</code></td><td>Filters packets by the specified destination port number</td></tr><tr><td><code>tcpdump PROTOCOL</code></td><td>Filters packets by protocol; examples include <code>ip</code>, <code>ip6</code>, and <code>icmp</code></td></tr></tbody></table>

* `tcpdump -i any tcp port 22` listens on all interfaces and captures `tcp` packets to or from `port 22`, i.e., SSH traffic.
* `tcpdump -i wlo1 udp port 123` listens on the WiFi network card and filters `udp` traffic to `port 123`, the Network Time Protocol (NTP).
* `tcpdump -i eth0 host example.com and tcp port 443 -w https.pcap` will listen on `eth0`, the wired Ethernet interface and filter traffic exchanged with `example.com` that uses `tcp` and `port 443`. In other words, this command is filtering HTTPS traffic related to `example.com`.
* `tcpdump -r filename.pcap icmp -n | wc -l` wil give you a list of all icmp packets in the filename.pcap and it'll give you a count of how many packets there `are`
* `tcpdump -r traffic.pcap arp and host 192.168.124.137 -n` to find the IP address of the host that asked for the MAC address of 192.168.124.137 (in a file )
* `tcpdump -r traffic.pcap port 53 -n` to see DNS packets in a file (because thats what port 53 does)

## Advanced Filtering

<figure><img src="../.gitbook/assets/5f04259cf9bf5b57aed2c476-1723126044024.svg" alt=""><figcaption><p>Advanced FIltering!</p></figcaption></figure>

Manual page accessed by `man pcap-filter`

### Filter by size:

#### **How It Works:**

When you use `greater <number>`, **tcpdump** filters packets where the total packet size exceeds the specified `<number>` in bytes. This size includes:

1. Layer 2 (Data Link Layer) headers (like Ethernet headers).
2. Layer 3 (Network Layer) headers (like IP headers).
3. Layer 4 (Transport Layer) headers (like TCP/UDP headers).
4. The actual payload of the packet.

* `greater LENGTH`: Filters packets that have a length (size in bytes) by greater than or equal to the specified length
* `less LENGTH`: Filters packets that have a length (size in bytes) less than or equal to the specified length

**`&` (And)** takes two bits and returns 0 unless both inputs are 1, as shown in the table below.

| Input 1 | Input 2 | Input1 `&` Input 2 |
| ------- | ------- | ------------------ |
| 0       | 0       | 0                  |
| 0       | 1       | 0                  |
| 1       | 0       | 0                  |
| 1       | 1       | 1                  |

**`|` (Or)** takes two bits and returns 1 unless both inputs are 0. This is shown in the table below.

| Input 1 | Input 2 | Input 1 `\|` Input 2 |
| ------- | ------- | -------------------- |
| 0       | 0       | 0                    |
| 0       | 1       | 1                    |
| 1       | 0       | 1                    |
| 1       | 1       | 1                    |

**`!` (Not)** takes one bit and inverts it; an input of 1 gives 0, and an input of 0 gives 1, as shown in the table below.

| Input 1 | `!` Input 1 |
| ------- | ----------- |
| 0       | 1           |
| 1       | 0           |



Using pcap-filter, Tcpdump allows you to refer to the contents of any byte in the header using the following syntax `proto[expr:size]`, where:

* `proto` refers to the protocol. For example, `arp`, `ether`, `icmp`, `ip`, `ip6`, `tcp`, and `udp` refer to ARP, Ethernet, ICMP, IPv4, IPv6, TCP, and UDP respectively.
* `expr` indicates the byte offset, where `0` refers to the first byte.
* `size` indicates the number of bytes that interest us, which can be one, two, or four. It is optional and is one by default.

To better understand this, consider the following two examples from the pcap-filter manual page (and don’t worry if you find them difficult):

* `ether[0] & 1 != 0` takes the first byte in the Ethernet header and the decimal number 1 (i.e., `0000 0001` in binary) and applies the `&` (the And binary operation). It will return true if the result is not equal to the number 0 (i.e., `0000 0000`). The purpose of this filter is to show packets sent to a multicast address. A multicast Ethernet address is a particular address that identifies a group of devices intended to receive the same data.\

* `ip[0] & 0xf != 5` takes the first byte in the IP header and compares it with the hexadecimal number F (i.e., `0000 1111` in binary). It will return true if the result is not equal to the (decimal) number 5 (i.e., `0000 0101` in binary). The purpose of this filter is to catch all IP packets with options.

The following TCP flags are available to compare with:

* `tcp-syn` TCP SYN (Synchronize)
* `tcp-ack` TCP ACK (Acknowledge)
* `tcp-fin` TCP FIN (Finish)
* `tcp-rst` TCP RST (Reset)
* `tcp-push` TCP Push

Few examples:

`tcpdump "tcp[tcpflags] == tcp-syn"` to capture TCP packets with **only** the SYN (Synchronize) flag set, while all the other flags are unset.

`tcpdump "tcp[tcpflags] & tcp-syn != 0"` to capture TCP packets with **at least** the SYN (Synchronize) flag set.

`tcpdump "tcp[tcpflags] & (tcp-syn|tcp-ack) != 0"` to capture TCP packets with **at least** the SYN (Synchronize) **or** ACK (Acknowledge) flags set.

## Displaying Packets

* `-q`: Quick output; print brief packet information
* `-e`: Print the link-level header
* `-A`: Show packet data in ASCII
* `-xx`: Show packet data in hexadecimal format, referred to as hex
* `-X`: Show packet headers and data in hex and ASCII

