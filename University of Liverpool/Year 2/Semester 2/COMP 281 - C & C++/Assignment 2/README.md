# COMP281 Assignment 2: Brief Report

## Introduction

This document details the strategies and methods used to tackle the programming tasks in Parts 1 and 2 of the coursework. Emphasis was placed on crafting efficient, robust solutions that met functional requirements and adhered to good coding practices.

## Part 1: Run Length Encoding of ASCII Art

### Task

Implement a program for compressing and expanding ASCII Art images using Run Length Encoding (RLE).

### Strategy

- **Compression (`C` mode):** The program reads each line of ASCII Art, identifies sequences of repeating characters, and encodes them using RLE.
- **Expansion (`E` mode):** It decodes RLE-compressed lines back to their original form.
- Functions `compressLine` and `expandLine` manage these tasks using loops, conditionals, and string manipulation techniques to achieve the transformations. The program efficiently handles file I/O operations, ensuring output aligns with specified formats.

## Part 2: Searching a Text for a Word

### Task

Develop a program to search for a specific word in a given text using suitable data structures and algorithms.

### Strategy

- A binary search tree (BST) is employed to store and count unique words from the input text after cleansing them of punctuation and converting them to lowercase.
- The `insert` function builds the tree, placing words in alphabetical order, while the `search` function looks up the tree for the search word, displaying the count if found or a "not found" message otherwise.
- This approach ensures efficient word lookup and counting, demonstrating effective use of dynamic memory allocation and tree data structures.

## Conclusion

Completing Parts 1 and 2 of the assignment has deepened my understanding of various aspects of C programming, from file handling and memory management to advanced topics like data structures. Each solution was designed with efficiency, readability, and robustness in mind, ensuring that the programs met specified requirements and were structured to support maintainability and scalability. This experience significantly enhanced my programming skills, particularly in problem-solving, algorithmic thinking, and applying C programming concepts to real-world scenarios.
