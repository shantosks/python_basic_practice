#Comparison Operators

x = 5
y = 6

print(x==y)   #	Equal
print(x!=y)   #	Not Equal
print(x>y)   #	Greater than
print(x<y)   #	Less than
print(x>=y)   #	Greater than or equal to
print(x<=y)   #	Less than or equal to

#Logical Operators

x = 5
print(x > 4 and x < 9)  #and operator--Returns True if both statements are true
y = 6
print(y < 5 or y < 4)   #or opearator--Returns True if one of the statements is true
x = 5
print(not(x > 3 and x < 10))   #Not operator--Reverse the result, returns False if the result is true

#Identity Operators

#----------------is------------------

x = ["King", "Queen"]
y = ["King", "Queen"]
z = x

print(x is z)    # returns True because z is the same object as x
print(x is y)    # returns False because x is not the same object as y, even if they have the same content
print(x == y)    # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

#--------------is not-----------------
x = ["Charlie", "Tessa"]
y = ["Charlie", "Tessa"]
z = x

print(x is not z)   # returns False because z is the same object as x
print(x is not y)   # returns True because x is not the same object as y, even if they have the same content
print(x != y)       # to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y


#Membership Operators

#---------------------in-----------------
x = ["Sun", "Moon"]
print("Sun" in x)       #Returns True if a sequence with the specified value is present in the object

#---------------------not in-----------------
y = ["Sun", "Moon"]
print("Moon" not in y)      #Returns True if a sequence with the specified value is not present in the object



#Odd and Even number

x = int(input("Enter the Number: "))

if x % 2 == 0:
    print(x, " is an Even Number")
else:
    print(x, " is an Odd Number")


#finding the lowest number between 4 numbers using min function

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
d = int(input("Enter fourth number : "))

result = min(a,b,c,d)
print("The lowest number is : ", result)

#finding the lowest number between 4 numbers using  conditions

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
d = int(input("Enter fourth number : "))

if a<b and a<c and a<d:
    print("Your given first number is lowest.")
elif b<a and b<c and b<d:
    print("Your given second number is lowest.")
elif c<a and c<b and c<d:
    print("Your given third number is lowest.")
else:
    print("Your given fourth number is lowest.")


#find the Grade 

x = int(input("Enter your marks: "))
if x > 100 or x < 0:
    print("Invalid Number.")
elif x >=80:
    print("You got A+")
elif x >=70:
    print("You got A")
elif x >=60:
    print("You got A-")
elif x >=50:
    print("You got B")
elif x >=40:
    print("You got C")
elif x >=33:
    print("You got D")
else:
    print("You Have Failed.")