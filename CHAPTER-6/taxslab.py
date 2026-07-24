P=float(input("enter the amount:"))
if P<=300000:
    print("No tax")
elif P<=600000:
    tax=(P-300000)*0.05
    print("Tax:",tax)
elif P<=1000000:
    tax=(P-600000)*0.1+15000 # 10% on amount exceeding 6 lakh + 5% on 3 lakh
    print("Tax:",tax)
    
else:
    tax=(P-1000000)*0.20+55000 # 20% on amount exceeding 10 lakh + 10% on 4 lakh + 5% on 3 lakh
    print("Tax:",tax)