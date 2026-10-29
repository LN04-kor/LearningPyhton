def Add(a, b):   
    return a + b


def Sub(a, b):
    return a - b


def WrongIndex():
    try:
        a, b = map(int, input("insert two number>")
        return a, b
    except ValueError:
        print("wrong type index")
        return None

    

def main():
    while True:
        command = input("command>")
        if command == "end" :
            break
        
        if command not in ("+", "-") :
            print("i can't understand about it")
            continue

        index = WrongIndex()
        if index is None : 
            continue
        a, b = index

        if command == "+" : 
            print(add(a, b)
        elif command == "+" : 
            print(sub(a, b)) 
        
    
        print("\n", "-----", "\n")


#I made this code with while() so there are  evidences
       

if __name__ == "__main__" :
    main()