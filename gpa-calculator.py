#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 17:58:08 2021

@author: Marco
"""
# =============================================================================
#Task: program a  GPA-caculator which takes the weighting of the marks into account. 
#Date: 09.05.2021
#Author: Marco Sidler
# =============================================================================
# =============================================================================
# 0. Setup
# =============================================================================
import numpy as np
import math as math
import matplotlib.pyplot as plt

# array in which we safe the name of the subject, value and mark
userarray = []
# array in which we safe the semester the user is in. 
sem = []

# testing for errors: List will be used later to test if the userinput is in the range of the Unicode from A to Z and a to z. 
asciirange = list(range(65,90)) + list(range(97,122))

#arrays in which the Unicode characters will be stored
ascii1 = []
ascii2 = []

# used for the first while loop. While is_valid is True the user stays in the loop
is_valid = True

# testing for errors: List will be used later to test if the userinput is in the range of the Unicode from A to Z and a to z.
asciirange1 = list(range(65,90)) + list(range(97,122))

#arrays in which the Unicode characters will be stored 
ascii11 = []
ascii22 = []
#used for the first while loop. While is_valid is True the user stays in the loop
is_valid = True

# =============================================================================
# 1.  Creation of the error handling funtion:
    #1.	Create a while loop
    #2.	Ask the user to input in which semester he is in. 
    #3.	Convert the user-input into its Unicode character. 
        #First the program has to split the user-input into strings with a length of one. Then it converts the strings into its Unicode character and stores it into an array.
    #4.	Create an array, which contains the Unicode character of the numers 1 to 9. If all the elements of the input are in the range of 1 to 9, the program exits the loop. If the input is not in the required range the user as to enter his input again. 
# =============================================================================
def semesterinput():
    userascii = []
    is_correct = True
    numberlist = list(range(48,58))

    while is_correct == True:
        userinput = input("In which semester are you in: ")
            
        for t in range(len(userinput)):
            userascii.append(ord(userinput[t]))

        for q in range(len(userascii)):
            testforerror = userascii[q] in numberlist
                 
        if testforerror == True:
            semester = int(userinput)
            is_correct = False
        else:
            print("Ups something went wrong, your input as to be an integer")
            is_correct = True
        return semester


# =============================================================================
#  2.  Creation of the error handling funtion:
    #1.	Create a while loop
    #2.	Ask the user to input how many marks he wants to input. 
    #3.	Convert the user-input into its Unicode character. 
        #First the program has to split the user-input into strings with a length of one. Then it converts the strings into its Unicode character and stores it into an array.
    #4.	Create an array, which contains the Unicode character of the numers 1 to 9. If all the elements of the input are in the range of 1 to 9, the program exits the loop. If the input is not in the required range the user as to enter his input again. 
# =============================================================================
def markinput():
    userascii1 = []
    is_right = True
    numberlist1 = list(range(48,58))
    
    while is_right == True:
        row = input("Enter the number of marks you want to insert: ")
        
        for tt in range(len(row)):
            userascii1.append(ord(row[tt]))
            
        for qq in range(len(userascii1)):
            testforfalse = userascii1[qq] in numberlist1
            
        if testforfalse == True:
            R = int(row)
            is_right = False
        else:
            print("Ups something went wrong, your input as to be an integer")
            is_right = True
        return R
# =============================================================================
# 3. Start the program and welcome the user
# =============================================================================
print("\n")
print("Welcome to the GPA-calculator")
# =============================================================================
#  4. The follwing while loop asks the user if he wants to enter his marks, to see the previous GPAs or to exit the program. 
    #1.	Create a while loop
    #2.	Ask the user to input “Yes”, “show” or “exit”
    #3.	Convert the user-input into its Unicode character. 
        #First the program has to split the user-input into strings with a length of one. Then it converts the strings into its Unicode character and stores it into an array.
    #4.	Create an array, which contains the Unicode character A to Z and a to z. If all the elements of the input are in the range of A to Z and a to z, the program exits the loop. If the input is not in the required range the user as to enter his input again. 
# =============================================================================
while is_valid == True:
    userinput = input("Please enter: (Yes) for inserting marks, (show) for show previous GPA, (exit) for ending the program: ")

    for z in range(len(userinput)):
        ascii1.append(userinput[z])

    for l in range(len(ascii1)):
        ascii2.append(ord(ascii1[l]))

    for i in range(len(ascii2)):
        test = ascii2[i] in asciirange
        
    if test == True:
        loweruser = userinput.lower()
    
        if loweruser == "yes":
# =============================================================================
#           5. The following while loop asks if the user wants to calculate and safe his GPA or if he just wants to calculate
                #1.	Create a while loop
                #2.	Ask the user to input “yes” or "no"
                #3.	Convert the user-input into its Unicode character. 
                    #First the program has to split the user-input into strings with a length of one. Then it converts the strings into its Unicode character and stores it into an array.
                #4.	Create an array, which contains the Unicode character A to Z and a to z. If all the elements of the input are in the range of A to Z and a to z, the program exits the loop. If the input is not in the required range the user as to enter his input again. 
                #5.	If the input is in the correct range, the program will check whether the input was “Yes”, “show” “exit” or neither of those. 
                    #To be user-friendly, it should not matter whether the input is written in uppercase letters, in lowercase letters or a combination of those two. To take this into account the program converts the user-input into lowercase letters, so it does not matter if the user-input was originally a “Yes”, a “YEs" or a different combination, in the end every input is converted into an “yes”.
                    #Now the program checks if the user-input was “yes”, “show”, “exit” or neither of those. If the input was false, the user has to insert the input again. He remains in the while loop. Otherwise, the user moves forward. 
# =============================================================================
            while is_valid == True:
                userinput = input("For calculate and safe your GPA type (Yes), for only calculating type (No): ")

                for z in range(len(userinput)):
                    ascii11.append(userinput[z])
            
                for l in range(len(ascii11)):
                    ascii22.append(ord(ascii11[l]))
            
                for i in range(len(ascii22)):
                    test = ascii22[i] in asciirange1
                    
                if test == True:
                    loweruser = userinput.lower()
# =============================================================================
#                   6. Following code is the code for the option: calculate the GPA and safe it.
# =============================================================================
                    if loweruser == "yes":
# =============================================================================
#                       7. Show the user in which semester he was the last time he used the program. 
                            #Here the program uses try and except. Before the program asks the user in which semester he is, the program shows in which semester he was the last time when he used the program. 
                            #The problem which occurs, is in the situation, in which the user is in the first semester. In this case the program has no data to access, and it stops with an error. 
                            #With try and except it possible to solve this problem. In try: the program tries to access the data, if there is data to access the program takes out the required information. 
                            #If the user is in the first semester the program stops and goes into except and prints the following sentence out: “You are in the first semester”. 
# =============================================================================
                        try:               
                            #show the user his last semesternumber
                            txt_file = open("test3.txt", "r")
                        
                            txtaslist = txt_file.readlines()
                            split = []
                            for i in range(len(txtaslist)):
                                split.append(txtaslist[i])
                                 
                            lastsemster = split[-4]
                            txt_file.close()
                            print("\n")
                            print(f"Your last semester was {lastsemster}")

                        except:
                            print("\n")
                            print("You are in the first semester")
# =============================================================================
#                        8. Ask the user in which semester he is, while using the function from above to test for an error. 
# =============================================================================
                        semester = semesterinput()

                        #safe the user-input. This information will be used later for the file handling and for the construction of the graph. 
                        stringsem = f"semester:{semester}"
                        
                        sem.append(stringsem)
# =============================================================================
#                       9. Create a matrix in which we store the user-inputs
                            #By knowing how many marks the user will input and thanks to the fact that there will be for each mark three inputs, it is possible to create a matrix. 
                            #In the matrix the program will save the inputs from the user. 
                            #For each mark it creates a row and each row has three columns (name of the subject, value of the subject, mark).
                            #The user inserts then in a row name of the subject, value of the subject and mark. The inputs are separated by enter. This information is stored in the matrix above. 
                            #As the user has entered all the marks, the program has everything to calculate the GPA. To do so, it has to extract the values from one to n and the marks from one to n and stores the information into a second matrix.
# =============================================================================
                        #Ask the user how many marks he wants to insert, while using the function from above to test for an error. 
                        R = markinput()
                        C = 3
                        
                        print("Enter in rows for each subject: name of the subject, value of the subject, mark (separated by enter)")
                           
                        for i in range (R):
                            a = []
                            for j in range (C):
                                a.append(input())
                                userarray.append(a)
                            
                        #take column Nr. 2 out of the userarray
                        usermatrix = np.array(userarray)
                        column2 = usermatrix[:, 1]
                            
                        #convert column Nr. 2 into a float
                        convertcol2 = []
                        for y in range(len(column2)):
                            t = float(column2[y])
                            convertcol2.append(t)
                            
                        #the same thing we will do for column Nr. 3
                        column3 = usermatrix[:, 2]
                           
                        convertcol3 = []
                        for n in range(len(column3)):
                            l = float(column3[n])
                            convertcol3.append(l)
# =============================================================================
#                       10. Calculate the GPA:
                            #Thanks to the matrix format, it is possible to use numpy for the calculation. 
                            #The formula for the GPA is as followed: 
                                #1)	Multiply each mark with its value.
                                #2)	Calculate the sum of the results from step one.
                                #3)	Calculate the sum of the values 1 to n.
                                #4)	To get the GPA divide the result from step one by the result from step two. 
                            #The program will print then the GPA for the current semester. 
# =============================================================================
                        result1 = np.multiply(convertcol2, convertcol3)
                                
                        result11 = math.fsum(result1)
                        
                        result2 = sum(map(float,convertcol2))
                            
                        GPA = result11/result2
                            
                        print("\n")
                        print(f"Your current GPA is {GPA}\n")
                        
                        #safe the string "GPA" and the GPA. This will be stored into the file. 
                        sem.append("GPA:")
                        sem.append(GPA)
# =============================================================================
#                       11. Save the data into a text file
                            #To save the GPA, it is necessary to work with the file handling. 
                            #In order to do so, it is required to open a file and write the required data (Semester: n and GPA of the semester n) into it. 
                            #As at step eight explained, the information Semester: n, was received from the user-input. It is possible to append the file with this information. 
                            #To store the GPA in the file, the program just appends the result from step three.
# =============================================================================
                        txt_file = open("test3.txt", "a")
                            
                        for i in range(len(sem)):
                            txt_file.write(str(sem[i]))
                            txt_file.write("\n")
                        txt_file.write("\n")
                        txt_file.close()
# =============================================================================
#                       12. Calculating the overall GPA
                            # To calculate the overall GPA the program opens the file and takes out the third line of the text file and saves it into an array. 
                            #To receive the other GPAs, the program saves every fourth line from the text file into the array. 
                            #Once done that, the program can calculate the overall GPA.
                            #The overall GPA is calculated by taking the sum of the array and dividing it by the number of elements in the array. 
# =============================================================================
                        txt_file = open("test3.txt", "r")
                            
                    
                        userdata = txt_file.readlines()
                        #take out the third line of the file an safe into the array gpa
                        #the data we take out is the GPA
                        gpa = [float(userdata[2])]
                        #after the sixth line, we take out every fourth line and safe it into the array gpa.
                        #the data we take out is the GPA
                        for i in range(6,len(userdata),4):
                            gpa.append(float(userdata[i]))
                        
                        #calculate the overall GPA
                        summgpa = sum(gpa)
                        divisor = len(gpa)
                        overalgpa = (f"Your overall GPA is: {summgpa/divisor}")
                    
                        print(overalgpa)
                    
                        txt_file.close()
# =============================================================================
#                       13. Plotting GPA-Development Graph 
                            #The last step is to create a graph, which shows the development of the GPAs. 
                            #To create the graph the program uses mathplot. The x-axis consists of the number of semesters (1 to n) and the y-axis consists of the GPAs from semester 1 to n. 
                            #The label of the x-axis is defined as “semesters” and the label of the y-axis is defined as “GPA per semester”. 
# =============================================================================
                        xachse = list(range(1, divisor+1))
                        yachse = gpa
                        
                        # -o: graph style 
                        plt.plot(xachse, yachse, '-o')
                        # defin the x-axis from 0 to 6
                        plt.axis([0.5, divisor+0.5, 0, 6])
                        # fix the x-axis that it consists of integers
                        plt.locator_params(axis = "both", integer = True, tight = None)
                        #label the x-axis, y-axis and the graph
                        plt.xlabel('semester')
                        plt.ylabel('GPA per semester')
                        plt.title(f"Your GPA over the last {divisor} semesters")
                        plt.grid()
                        plt.show()
                            
                        is_valid = False
# =============================================================================
#                   14. Code if the user does not want to safe the GPA
# =============================================================================
                    elif loweruser == "no":
                        
                        #Ask the user how many marks he wants to insert, while using the function from above to test for an error. 
                        R = markinput()
                        C = 3
# =============================================================================
#                       15. Create a matrix in which we store the user-inputs
                            #By knowing how many marks the user will input and thanks to the fact that there will be for each mark three inputs, it is possible to create a matrix. 
                            #In the matrix the program will save the inputs from the user. 
                            #For each mark it creates a row and each row has three columns (name of the subject, value of the subject, mark).
                            #The user inserts then in a row name of the subject, value of the subject and mark. The inputs are separated by enter. This information is stored in the matrix above. 
                            #As the user has entered all the marks, the program has everything to calculate the GPA. To do so, it has to extract the values from one to n and the marks from one to n and stores the information into a second matrix.
# =============================================================================
                        print("Enter in rows for each subject: name of the subject, value of the subject, mark (separated by enter)")
                        
                        for i in range (R):
                            a = []
                            for j in range (C):
                                a.append(input())
                            userarray.append(a)
                        
                        #take  column Nr. 2 out of the userarray
                        usermatrix = np.array(userarray)
                        column2 = usermatrix[:, 1]
                        
                        #convert column Nr. 2 into a float
                        convertcol2 = []
                        for y in range(len(column2)):
                            t = float(column2[y])
                            convertcol2.append(t)
                        
                        #the same thing we will do for column Nr. 3
                        column3 = usermatrix[:, 2]
                       
                        convertcol3 = []
                        for n in range(len(column3)):
                            l = float(column3[n])
                            convertcol3.append(l)
# =============================================================================
#                       10. Calculate the GPA:
                            #Thanks to the matrix format, it is possible to use numpy for the calculation. 
                            #The formula for the GPA is as followed. 
                                #1)	Multiply each mark with its value.
                                #2)	Calculate the sum of the results from step one.
                                #3)	Calculate the sum of the values 1 to n.
                                #4)	To get the GPA divide the result from step one by the result from step two. 
                            #The program will print then the GPA for the current semester.
# =============================================================================
                        result1 = np.multiply(convertcol2, convertcol3)
                            
                        result11 = math.fsum(result1)
                        
                        result2 = sum(map(float,convertcol2))
                        
                        GPA = result11/result2
                        print("\n")
                        print(f"Your GPA would be {GPA}")
#=============================================================================
#                       17. Calculate the overall GPA
                            # To calculate the overall GPA the program opens the file and takes out the third line of the text file and saves it into an array. 
                            #To receive the other GPAs, the program saves every fourth line from the text file into the array. 
                            #Once done that, the program can calculate the overall GPA.
                            #The overall GPA is calculated by taking the sum of the array and dividing it by the number of elements in the array. 
# =============================================================================
                        txt_file = open("test3.txt", "r")
        
                        userdata = txt_file.readlines()
                        #take out the third line of the file an safe into the array gpa
                        #the data we take out is the GPA
                        gpa = [float(userdata[2])]
                        #after the sixth line take out every fourth line an safe it into the array gpa.
                        #the data we take out is the GPA
                        for i in range(6,len(userdata),4):
                            gpa.append(float(userdata[i]))
                        
                        #Calculate the ovarall GPA
                        summgpa = sum(gpa)
                        divisor = len(gpa)
                        overalgpa = (f"Your actual overall GPA is: {summgpa/divisor}")
                        #Print the overall GPA
                        print(overalgpa)
                    
                        txt_file.close()
                        
                        is_valid = False
                    #if the user-input is neither a "yes" nore "no". The program prints: Please enter a valid input
                    #the user remains in the secound while loop and must enter a valide input
                    else:
                        print("Please enter a valid input")
                        print("\n")
                        
                #if the user-input is not in the range of the Unicode characters the program prints: Please enter a valid input
                #the user remains in the secound while loop and must enter a valide input
                else:
                    print("Please enter a valid input")
                    is_valid = True
# =============================================================================
#       18. Second user option: show
            #With the option “show” the program gives the user as output the GPAs from Semester one to n, the overall GPA and shows him the GPA-Development Graph.
            #To come to this result, the first thing is to open the file, in which all GPA are stored. 
            #Once the file is opened, the program reads the whole file and prints it in the console.
            #The second step is to calculat the overall GPA
            #The third step is to plot the GPA-Development Graph
# =============================================================================
        elif loweruser == "show":
            #Print the whole file, in which the all the GPAs are stored.
            txt_file = open("test3.txt", "r")
            printfile = txt_file.read()
            print("\n")
            print(printfile)
            
            txt_file.close()
            
            #Calculate the overall GPA
            txt_file = open("test3.txt", "r")
                
            userdata = txt_file.readlines()
            #take out the third line of the file and safe into the array gpa
            #the data we take out is the GPA
            gpa = [float(userdata[2])]
            #after the sixth line, we take out every fourth line and safe it into the array gpa.
            #the data we take out is the GPA
            for i in range(6,len(userdata),4):
                gpa.append(float(userdata[i]))
            
            #Calculate the overall GPA
            summgpa = sum(gpa)
            divisor = len(gpa)
            overalgpa = (f"Your overall GPA is: {summgpa/divisor}")
            #Print the overall GPA
            print(overalgpa)
        
            txt_file.close()
            
            #Plot the GPA-Development Graph
            xachse = list(range(1, divisor+1))
            yachse = gpa
            # -o: graph style                        
            plt.plot(xachse, yachse, '-o')
            # defin the x-axis from 0 to 6
            plt.axis([0.5, divisor+0.5, 0, 6])
            # fix the x-axis that it consists of integers
            plt.locator_params(axis = "both", integer = True, tight = None)
            #label the x-axis, y-axis and the graph
            plt.xlabel('semester')
            plt.ylabel('GPA per semester')
            plt.title(f"Your GPA over the last {divisor} semesters")
            plt.grid()
            plt.show()
            
            is_valid = False
# =============================================================================
#       19. User option: Exit
            #With this option the program is ended and prints “Thanks for using the GPA-calculator” and “Goodbye”.             
# =============================================================================
        elif loweruser == "exit":
            print("\n")
            print("Thank you for using the GPA-calculator \nGoodbye")
            is_valid = False
# =============================================================================
#       20. First while loop
            #if the user-input is not in the range of the Unicode characters the program prints: Please enter a valid input
            #the user remains in the first while loop and must enter a valide input
# =============================================================================
        else:
            print("Please enter a valid input")
            print("\n")