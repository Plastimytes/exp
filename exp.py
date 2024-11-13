## User input which is an integer
num=int(input("Enter a number "))

#initialize the while loop
number=0

##While loop to find out if the number is even
while num%2  != 0:
    print(f"{num} is an odd number")
    num=int(input("Enter a number "))

#peinting the output
print(f" number is not odd")    
