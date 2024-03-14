# 1. creating an empty list called my_list
my_list = []

#2.appending 10, 20, 30, 40. to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

#3. inserting 15 at the second postion in the list
my_list.insert(1, 15)

#4. extend my_list with another list
my_list.extend([50, 60, 70])
print(my_list)

#5. Remove the last element from my_list
my_list.pop()
print(my_list)

#6. sort my_list in ascending order
my_list.sort()
print(my_list)

#7. To get the index of 30 in my_list
index_of_30 = my_list.index(30)
print('The index of value 30 in my_list is: ', index_of_30)
