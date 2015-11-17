"""
https://www.hackerrank.com/challenges/angry-professor
The professor is conducting a course on Discrete Mathematics to a class of N students. He is angry at the lack of their discipline, and he decides to cancel class if there are fewer than K students present after the class starts.

Given the arrival time of each student, your task is to find out if the class gets cancelled or not.

---

Basically count all students that arrive. If we have more students than we need for the class, break and print "NO".
If not, just repeat and repeat until we either have enough or not. If not, print "YES".

"""

test_cases = int(input())

if test_cases <= 10 and test_cases >= 1:
    for i in range(1, test_cases+1):
        condition = input()
        condition = condition.split(" ")
        students = int(condition[0])
        students_required = int(condition[1])

        if (students <= 1000 and students >=1) and (students_required <= students and students_required >= 1):
            student_arrival_data = input()
            student_arrival_data = student_arrival_data.split(' ')

            students_arrived = 0
            for s in student_arrival_data:
                if int(s) <= 0:
                    students_arrived += 1

                if students_arrived >= students_required:
                    print("NO")
                    break

            if students_arrived < students_required:
                print("YES")
