# Example 1:
#
# Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
# Output: 0
# Explanation:
# - Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
# - Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
# - Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
# - Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
# - Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
# - Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
# - Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
# - Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
# Hence all students are able to eat.
# Example 2:
# Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
# Input: students = [1,1,0,0,1], sandwiches = [0,0,0,1,1]
# Input: students = [1,0,0,1,1], sandwiches = [0,0,0,1,1]
# Input: students = [1,1,1], sandwiches = [0,1,1]
# Output: 3


def countStudents(students, sandwiches):


    while len(students) > 0:
        if students[0] == sandwiches[0]:
            students.pop(0)
            sandwiches.pop(0)
        if len(students) > 0 and students[0] != sandwiches[0]:
            students.append(students.pop(0))
        if len(students) and sandwiches[0] not in students :
            break
    return len(students)

print(countStudents([1,1,0,0], [0,1,0,1]))