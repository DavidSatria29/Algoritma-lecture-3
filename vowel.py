x = input("Kata : ")
v = ['a', 'i', 'u', 'e', 'o']
z = ""
for i in x :
    if i.lower() not in v :
        z += i 
print(z)
