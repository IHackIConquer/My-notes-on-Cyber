---
description: https://tryhackme.com/room/javascriptessentials
---

# Javascript  Essentials

## Abusing Dialogue Functions

### Alert window

```javascript
alert("Hello THM")     # shows a dialogue window with the message Hello THM
```

```javascript
# Annoying little script that displays the message "Hacked" 500 times
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Hacked</title>
</head>
<body>
    <script>
        for (let i = 0; i < 500; i++) {
            alert("Hacked");
        }
    </script>
</body>
</html>
```

### Prompt - Opens a window with a text field for user to enter data

```javascript
name = prompt("What is your name?");
    alert("Hello " + name);
```

### Confirm - window with a "cancel" and "OK"&#x20;

```javascript
confirm("Do you want to proceed?")
```

## Conditional statement

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Age Verification</title>
</head>
<body>
    <h1>Age Verification</h1>
    <p id="message"></p>

    <script>
        age = prompt("What is your age")
        if (age >= 18) {
            document.getElementById("message").innerHTML = "You are an adult.";
        } else {
            document.getElementById("message").innerHTML = "You are a minor.";
        }
    </script>
</body>
</html>
```

### A terrible example of how not to store credentials :relaxed:

<pre class="language-javascript"><code class="lang-javascript"><strong>&#x3C;!DOCTYPE html>
</strong>&#x3C;html lang="en">
&#x3C;head>
    &#x3C;title>Login Page&#x3C;/title>
&#x3C;/head>
&#x3C;body>
    &#x3C;h2>Login Authentication&#x3C;/h2>

    &#x3C;script>
        let username = prompt("Enter your username:");
        let password = prompt("Enter your password:");

        if (username === "admin" &#x26;&#x26; password === "ComplexPassword") {
            document.write("You are successfully authenticated!");
        } else {
            document.write("Authentication failed. Incorrect username or password.");
        }
    &#x3C;/script>
&#x3C;/body>
&#x3C;/html>

</code></pre>

## Exploring Minified Files & Obfuscator

{% embed url="https://codebeautify.org/javascript-obfuscator" %}

Obfuscator above takes a simple code like this:

```javascript
function hi() {
  alert("Welcome to THM");
}
hi();
```

And makes it unreadable for humans. It's the same code. But just scrambled.

{% code overflow="wrap" %}
```javascript
function _0x3bcb(_0x6fd682,_0x32612c){var _0x57d9e3=_0x228d();return _0x3bcb=function(_0x281877,_0x57a842){_0x281877=_0x281877-(0x1d47+-0x1*-0x1f21+-0x3a87*0x1);var _0x1f9ed1=_0x57d9e3[_0x281877];return _0x1f9ed1;},_0x3bcb(_0x6fd682,_0x32612c);}(function(_0x2e6ceb,_0x31fef2){var _0x1422ba=_0x3bcb,_0x4d8a14=_0x2e6ceb();while(!![]){try{var _0x137e2c=-parseInt(_0x1422ba(0x1e9))/(0x2072+0x1ea5*-0x1+-0x1cc)+-parseInt(_0x1422ba(0x1ea))/(0x2319+0x1ff7+-0x430e)*(parseInt(_0x1422ba(0x1e1))/(-0xd1b+-0x1d19+0x2a37))+parseInt(_0x1422ba(0x1e5))/(0x1*-0x14b7+0x1*-0x115d+0x2618)+parseInt(_0x1422ba(0x1ec))/(-0x217e+-0x61d*0x1+0x13d0*0x2)+-parseInt(_0x1422ba(0x1e4))/(0x152f+0x3e6+-0x190f)+parseInt(_0x1422ba(0x1e2))/(0x2470+-0x2210+0x259*-0x1)+parseInt(_0x1422ba(0x1e3))/(0x104f+-0x1*-0x20ed+0x10c*-0x2f);if(_0x137e2c===_0x31fef2)break;else _0x4d8a14['push'](_0x4d8a14['shift']());}catch(_0x3cd0e4){_0x4d8a14['push'](_0x4d8a14['shift']());}}}(_0x228d,0x98729+-0x2*0x11b85+0x2c430));function hi(){var _0x11e568=_0x3bcb,_0x4d2952={'fvTjV':function(_0x53ddea,_0x702ba8){return _0x53ddea(_0x702ba8);},'QIEge':_0x11e568(0x1e6)+_0x11e568(0x1e8)};_0x4d2952[_0x11e568(0x1eb)](alert,_0x4d2952[_0x11e568(0x1e7)]);}function _0x228d(){var _0x5ca9c7=['139797cFRjma','7351855Vubkzx','3861984BJpTyw','5843610BDMZNN','2464220slaMDb','Welcome\x20to','QIEge','\x20THM','181039zjyaag','36EswSZp','fvTjV','2526235aRBwTl'];_0x228d=function(){return _0x5ca9c7;};return _0x228d();}hi();
```
{% endcode %}

### Deobfuscate

{% embed url="https://obf-io.deobfuscate.io/" %}

Use this tool to unscrabmle the code. It will literaly reverse the proccess
