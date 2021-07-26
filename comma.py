def comma(s1):
    for f in range(len(s1)):
        if s1[f] not in "0123456789,":
            raise Exception("Invalid input. Your input contains characters other than numbers and commas.")
        else:
            if s1[f]=="," and s1[f+1]==",":
                raise Exception("Invalid input. Your input contains 2 or more consecutive commas.")
            else:
                return "The input is valid."
    
while True:
    comma(input("Enter a string and i will validate it:"))