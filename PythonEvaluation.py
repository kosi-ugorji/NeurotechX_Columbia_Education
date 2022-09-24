# -*- coding: utf-8 -*-

import random
import numpy as np

'''
IMPORTANT
To submit, go to the google form (https://docs.google.com/forms/d/e/1FAIpQLSfgPg7FNCTqhb8DGHDQQq4Lhxf8jLiexdgZbg6SSGAGQjl3vg/viewform?usp=sf_link_)
 and upload a picture of the output you receive when you run your code
'''

"""
PART 1: Variables
 
Find the average area of triangles with the same height. 
The average area of triangles with the same height can be found by 
averaging the widths of the triangles and calculating an area using the
averaged width and height. 
In this section, you would be given a list of widths. You should find the
average of these widths, store this average in a variable, calculate the 
area using this variable, store it in another variable then return the 
function. 


Step 1: Set a variable called avg to the sum of the elements in li
Step 2: Set a variable called area to the area of a triangle calculated using 
 avg, and height. (Formula for a triangle: 1/2*b*h)
 
"""
height = 2
li = [2,3,4]

avg = #to fill 

area = #to fill 


'''!!! Do not edit this'''
A = q1.check(area, avg)



"""
Part 2: Conditionals 

Given a random number- random_int determine if this number is in the forbidden_list


"""

random_int = random.randint(1,10)
forbidden_list = [3,4,5]
#your code here 

B = q2.check(random_int, forbidden_list)


"""
Part 3: Loops

Giving two lists of numbers, find the difference between the numbers at a particular 
index in each list. 
E.g suppose you are given:
    li1= [1,2,3]
    li2 = [3,6,0]
The difference would be li1-li2:    
    diff = [-2, -4, 3]

NOTE: To get this right, make sure to call your list diff
"""
diff = []
li1 = [1, 5, 6, 7]
li2 = [1, 7, 8, 9]

# create a loop that goes through each element and computes a difference


'''Don't edit this '''
C = q3.check(li1, li2, diff)



""" 
Part 4: Dictionaries and Sets

Create a dictionary  of names called names_dict mapped to a set of data called forged_data

Step 1: from forged_data_list create a set
Step 2: Assign each name in the names_list to the set forged_data_list. 
(all keys are mapped to the same value- think about if this is possible in the reverse case)

"""
neames = ["Sarah", "John"]
forged_data_list = [1,1,2,3,4,5,5,6,6,7]

forged_data_set = #implement this 

names_dict = #implement this

'''Don't edit this '''
D = q4.check(li1, li2, diff) 




"""
Part 5: Functions

Make a function that adds two numers x1 and x2. 

"""

def addTwo(x1, x2):
    #your function here
    
    
E = q5.check(addTwo)



"""
Part 6: Numpy


Create a 2-D numpy array with the list of lists given and find the value at the 
second row and third column

Note here that numpy has already been imported as np here. 


"""

li_of_li = [[1,2,3], [0,4,5], [3,4,5]]

F = q6.check(li_of_li)

'''Final Evaluation ''' 

print(A&B&C&D&E&F)
