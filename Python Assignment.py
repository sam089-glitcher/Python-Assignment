#!/usr/bin/env python
# coding: utf-8

# In[1]:


list1 = list(map(int, input().split()))
if len(set(list1)) < 2:
    print()
else:
    list1.sort()
    print(list1[-2])


# In[3]:


user_input = input()
_list = list(map(int, user_input.split()))
new = list(set(_list))
print(new)


# In[4]:


user_input = input()
lst = list(map(int, user_input.split()))
total = sum(lst)
average = total / len(lst)
print("Sum is:", total, "Average is:", average)


# In[5]:


num = int(input("Enter a number: "))
is_prime = num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))
print("Is prime:", is_prime)


# In[6]:


bolo = input("Enter string: ")
vowels = 0
consonants = 0
digits = 0
special = 0
for ch in bolo:
    if ch.lower() in 'aeiou':
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    else:
        special += 1
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Special Characters:", special)


# In[10]:


for i in range(1, 101):
    if i % 2 == 0:
        print(i, end=" ")


# In[14]:


num = int(input())
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


# In[15]:


lst = [i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0]
print(lst)


# In[16]:


num=input()
print(num[::-1])


# In[17]:


s = input()
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)


# In[19]:


n = int(input())
primes = []
i = 2
while len(primes) < n:
    if all(i % p != 0 for p in primes):
        primes.append(i)
    i += 1
print(primes)


# In[23]:


n=input()
print(n == n[::-1])


# In[1]:


user_input = input()
lst = user_input.split()
element = input("Enter the element to count: ")
count = lst.count(element)
print(f"{element} appears {count} time(s) in the list.")


# In[2]:


square=[i*i for i in range (2,51,2)]
print(square)


# In[1]:


user_input = input()
lst = user_input.split()
unique_list = []
for item in lst:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list)


# In[2]:


def is_even(n):
    return n % 2 == 0
num = int(input())
print(is_even(num))


# In[6]:


def cumulative_sum(numb):
    result = []
    total = 0
    for num in numb:
        total += num
        result.append(total)
    return result
user_input = input()
numbers = list(map(int, user_input.split()))
cum_sum = cumulative_sum(numbers)
print("Cumulative sum:", cum_sum)


# In[7]:


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
num = int(input("number: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {num} is {factorial(num)}")


# In[8]:


def fibonacci_series(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
num = int(input("number of term: "))
if num <= 0:
    print("Please enter a positive integer.")
else:
    print(f"Fibonacci series up to {num} terms:")
    fibonacci_series(num)


# In[56]:


def is_palindrome(s):
    return s == s[::-1]
bolo_ji = input("Enter a string: ").strip().lower()
if is_palindrome(bolo_ji):
    print(f"'{bolo_ji}'is palindrome.")
else:
    print(f"'{bolo_ji}'not palindrome.")


# In[12]:


def find_max_min(lst):
    return max(lst), min(lst)
user_input = input()
numbers = list(map(int, user_input.split()))
maximum, minimum = find_max_min(numbers)
print("Maximum:", maximum)
print("Minimum:", minimum)


# In[13]:


def is_pangram(s):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return set(s.lower()) >= alphabet
text = input("Enter sentence: ")
if is_pangram(text):
    print("pangram.")
else:
    print("not a pangram.")


# In[14]:


def find_primes(start, end):
    return [n for n in range(start, end+1) if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1))]
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print(find_primes(start, end))


# In[15]:


def count_case_letters(s):
    upper = sum(1 for ch in s if ch.isupper())
    lower = sum(1 for ch in s if ch.islower())
    return upper, lower
text = input("Enter a string: ")
upper, lower = count_case_letters(text)
print(upper)
print(lower)


# In[17]:


def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))
num = int(input("Enter a number: "))
print(sum_of_digits(num))


# In[18]:


def count_words(sentence):
    return len(sentence.split())
say = input("Enter a sentence: ")
print(count_words(say))


# In[20]:


def remove_punctuation(text):
    punct = '''!()-[]{};:'",<>./?@#$%^&*_~'''
    result = ""
    for ch in text:
        if ch not in punct:
            result += ch
    return result

bol = input("Enter a string: ")
print(remove_punctuation(bol))


# In[21]:


def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
num1 = int(input("first number: "))
num2 = int(input("second number: "))
print("GCD is:", find_gcd(num1, num2))


# In[22]:


def find_duplicates(lst):
    return list(set([x for x in lst if lst.count(x) > 1]))
user_input = input("Enter list elements separated by space: ")
lst = user_input.split()
print("Duplicate elements:", find_duplicates(lst))


# In[23]:


def largest_of_three(a, b, c):
    return max(a, b, c)
x = int(input())
y = int(input())
z = int(input())
print(largest_of_three(x, y, z))


# In[51]:


sentence = input("Enter a sentence: ")
words = sentence.split()
words.sort()
print("Sorted words:", words)


# In[24]:


dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged = {**dict1, **dict2}
print("Concatenated dictionary:", merged)


