# ACER Headless Debian Setup & Notes

Some random notes from messing around with my headless Debian box (an old Acer machine). Mostly just things I had to learn the hard way.

## Disclosure
This write-up (including this disclosure) was reformatted by chat GPT for GitHub Markdown readability:
- Added **headings** and a **table of contents** for navigation.  
- Cleaned up formatting (code blocks, bullet points, spacing).  
- Did minimal proofreading for grammar/clarity, but kept the original casual tone.  
- No technical details were changed — all commands, outputs, and observations remain as originally written
- See bellow to find the original text
---

## Table of Contents
- [Getting Started](#getting-started)
- [Jellyfin Setup](#jellyfin-setup)
- [Terminal Quality-of-Life](#terminal-quality-of-life)
- [Firewall & Networking](#firewall--networking)
- [External USB HDD (1TB)](#external-usb-hdd-1tb)
- [Experiment: Playing a Movie Over SSH](#experiment-playing-a-movie-over-ssh)
- [Next Steps / Things To Try](#next-steps--things-to-try)

---

## Getting Started

- Debian didn’t have `sudo` out of the box, so I had to learn to use `su`.  
  Installed sudo with:  
  ```bash
  apt install sudo
  ```

- Learned how to reboot from the command line:  
  ```bash
  sudo systemctl start reboot.target
  ```

- Added my user to the sudo group:  
  ```bash
  sudo adduser casper sudo
  ```

- Installed curl:  
  ```bash
  sudo apt install curl
  ```

---

## Jellyfin Setup

- Installed Jellyfin using the repo’s script:  
  ```bash
  curl https://repo.jellyfin.org/install-debuntu.sh | sudo bash
  ```

- Jellyfin was missing a dependency (`libicu`), so I had to install it manually.

- Learned that `ifconfig` isn’t available by default → used `ip address` instead.

- Tried to start Jellyfin by typing `jellyfin`.  
  Correct way is:  
  ```bash
  sudo systemctl start jellyfin
  ```

---

## Terminal Quality-of-Life

- Installed tmux so I could scroll in the terminal:  
  ```bash
  sudo apt install tmux
  ```
  - Scroll mode: `Ctrl + b` then `[` → use arrow keys.  

- Alternative:  
  ```bash
  command | less
  ```
  Exit with `q`.

---

## Firewall & Networking

- Decided to try out UFW (Uncomplicated Firewall):  
  ```bash
  sudo ufw enable
  sudo ufw allow 8086
  ```
  ✅ Did this successfully.

- Connected from my Kali laptop → Acer headless via SSH.

- Learned how to view live connections using `ss` on both machines.  
  Noted peer address as `56820`.

---

## External USB HDD (1TB)

- Plugged in the drive and used `lsblk` to identify it.

- Created mount point + mounted it:  
  ```bash
  sudo mkdir /mnt/usb
  sudo mount /dev/sdb1 /mnt/usb
  ```

- Realized no NTFS support by default → installed `ntfs-3g`:  
  ```bash
  sudo apt install ntfs-3g
  sudo mount -t ntfs-3g /dev/sdb1 /mnt/usb
  ```

- Drive mounted successfully 🎉

---

## Experiment: Playing a Movie Over SSH

- Tried streaming a movie from the Acer box to my laptop via SSH + VLC:  
  ```bash
  ssh user@LT2 "cat /path/to/movie.mp4" | vlc -
  ```

- Failed at first because VLC wasn’t installed →  
  ```bash
  sudo apt install vlc
  ```

- Path with spaces was a pain (quotes didn’t help). Eventually tested with a different AVI file that worked.

- Managed to get **sound only**, no video. VLC threw a codec error.  

---

## Next Steps / Things To Try
- Fix the VLC codec issue so I get video, not just audio.
- Clean up how I mount drives (maybe set up auto-mounts).
- Harden SSH + firewall rules.
- Properly configure Jellyfin and stream media over the network instead of hacking it with `ssh | vlc`.

## Original notes, using Notepad++
```
ACER headless Debian

learn to use "su" because "sudo wasn't a thing here
"apt install sudo"
learnt a command line way of rebooting "sudo systemctl start reboot.target"

"sudo adduser casper sudo"
had to "sudo apt install curl"

"curl https://repo.jellyfin.org/install-debuntu.sh | sudo bash"
had to installl libicu as jellyfin was missing it.
learnt "ifconfig" isn't a thing here, instead it's "ip address"
tried starting jellyfin by just typing "jellyfin". The correct way is "sudo systemctl start jellyfin"
installed tmux "sudo apt install tmux" so i can scroll up in the terminal. "ctrl + b" and then "[" and then up and down arrows 
alternatively use "command | less" then "q" to exit
Maybe look at ufw(firewall)? "sudo ufw enable" "sudo ufw allow 8086"
Did this ^^
connected from my kali laptop to ACER headless via ssh
Looked up how to see all current connections  - used "ss" to view the live connection on both machines
noted the peer address is "56820"

Plugged in the ext usb hdd 1TB
"lsblk" to identify device's name
create a mount point with "sudo mkdir /mnt/usb and mount the drive using "sudo mount /dev/sdb1 /mnt/usb"
discovered there's no support for ntfs, so installed ntfs-3g "sudo apt install ntfs-3g" 
mount the drive using ntfs-3g "sudo mount -t ntfs-3g /dev/sdb1 /mnt/usb"
Drive succesfully mounted
Had a go at playing a film via ssh "ssh user@LT2 "cat /path/to/movie.mp4" | vlc -"
This was unnusuccesful because I realised vlc aint installed so "sudo apt install vlc"
Struggled to get the correct path right, as the name was had a lot of spaces and even with additional speech marks and quotations marks I couldnt get it working. Luckily found a different avi file that I was able to play.
Soundly only, no video, vlc outputted an error message about codecs
```
