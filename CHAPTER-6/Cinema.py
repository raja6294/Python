n=int(input("enter age of the person:"))
TC=int(input("enter ticket cost:"))
time = int(input("enter time of the show in 12-hour format :"))
if n>=60 :
    print("you are eligible for senior citizen discount")
    discount=TC*0.15
    total_cost=TC-discount
    print("total cost after discount:",total_cost)
    
elif n>=18 and time <4 :
    print("you are eligible for adult discount")
    discount=TC*0.1
    total_cost=TC-discount
    print("total cost after discount:",total_cost)
    
else:
    print("you are not eligible for free ticket")
    total_cost=0
    print("total cost:",total_cost)
    
    
    