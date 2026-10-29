def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def main():
    while():
        a, b = map(int, input().split())
        command = input() # I want to place input in 1 line
        if(command == "-"):
            num = sub(a, b)
            print(num)
        elif(command == "+"):
            num = add(a, b)
            print(num)
        elif(command == "end"):
            break
        else:
            print("i can understand only +, -,end")
    
        print("\n", "-----", "\n")


#I made this code with while() so there are  evidences
       

if __name__ == "__main__" : # interesting usage
    main()