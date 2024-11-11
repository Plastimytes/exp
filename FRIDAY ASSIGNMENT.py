##2 CHARACTER FREQUENCY COUNT
str=input("Enter the string: ")
#list
l=list(str)
f=[l.count(ele)for ele in l]
print(f)
d=dict(zip(l,f))
print(d)


num1=23
num2=12

#Find the sum of the numbers
sum=num1+num2
print(f"The sum is : {sum}")