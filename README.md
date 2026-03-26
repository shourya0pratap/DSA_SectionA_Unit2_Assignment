# ETCCDS202: Data Structures Lab
**Student Name:** Shourya Pratap  
**Program:** B.Tech CSE  
**Section:** A   
**Course Code:** ETCCDS202  

# 📌 Overview
This repository contains the implementation of the Data Structures lab curriculum for the 2026 session. While the manual includes faculty-led experiments, this section focuses on the completed Unit 1 and Unit 2 Assignment tasks.

# 📂 Unit 1 Assignment: Foundations & Algorithmic Analysis
The following tasks were implemented independently to demonstrate foundational DS concepts: 
- **Recursive Factorial & Fibonacci:** Implementations of both naive and memoized versions to compare efficiency.
- **Performance Analysis:** Detailed time and space complexity justifications, specifically addressing why naive Fibonacci is inefficient ($O(2^n)$). 
- **Tower of Hanoi:** Recursive solution including a manual state trace for $N=3$ and derivation of time complexity. 
- **Recursive Binary Search:** Implementation with a complexity explanation based on the recurrence intuition $T(n) = T(n/2) + O(1)$. 

# 📂 Unit 2 Assignment: Linear Data Structures
Implementation of fundamental linear structures focusing on dynamic memory and pointer management:
- **Singly & Doubly Linked Lists:** Robust implementations of node insertion and deletion logic, including boundary case handling.
- **Stack & Queue (SLL Based):** ADT implementations using linked structures to ensure $O(1)$ operations for Push/Pop and Enqueue/Dequeue.
- **Balanced Parentheses:** A stack-based validation script for multi-type bracket matching in expressions.
- **Dynamic Array Simulation:** A custom `DynamicArray` class utilizing the `ctypes` module to demonstrate manual resizing and capacity doubling logic.

# 🛠️ Requirements
- **Language:** Python 3.x
- **Modules:** `ctypes` (Standard Library)
- **Environment:** Terminal/CLI for execution 
