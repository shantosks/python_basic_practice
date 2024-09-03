#==================File Handling=================#

#Open a File on the Server------------------------

file = open(r"C:\Users\ShantoSen\Desktop\Easy_coding\seven\student.txt", "r")
print(file.read())

#Write to an Existing File----------------

file = open(r"C:\Users\ShantoSen\Desktop\Easy_coding\seven\student.txt", "a")
file.write("\nSession : 2019-2020")
file.close()

#open and read the file after the appending:
file = open(r"C:\Users\ShantoSen\Desktop\Easy_coding\seven\student.txt", "r")
print(file.read())
file.close()

#Write to an Existing File html form----------------

file = open(r"C:\Users\ShantoSen\Desktop\Easy_coding\seven\student.html", "a")
file.write("<h1>Kingsclan</h1>")
file.close()


#typeerror-------------------------

try:
    x = input("Enter your number: ")
    result = 10/x
    print(result)
except TypeError:
    print("Invalid Key.")

#zerodivisionerror-------------------------

try:
    x = int(input("Enter your number: "))
    result = 10/x
    print(result)
except ZeroDivisionError:
    print("Invalid Key.")

#indexerror-------------------------

try:
    x ="Shanto Kummar Shen"
    print(x[18])
except IndexError:
    print("Invalid Key.")