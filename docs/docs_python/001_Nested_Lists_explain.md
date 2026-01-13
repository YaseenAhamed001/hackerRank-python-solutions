# Nested Lists
---
## HackerRank URL: https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true 
---
## **Query 01:**  How can I sort it with respect to marks (second value of every inner list): `python_students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]`  Explain the sorted function arguments?
---
### General syntax of sorted()
### `sorted(iterable, key=None, reverse=False)`

**1️⃣ iterable**

This is the data you want to sort.
In your case:

`python_students` It’s a list of lists:

`
[['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
`

**2️⃣ key**

The key argument tells Python what value to use for sorting.

`key=lambda x: x[1]`

What does this mean?

x represents one inner list at a time. x[1] is the second element (the marks). So for each student:

```python
['Harry', 37.21]  → key = 37.21
['Berry', 37.21]  → key = 37.21
['Tina', 37.2]    → key = 37.2
```
Python sorts the list based on these key values, not the full sublist.
---
**👉 Think of it like:** 

“Sort the students by their marks”
---
**3️⃣ reverse**

Controls sorting order.

```python
reverse=False   # default → ascending
reverse=True    # descending
```
Example:

`sorted(python_students, key=lambda x: x[1], reverse=True)`

This sorts from highest marks to lowest.

**Step-by-step internal view**

When Python runs:

`sorted(python_students, key=lambda x: x[1])`


Internally, it sees something like:
```python
[
  (37.21, ['Harry', 37.21]),
  (37.21, ['Berry', 37.21]),
  (37.2,  ['Tina', 37.2]),
  (41,    ['Akriti', 41]),
  (39,    ['Harsh', 39])
]
```

It sorts using the first value of each tuple (the key), then removes the keys.

Multiple sorting conditions: 

`
sorted(python_students, key=lambda x: (x[1], x[0]))
`

This means: ***Sort by marks (x[1]) If marks are equal, sort by name (x[0])***

### | Difference between `sorted()` and `.sort()` |

| Feature | `sorted()` | `.sort()` |
|---------|------------|-----------|
| Returns | Returns a new list | Modifies original list |
| Works on | Any iterable | Only lists |
| Notes | `iterable` → what to sort <br> `key` → by what value <br> `reverse` → in which order | Same parameters, but sorts in place |

---
---
## **Query 02:** Explain the mentioned lines of code in the code below: 
```python
if __name__ == '__main__':
    python_students = []
    scores = set()

    for _ in range(int(input())):
        name = input()
        score = float(input())
        python_students.append([name, score])
        scores.add(score)

    # get second lowest score
    sorted_scores = sorted(scores)
    second_lowest = sorted_scores[1]
```
>>>**Explain the below code in detail:**
```python
    # print names with second lowest score
    for student in python_students:
        if student[1] == second_lowest:
            print(student[0])
```
---

**1️⃣ for student in python_students:**

python_students is a list of lists, like:
```python
[
    ['Harry', 37.21],
    ['Berry', 37.21],
    ['Tina', 37.2],
    ['Akriti', 41],
    ['Harsh', 39]
]
```

Each time the loop runs, student becomes one inner list. Example iterations:
```python
student = ['Harry', 37.21]
student = ['Berry', 37.21]
student = ['Tina', 37.2]
```
So:
```python
student[0] → name
student[1] → score
```
**2️⃣ if student[1] == second_lowest:**

`student[1] → the student’s score`

`second_lowest → a number (e.g. 37.21)`

This line checks: **“Is this student’s score equal to the second lowest score?”**

Example:

`if 37.21 == 37.21:  # True`

**3️⃣ print(student[0])**

`student[0] → the student’s name`

So if the condition is true, it prints the name.

**🔄 Full logic in plain English**

Go through each student. If the student’s score is the second lowest, Print that student’s name

**One-line version (just for learning)**
```python 
print(student[0] for student in python_students if student[1] == second_lowest)
```

---
---
## **Query 03:** Is there any way to fix the following code without using extra for loop for printing name in alphabetic order:
```python
if __name__ == '__main__':
    python_students = []
    scores = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        python_students.append([name, score])
        scores.add(score)
    sorted_scores = sorted(list(scores))
    
    for i in python_students:
        print(i[0]) if i[1] == sorted_scores[1] else ""
```
---

**Yes — you can fix this without adding another for loop, but there’s an important limitation to understand first.**

👉 You cannot print names in alphabetical order if you iterate over an unsorted list.
So the trick is: sort before the loop, not after.

