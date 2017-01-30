classmates = ['Michael','Bob','Tracy']
print(classmates,len(classmates))
print(classmates[0], classmates[1])
print(classmates[-1], classmates[-2])

classmates.append('Adam')
print(classmates)

classmates.insert(1, 'Jack')
print(classmates)

classmates.pop()
print(classmates)

classmates.pop(1)
print(classmates)

classmates[1] = 'Sarah'
print(classmates)

L = ['Apple', 123, True]
s = ['python', 'java', ['asp','php'],'scheme']
print(len(s))
