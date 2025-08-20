---
description: 'Notes on Linux scripting with #!/bin/bash from TryHackMe.com'
---

# 🍕 Linux Scripting

## Creating script file:

```bash
nano first_script.sh
```

Start every script with shebang like this:

<pre class="language-bash"><code class="lang-bash"><strong>#!/bin/bash
</strong></code></pre>

### Before running a script for the first time:

#### 1) Give it permission by:

<pre class="language-bash"><code class="lang-bash"><strong>chmod +x first_script.sh
</strong></code></pre>

2\) To run the script add ./

```
./first_script.sh
```

## Variables

{% code lineNumbers="true" %}
```shell
# Defining the Interpreter 
#!/bin/bash
echo "Hey, what’s your name?"
read name
echo "Welcome, $name"
```
{% endcode %}

The script above displays a string on the screen: "Hey, what’s your name?” This is done by `echo` command. The second line of the script contains the code `read name`. `read` is used to take input from the user, and `name` is the variable in which the input would be stored. The last line uses `echo` to display the welcome line for the user, along with its name stored in the variable.

## Loops

{% code lineNumbers="true" %}
```bash
# Defining the Interpreter 
#!/bin/bash
for i in {1..10};
do
echo $i
done
```
{% endcode %}

The first line has the variable `i` that will iterate from 1 to 10 and execute the below code every time. `do` indicates the start of the loop code, and `done` indicates the end. In between them, the code we want to execute in the loop is to be written. The for loop will take each number in the brackets and assign it to the variable `i` in each iteration. The `echo $i` will display this variable’s value every iteration.

## The IF statement

{% code lineNumbers="true" %}
```shell
# Defining the Interpreter 
#!/bin/bash
echo "Please enter your name first:"
read name
if [ "$name" = "Stewart" ]; then
        echo "Welcome Stewart! Here is the secret: THM_Script"
else
        echo "Sorry! You are not authorized to access the secret."
fi
```
{% endcode %}

## Comments

If the code is getting lengthy and complicated it's good practice to start adding comments

{% code lineNumbers="true" %}
```bash
# Defining the Interpreter
#!/bin/bash

# Asking the user to enter a value.
echo "Please enter your name first:"

# Storing the user input value in a variable.
read name

# Checking if the name the user entered is equal to our required name.
if [ "$name" = "Stewart" ]; then

# If it equals the required name, the following line will be displayed.
echo "Welcome Stewart! Here is the secret: THM_Script"

# Defining the sentence to be displayed if the condition fails.
else
        echo "Sorry! You are not authorized to access the secret."
fi
```
{% endcode %}

## Putting all I've learned together into a simple locker script&#x20;

&#x20;Asks a user to input Username, Company name and a PIN. If all credentials are correct, shows the balance of gold coins                                                                                                                                     &#x20;

<pre class="language-bash" data-title="locker_script.sh" data-line-numbers><code class="lang-bash">#!/bin/bash

#This determines the variables
username=""
companyname=""
pin=""

#the loop
for i in {1..3}; do
#conditional statements of the loop
if [ "$i" -eq 1 ]; then
        echo "Enter your Username:"
        read username
elif [ "$i" -eq 2 ]; then
        echo "Enter your Company name:"
            read companyname
else
    echo "Enter your PIN:"
<strong>    read pin
</strong>fi
done
#checking if user entered the correct details
if [ "$username" = "Alesh" ] &#x26;&#x26; [ "$companyname" = "Tryhackme" ] &#x26;&#x26; [ "$pin" = "9191" ]; then
echo "  Authentication Successful. You can now access your locker, $username." &#x26;&#x26; echo "        You have over 9999 Gold coins!"
else
echo "  Authentication Denied,$username!"
fi
</code></pre>

## A Search Script

This script searches for a specific keyword in all the files (with .log extension) in a specific directory.

{% code title="flag_hunt.sh" lineNumbers="true" %}
```bash
#!/bin/bash

# Defining the directory to search our flag
directory="/var/log"

# Defining the flag to search
flag="thm-flag01-script"

echo "Flag search in directory: $directory in progress..."

# Defining for loop to iterate over all the files with .log extension in the defined directory
for file in "$directory"/*.log; do
 # Check if the file contains the flag
if grep -q "$flag" "$file"; then
 # Print the filename
echo "Flag found in: $(basename "$file")"
fi
done
```
{% endcode %}

To run the script:

```bash
./flag_hunt.sh
```

How to search the file:

```bash
grep "cat" /var/log/authentication.log
```
