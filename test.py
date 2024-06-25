with open('data.csv', 'r') as file:
    data = file.readlines()
    for line in data:
        words = list(line.split(','))
        print(words)

a = 10
for i in range(10):
    print(i)

print(a * a)
