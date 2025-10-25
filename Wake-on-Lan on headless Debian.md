
# The Quest for Wake-on-LAN: Adventures on Headless Debian

*Documented and narrated with the assistance of ChatGPT (GPT-5)*

---

## Prologue

I’m having a bit of fun with my headless Debian server.  
**Mission**: Figure out if I can wake it from sleep over the network using the *Magic Packet*

Challenges abound: VPN quirks, suspended SSH sessions, and mysterious PCIe devices that may or may not be my Ethernet card.

---

## Chapter 1: SSH Shenanigans

First, I tried connecting via SSH.  
Access kept being denied.

After some detective work:

- Noticed I was connected to ProtonVPN  
- Disconnecting solved the SSH access problem

**Lesson**: VPNs can be sneaky gatekeepers.

---

## Chapter 2: Suspenseful Suspension

Aftern being able to connect, me being a curious creature, I ran:

```
sudo systemctl suspend
```

No surprise: my SSH session dropped.  
The server was asleep. Mission failed—temporarily.

---

## Chapter 3: Enter the Magic Packets

**Goal**: Wake my Debian server remotely.

- Googled “wake-on-lan Debian”  
- Found `etherwake` and installed it  
- Opened Wireshark on my main PC to watch packets fly 

Attempted a magic packet with:

```
sudo etherwake [MAC]
```

Nada. Nothing. Silence.

---

## Chapter 4: Enabling Wake-on-LAN

Turns out WoL wasn’t enabled by default.  
Commands I used:

```
sudo ethtool enp1s0
sudo ethtool -s enp1s0 wol g
sudo ethtool enp1s0 | grep Wake
```

**Outcome**: `Wake-on: g` ✅  
Now the network card was ready for action.

---

## Chapter 5: Testing WoL

- Sent Debian back to sleep  
- Attempted:

```
sudo etherwake [MAC] -D
```

Still nothing.

Then:

```
wakeonlan -f [file with MAC address]
```

**Success!** The server woke.

---

## Fun Fact Learned

Port 9 on broadcast address `255.255.255.255` is used because:

- It’s mostly unused  
- WoL packets are one-way only  
- Your NIC ignores the port number but watches for the repeating MAC in the payload

ChatGPT added colorful commentary:

> “Port 9 is a funny little goblin of the networking world...”  
> “…wake up, you sleepy motherboard.”  
> “You’re very close to network necromancy. Fancy seeing if your NIC is part of that PXSX secret society?”

---

## Chapter 6: ACPI Wake Permissions

Checked which devices are allowed to wake the system:

```
cat /proc/acpi/wakeup | grep enabled
```

Learned about some of the key devices:

| Code | Typical Hardware         | What it means for wake events                  |
|------|--------------------------|-----------------------------------------------|
| PS2K | PS/2 Keyboard controller | Hitting a key could wake the system           |
| XHC  | USB 3.0 controller       | Any USB wake-capable device (mouse jiggle)    |
| RP05 | PCIe Root Port           | A pathway for wake events from PCIe devices   |
| PXSX | PCIe device behind a port| Often a GPU or Ethernet card                  |

Also used `last reboot` and `uptime` to track uptime and reboot history.  
Poweroff testing revealed that WoL settings do not persist by default.

---

## Chapter 7: Identifying the Ethernet NIC

ACPI dump helped locate my NIC:

```
GLAN      S5
```

This is the one responsible for Wake-on-LAN.

---

## Chapter 8: Persisting WoL Across Reboots

**Problem**: After poweroff, `Wake-on: g` would reset to `d`.

**Solution**: Create a systemd service:

```
sudo nano /etc/systemd/system/wol-enp1s0.service
```

**Contents:**

```
[Unit]
Description=Enable Wake-on-LAN for enp1s0
After=network-online.target
Wants=network-online.target

[Service]
Type=oneshot
ExecStart=/usr/sbin/ethtool -s enp1s0 wol g
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```

**Commands to activate:**

```
sudo systemctl daemon-reload
sudo systemctl enable wol-enp1s0.service
sudo systemctl start wol-enp1s0.service
```

**Poweroff and check:**

```
sudo ethtool enp1s0 | grep -i "Wake-on"
```

**Outcome**: `Wake-on: g` ✅ Success. Persistent WoL achieved.

---

## Chapter 9: Lessons Learned

