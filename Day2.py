def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def main():
    a, b = 0
    while True:
        command = input()
        if(command == "end"):
            break
        else:
            command = input()


        if(command == "-"):
            print(input(add(a, b)))
        elif(command == "+"):
            print(input(add(a, b)))
        else:
            print("i can understand only +, -")
    
        print("\n", "-----", "\n")


#I made this code with while() so there are  evidences
       

if __name__ == "__main__" :
    main()