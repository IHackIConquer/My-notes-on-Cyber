---
description: https://tryhackme.com/room/sqlfundamentals
---

# SQL Fun.damentals

Structured Query Language

<figure><img src="../../.gitbook/assets/66c513e4445cb5649e636a36-1727686918382.png" alt=""><figcaption><p><a href="https://tryhackme.com/room/sqlfundamentals">https://tryhackme.com/room/sqlfundamentals</a></p></figcaption></figure>

Within a database you'll find tables. Within tables, there are columns and rows. Columns are the "categories" while rows are the one specific thing.

### Primary Keys & Foreign Keys

<figure><img src="../../.gitbook/assets/66c513e4445cb5649e636a36-1727686918373 (1).png" alt=""><figcaption><p>These provide a link between databases</p></figcaption></figure>

## SQL Commands

To get started:

```bash
mysql -u root -p
```

all sql commands must end with this ---> **;**

```sql
show databases;                          # To see a list of databases
use name_of_database;                    # To interact with the database
create database name_of_new_database;    # Create a new database
drop database name_of_database;          # To delete a database
show tables;                             # Shows all tables within a database
describe name_of_table;                  # Shows what columns are within a table
alter table name_of_table ADD new_column;# Add new column to a table
drop table table_name;                   # Removes a table
```

<figure><img src="../../.gitbook/assets/sql.PNG" alt=""><figcaption></figcaption></figure>



### Create Operation

{% code overflow="wrap" %}
```sql
INSERT INTO books (id, name, published_date, description)
    VALUES (1, "Android Security Internals", "2014-10-14", "An In-Depth Guide to Android's Security Architecture");
```
{% endcode %}

### Read Operation (select)

```sql
select * from name_of_table;         # The * will retrieve all columns from the table
```

### Update Operation&#x20;

{% code overflow="wrap" %}
```sql
UPDATE books
    SET description = "Not so In-Depth Guide to Android's Security Architecture."
    WHERE id = 1;     
    
# The UPDATE statement specifies the table, in this case, books, and then we can use  SET followed by the column name we will update. The WHERE clause specifies which row to update when the clause is met, in this case, the one with id 1.
```
{% endcode %}

### Delete Operation

```sql
DELETE FROM books WHERE id = 1;
# Delete a row from "books" with the id = 1
```

### Clauses

### Distinct Clause

<pre class="language-sql" data-overflow="wrap"><code class="lang-sql">SELECT DISTINCT name FROM books;
<strong>#The DISTINCT clause in SQL is used to retrieve only unique values from a query's result set, eliminating duplicate rows. It's used with the SELECT statement to ensure that each returned value appears only once, regardless of how many times it might appear in the underlying table
</strong></code></pre>

### Group by clause

<pre class="language-sql" data-overflow="wrap"><code class="lang-sql"><strong>SELECT name, COUNT(*)
</strong>    FROM books
    GROUP BY name;
#The GROUP BY statement groups rows that have the same values into summary rows, like "find the number of customers in each country".
</code></pre>

### Order by clause

{% code overflow="wrap" %}
```sql
 SELECT *
    FROM books
    ORDER BY published_date ASC;
# This sorts all items in the "books" table by "published_date" in ascending order.
# The ORDER BY clause in SQL sorts the results of a query in a specified order, either ascending or descending, based on one or more columns
```
{% endcode %}

{% code overflow="wrap" %}
```sql
SELECT *
    FROM books
    ORDER BY published_date DESC;
# This sorts all items in the "books" table by "published_date" in descending order.

```
{% endcode %}

### Having Clause

{% code overflow="wrap" %}
```sql
SELECT name, COUNT(*)
    FROM books
    GROUP BY name
    HAVING name LIKE '%Hack%';
# This will show any books that containt thw word "hack in the name". Results in picture 1
# The HAVING clause is used with other clauses to filter groups or results of records based on a condition. In the case of GROUP BY, it evaluates the condition to TRUE or FALSE, unlike the WHERE clause HAVING filters the results after the aggregation is performed.
```
{% endcode %}

<figure><img src="../../.gitbook/assets/sqqs.PNG" alt=""><figcaption><p>Picture 1</p></figcaption></figure>

{% code overflow="wrap" %}
```sql
SELECT description, COUNT(*)     FROM books     GROUP BY description    HAVING description LIKE '%guide%';
# shows all the description that contain the word "guide" but not the books...not very helpful. Let's see if I can find a command that shows the books whose description contain the word guide. See picture 2 
```
{% endcode %}

<figure><img src="../../.gitbook/assets/sqqq.PNG" alt=""><figcaption><p>Picture 2</p></figcaption></figure>

{% code overflow="wrap" %}
```sql
SELECT name, description
FROM books
WHERE description LIKE '%guide%';
# Shows all books whos descriptions contains the word "guide". See picture 3.
```
{% endcode %}

<figure><img src="../../.gitbook/assets/ssqs.PNG" alt=""><figcaption><p>Picture 3</p></figcaption></figure>

