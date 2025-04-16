# TODO: Open the file "students.txt" in read mode
f= open("students.txt", "r")
# TODO: Read lines from the file and store them in a list
info_list = []
bad_list=[]
for line in f:
    line=line.strip("  \n")
    info_list.append(line)
for line in f:
    bad_list.append(line)
#TODO: Remove extra spaces and newlines from each name. Use list comprehension to STRIP whitespace
print(bad_list)
print(info_list)
# TODO: Print the list
# TODO: Print the cleaned-up list
