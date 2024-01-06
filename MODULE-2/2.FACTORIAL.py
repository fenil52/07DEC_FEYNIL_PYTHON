import math 

# == FIRST METHOD ===

a = int(input("Enter Number :"))

c=math.factorial(a)

print(c)

# === SECOND METHOD ===

b=int(input("Enter Number :"))
factorial = 1

for i in range(1,b+1):
    factorial *= i
print("Factorial Number Is :",factorial)




    
