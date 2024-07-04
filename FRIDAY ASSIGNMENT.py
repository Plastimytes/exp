##2 CHARACTER FREQUENCY COUNT
str=input("Enter the string: ")
#list
l=list(str)
f=[l.count(ele)for ele in l]
print(f)
d=dict(zip(l,f))
print(d)
