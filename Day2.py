def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def main():
    a, b = 0, 0
    while True:
        command = input("command>")
        if(command == "end"):
            break
        elif(command == "-"):
            print(int(input("insert two number>", sub(a, b).split())))
        elif(command == "+"):
            print(int(input("insert two number>", add(a, b).split())))
        else:
            print("i can understand only +, -")
    
        print("\n", "-----", "\n")


#I made this code with while() so there are  evidences
       

if __name__ == "__main__" :
    main()