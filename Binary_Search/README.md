# 🔍 Binary Search

### 🐍 Python | Data Structures & Algorithms | LeetCode

A structured collection of **Binary Search concepts and LeetCode problems solved in Python**, focusing on efficient searching, search space reduction, boundary handling, rotated arrays, and Binary Search on Answer patterns.

---

## 📌 About Binary Search

**Binary Search** is an efficient searching algorithm used primarily on **sorted or monotonic data**.


Instead of checking every element one by one, Binary Search repeatedly divides the search space into half and eliminates the half that cannot contain the answer.

---
### ⚡ Complexity Comparison

| Searching Technique | Time Complexity |
|---|---:|
| Linear Search | `O(n)` |
| Binary Search | `O(log n)` |

Binary Search significantly improves searching performance when the search space can be divided into smaller parts.

---

## 🎯 Learning Objectives

Through this topic, I aim to understand:

- 🔹 Basic Binary Search
- 🔹 Search Space Reduction
- 🔹 `left`, `right`, and `mid` pointers
- 🔹 Searching in sorted arrays
- 🔹 Finding insertion positions
- 🔹 First and last occurrence
- 🔹 Boundary-based Binary Search
- 🔹 Searching in rotated sorted arrays
- 🔹 Finding minimum and maximum using Binary Search
- 🔹 Binary Search on Answer
- 🔹 Handling edge cases
- 🔹 Time and Space Complexity optimization

---

## 🧩 Core Idea

The basic idea of Binary Search is:

```text
Search Space
     ↓
Find Middle Element
     ↓
Compare with Target
     ↓
 ┌───┴───┐
 ↓       ↓
Left    Right
Half    Half
 ↓       ↓
Eliminate the unnecessary half
```
---

## 🧩 Binary Search Patterns

Binary Search can be applied using different patterns depending on the problem.

The major patterns are:

### 1️⃣ Basic Binary Search

Used to find a specific target in a sorted array.

```text
Sorted Array
     ↓
Find Middle
     ↓
Compare Target
     ↓
Eliminate Half
     ↓
Repeat
     ↓
Target Found / Search Space Empty
```

### 2️⃣ Boundary Search

Used when we need to find a specific position or boundary instead of simply finding an element.

Common applications:

- First occurrence
- Last occurrence
- First valid position
- Last valid position
- Lower Bound
- Upper Bound


### 3️⃣ Binary Search in Rotated Arrays

Used when a sorted array has been rotated.

Example:

```text
Original:
[1, 2, 3, 4, 5, 6, 7]

Rotated:
[4, 5, 6, 7, 1, 2, 3]
```
### 4️⃣ Binary Search on Answer

Instead of searching for an element, we search for the minimum or maximum possible answer.

This pattern is commonly used in optimization problems.

Examples include:

Minimum time
Minimum capacity
Minimum speed
Maximum distance
Maximum possible value


General idea:
``` text
Possible Answers
       ↓
   Find Middle
       ↓
   Check Validity
      ↙    ↘
    Yes    No
     ↓      ↓
Search    Search
Better    Other
Answer    Half
```
---

## 🔑 Basic Binary Search Template
``` text
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1


    while left <= right:
        mid = left + (right - left) // 2


        if nums[mid] == target:
            return mid


        elif nums[mid] < target:
            left = mid + 1


        else:
            right = mid - 1


    return -1

```
---
### 📌 Template Breakdown
left → Starting index of the search space
right → Ending index of the search space
mid → Middle index
Compare nums[mid] with the target
Eliminate half of the search space
Continue until the target is found or the search space becomes empty

---

### ⏱️ Complexity

For an array containing n elements:
```text
Time Complexity  → O(log n)
Space Complexity → O(1)
```

Each iteration eliminates approximately half of the remaining search space.

---

## 📚 Important Binary Search Concepts

### 🔹 1. Search Space

The **search space** is the range in which we are currently looking for the answer.

It is generally represented using:

```python
left = 0
right = len(nums) - 1

```
After every comparison, a part of the search space is eliminated.

