def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def main():
    #while():
    a, b = map(int, input().split()) #wtf is map?
    command = input() # I want to place input in 1 line
    if(command == "-"):
        num = sub(a, b)
        print(num)
    elif(command == "+"):
        num = add(a, b)
        print(num)
    else
        print("i can understand only + or -")
    
    #if(num == 0):
    #    break
    #print("₩n", "-----", "₩n")

    #I made this code with while() so there are  evidences
    

    

if __name__ == "__main__" :
    main()