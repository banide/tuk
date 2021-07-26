def comma(s1):
    for f in range(len(s1)):
        if s1[f] not in "0123456789,":
            print("NaN")
            #return
        else:
            print(1) 
comma("06,,4")