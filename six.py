#odd number by while loop

print("\nodd number by while loop: ")
i = 1
while i <= 100:
    print(i,end=" ")
    i += 2

#Even number by while loop

print("\n\nEven number by while loop: ")
j = 0
while j <= 100:
    print(j,end=" ")
    j += 2

#Odd number by for loop

print("\n\nodd number by for loop: ")
for i in range(1,100,2):
    print(i,end=" ")

#Even number by for loop

print("\n\nEven number by for loop: ")
for j in range(0,100,2):
    print(j,end=" ")



#Area of 3 triangles

def area_of_triangle(base,height):
    return (0.5*base*height)
for i in range (1,4):
    print(f"\n\nTriangle {i}: ")
    base = int(input("Enter the base of the triangle: "))
    height = int(input("Enter the height of the triangle: "))
    area = area_of_triangle(base,height)
    print(f"\n\nTriangle {i}'s area is = {area}\n")
    print("*-" * 20 )


#adding four numbers

def add_numbers(a,b,c,d):
    return a+b+c+d
a= int(input("Enter 1st Number: "))
b= int(input("Enter 2nd Number: "))
c= int(input("Enter 3rd Number: "))
d= int(input("Enter 4th Number: "))

sum = add_numbers(a,b,c,d)
print(f"The Summation of four numbers is = {sum}.")