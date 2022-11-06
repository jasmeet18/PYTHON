print ("hello world")

if 6>4:
   print ('6 is greter than 4')
   print ("hey")

   #100 lines of code but with no indentation/space error (while block creation)
#hashtag is to comment it i.e the comment won't be compiled
#organised
x = 10 #number
y = "hey" #string
print (x)
print(y)
#for string or text we can use either single or double quotations

#later value will print out i.e. latest
x = 10
x = "bye"
print (x)

#to print both do:
x = 10
print (x)
x = "bye"
print (x)

#python is a case sensitive language
a=60
A="hi"
print(a) #A will not overwrite

#get the type of variable printed i.e class type
x = 50 #int for integers
y = "aanya" #str for string/text
z = 1.546 #float for decimal values
print (type(x))
print (type(y))
print (type(z))

#casting

#to specify the data type of a variable using casting

x=int(10)
y=str(10)
z=float(10)
print (x,y,z) #will give 10 10 10.0
#print (x+y) will give error as int can't be added to str
#same with y and z
print(x+z) #comes out 20.0 as it's int+float (no. + decimal value)
 34  
1. basics/b.Variablesrules.py
@@ -0,0 +1,34 @@

#Acceptable Variable Names

myname = "john"
print(myname)
my_name = "john"
print (my_name)
#more examples
#_my_name = "john"
#myName  = "john"
#MYNAME = "john"
#myname3 = "john"

#Not Acceptable variable names

#2myname = "john"
#-myname$ ="john" (- is not underscore_)
#my name = "john" (there's space in between my , name and python takes intdentation seriously)

#typing cases

myfirstname = "peter"

# 1.camel case
# myFirstName = "peter"

# 2. pascal case
# MyFirstName = "peter"

# 3.snake case
# my_first_name "peter"

print(myfirstname)