def addfriend():
    fp=open("friends.txt","a")
    name=input("PLEASE INPUT YOUR FRIENDS NAME TO ADD: ")
    name=name.strip(' ')
    if len(name)>0:
        print(name,file=fp)
        fp.close()
    print(name," WAS ADDED WITH SUCCESS ")

def showfriend():
    print("CURRENT FRIEND LIST :")
    fp=open("friends.txt","r")
    i=1
    for name in fp:
        fp=open("friends.txt")
        print(i,name.rstrip('\n'))
        i+=1
        fp.close()

        
def main():
    while True:
        print("MENU\n------")
        print("1. ADD A NEW FRIEND  ")
        print("2. SHOW FRIEND   ")
        print("0. EXIT  ")

        choice=input("\nPLEASE INPUT CHOICE")
        if choice=='1':
            addfriend()
        elif choice=='2':
            showfriend()
        elif choice=='0':
            break
        else:
            print("INVALID CHOICE")
main()
