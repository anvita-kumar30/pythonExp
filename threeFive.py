def square(n):
  return n**2
def cube(n):
  return n**3
def decor_add4(func,n):
  return func(n)+4
def decor_multiply2(func,n):
  return func(n)*2
n=int(input("Enter a number: "))
print("Square of",n,"is",square(n))
print("Adding 4 to the result:",decor_add4(square,n))
print("Multiplying the result by 2:",decor_multiply2(square,n))
print("Cube of",n,"is",cube(n))
print("Adding 4 to the result:",decor_add4(cube,n))
print("Multiplying the result by 2:",decor_multiply2(cube,n))