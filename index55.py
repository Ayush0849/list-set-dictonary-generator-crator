
# ls = []
# for i in range(100):
#     if i%3==0:
#         ls.append(i)

# ls = [i for i in range(100) if i%3==0]
#
# print(ls)


# dict1 = {i:f"item {i}" for i in range(1, 10001) if i%100==0}
# dict1 = {i:f"Item {i}" for i in range(5)}
#
# dict2 = {value:key for key,value in dict1.items()}
# print(dict1,"\n", dict2)

# dresses = {dress for dress in ["dress1", "dress2","dress1",
#                                "dress2","dress1", "dress2"]}
# print(type(dresses))

# evens = (i for i in range(100) if i%2==0)
# print(evens.__next__())

# for item in evens:
#     print(item)



lst = list()
print('Hello user!')
_i = int(input('Please enter how many items you want: '))
for i in range(_i):
     inpu = input(f'Please enter your {i + 1} item: ')
     lst.append(inpu)
# print(lst) 
choice = int(input('please enter what do your want:\n (1) for list\n (2) for dictonary\n (3) for set\n (4) for generator\nYour choice: '))
if choice == 1:
    lit = [i for i in lst]
    print(f'So here is your list: {lit}')
if choice == 2:
    dictonary = {f'item {i + 1 }':i for i in (lst)}
    print(f"So here is your dictonary: {dictonary}")
if choice == 3:
    sett = {i for i in lst}
    print(f"So here is your set: {sett}")
if choice == 4:
    generator = (i for i in lst)
    # print(generator.__next__)
    for items in generator:
        print(items)
