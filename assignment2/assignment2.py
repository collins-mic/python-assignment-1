# Creating an empty list
my_list =[]

# Appending 10,20,30,40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#inserting 15 at index 1
my_list.insert(1,15)

# extending the list
my_list.extend([50,60,70])

# removing the last element
my_list.pop()

# index of 30
index = my_list.index(30)
print("My list:", my_list)
print("Index of 30:",index)