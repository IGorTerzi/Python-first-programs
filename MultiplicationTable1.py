print('\n')
print('Таблица умножения')
print('\n')
for i in range(1, 11):
    for k in range(2, 5):
        print(f'{k} x {i} = {k * i}\t', end='')
        if(i==11):
            print('\t')
    print('') 
print('\n')

for i in range(1,11):
    for m in range(5, 8):
        print(f'{m} x {i} = {m * i}\t', end='')
        if(i==11):
            print('\t')
    print('') 
print('\n')

for i in range(1,11):   
    for l in range(8, 11):
        print(f'{l} x {i} = {l * i}\t', end='')
        if(i==11):
            print('\t')
    print('') 
print('\n')