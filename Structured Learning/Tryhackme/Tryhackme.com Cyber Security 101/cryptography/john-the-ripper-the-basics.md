---
description: https://tryhackme.com/r/room/johntheripperbasics
---

# John the Ripper: The Basics

[https://www.openwall.com/john/doc/](https://www.openwall.com/john/doc/)

John the Ripper is a free and open-source password-cracking tool. It can crack passwords stored in various formats, including hashes, passwords, and encrypted private keys. It can be used to test passwords' security and recover lost passwords.

## Cracking Hashes

It's good idea to identify what kind hash you're working with.&#x20;

To use hash-identifier, you can use `wget` or `curl` to download the Python file `hash-id.py` from its GitLab [page](https://gitlab.com/kalilinux/packages/hash-identifier/-/raw/kali/master/hash-id.py). Then, launch it with `python3 hash-id.py` and enter the hash you’re trying to identify. It will give you a list of the most probable formats.&#x20;

Once you have identified the hash that you’re dealing with, you can tell John to use it while cracking the provided hash using the following syntax:

`john --format=[format] --wordlist=[path to wordlist] [path to file]`

**Example Usage:**

`john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt hash_to_crack.txt`

You might need to add a prefix like shown above "raw" to md5 . To check if you need a prefix:

&#x20;you can search `john --list=formats | grep -iF "md5"`.

#### Windows Authentication hashes got a separate tab on THM so I'm making a note on this&#x20;

it's the NT hash&#x20;

## Unshadowing

eli5: takes 2 files and smashes them together for John to crack wide open

`unshadow [path to passwd] [path to shadow]`

* `unshadow`: Invokes the unshadow tool
* `[path to passwd]`: The file that contains the copy of the `/etc/passwd` file you’ve taken from the target machine
* `[path to shadow]`: The file that contains the copy of the `/etc/shadow` file you’ve taken from the target machine

**Example Usage:**

unshadow local\_passwd local\_shadow > **unshadowed.txt**

This creates the file needed for John to use to crack the password

john --wordlist=/usr/share/wordlists/rockyou.txt --format=sha512crypt unshadowed.txt

## Single Crack Mode

### World Mangling

John builds a dictionary based on the information you provide it with a set of rules called the **mangling rules.** This mutates the input as seen bellow.

Consider the username “Markus”.

Some possible passwords could be:

* Markus1, Markus2, Markus3 (etc.)
* MArkus, MARkus, MARKus (etc.)
* Markus!, Markus$, Markus\* (etc.)

### GECOS (General Electric Comprehensive Operating System)

If you look at the files of `/etc/shadow` and `/etc/passwd`  you'll see entries seperated by a colon `:`

The fifth field in the user account record is the GECOS field. It stores info about the user: full name, office number, telephone number and more.&#x20;

John can take all this information and adds it to a wordlist when cracking /etc/shadow hashes with single crack mode.

### Using Single crack Mode

`john --single --format=[format] [path to file]`

**Example Usage:**

`john --single --format=raw-sha256 hashes.txt`

If you’re cracking hashes in single crack mode, you need to change the file format that you’re feeding John for it to understand what data to create a wordlist from. You do this by prepending the hash with the username that the hash belongs to, so according to the above example, we would change the file `hashes.txt`

**From** `1efee03cdcb96d90ad48ccc7b8666033`

**To** `mike:1efee03cdcb96d90ad48ccc7b8666033`

## Custom Rules

[https://www.openwall.com/john/doc/RULES.shtml](https://www.openwall.com/john/doc/RULES.shtml)

[https://akimbocore.com/article/custom-rules-for-john-the-ripper/](https://akimbocore.com/article/custom-rules-for-john-the-ripper/)

Similar to Single Crack Mode, but with added difficulty :smile: If you have an idea of what the password might be, you can configure John to start guessing based on what you provide with.

To add a new rule, you'll need to add it to  `/opt/john/john.conf`&#x20;

You need to start with `[List.Rules:NameOfYourRule]`

and then under neath this you would add your special rules as shown bellow

Basic rules:

* `Az`: Takes the word and appends it with the characters you define (suffix)
* `A0`: Takes the word and prepends it with the characters you define (prefix)
* `c`: Capitalises the character positionally

These can be used in combination to define where and what in the word you want to modify.

Lastly, we must define what characters should be appended, prepended or otherwise included. We do this by adding character sets in square brackets `[ ]` where they should be used. These follow the modifier patterns inside double quotes `" "`. Here are some common examples:

* `[0-9]`: Will include numbers **0-9**
* `[0]`: Will include only the number **0**
* `[A-z]`: Will include both **upper** and **lowercase**
* `[A-Z]`: Will include only **uppercase** letters
* `[a-z]`: Will include only **lowercase** letters

Please note that:

* `[a]`: Will include only `a`
* `[!£$%@]`: Will include the symbols `!`, `£`, `$`, `%`, and `@`

Putting this all together, to generate a wordlist from the rules that would match the example password `Polopassword1!` (assuming the word `polopassword` was in our wordlist), we would create a rule entry that looks like this:

`[List.Rules:PoloPassword]`

`cAz"[0-9] [!£$%@]"`

Utilises the following:

* `c`: Capitalises the first letter
* `Az`: Appends to the end of the word
* `[0-9]`: A number in the range 0-9
* `[!£$%@]`: The password is followed by one of these symbols

In CLI you'd then use  `john --wordlist=[path to wordlist]`` `**`--rule=PoloPassword`**` ``[path to file]`

## Zip2John

1\) `zip2john zipfile.zip > zip_hash.txt`

2\) `unzip zipfile.zip`&#x20;

3\) You'll be asked for a password . Put in the password you've discovered

4\) Read the files

## Cracking Password-Protected RAR archive

Same as Zip2John but with RAR!

1\) `rar2john rarfile.rar > rar_hash.txt`&#x20;

2\) `unrar e -pPASSWORD FILE.rar` (yes, there's no space between the -p and the password )

3\) Read the files

## Cracking SSH Key Password

Same syntax as before unles you don’t have `ssh2john` installed, you can use `ssh2john.py`, located in the `/opt/john/ssh2john.py`. If you’re doing this on the AttackBox, replace the `ssh2john` command with `python3 /opt/john/ssh2john.py` or on Kali, `python /usr/share/john/ssh2john.py`.

1\) `ssh2john id_rsa_file > id_rsa.txt` (or `/opt/john/ssh2john.py id_rsa > id_rsa_hash.txt`)

2\) `john --wordlist=/usr/share/wordlists/rockyou.txt id_rsa_hash.txt`

3\) You'll see the password highlighted in yellow&#x20;



Further Reading:

[https://www.openwall.com/john/](https://www.openwall.com/john/)





