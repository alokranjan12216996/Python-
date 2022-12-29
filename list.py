marks = [95,65,96,"mohan"]
print(marks)

#for specific mark to print

marks = [95,65,96,32]
print(marks[2])

#python mai negative number matlab counting start from backward.
marks = [95,65,96,32]
print(marks[-1])

#agar humae doo number chaiyea toh 
marks = [96,95,65,32]
print(marks[0:2])#iss mai last number include nahi karte hai

#for loop in list
marks = [95,98,97]
for score in marks:
    print(score)

#using append in list(it adds number in last)

marks = [95,98,97]
marks.append(99)
print(marks)

#using insert in list(it help to add number any where in the line)
marks = [95,98,97]
marks.insert(1,78)
print(marks)

##to print length of list
marks = [95,98,97]
marks.insert( 0,99)
print(len(marks))

#printing marks  using while loop
marks = [95,98,97]
i = 0
while i < len(marks):
    print(marks[i])
    i = i + 1

    #to print empty box
    marks.clear()
    print(marks)

    ##using break(name will be printed till krishan)
    student = ["ram","shyam","mohan","kishan","radha","radhika"]
    for student in student:
        if student == "radha":
            break;
        print(student)

    ##using continue(iss mai agar kissi bhi name ko remove karna hai aur baki ko print karna hai tab)
    student = ["ram","shyam","mohan","kishan","radha","radhika"]
    for student in student:
        if student == "kishan":
            continue;
        print(student)

 ##tuple(it is immutable)
marks = (95,98,97,97,97)
print(marks.count(97))
print(marks.index(97))##(index matlab phali bar kiss position per aaya. )

##sets(bas curly braces lagta hai.)
marks = {95,98,97,97,97}
print(marks)

for score in marks:
    print(score)

##[list],,,(tuple),,,{set}

##dictionary
marks = {"english" :96, "chemistry":97}
print(marks["chemistry"])

marks["physics"] = 97;##(agar extra marks add karna ho tab iss tarahe likha na hai)
print(marks)

marks["physics"] = 99;##(iss tarah value ko change karna k liye use karte hai)
print(marks)

##module function
import math
print(dir(math))

from math import sqrt##(agar bas ek chaiyea sab mai se)
print(sqrt(25))

##user defined function

def print_sum(first,second):
    print(first +second)

print_sum(1,2)
