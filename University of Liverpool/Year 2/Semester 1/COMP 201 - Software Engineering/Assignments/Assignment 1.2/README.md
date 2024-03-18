# COMP201: Software Engineering I - Assignment 1.2 (2023/24)

## Objective
This assignment, focusing on "design/implementation," involves implementing a simulation for part of a security system based on previously defined requirements and use cases from coursework 1. Specifically, the simulation will cover the card/code entry part of the system, with no UI code required.

## Key Information
- **Assignment Number:** 1 of 2 (Part 2)
- **Weighting:** 5% of COMP201 grade
- **Circulated Date:** 2nd November 2023
- **Deadline:** 12th December 2023, 17:00
- **Submission Mode:** Electronic submission via Canvas
- **Learning Outcomes:**
  1. Identify challenges in designing and building significant computer systems.
  2. Design systems to meet user requirements fully.
  3. Apply design principles in practice.
  4. Implement an OO design in an O-O language like Java or Python.

## Purpose
To assess the ability to analyze a problem and implement a solution in code, specifically simulating part of a security system. This exercise helps understand the challenges of implementing a design from requirements and the state modeling required.

## Problem Description
You are to produce code to support a security system simulation in Java, using provided base code. Focus on modifying `Authenticator.java` and `Card.java` without altering their public interfaces. Follow the TODO comments in the source files for guidance.

### Specific Functions
- **checkFireCode:** Implement behavior based on card status, code validity, and lock count.
- **checkBurglaryCode:** Similar to `checkFireCode`, but for burglary codes.

Ensure that incorrect codes increase the lock count, whereas invalid codes do not affect it. Correct codes should reset the lock count to zero.

## Marking Criteria
The assignment will be assessed through automatic testing, focusing on functionality rather than code structure or format. Ensure your code compiles as non-compiling code may receive zero marks.

## Implementation Notes
- This assignment demonstrates two common class design approaches in OO systems: data-driven and responsibility-driven design.
- `Card.java` is a data-driven design example, focusing on modeling, storing, and validating card data.
- `Authenticator.java` exemplifies responsibility-driven design, focusing on the authentication process.

Start working on this assignment as soon as possible to accommodate the complexity of implementing a design from requirements.

For full details on behavior and implementation requirements, refer to the comments within `Card.java` and `Authenticator.java`.

