
def countWords():
    f = open(input('enter the file name: '))
    fileline = f.readlines()  
    file = open(input('transfer your data to another file: '), 'w+')
    for line in fileline:
        file.write(line)   

countWords()