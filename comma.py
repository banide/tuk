def comma(s1):
    for f in range(len(s1)):
        if s1[f] not in "0123456789,":
            raise Exception("")
        else:
            for d in range(len(s1)):
                if s1[d]=="," and s1[d+1]==",":
                    raise Exception("Invalid input")
    
while True:
    comma(input("Enter a string and i will validate it:"))