print("Hello World")

# This is how you comment (press ctrl + / for universal comment)

# Variables:
name = "Clinton"
age = 31
found = False


# if/else statement
if age<100:
    print("Success")
    #MUST BE INDENTED for nesting (can also use {} to wrap if necessary)
elif age==100:
    print("you are 100")
else:
    print("you are over 100")


#functions
def say_Hello():
    print("Hello V2")


#Calling functions
say_Hello()


#Select code to run, right click and select run (Or shift + enter) (Everything needed for code selection needs to be loaded into memory)
print("my age is "+str(age)+" years old") #Must stringify to concat


#Array ('list')
colors = ["yellow","green","Blue"]
print(colors)


#Add element to array
colors.append("Pink")
print(colors)


#Remove element from array
colors.remove("yellow")
print(colors)
#Remove by position
colors.pop(0)
print(colors)
#Remove by slice by index
del colors[1]
print(colors)


#Logical AND/OR (Just the words)
if 100>5 and 200-6==6:
    print("yes")
elif 100>200 or 200-6==7:
    print("opt 2")
else:
    print("no")


#FOR loops
for color in colors:
    print(color)


#Dictionary
me = {
    "First_Name":"Clinton",
    "Last_Name":"Hockenberry",
    "Age":31
}
print(me)
print(me["First_Name"])
me["First_Name"] = "James"
print(me)