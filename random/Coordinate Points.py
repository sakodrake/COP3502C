x = float(input("Enter an x coordinate: "))
y = float(input("Enter a y coordinate: "))

Euclidean_distance = (x**2 + y**2)**0.5
Manhattan_distance = abs(x) + abs(y)
xmidpoint = x / 2
ymidpoint = y/2
print(f"The Euclidean distance between the two points {x}, {y}, is {Euclidean_distance:.2f}")
print(f"The Manhattan distance between the two points {x}, {y}, is {Manhattan_distance:.2f}")
print(f"The midpoint between the two points is x={xmidpoint:.1f}, y={ymidpoint:.1f}")

                