**✅ Minimal change (no extra loop)**

Sort python_students by name first, then reuse your loop:
```python
if __name__ == '__main__':
    python_students = []
    scores = set()

    for _ in range(int(input())):
        name = input()
        score = float(input())
        python_students.append([name, score])
        scores.add(score)

    sorted_scores = sorted(scores)

    # sort students alphabetically by name
    python_students.sort(key=lambda x: x[0])

    for i in python_students:
        print(i[0]) if i[1] == sorted_scores[1] else ""
```

**🧠 Why this works**

`python_students.sort(key=lambda x: x[0])`

- sorts in place
- orders students alphabetically by name

The existing loop: `for i in python_students:` now visits students in alphabetical order

Your condition still filters: `i[1] == sorted_scores[1]`

- ✅ Same loop
- ✅ No extra loop
- ✅ Alphabetical output

**📌 Example Output**
```python
Berry
Harry
```

**⚠️ Important note (for interviews / HackerRank)**

Your current print style: `print(i[0]) if condition else ""` is valid but un-Pythonic.

Preferred:
```python
if i[1] == sorted_scores[1]:
    print(i[0])
```
(Logic is identical, readability is better.)

**Final takeaway 🧠**

If you don’t want an extra loop, sort the data structure itself before iterating.

---
---
## **Query 04:** Explain this in more detail as I have never used sort() function like this , such that using **key and lambda**:
```python
# sort students alphabetically by name
    python_students.sort(key=lambda x: x[0])
```
---

**Great question — this is an important Python concept, and I’ll explain it from zero, slowly and clearly 👍**

The line we’re explaining 
`python_students.sort(key=lambda x: x[0])`

**1️⃣ What is sort()?**

sort() is a list method that:
- sorts the list in place (modifies the original list)
- returns nothing

**Example:**
```python
nums = [3, 1, 2]
nums.sort()
print(nums)   # [1, 2, 3]
```

---
**2️⃣ Why plain sort() is NOT enough here**

Your list is:
```python
python_students = [
    ['Harry', 37.21],
    ['Berry', 37.21],
    ['Tina', 37.2],
    ['Akriti', 41],
    ['Harsh', 39]
]
```

If you do: `python_students.sort()`

Python sorts the inner lists as whole objects, comparing: ['Harry', 37.21] vs ['Berry', 37.21]

This happens to sort by name, but:
- it’s not explicit
- it’s unreliable for complex data
- it’s bad practice

We want to clearly say: *“Sort by name only”* 

---
**3️⃣ What does key mean?**

Think of key as: **“Which value should Python use to sort each item?”**

Syntax: `list.sort(key=some_function)`

Python:
- Takes each element of the list
- Applies some_function to it
- Uses the returned value for sorting

---
**4️⃣ What is lambda?** A lambda is a small anonymous function (a function without a name).

Normal function:

`def get_name(student):`
>    `return student[0]`

Lambda version (same logic):

`lambda student: student[0]`

Meaning: *“Take a student and return their name”*

---
**5️⃣ Breaking the line into human language**

`python_students.sort(key=lambda x: x[0])`

Read it like this:
- Sort python_students
- For each student x
- Use x[0] (the name) as the sorting value

---
**6️⃣ Step-by-step internal working**

Python internally does something like this:
```python
Student	Key (x[0])
['Harry', 37.21]	"Harry"
['Berry', 37.21]	"Berry"
['Tina', 37.2]	"Tina"
['Akriti', 41]	"Akriti"
['Harsh', 39]	"Harsh"

#Then it sorts by the key values:

Akriti
Berry
Harsh
Harry
Tina
```

Final list becomes:
```python
[
    ['Akriti', 41],
    ['Berry', 37.21],
    ['Harsh', 39],
    ['Harry', 37.21],
    ['Tina', 37.2]
]
```
---
**7️⃣ Without lambda (same behavior)**

If lambdas feel confusing, this is equivalent:
```python
def get_name(student):
    return student[0]

python_students.sort(key=get_name)
```
---
**8️⃣ Common patterns you’ll see often**
| Task | Code |
|------|------|
| Sort by name | `key=lambda x: x[0]` |
| Sort by score | `key=lambda x: x[1]` |
| Sort by score then name | `key=lambda x: (x[1], x[0])` |
| Descending order | `sort(..., reverse=True)` |

**🧠 One sentence takeaway**

*key=lambda x: x[0] tells Python exactly which part of each item should be used for sorting.*

