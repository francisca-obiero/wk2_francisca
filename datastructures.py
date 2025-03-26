# Create an empty list  my_list
my_list = []  

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#Insert 15 at the second postition (index 1)
my_list.insert(1, 15)

my_list.extend([50, 60, 70])

# Remove the last element
my_list.pop()

# Sort in ascending order
my_list.sort()

index_30 = my_list.index(30)
print(index_30)