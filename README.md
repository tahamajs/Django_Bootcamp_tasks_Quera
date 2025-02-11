# Django Web Development Bootcamp Projects
## Overview
This repository contains a collection of projects and exercises completed during the **Django Web Development Bootcamp**. Each project is designed to enhance understanding of Django's core functionalities, including models, views, templates, forms, authentication, and more advanced features like custom validators and third-party integrations. Below is a detailed explanation of each project folder, including the key concepts and skills applied.
---
## Table of Contents
- [Project List](#project-list)
  - [Project 1: One-Liner Problem (CA1)](#project-1-one-liner-problem-ca1)
  - [Project 2: Greedy Algorithm Contest (CA2)](#project-2-greedy-algorithm-contest-ca2)
  - [Project 3: Graph and Tree Problem (CA3)](#project-3-graph-and-tree-problem-ca3)
  - [Project 4: Orange Startup (CA4)](#project-4-orange-startup-ca4)
  - [Project 5: StackUnderflow (CA5)](#project-5-stackunderflow-ca5)
  - [Project 6: Logistics System (CA6)](#project-6-logistics-system-ca6)
  - [Project 7: Course Selection System (CA7)](#project-7-course-selection-system-ca7)
- [Conclusion](#conclusion)
- [How to Run the Projects](#how-to-run-the-projects)
- [Requirements](#requirements)
- [License](#license)
- [Acknowledgements](#acknowledgements)
---
## Project List
### Project 1: One-Liner Problem (CA1)
#### Description
A Python exercise focused on writing efficient code using a single line of logic. The task involves modifying input based on conditions, creating a list, sorting it, and printing the result—all in one line.
#### Key Skills and Concepts
- **List Comprehensions**: Creating lists using a single line of code with conditional logic.
- **Conditional Expressions**: Applying `if-else` logic within a list comprehension.
- **Python Built-in Functions**: Utilizing functions like `sorted()` and `print()` effectively.
#### Challenge
- Modify a list of inputs based on specific conditions.
- Implement sorting and output in one concise line.
---
### Project 2: Greedy Algorithm Contest (CA2)
#### Description
An algorithmic challenge to solve a scheduling problem using a greedy algorithm. The goal is to maximize the number of non-overlapping events.
#### Key Skills and Concepts
- **Greedy Algorithms**: Making the locally optimal choice at each step with the hope of finding a global optimum.
- **Time Complexity Management**: Writing algorithms that efficiently handle large datasets.
- **Competitive Programming Techniques**: Reading input efficiently and optimizing code for performance.
#### Challenge
- Schedule events to maximize usage without overlaps.
- Handle large input sizes within time constraints.
---
### Project 3: Graph and Tree Problem (CA3)
#### Description
A problem centered around calculating the sum of all paths in a binary tree. The exercise emphasizes graph traversal techniques.
#### Key Skills and Concepts
- **Tree Traversal Algorithms**: Implementing Depth-First Search (DFS) or Breadth-First Search (BFS).
- **Graph Theory**: Understanding nodes, edges, and pathfinding.
- **Recursive Programming**: Utilizing recursion to navigate tree structures.
#### Challenge
- Accurately calculate the sum of all possible paths.
- Optimize traversal to avoid redundant computations.
---
### Project 4: Orange Startup (CA4)
#### Description
A Django web application developed for an orange-selling business to manage sales and orders.
#### Key Features
- **Models**:
  - `Seller`: Extended user model with additional fields.
  - `Product`: Includes attributes like `price`, `weight`, and `due_date`.
  - `Order`: Manages order details linked to `Product` and `Seller`.
- **Custom Validators**:
  - Implemented password validation using both Argon2 and SHA-1 encryption.
  - Enforced strong password policies.
- **Django Jalali Calendar**:
  - Integrated Jalali (Persian) date fields using third-party libraries.
- **Admin Panel Customization**:
  - Displayed specific fields in the admin list view.
  - Added search functionality for models.
#### Skills Applied
- **Django ORM**: Designing models with relationships and custom fields.
- **Custom User Models**: Extending Django's default `User` model.
- **Security Best Practices**: Implementing password hashing and validation.
- **Third-Party Integration**: Using external libraries for additional functionalities.
---
### Project 5: StackUnderflow (CA5)
#### Description
A Q&A platform inspired by StackOverflow, allowing users to post questions and answers with upvote and downvote functionality.
#### Key Features
- **Models**:
  - `User`: Extended to include `phone_number` and `national_id`.
  - `Question`: Users can post questions with titles and descriptions.
  - `Answer`: Users can provide answers to questions.
- **Upvote/Downvote System**:
  - Implemented voting mechanisms for questions and answers.
  - Calculated scores based on votes.
- **Authentication and Permissions**:
  - Only registered users can post and vote.
  - Utilized Django's authentication system.
#### Skills Applied
- **Django Forms and Templates**: Creating dynamic forms and rendering data.
- **Advanced QuerySets**: Filtering and annotating data based on votes.
- **Business Logic Implementation**: Handling complex interactions between models.
---
### Project 6: Logistics System (CA6)
#### Description
Developed a system for managing warehouses and orders for a logistics company, including tracking products and managing stock levels.
#### Key Features
- **Models**:
  - `Inventory`: Tracks product quantities and warehouse locations.
  - `Product`: Details like `weight`, `price`, and `category`.
  - `Order`: Manages customer orders linked to products.
- **Views and Forms**:
  - Implemented CRUD operations for orders and inventory management.
  - Utilized class-based views for efficient code organization.
- **Admin Customization**:
  - Enhanced the admin interface with custom list displays and filters.
  - Added inline editing capabilities.
#### Skills Applied
- **Class-Based Views**: Leveraging Django's generic views for common patterns.
- **Model Relationships**: Handling `ForeignKey` and `ManyToMany` relationships.
- **User Authentication**: Restricting access to certain views based on user roles.
---
### Project 7: Course Selection System (CA7)
#### Description
A comprehensive Django application that allows students to register for courses, manage their schedules, and handle potential course conflicts.
#### Key Features
- **Models**:
  - `Student`: Extended user model with academic information.
  - `Course`: Includes details like `course_id`, `name`, `credits`, and `schedule`.
  - `Registration`: Junction table between `Student` and `Course` with additional fields.
- **Conflict Detection**:
  - Implemented logic to prevent students from enrolling in courses with overlapping schedules.
  - Provided feedback messages for conflicts.
- **User Interface**:
  - Forms for course selection with dynamic validation.
  - Schedule overview displaying enrolled courses.
#### Skills Applied
- **Complex Form Handling**: Customizing form validation and error messages.
- **Time-Based Validation**: Checking for schedule overlaps using datetime fields.
- **Efficient ORM Queries**: Optimizing database access for performance.
---
## Conclusion
Each project in this repository contributes to a comprehensive understanding of Django web development and Python programming. The exercises cover a wide range of topics:
- Core programming fundamentals.
- Advanced Django features like custom validators, third-party integrations, and security practices.
- Algorithmic problem-solving with a focus on optimization and efficiency.
- Building full-fledged web applications with user authentication, complex models, and interactive features.
This README provides an overview of the projects. For detailed instructions, code examples, and further explanations, please refer to the respective project folders.
---
## How to Run the Projects
To run any of the Django projects, follow these general steps:
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/django-bootcamp-projects.git
   cd django-bootcamp-projects
   ```
2. **Navigate to the Project Directory**
   ```bash
   cd CA4-orange-startup  # Replace with the specific project folder
   ```
3. **Create a Virtual Environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```
4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
5. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```
6. **Create a Superuser (if required)**
   ```bash
   python manage.py createsuperuser
   ```
7. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```
8. **Access the Application**
   - Open your web browser and navigate to `http://localhost:8000/`.
   - Access the admin panel at `http://localhost:8000/admin/`.
**Note:** Some projects may have additional setup steps or dependencies. Please refer to the `README.md` file within each project folder for project-specific instructions.
---
## Requirements
- **Python 3.6 or higher**
- **Django 3.x or higher**
- **Additional Libraries**: Listed in each project's `requirements.txt` file.
---
## License
This repository is licensed under the **MIT License**. You are free to use, modify, and distribute the code as per the license terms. See the [LICENSE](LICENSE) file for more details.
---
## Acknowledgements
- **Django Web Framework**: For providing a robust platform for web development.
- **Third-Party Libraries**: Such as Django Rest Framework, Django Jalali, and others used across projects.
- **Bootcamp Instructors and Peers**: For guidance, support, and collaboration.
- **Community Contributors**: For open-source packages and helpful resources.
---
**Contact Information**
If you have any questions, suggestions, or would like to contribute to these projects, feel free to contact me:
- **Email**: [tahamaj4@gmail.com](tahamaj4@gmail.com)
- **GitHub**: [tahamajs](https://github.com/tahamajs)
