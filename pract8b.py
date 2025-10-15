#Derive the expression based on distributive law

# 1. With random
import random
a = random.randint(0, 99)
b = random.randint(0, 99)
c = random.randint(0, 99)
print ("Distributive laws ->")
print ("A*(B+C) ->", (a * (b + c)))
print ("(A*B)+(A*C) ->", ((a * b) + (a * c)))

# 2. Without random
a = 3
b = 7
c = 8
print ("Distributive laws ->")
print ("A*(B+C) ->", (a * (b + c)))
print ("(A*B)+(A*C) ->", ((a * b) + (a * c)))