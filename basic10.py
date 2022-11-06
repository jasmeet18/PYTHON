@@ -9,29 +9,65 @@
print(type(x))

#multiline strings
a="""hello coders.
a = """hello coders.
welcome to the world of coding.
enjoy creating things."""
print(a)

#access strings as array using index
myDict={"jake": "jakes value"}
myDict = {"jake": "jakes value"}
print(myDict["jake"])

#looping through a string
t="hello"
t = "hello"
for i in range(len(t)):
  print(t[i])

#string length
b="hello world"
b = "hello world"
print(len(b))

#slice
c="hello,world"
slice_obj=slice(5,11)
c = "hello,world"
slice_obj = slice(5,11)
print(c[slice_obj])

#slice from start
print(c[:5])
print(c[-5:-2])
print(c[-5:-2])

#modify strings using sets of built in methods


#uppercase
x = "hello"
print(x.upper())

#lowercase
print(x.lower())

#remove white spaces
x= " Let's study python"
print(x.strip())

#replace
x = "hello"
print(x.replace('h','e'))

#splitting the string
x = "hello world"
y = x.split()
print(x.split())
print(x.split(','))
print(y[0])


#string concatenation

x = "sam"
y = "iksha"
z = x+y
print(x+y)
print(z)