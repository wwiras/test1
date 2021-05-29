def reverseit(ori):
    newoutput = ''
    for i in ori:
        if i.isdigit():
            newoutput = newoutput + i 
    newoutput = newoutput[::-1]
    return newoutput

n = input('Please type an integer :')
answer = reverseit(n)
print(answer)