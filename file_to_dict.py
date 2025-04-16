# TODO: Open "student_data.txt" in read mode
f= open("student_data.txt", "r")
# TODO: Create dictionary student_dict 
# TODO: For each line, split line into name and age (separated by comma)
i=1
d={}
for line in f:
        data = line.split()
        key, value = data[0], data[1]
        d[key] = value
# TODO: Store in the dictionary with the name as the key and age as the value

# TODO: Print the dictionary
print(d)