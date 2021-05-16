# GPA-calculator
This is a project of the university of St. Gallen of the course programming – introduction level.  The goal of the project was to create a program which calculates the GPA. Thanks to the program the user is able to enter for each semester his marks. The program calculates then the GPA. As an extra the program plots a Graph, which shows the development over the past semesters.   The program is inspired by the fact that at the university of St. Gallen not every mark has the same weighting. This leads to the problem, that if you want to calculate your GPA, it is not possible to use the commune formula: sum of marks divided by the number of marks. The fact, that for the calculation of the GPA it is necessary to take the value into account, makes the calculation rather cumbrous. Thanks to the GPA-calculator the user is able to enter his marks and its value. The calculator will provide a GPA, which has taken the value into consideration.

# Pre-requests

The program works with Python 3.8. In order to run the GPA-calculator the libraries “numpy” “math” and “matplotlib.pyplot” have to be installed. 

# Instructions:
1.	Start the gpa-calculator.py
2.	Enter “yes”, “show” or “exit”. It does not matter if the input is written in uppercase or in lowercase letters.
3.	If entered “yes”, insert “yes” or “no”. It does not matter if the input is written in uppercase or in lowercase letters.
4.	If entered “yes”, insert in which semester you are in, followed be the input of how many marks you want to insert. Both inputs must be an integer. 
5.	If entered “no”, insert how many marks you want to insert. The input must be an integer. 
6.	If entered “yes” at step three The program asks you to insert in a row the name of the subject, the value of the subject and the mark.
a.	It is important that after each input (after the name, after the value and after the mark) to press enter. 
b.	After entered the first subject, you can start inserting straightaway the next subject. 
c.	The value and the mark must be an integer.
d.	“Value of the subject” is the weighting of the subject. Normally it is the number of ECTS. 
