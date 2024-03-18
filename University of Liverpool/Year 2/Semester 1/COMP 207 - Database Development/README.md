# COMP207 - Assignment 1: The Epature Bus Company Database

## Overview
This assignment involves creating a database for the Epature bus company. The initial task is to build the database structure (tables, etc.), while the subsequent tasks focus on crafting useful queries. The assignment is worth 100 points and contributes 25% to the overall course grade.

## Tasks and Points Distribution
- The assignment is divided into several tasks, each worth a certain number of points.
- Public data: For each question from 2 to 7, 2 points are awarded for generating the correct output on the public test data described in an additional file.
- Hidden data: The remaining points are allocated based on the correct output on a hidden data set to prevent hardcoding of answers.

## Guidelines
- Questions should be posted on the discussion board to benefit everyone.
- Direct assistance from the instructor will be more readily available for questions 1-2, with limited guidance provided for the harder questions 6-7.
- Each question from 2-7 requires the creation of a view with a specified name.

## Prohibitions
- Using ChatGPT or any form of plagiarism is strictly prohibited.

## Submission Details
- **Deadline:** Wednesday, 8th November, 17:00.
- **Feedback:** General feedback will be provided on Tuesday, 21st November.
- **Format:** The assignment should be submitted in `.sql` format, with the file named `epature.sql`. This file should include:
  - `CREATE TABLE` statements for question 1.
  - `CREATE VIEW` statements for questions 2-7.
  - SQL comments (`--`) if necessary, but these are not mandatory.

## Specific Instructions
- Do not include `CREATE DATABASE` or `USE` statements to ensure compatibility with the testing environment.
- The file should not contain commands that may lead to errors, as MySQL will stop executing the file at the first encountered error.

## Questions Overview
- **Question 1:** Create tables according to specified schemas.
- **Question 2:** Create a view to find the number of trips made by a specific employee in a given month.
- **Question 3:** Generate a list of customers and employees who have been on a specific route.
- **Question 4:** Sort employees by their upcoming birthdays from a specific date.
- **Question 5:** Identify bus trips where the number of passengers exceeded the bus capacity at any stop.
- **Question 6:** Calculate the cost for customers based on the cheapest ticket option (single or day tickets) for each day they traveled.
- **Question 7:** Extend the solution from Question 6 to include weekly tickets and calculate the cost per week.

## Important Notes
- Ensure the SQL file can run successfully on MySQL with the Epature database, starting with an empty database.
- Avoid using commands not covered in class or specific to newer MySQL versions, as the grading environment may not support them.

## Submission Tips
- You are encouraged to use CodeGrade to test your solutions against the public dataset before the deadline.
- Avoid actions that would invalidate your submission, such as dropping the database at the end of your file.

This README provides an overview of the assignment requirements, submission guidelines, and specific instructions for each task. Ensure to read the detailed assignment description for complete information on each question.
