def Add(a, b):   
    return a + b


def Sub(a, b):
    return a - b


def Mul(a, b):
    return a * b

def Div(a, b):
    return a / b


def GetNumber():
    try:
        a, b = map(int, input("insert two number>").split())
        return a, b
    except ValueError:
        print("wrong type index")
        return None

    

def main():
    while True:
        command = input("command>").strip
        if command == "end" :
            break
        
        if command not in ("+", "-", "*", "/") :
            print("i can't understand about it")
            continue

        index = GetNumber()
        if index is None : 
            continue
        a, b = index

        if command == "+" : 
            print(Add(a, b))
        elif command == "-" : 
            print(Sub(a, b)) 
        elif command == "*" : 
            print(Mul(a, b))
        elif command == "/" : 
            try:
                print(Div(a, b))
            except ZeroDivisionError:
                print("you can't do that")
        
    
        print("\n", "-----", "\n")


#I made this code with while() so there are  evidences
       

if __name__ == "__main__" :
    main()