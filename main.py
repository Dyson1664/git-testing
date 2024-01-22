numbers = [1, 2, 3, 4, 5]
letters = ['a', 'b', 'c', 'd', 'e']

list1 = []
for number, letter in zip(numbers, letters):
    list1.append((number, letter))

print(list1)


for i in enumerate(letters, 1):
    print(i)


names = ['Alice', 'Bob', 'Charlie']
ages = [24, 50, 18]

for i, (name, age) in enumerate(zip(names, ages), 1):
    print(i, name, age)



#adding this comment to dave branch
