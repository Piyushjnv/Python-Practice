import matplotlib.pyplot as plt
import math


radias  = 4
y = [] #y-coordinate
x = [] #x-coordinate

# First Quadrant
for i in range(401):
    i = int(i)/100
    try:
       
        z = math.pow(radias,2)- math.pow(i,2)
        x.append( math.sqrt(z))
        y.append(i)
    except (ValueError, TypeError):
        print("Error: Invalid input or type mismatch.")
        continue

# Second Quadrant
for i in range(400,-1,-1):
    i = int(i)/100
    try:
       
        z = math.pow(radias,2)- math.pow(i,2)
        x.append( -math.sqrt(z))
        y.append(i)
    except (ValueError, TypeError):
        print("Error: Invalid input or type mismatch.")
        continue

# THird Quadrant
for i in range(401):
    i = int(i)/100
    try:
       
        z = math.pow(radias,2)- math.pow(i,2)
        x.append( -math.sqrt(z))
        y.append(-i)
    except (ValueError, TypeError):
        print("Error: Invalid input or type mismatch.")
        continue

# Fourth Quadrant
for i in range(400,-1,-1):
    i = int(i)/100
    try:
       
        z = math.pow(radias,2)- math.pow(i,2)
        x.append( math.sqrt(z))
        y.append(-i)
    except (ValueError, TypeError):
        print("Error: Invalid input or type mismatch.")
        continue


plt.plot(x,y)
plt.title("circle figure")
plt.axis('equal')
plt.grid(True)
plt.show()
         