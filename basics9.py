#list
#list is used to store multiple items(same or diferent data types) in a single variable
#used to store collection of data
#start from index 0
#ordered collection
#list is changeable(change,add,remove)
#allows duplicate items

list = [10,20,30,40,"apples","oranges"]
print(list)
print(type(list))
print(list[0])

list = ["abcd", 40 , True , 60 , "apples"]
print(list)


#creating a list through constructor
list = "list((10,20,30))"
print(list)

#access items of a list
list1 = [10,20,30,40,50]
print(list1[-2])

#search will start at index 2(included) and end at index 5(not included)
print(list1[2:5])

print(list1[:4])

print(list1[2:])

#change the list items
list=[30,60,10,20,80]
list[1] = 90
list[2] = "hello"
print(list)

#change a range of list items
list[1:3] = ["hi" , "bye"]
print(list)

#insert more items than replace then new items will be inserted at the index that we provided
list2 = [10,20,30]
list2[1:2] = ["hi" , "hello"]
print(list2)

#insert items
list4 = [10,20,30]
list4.insert(2,40)
print(list4)

#for adding the items at the end of the list
list4.append(50)
list4.append(60)
list4.append(70)
print(list4)

#extend list
#to append or to add elements from another list into the current list we use extent()
#you can add or append any kind of iterable objects like tuples,sets,dictionaries etc.
lista = [10,20,30]
listb = [40,50,60]
lista.extend(listb)
print(lista)
print(listb)


listc=[90,80,70]
tuple = (50,60)
listc.extend(tuple)
print(listc)

#remove a specified iem from the list
#remove()
mylist = ["john","peter","jake"]
mylist.remove("john")
print(mylist)

#remove item from specified index
mylist1 = ["john","peter","jake"]
mylist1.pop(2)
print(mylist1)

#removing last item
#.pop()

#remove item from specified index using del keyword
mylist9=[10,20,30,40]
del mylist9[0]
print(mylist9)

#if we use del without mentioning any index it will show an error

#empty the list
mylist8=[1,2,3,4,5]
mylist8.clear()
print(mylist8)
