---
description: https://tryhackme.com/room/pythonbasics
---

# THM Python

<pre class="language-python"><code class="lang-python"># Code to calcute shipping + cost and if shipping is free (THM code)
shipping_cost_per_kg = 1.20
customer_basket_cost = 34
customer_basket_weight = 44

<strong>if(customer_basket_cost >= 100):
</strong>  print('Free shipping!')
else:
  shipping_cost = customer_basket_weight * shipping_cost_per_kg
  customer_basket_cost = shipping_cost + customer_basket_cost

print("Total basket cost including shipping is " + str(customer_basket_cost))
</code></pre>

```python
# Code to calcute shipping + cost and if shipping is free (My code)
shipping_cost_per_kg = 1.20 
customer_basket_cost = 34
customer_basket_weight = 44

if customer_basket_cost >=100:
  print("FREE SHIPPING")
else:
  shipping_cost = customer_basket_weight * shipping_cost_per_kg
  grand_total = shipping_cost + customer_basket_cost
  
  print("Your grand total, inclduing shipping is: £" + str(grand_total))
```



```python
# Code to calculate if overall investment in bitcoin is above or bellow $30,000
investment_in_bitcoin = 1.2
bitcoin_to_usd = 14000

def bitcoinToUSD(bitcoin_amount, bitcoin_value_usd):
  usd_value = bitcoin_amount * bitcoin_value_usd
  return usd_value

investment_in_usd = bitcoinToUSD(investment_in_bitcoin, bitcoin_to_usd)
if investment_in_usd <= 30000:
  print("Investment below $30,000! SELL!")
else:
  print("Investment above $30,000")
```





```python
# This opens a file in the same directory in the Read mode 
with open("flag.txt", "r") as file:
    contents = file.read()
    print(contents)
    
file = open("flag.txt", "r")
contents = file.read()
print(contents)
file.close()
```

Here are some popular libraries you may find useful in scripting as a pentester:

Might need to use Pip like a so: `pip install scapy`,&#x20;

* Request - simple HTTP library.
* [Scapy](https://scapy.readthedocs.io/en/latest/introduction.html) - send, sniff, dissect and forge network packets
* [Pwntools](https://docs.pwntools.com/en/stable/) - a CTF & exploit development library.
