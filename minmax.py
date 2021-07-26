l3=[]
min1=0
max2=0
def min1(l1):
    if type(l1)!=list:
        raise Exception("Error: Invalid input")
    else:
        min2=l1[0]
        for a in range(1,len(l1)):
            if min2>l1[a]:
                min2=l1[a]
        return min2

                              
def max1(l2):
    if type(l2)!=list:
        raise Exception("Error: Invalid input")
    else:
        max2=l2[0]
        for a in range(1,len(l2)):
            if max2<l2[a]:
                max2=l2[a]
        return max2

option=input("Press 1 for min function and 2 for max function:")

print(max1(list(option)))