{% code overflow="wrap" %}
```sql
SELECT * FROM hacking_tools where category = "Multi-tool" and  description like "%geeks%";
# Finds records in the hacking_tools table in the Multi_tool category with the description containing "geeks"

SELECT * FROM hacking_tools where category = "Multi-tool" and  description like "%geeks%" AND description like "%pentesters%";
# Finds records in the hacking_tools table in the Multi_tool category with the description containing "geeks" and "pentesters"



```
{% endcode %}

### OR operator

{% code overflow="wrap" %}
```sql
SELECT * FROM hacking_tools where category = "Multi-tool" and  description like "%tool%" OR  description like "%usb%";
 #Finds records in the hacking_tools table in the Multi_tool category with the description containing either "tools" OR "usb"
```
{% endcode %}

<figure><img src="../../.gitbook/assets/d2qw.PNG" alt=""><figcaption><p>OR statement</p></figcaption></figure>

### More Operators

{% code overflow="wrap" %}
```sql
SELECT *
    FROM books
    WHERE category != "Offensive Security";
     # select books that ARENT in the Offensive security category
    
SELECT * 
    FROM hacking_tools 
    WHERE amount >= 300;
    # Select tools where amount is 300 or above

    
SELECT *
    FROM books
    WHERE published_date >= "2021-11-02";
    # Select books where published after January 1, 2020
```
{% endcode %}

## Functions

### LEnGTH()

{% code overflow="wrap" %}
```sql
SELECT name,LENGTH(name) AS name_length FROM hacking_tools;
# This function returns the number of characters in a string. This includes spaces and punctuation. We can find an example below.
```
{% endcode %}

<figure><img src="../../.gitbook/assets/sqqqsss.PNG" alt=""><figcaption></figcaption></figure>

### SUM()

{% code overflow="wrap" %}
```sql
select sum(amount) as total_number_of_tools from hacking_tools;
#This function sums all values (not NULL) of a determined column.
```
{% endcode %}

### COUNT()

{% code overflow="wrap" %}
```sql
SELECT COUNT(*) AS total_books FROM books;
#This function returns the number of records within an expression, as the example below shows.
```
{% endcode %}

### MAX() & MIN()

{% code overflow="wrap" %}
```sql
SELECT MAX(published_date) AS latest_book FROM books;
#This function calculates the maximum value within a provided column in an expression.

SELECT MIN(published_date) AS earliest_book FROM books;
#This function calculates the minimum value within a provided column in an expression.

```
{% endcode %}

### SUBSTRING()

{% code overflow="wrap" %}
```sql
SELECT SUBSTRING(published_date, 1, 4) AS published_year FROM books;
#This function will retrieve a substring from a string within a query, starting at a determined position. The length of this substring can also be specified.
```
{% endcode %}

### CONCAT()

{% code overflow="wrap" %}
```sql
SELECT CONCAT(name, " is a type of ", category, " book.") AS book_info FROM books;
# This function is used to add two or more strings together. It is useful to combine text from different columns.
```
{% endcode %}

<figure><img src="../../.gitbook/assets/conca.PNG" alt=""><figcaption></figcaption></figure>

{% code overflow="wrap" %}
```sql
SELECT CONCAT(name, " is a type of ", description,".") AS "Tool Details" FROM hacking_tools;
# Add the name + "is a type of " + description + "." and creates Tool Details table.
```
{% endcode %}

<figure><img src="../../.gitbook/assets/s1a.PNG" alt=""><figcaption></figcaption></figure>

{% code overflow="wrap" %}
```sql
SELECT CONCAT(name, " falls under the category of ", category, ", it's used as ", description,"."" Currently in stock: ", amount) AS "Tool Details" FROM hacking_tools;

# This command add the name, category, description and the amount into one long output.
```
{% endcode %}

<figure><img src="../../.gitbook/assets/sqssaq.PNG" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/ssasa.PNG" alt=""><figcaption></figcaption></figure>

### GROUP\_CONCAT()

<pre class="language-sql" data-overflow="wrap"><code class="lang-sql">SELECT category, GROUP_CONCAT(name SEPARATOR ", ") AS books
    FROM books
    GROUP BY category;
<strong>#This function can help us to concatenate data from multiple rows into one field
</strong></code></pre>

## Final question in this room

### Using the `tools_db` database, what are the tool names where the amount does not end in 0, and group the tool names concatenated by " & ".

I had to use chatgpt to look into this as I couldnt figure how to find amount that doesn't end in 0

{% code overflow="wrap" %}
```sql
SELECT GROUP_CONCAT(name SEPARATOR ' & ') AS combined_tools
FROM hacking_tools
WHERE amount % 10 != 0;
# This is the prefered way of doing things.
SELECT name
FROM hacking_tools
WHERE RIGHT(amount, 1) != '0';
#This works too, but isn't as "clean"
# If someone else reads amount % 10 != 0, they instantly understand: “Ah, checking if the last digit is 0.”
#But if they see RIGHT(amount, 1) != '0', they might pause and think, “Wait, are we checking strings now?”
SELECT GROUP_CONCAT(name SEPARATOR ' & ') AS combined_tools
FROM hacking_tools
WHERE SUBSTRING(amount, -1) != '0';
#Another way of doing things, but according to ChatGPT, not as good as "amount % 10 != 0"
```
{% endcode %}
