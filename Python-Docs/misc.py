# for i in range(2):
#    print(i)

for i in range(0, 10, 3):
    print(i)

print("############")

a = ['Mary', 'had', 'a', 'little', 'lamb']
for person in range(len(a)):
    print(person, a[person])

print("############")

for x in range(2, 3):
    print("ran!")

print("############")

for n in range(2, 10):
     for x in range(2, n):
         if n % x == 0:
             print(n, 'equals', x, '*', n//x)
             break
     else:
         # loop fell through without finding a factor
         print(n, 'is a prime number')

print("##########")

status = 418
def http_error(status):
    match status:
        case 400:
             print("Bad request")
        case 404:
            print("Not found")
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
print(http_error(status))

print("###########")

# point is an (x, y) tuple
point = (1, 2)
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")

print("#############")

class Point:
    x: int
    y: int
point = [Point(0,0)]
match points:
    case []:
        print("No points")
    case [Point(0, 0)]:
        print("The origin")
    case [Point(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")
