def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def main():
    while True:
        indexs = input().split()
        a, b = map(int, indexs[:2])
        command = indexs[2]


        
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
       

if __name__ == "__main__" :
    main()