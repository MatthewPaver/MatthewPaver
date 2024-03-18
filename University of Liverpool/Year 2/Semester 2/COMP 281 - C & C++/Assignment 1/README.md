# COMP281 Assignment 1: Programming Solutions Report

## Introduction

This document summarizes the approaches and methodologies employed in solving five distinct programming challenges as part of COMP281 coursework. The tasks involved creating C programs that addressed various computational and data manipulation challenges, emphasizing code efficiency, readability, and precision in output.

## Problems and Solutions

### Problem 1: Area and Circumference of Circles

- **Task:** Calculate the cumulative area and circumference of circles with radii incrementing from `r1` to `r2`.
- **Strategy:** Implemented a for-loop to iterate through each radius within the specified range, calculating the area and circumference during each iteration and cumulatively adding these values. Output precision was maintained to three decimal places.

### Problem 2: Count Characters in a String

- **Task:** Analyze a string to count occurrences of English letters, digits, spaces, and other characters.
- **Strategy:** Adopted a character-by-character analysis approach, categorizing each based on ASCII values and tallying them in respective counters to ensure accurate counts.

### Problem 3: Reverse String

- **Task:** Reverse the characters of an input string.
- **Strategy:** After capturing the string, I used a two-pointer approach to swap characters from both ends of the string until the center was reached, ensuring efficiency and simplicity.

### Problem 4: Precise Division

- **Task:** Determine the `n-th` digit following the decimal in the quotient of `a` divided by `b`.
- **Strategy:** The solution involved discarding the integer part of the quotient and iteratively extracting each subsequent decimal digit by repeatedly multiplying the remainder by 10 to isolate and print the desired digit.

### Problem 5: Swap Array

- **Task:** Identify the array element with the smallest absolute value and swap it with the final element in the array.
- **Strategy:** Performed an array traversal to locate the index of the element with the minimum absolute value, followed by a simple swap operation to reposition this element at the array's end.

## Conclusion

Addressing these programming challenges reinforced key programming concepts and the C language syntax, enhancing my problem-solving and code optimization skills. Each solution was crafted with a focus on clarity, efficiency, and meeting specified requirements, ensuring functionality across various test cases. This report encapsulates the strategies and rationale behind my solutions, reflecting the analytical and technical skills acquired through this assignment.
