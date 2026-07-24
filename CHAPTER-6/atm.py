p = 20000
TW =int(input("Enter the amount to withdraw:"))
if TW>p:
    print("Insufficient balance")
    
elif TW%100!=0:
    print("Please enter the amount in multiples of 100")
    
else:
    p=p-TW
    print("Please collect your cash")
    print("Available balance:",p)