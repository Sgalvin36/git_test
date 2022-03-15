inputs = []
while True:
    sval = input("Enter a number or DONE: ")
    if sval == 'DONE' :
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    try:
        inputs.append(int(sval))
    except:
        inputs.append(float(sval))
print(inputs)
print(len(inputs))

x = 0
sum = 0
while x < len(inputs):
    y = inputs[x]
    sum = sum + y
    x = x + 1

sum = sum/len(inputs)
print(sum)