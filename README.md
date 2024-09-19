
# Django Web Development Bootcamp Projects

## Overview

This repository contains various Django projects and exercises completed during the Django Web Development Bootcamp. The goal of each project is to enhance understanding of Django's core functionalities, such as ORM, forms, views, and more advanced features like user authentication and API development. Below is an explanation of each project folder and the skills applied.

---

### 1. **CA1 - One-Liner Problem**

- **Description:** A small exercise focused on writing efficient Python code using a single line of logic.
- **Key Skills:**
  - List comprehension
  - Conditional logic within a single Python statement.
- **Challenge:** Modify input based on conditions, create a list, sort it, and print the result in one line.

---

### 2. **CA2 - Greedy Algorithm Contest**

- **Description:** In this exercise, the goal was to solve a scheduling problem using a greedy algorithm to maximize the number of non-overlapping events.
- **Key Skills:**
  - Greedy algorithms
  - Efficient time complexity management
  - Handling large inputs in competitive programming.

---

### 3. **CA3 - Graph and Tree Problem**

- **Description:** This task involved calculating the sum of all paths in a binary tree. It was focused on graph traversal techniques.
- **Key Skills:**
  - Tree traversal (DFS/BFS)
  - Graph theory
  - Efficient pathfinding algorithms.

---

### 4. **CA4 - Orange Startup**

- **Description:** This was a more complex Django application aimed at managing sales and orders for an orange-selling business.
- **Key Features:**
  - **Models:** Seller, Product, Order with attributes such as price, weight, and due date.
  - **Custom Validator:** Validation logic was applied to passwords, using both Argon2 and SHA-1 encryption.
  - **Django Jalali Calendar:** The project incorporated date fields using the Jalali calendar.
  - **Admin Panel:** Customized to show specific fields like username, product, and order details.
  - **Skills Applied:**
    - Django ORM
    - Custom user model and admin customization
    - Security best practices (password hashing, validation).

---

### 5. **CA5 - Fifth Exercise: StackUnderflow**

- **Description:** A project to create a Q&A system similar to StackOverflow, allowing users to post and answer questions, with upvote and downvote functionality.
- **Key Features:**
  - **User Model:** Extended Django's user model to add fields like `phone_number` and `national_id`.
  - **Questions and Answers:** Users can post questions, and others can provide answers, each with upvotes/downvotes.
  - **Skills Applied:**
    - Django forms and templates
    - Advanced use of models and querysets
    - Upvoting and downvoting logic.

---

### 6. **CA6 - Logistics System**

- **Description:** Developed a system for managing warehouses and orders for a logistics company, including tracking products and managing stock levels.
- **Key Features:**
  - **Models:** Inventory, Product, Order with fields such as `weight`, `created_at`, and `user`.
  - **Views and Forms:** Managed CRUD operations for orders and inventory through Django views and forms.
  - **Admin Customization:** Custom fields and search functionalities were added to the admin panel.
  - **Skills Applied:**
    - Django class-based views
    - Complex model relationships and querying
    - User authentication for warehouse managers.

---

### 7. **CA7 - Final Project: Course Selection System**

- **Description:** The final project involved creating a course selection system where students can register for courses, manage their schedules, and handle potential course conflicts.
- **Key Features:**
  - **Models:** Courses, Students, and Registrations with validations to prevent course overlaps.
  - **Views and Forms:** Created forms for students to select courses and validate time conflicts.
  - **Skills Applied:**
    - Handling complex form logic
    - Validation of time-based conflicts
    - ORM queries for complex filtering.

---

## Conclusion

Each project in this repository contributed to a comprehensive understanding of Django web development. The exercises covered a wide range of topics, from core programming fundamentals to more advanced concepts like user authentication, database management, and efficient algorithmic solutions.

This README serves as an overview of the projects. For further details, please refer to the respective project folders.

---