### 🔹 2. Middle Element

The middle index is calculated using:
```text
mid = left + (right - left) // 2
```
This is preferred over:
```text
mid = (left + right) // 2
```
because it avoids potential integer overflow in languages where integer size is limited.

### 🔹 3. Left and Right Boundaries

The boundaries determine the current search range.
```text
left                         right
 ↓                              ↓
[  1   3   5   7   9   11   13  ]
             ↑
            mid
```            

Depending on the comparison:

``` text
left = mid + 1
```
or
```text
right = mid - 1
```
### 🔹 4. Loop Condition

The most common Binary Search condition is:

```text
while left <= right:
```
This is generally used when both boundaries are inclusive.

Another common form is:

```text
while left < right:
```
This is useful in certain boundary-based Binary Search problems.

The correct condition depends on the specific problem and search-space definition.

---
## ⚠️ Common Mistakes

While implementing Binary Search, avoid these common mistakes:

- ❌ Using Binary Search on an unsuitable search space
- ❌ Incorrect calculation of `mid`
- ❌ Forgetting `+1` or `-1` while updating boundaries
- ❌ Using the wrong loop condition
- ❌ Causing an infinite loop
- ❌ Accessing an invalid index
- ❌ Ignoring edge cases
- ❌ Returning the wrong boundary

---
### 🧪 Edge Cases

Always consider the following cases:

Empty Array
Single Element
Target at First Index
Target at Last Index
Target Not Present
Target Smaller Than All Elements
Target Greater Than All Elements
Duplicate Elements
Rotated Sorted Array

Testing edge cases helps ensure that the Binary Search implementation handles all possible inputs correctly.

---
### 📈 Complexity Analysis

Binary Search repeatedly divides the search space into approximately half.

For n elements:
```text
1st iteration → n / 2
2nd iteration → n / 4
3rd iteration → n / 8
       ↓
       ↓
       ↓
Final         → 1
```
Therefore:
```text
Time Complexity  → O(log n)
Space Complexity → O(1)
```
For a recursive implementation, the auxiliary space can be:
```text
Space Complexity → O(log n)
```
because of the recursive call stack.

---
# 📚 LeetCode Practice

This section contains the Binary Search problems solved as part of my DSA practice.

The problems are organized according to their difficulty and the Binary Search pattern they demonstrate.

---

## 🟢 Easy Problems

| # | LeetCode Problem | Pattern |
|---|---|---|
| 704 | Binary Search | Basic Binary Search |
| 35 | Search Insert Position | Boundary Search |
| 69 | Sqrt(x) | Binary Search on Answer |
| 278 | First Bad Version | Boundary Search |

---

## 🟡 Medium Problems

| # | LeetCode Problem | Pattern |
|---|---|---|
| 34 | Find First and Last Position of Element in Sorted Array | Boundary Search |
| 33 | Search in Rotated Sorted Array | Rotated Array |
| 81 | Search in Rotated Sorted Array II | Rotated Array |
| 153 | Find Minimum in Rotated Sorted Array | Rotated Array |
| 162 | Find Peak Element | Binary Search |
| 74 | Search a 2D Matrix | Binary Search |
| 540 | Single Element in a Sorted Array | Binary Search |
| 875 | Koko Eating Bananas | Binary Search on Answer |
| 1011 | Capacity To Ship Packages Within D Days | Binary Search on Answer |
| 1283 | Find the Smallest Divisor Given a Threshold | Binary Search on Answer |
| 1482 | Minimum Number of Days to Make m Bouquets | Binary Search on Answer |
| 1552 | Magnetic Force Between Two Balls | Binary Search on Answer |

---

## 🔴 Hard Problems

| # | LeetCode Problem | Pattern |
|---|---|---|
| 4 | Median of Two Sorted Arrays | Advanced Binary Search |
| 410 | Split Array Largest Sum | Binary Search on Answer |

---

## 🧠 Recommended Learning Order

The problems should be practiced in the following order:

