my_list= [ ]
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.insert(1, 15)#index first then value
list2 = [50,60,70]
my_list.extend(list2)
my_list.pop(-1)#removes last item from list
my_list.sort()
if 30 in my_list:
    print(f"Value 30 is found at index {my_list.index(30)}")
else:
    print("value not found")

print(my_list)
