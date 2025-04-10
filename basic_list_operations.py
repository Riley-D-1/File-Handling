# 1. Create a list named 'students' with at least 4 student names.
students = ['Alice', 'Bob', 'Charlie', 'Diana']

# 2. Print the first and last student's name using indexing.
# Remember that the first item has an index of 0.
print(students[0])
print(students[3])

# 3. Add a new student to the end of the list.
# Use append() to add a new name to the list.
students.append('Dave')
# 4. Remove the second student from the list.
# Use pop()to delete an element by index.
students.pop(1)
# 5. Print the updated list.
print(students)