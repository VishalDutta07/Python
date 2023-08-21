
def test():
    print("testing:")
    fp=open("qwerty.txt","w")
    i=1
    for name in fp:
        fp=open("qwerty.txt")
        print(i,name.count('\n'))
        i+=1
        fp.close()

test()