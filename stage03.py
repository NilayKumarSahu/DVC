with open('artifacts.txt', 'r') as f:
    txt = f.read()
    print(txt)


with open('artifacts.txt', 'w') as f:
    txt = f.write(txt+ 'I have added one more line' )
    print(txt)  
    print("Its the end of stage03")  