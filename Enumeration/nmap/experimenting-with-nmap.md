---
description: 'experimenting with some of the option Nmap provides:'
---

# Experimenting with nmap

shows a whole load of packets being sent from my ip and various ports to the target IP and various ports

```
--packet-trace #explanation is always above
```

shows reason why port is open and what type of packet was sent as well as Time To Live of each packet

```
--reason
```

produced the same result as when using straight up "nmap target"

```
-- priviliged & -- unpriviliged 
```

tried the "not intrusive" script. Interestingly enough, I think it found more stuff about my network than about the target

```
--script "not intrusive"
```