- VPNs can silently block SSH access.  
- Suspend drops network sessions.  
- WoL requires both NIC support and ACPI permission.  
- Port 9 is the magic goblin of networking.  
- `ethtool` is indispensable for checking and enabling WoL.  
- Persistence after poweroff requires a systemd service.  
- ChatGPT sometimes gets… whimsical.

---

## Epilogue

My headless Debian server now:

- Sleeps on command  
- Wakes on magic packets  
- Remembers to do so after a full poweroff

**Tools learned and used:**

- SSH  
- `systemctl suspend/poweroff`  
- `ethtool`  
- `etherwake` / `wakeonlan`  
- Wireshark  
- `/proc/acpi/wakeup`

---

## Document Authorship

Created through my exploration and testing,  
and narrated with the help of ChatGPT (GPT-5),  
who occasionally indulged in network necromancy commentary.

---

### Bellow are my original notes
```
having fun with my headless debian

 tried connecting via ssh, at firrst my acces kept denied, then I've noticed I'm connected to a Proton vpn. I don't remember that ever being a problem, but after disconnecting, ssh works.
 
 tried sudo systemctl suspend to see if it would kick me out of my ssh, and no surprise it did.
 wanted to see if I can wake my debian server with a magic packet
 googled how to do that and found etherwake - installed that
openedup wireshark to see the magic packet flying 
 didn't work, so had to enable wake on lan
 "sudo ethtool enp1s0"
 "sudo ethtool -s enp1s0 wol g" to enable
 "sudo ethtool enp1s0 | grep Wake" to check if it says "g" now = yes

sent debian back to sleep
"sudo etherwake [mac] -D"
nothing - no luck
"wakeonlan -f [file with mac addres]"  = success
learned about port 9 on broadcast address 255.255.255.255
Also my chatgpt lost its marbles and without any prompt talks like this"Port 9 is a funny little goblin of the networking world..." and “wake up, you sleepy motherboard” "You’re very close to network necromancy. Fancy seeing if your NIC is part of that PXSX secret society?"

"cat /proc/acpi/wakeup | grep enabled" to see which devices allow waking
learnt about 
Code	Typical Hardware	What it means for wake events
PS2K	PS/2 Keyboard controller	Hitting a key could wake the system
XHC	USB 3.0 controller	Any USB wake-capable device (mouse jiggle, USB dongle magic)
RP05	PCIe Root Port	A pathway for wake events from devices plugged into specific PCIe slots
PXSX	A PCIe device behind one of those ports	Very often a GPU or Ethernet card

learnt new command "last reboot" and "uptime" "sudo systemctl poweroff"


reboot   system boot  6.12.48+deb13-am Fri Oct 24 15:26 - still running
reboot   system boot  6.12.48+deb13-am Fri Oct 24 14:05 - 15:25  (01:20)
reboot   system boot  6.12.48+deb13-am Wed Oct 22 19:20 - 20:53  (01:33)
reboot   system boot  6.12.48+deb13-am Wed Sep 24 12:47 - 08:54 (27+20:06)
reboot   system boot  6.12.48+deb13-am Wed Sep 24 12:40 - 12:45  (00:04

checked whether a poweroff would would keep the wakeonlan setting and nope
"cat /proc/acpi/wakeup" and output into chatgtp to tell me which one is ethernet = GLAN S5

after poweroff the setting would always revert back to no wake on lan so did this: 
Method A: Create a systemd service

Create a new service file, e.g.
sudo nano /etc/systemd/system/wol-enp1s0.service
Inside the service file put something like:
[Unit]
Description=Enable Wake-on-LAN for enp1s0
After=network-online.target
Wants=network-online.target

[Service]
Type=oneshot
ExecStart=/usr/sbin/ethtool -s enp1s0 wol g
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target

Make sure the path to ethtool is correct (you can confirm with which ethtool).

The After=network-online.target helps ensure the network interface is up before the command runs.

RemainAfterExit=yes ensures that systemd treats the service as “done but staying active” so it doesn’t get repeated unexpectedly.

Reload systemd, enable and start the service:
sudo systemctl daemon-reload
sudo systemctl enable wol-enp1s0.service
sudo systemctl start wol-enp1s0.service

poweroff and check:

sudo ethtool enp1s0 | grep -i "Wake-on"

You should see Wake-on: g. If you instead see Wake-on: d, something ran after your service and reset it (may need adjusting).

Success
