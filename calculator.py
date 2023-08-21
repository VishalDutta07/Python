def add():
    fp=open("calculator.txt","a")
    print("to add two numbers")
    a=input("enter first number: ")
    b=input("enter second number: ")
    c=int(a)+int(b)
    print("result of",a,"plus",b,"is",c,file=fp)
    fp.close()



def sub():
    fp=open("calculator.txt","a")
    print("to subtract two numbers")
    a=input("enter first number: ")
    b=input("enter second number: ")
    c=int(a)-int(b)
    print("result of",a,"minus",b,"is",c,file=fp)
    fp.close()



def mul():
    fp=open("calculator.txt","a")
    print("to multiply two numbers")
    a=input("enter first number: ")
    b=input("enter second number: ")
    c=int(a)*int(b)
    print("result of",a,"multiply",b,"is",c,file=fp)
    fp.close()

def div():
    fp=open("calculator.txt","r")
    print("to divide two numbers")
    a=input("enter first number: ")
    b=input("enter second number: ")
    c=int(a)/int(b)
    print("result of",a,"divide",b,"is",c,file=fp)
    fp.close()

def show():
    print("RESULTS......")
    fp=open("calculator.txt","r")
    print(fp.read())
    fp.close()

def main():
    print("1. ADDITION")
    print("2. SUBTRAACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISION")
    print("5. SHOW ALL RESULTS")
    print("0. BREAK")
    x=input("ENTER YOUR CHOICE>>>>>>")
    if x=='1':
        add()
        main()
    elif x=='2':
        sub()
        main()
    elif x=='3':
        mul()
        main()
    elif x=='4':
        div()
        main()
    elif x=='5':
        show()
        main()
    elif x=='0':
       exit()
    else:       
        print("<<<<<<<<<<<<<<<INVALID>>>>>>>>>")
main()