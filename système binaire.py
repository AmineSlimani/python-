print("-"*40)
print("Codage de nombre dans base 2 (1)(0) ")
print("-"*40)
x = input(" Write a number : ")
x = int(x)
print("-"*40)
x = int(x)

print("-"*40)
print("Solution : ")
print("-"*40)

cody = []

i = 0
while x>0:
    r = x%2
    r=int(r)
    cody.append(r)
    x = (x-r)/2
    i = i + 1


cody.reverse()
print(cody)

print("="*20)
print("="*20)
print("Developped by Amine Slimani")
