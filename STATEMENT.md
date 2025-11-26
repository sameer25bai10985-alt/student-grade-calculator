# Student Grade System – Problem Statement

## *1. Problem Statement*

The goal is to develop a simple *Student Grade Calculator* that takes marks of five subjects as input, computes the total marks, calculates the percentage, and assigns a grade based on predefined criteria.

The program should be easy to use, handle numeric inputs, and display the final result clearly.

---

## *2. Requirements*

* The system must allow the user to enter marks for *five subjects*.
* Marks should be accepted as numerical values (integers or floats).
* Maximum marks for each subject is assumed to be *100*.
* The program must calculate:

  * Total marks
  * Percentage
  * Grade
* The grade must be assigned according to the percentage obtained.
* The final output must be displayed in a structured format.

---

## *3. Functional Requirements*

### *Input Functions*

* Accept user input for five subject marks.
* Validate that the input values are numeric.

### *Processing Functions*

* Calculate *total marks* using:
  total = m1 + m2 + m3 + m4 + m5
* Calculate *percentage* using:
  percentage = (total / 500) * 100
* Determine grade using the following rules:

  * *A+* → percentage ≥ 90
  * *A* → percentage ≥ 80
  * *B* → percentage ≥ 70
  * *C* → percentage ≥ 60
  * *D* → percentage ≥ 50
  * *Fail* → percentage < 50

### *Output Functions*

* Display:

  * Total marks
  * Percentage (rounded to 2 decimal places)
  * Grade

---

## *4. Technical Requirements*

* Programming Language: *Python*
* Must use:

  * input() function for user input
  * float() for numeric conversion
  * if-elif-else for grade conditions
  * print() for output display
* Code should run in any Python 3 environment.
* No external libraries are required.

---

## *5. Expected Outcome*

* The user enters five subject marks.
* The system computes:

  * Total Marks (out of 500)
  * Percentage
  * Grade
* Output should look like:


----- Result -----
Total Marks: 421
Percentage: 84.2 %
Grade: A


The program should correctly classify students into appropriate grade categories based on their performance.