# In[25]:


sentence = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
for word in sentence.split():
    count = sum(1 for ch in word if ch in vowels)
    print(f"{word}: {count} vowel(s)")


# In[50]:


tup = tuple(input().split())
lst = list(tup)
print("Converted list:", lst)


# In[ ]:


def remove_whitespace(s):
    return s.replace(" ", "")

text = input("Enter string: ")
print("Without whitespace:", remove_whitespace(text))


# In[26]:


keys = input("Enter keys: ").split()
values = input("Enter values: ").split()
merged_dict = dict(zip(keys, values))
print("Merged dictionary:", merged_dict)


# In[ ]:


n = int(input("How many key-value pairs do you want to enter? "))
data = {}
for _ in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    data[key] = value
max_key = max(data, key=data.get)
print("Key with maximum value:", max_key)


# In[27]:


sentence = input()
words = sentence.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print("Word frequencies:", freq)


# In[ ]:


n = int(input("How many key-value pairs do you want to enter? "))
d = {}

for _ in range(n):
    k = input("Enter key: ")
    v = input("Enter value: ")
    d[k] = v
key = input("Enter key to check: ")
print("Exists:" if key in d else "Does not exist")


# In[28]:


s = input()
result = ''.join('*' if ch in 'aeiouAEIOU' else ch for ch in s)
print(result)


# In[41]:


filename = input("Enter the filename to read: ")

try:
    # Try to open and read the file
    with open(filename, "r") as file:
        content = file.read()
        print("\nFile contents:\n")
        print(content)

except FileNotFoundError:
    print(f"\nError: The file '{filename}' does not exist.")
    create = input("Do you want to create this file? (yes/no): ")
    
    if create.lower() == 'yes':
        data = input("Enter content to write in the new file: ")
        with open(filename, "w") as file:
            file.write(data)
        print(f"File '{filename}' created successfully.")
    else:
        print("File not created.")


# In[40]:


filename = "eg.txt"
try:
    with open(filename, "w") as file:
        file.write("Python is a powerful programming language.\nIt is easy to learn and use.")
    print(f"File '{filename}' created and written successfully.")
except Exception as e:
    print("Error writing to file:", e)
try:
    with open(filename, "r") as file:
        content = file.read()
        words = content.split()
        word_count = len(words)

    print("\n--- File Contents ---")
    print(content)
    print("\nTotal number of words:", word_count)
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("Error reading file:", e)


# In[38]:


# Create a source file with some content
with open("source.txt", "w") as f:
    f.write("This is the source file.\nIt contains some lines.\nTo be copied!")

# Now copy to destination file
source_file = "source.txt"
destination_file = "destination.txt"

with open(source_file, "r") as src:
    content = src.read()

with open(destination_file, "w") as dst:
    dst.write(content)

print("Contents copied successfully!")

source_file = input("Enter the source file name: ")
destination_file = input("Enter the destination file name: ")

try:
    with open(source_file, "r") as src:
        content = src.read()
    with open(destination_file, "w") as dest:
        dest.write(content)

    print("File copied successfully.")
except FileNotFoundError:
    print("Error: Source file not found.")
except Exception as e:
    print("An error occurred:", e)


# In[37]:


with open("example.txt", "w") as f:
    f.write("This is a short line.\n")
    f.write("This is a very long line that definitely has more than fifty characters in total.\n")
    f.write("Another small one.\n")
    f.write("Here is another long line that should be printed because it's long enough.\n")

filename = input("Enter the file name: ")

try:
    with open(filename, "r") as file:
        print("\nLines with more than 50 characters:\n")
        for line in file:
            if len(line.strip()) > 50:
                print(line.strip())
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("An error occurred:", e)


# In[43]:


try:
    filename = input("Enter filename to create: ")

    # Get number of lines from user
    n = int(input("How many lines do you want to write? "))
    lines = []
    for i in range(n):
        line = input(f"Enter line {i+1}: ")
        lines.append(line)
    with open(filename, "w") as file:
        for line in lines:
            file.write(line + "\n")

    print(f"\nFile '{filename}' created and lines written successfully.")

except Exception as e:
    print("An error occurred:", e)


# In[44]:


try:
    a = int(input("first number: "))
    b = int(input("second number: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero isn't allowed.")


# In[45]:


try:
    num = int(input("Enter a number: "))
    print(num)
except ValueError:
    print("Invalid input! Please enter a valid number.")


# In[46]:


try:
    filename = input("Enter filename to open: ")
    with open(filename, "r") as file:
        content = file.read()
        print("File content:\n", content)
except FileNotFoundError:
    print("Error: File not found.")


# In[48]:


numbers = input()

try:
    index = int(input("Enter an index to access: "))
    print("Value at index", index, "is", numbers[index])
except IndexError:
    print("Error: Index out of range.")


# In[49]:


try:
    x = int(input())
    y = 10 / x
    print(y)
except ZeroDivisionError:
    print("Caught division by zero error.")
finally:
    print("This block always runs (finally).")


# In[ ]:




