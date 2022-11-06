#sorting list
Students=['Jhon','Jake','Maria','Arya','Olivia','Emma']
Students.sort()
print(Students)

#descending list
mylist=[55,90,34,67]
mylist.sort(reverse=True)
print(mylist)

#coying list
my_list1=['hello','world']
my_list2 = my_list1.copy()
print(my_list2)



#creating tuple

my_tuple=(20,30,40)
print(my_tuple)

my_tuple1=(2,)
print(my_tuple1)

my_tuple2=tuple[(1,2,3,4,55,6)]
print(my_tuple2)

#index of tuple
my_tuple3=(10,20,30,40)
print(my_tuple3[-3])

#length of tuple
print(len(my_tuple3))

#change in tuple
my_tuple4=('a','b','e','d')
mylist=list(my_tuple4)
mylist[2]='c'
my_tuple4=tuple(mylist)
print(my_tuple4)

#append tuple with another tuple
my_tuple5=('hello',)
x=('world',)
mytuple6=my_tuple5+x
print(mytuple6)