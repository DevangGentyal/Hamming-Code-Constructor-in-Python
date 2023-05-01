#Declaring required Arrays
arr=[]
p1arr=[]
p2arr=[]
p3arr=[]
finalarr=[]

# Chechiking if all the entered digits are in Binary or not
def digits(x):
    flag=0
    i=0
    while(x>0):
        dig = x%10
        if (dig!=1 and dig!=0):
            flag=1
            break
        else:
            arr.append(dig)
            flag=0
            i+=1
        x=int(x/10)
    return flag



#Returning the 1st parity bit i.e. p1
def parity1():
    p1arr=[arr[0],arr[1],arr[3]]

    count=0
    for i in p1arr:
        if i==1:
            count+=1
    if(count%2==0):
        return 0
    else:
        return 1

#Returning the 2nd parity bit i.e. p2
def parity2():
    p2arr=[arr[0],arr[2],arr[3]]

    count=0
    for i in p2arr:
        if i==1:
            count+=1
    if(count%2==0):
        return 0
    else:
        return 1

# Returning the 3rd parity bit i.e. p3
def parity3():
    p3arr=[arr[1],arr[2],arr[3]]

    count=0
    for i in p2arr:
        if i==1:
            count+=1
    if(count%2==0):
        return 0
    else:
        return 1
    
# Main Program for getting all the Parity bits and appending them to the Message bits
def main():
    k=0
    while(((2**k)>=(k+n+1))!=True):
        k+=1
    if(k==3):
        p1 = parity1()
        p2 = parity2()
        p3 = parity3()
        finalarr=p1,p2,arr[0],p3,arr[1],arr[2],arr[3]
        print("The Hamming Code is:\n",finalarr)

# Starting Execution from Here
x = int(input("Enter a number: "))
n=len(str(x))
if(n!=4):
    print("Only four digits Allowed!")
else:
    check = digits(x)
    arr=list(reversed(arr))

    if(check!=0):
        print("Only Binary Digits Allowed!")
    else:
        main()
