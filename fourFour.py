d = {}
n = int(input("Enter the size of dictionary: "))
for i in range(n):
    d.update({input('Key:'):input('Value:')})
    print('Dictionary:',d)
K = list(d.keys())
K.sort()
print("After sorting the dictionary by key:-")
print({i:d[i] for i in K})
d1 = {}
n1 = int(input("Enter the size of first dictionary: "))
for i in range(n1):
    d1.update({input('Key:'):input('Value:')})
d2 = {}
n2 = int(input("Enter the size of second dictionary: "))
for i in range(n2):
    d2.update({input('Key:'):input('Value:')})
    d1.update(d2)
print("After concatenating the two dictionaries:",d1)