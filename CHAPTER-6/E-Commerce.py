n=int(input("enter product cost:"))
if n>5000:
    print("you are eligible for 20% discount")
    discount=n*0.2
    total_cost=n-discount
    print("total cost after discount:",total_cost)
    
elif n>2000:
    print("you are eligible for 10% discount")
    discount=n*0.1
    total_cost=n-discount
    print("total cost after discount:",total_cost)
   
elif n>1000:
    print("you are eligible for 5% discount")
    discount=n*0.05
    total_cost=n-discount
    print("total cost after discount:",total_cost)
    
else:
    print("you are not eligible for any discount")
    total_cost=n
    print("total cost:",total_cost)
    