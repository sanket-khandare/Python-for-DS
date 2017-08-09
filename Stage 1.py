# Task 1 - Hello World
print('Hello World!')

# Task 2 - basic operations
name = 'sanket'
print('Hello '+ name)

# Task 3 - using lists
name_list = ['Sanket','Abhay','Pravin',['Friends', 3]]
print(name_list[3][1])

# Task 4 - copy & update list
new_name_list = name_list[:]
new_name_list[3][0] = 'Total Friends'
print(new_name_list)

# Task 5 - check help doc
#help(round)

# Task 6 - use len and type of
print(len(new_name_list))
print(type(new_name_list[3]))
print(len(new_name_list[3]))

# Task 7 - sort list
print(sorted(new_name_list))

# Task 8 - use index
print(name_list.index('Pravin'))

# Task 9 - append list & reverse
name_list.append("Sagar")
print(name_list)
name_list.reverse()
print(name_list)