```text
Basic Binary Search
        ↓
Search Insert Position
        ↓
Boundary Search
        ↓
Rotated Sorted Array
        ↓
Find Minimum / Peak
        ↓
Binary Search on Answer
        ↓
Advanced Binary Search
```
---
## 🛠️ Problem-Solving Approach

When solving a Binary Search problem, follow these steps:

### Step 1️⃣ — Identify the Search Space

Determine what part of the input contains the possible answer.

```text
left → Starting Point
right → Ending Point
```
### Step 2️⃣ — Check the Condition

Ask yourself:

Is the array sorted?
Is the search space monotonic?
Can half of the search space be eliminated?
Am I searching for an element or an answer?

### Step 3️⃣ — Calculate Middle

Use:

```text
mid = left + (right - left) // 2
```
### Step 4️⃣ — Compare and Eliminate

Compare the middle element or answer with the required condition.
```text
Target == nums[mid]
        ↓
     Answer


Target > nums[mid]
        ↓
    Move Right


Target < nums[mid]
        ↓
     Move Left
```
### Step 5️⃣ — Update Boundaries

For the right half:
```text
left = mid + 1
```
For the left half:
```text
right = mid - 1
```
---
### Step 6️⃣ — Handle Edge Cases

Before submitting the solution, test:

Empty input
Single element
Target at beginning
Target at end
Target not present
Target smaller than all elements
Target greater than all elements
Duplicate values
Rotated arrays

### Step 7️⃣ — Analyze Complexity

Always determine:
```text
Time Complexity
Space Complexity
```

For standard iterative Binary Search:
```text
Time  → O(log n)
Space → O(1)
```
---
### 💡 Key Takeaways

The most important concepts to remember are:

Binary Search works by reducing the search space.
A sorted or monotonic search space is usually required.
Always maintain correct left and right boundaries.
Calculate mid carefully.
Choose the correct loop condition.
Boundary problems require extra attention to left and right.
Rotated arrays require identifying the sorted half.
Binary Search on Answer searches over possible answers instead of array elements.
Correct edge-case handling is essential.

---
### 🎯 Interview Preparation

Binary Search is one of the most important DSA patterns for technical interviews.

Interviewers commonly test:

Basic Binary Search
Search Insert Position
First and Last Occurrence
Rotated Sorted Arrays
Peak Element
Binary Search on Answer
Optimization problems
Advanced Binary Search

The goal is not only to memorize the Binary Search template, but to understand **when and why Binary Search can be applied.**

---

📂 Folder Structure
```text
Binary Search/
│
├── README.md
│
├── 704-binary-search.py
├── 35-search-insert-position.py
├── 69-sqrt-x.py
├── 278-first-bad-version.py
│
├── 34-find-first-and-last-position.py
├── 33-search-in-rotated-sorted-array.py
├── 153-find-minimum-in-rotated-sorted-array.py
└── ...
```
---

### 🚀 Progress Tracker
 Basic Binary Search
 Search Insert Position
 Sqrt(x)
 First Bad Version
 First and Last Position
 Search in Rotated Sorted Array
 Find Minimum in Rotated Sorted Array
 Find Peak Element
 Search a 2D Matrix
 Binary Search on Answer
 Advanced Binary Search

 ---
### ⭐ Practice Philosophy

**Understand the pattern, not just the solution.**

Every solved problem should improve the ability to:
```text
Identify the Pattern
        ↓
Define the Search Space
        ↓
Choose the Correct Template
        ↓
Handle Boundaries
        ↓
Optimize the Solution
        ↓
Analyze Complexity

```
---
## 👩‍💻 Author

**Palak Raghuwanshi**

B.Tech — Computer Science & Engineering

---
### 💻 Focus Areas
Python
Data Structures & Algorithms
LeetCode
Problem Solving
Git & GitHub

---

### ⭐ Support

If this repository helps you in your DSA journey, consider giving it a ⭐ on GitHub.

**Keep Learning. Keep Solving. Keep Improving. 🚀**

---