---
---
## **Query 05:** Is there an optimise way of solving this question. Please dont make it more complex and hard to understand by using way too much shortcuts:
```python
if __name__ == '__main__':
    python_students = []
    scores = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        python_students.append([name, score])
        scores.add(score)
        
    sorted_scores = sorted(list(scores))
    python_students.sort(key = lambda x : x[0])
    
    for i in python_students:
        print(i[0]) if i[1] == sorted_scores[1] else ""
```

**Absolutely! Your current solution is already simple and readable, but we can make it slightly more optimized without making it harder to understand. The goal is:**
- Avoid creating unnecessary lists
- Avoid sorting twice if possible

Here’s an optimized but still very readable version:

**Optimized Solution**
```python
if __name__ == '__main__':
    python_students = []

    # Read input
    for _ in range(int(input())):
        name = input()
        score = float(input())
        python_students.append([name, score])

    # Find second lowest score
    scores = {student[1] for student in python_students}  # set comprehension
    second_lowest = sorted(scores)[1]  # get second lowest

    # Sort students alphabetically and print those with second lowest score
    for student in sorted(python_students, key=lambda x: x[0]):
        if student[1] == second_lowest:
            print(student[0])
```
---
**✅ What’s improved**

- No extra scores set creation inside loop
  
`scores = {student[1] for student in python_students}`
- This is a set comprehension
- Collects all scores in one line, avoids appending inside a loop
- Sort and filter in a single loop

`for student in sorted(python_students, key=lambda x: x[0]):`
- Sorts students alphabetically while iterating
- No separate python_students.sort() call needed

**Still readable. Every step is clear:**
- Read input
- Find second lowest score
- Print students with that score in alphabetical order. 

This keeps it simple, readable, and slightly more efficient than your original code.

---
---
## **Query 06:** Make it more readable without adding much code:
```python
for student in sorted(python_students, key=lambda x: x[0]):
        if student[1] == second_lowest:
            print(student[0])
```
---

**Absolutely! You can make it more readable by splitting the logic clearly instead of putting everything in one line. Here's a simple, readable version without adding extra loops:**
```python
# Sort students alphabetically by name
sorted_students = sorted(python_students, key=lambda x: x[0])

# Print students with second lowest score
for student in sorted_students:
    if student[1] == second_lowest:
        print(student[0])
```
**✅ Why this is more readable**

- sorted_students clearly shows that we sorted the list, instead of doing it inside the for loop.
- The for loop is clean: just iterates over the sorted list and checks the score.
- Easy for anyone reading the code to understand: sort → filter → print.


---
---
## **Query 07:** Why didnt you use sort()? Is there any particular reason you avoid it?


**Ah! Good question — there is a reason I suggested sorted() instead of sort(), and it comes down to clarity, readability, and flexibility. Let me explain carefully.**

**1️⃣ Difference between `list.sort()` and `sorted()`**

| Feature | `list.sort()` | `sorted()` |
|--------|---------------|------------|
| Sorts in place | ✅ Modifies original list | ❌ Returns a new sorted list |
| Works on any iterable | ❌ Only works on lists | ✅ Works on lists, tuples, sets, etc. |
| Returns value | `None` | New sorted list |
---

**Example:**
```python
a = [3, 1, 2]

b = sorted(a)   # b = [1, 2, 3], a unchanged
a.sort()        # a = [1, 2, 3], returns None
```
---
**2️⃣ Why I suggested sorted() in your loop**
```python
for student in sorted(python_students, key=lambda x: x[0]):
    if student[1] == second_lowest:
        print(student[0])
```

Reasons:

Doesn’t modify the original list
- sorted() creates a temporary sorted list just for the loop
- Original python_students stays unchanged, which can help avoid bugs if you need the original order later

Readable in a single statement
- It’s immediately clear: we are iterating over the alphabetically sorted list

Flexible

- You can pass any iterable (even a set or tuple) and it works
- sort() only works on lists, so sometimes sorted() is safer

---
**3️⃣ When would sort() be better?**

If you don’t need the original list order anymore, sort() is slightly faster and more memory-efficient:
```python
python_students.sort(key=lambda x: x[0])
for student in python_students:
    if student[1] == second_lowest:
        print(student[0])
```

- Modifies python_students in place
- No extra list is created
- Slightly more memory efficient, but behaviorally identical

---
**✅ Summary**

- `sorted()` → good for readability, temporary sorted view, flexible

- `sort()` → good for in-place sorting if you don’t care about original list order
  
---
---
