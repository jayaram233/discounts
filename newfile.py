price=int(input())
if 1000<=price<2000:
	print("total bill is",price) 
        print("Discount on billed amount is",(10*price)/100)
	print("paid bill is",price-(price*10)/100)
elif 2000<=price<3000:
	print("total bill is",price) 
        print("Discount on billed amount is",(20*price)/100)
	print("paid bill is",price-(price*10)/100)
elif 3000<=price<5000:
	print("total bill is",price) 
        print("Discount on billed amount is",(30*price)/100)
	print("paid bill is",price-(price*10)/100)		
elif price>=5000:
	print("total bill is",price) 
        print("Discount on bill amount is",(40*price)/100)
	print("paid bill is",price-(price*10)/100)	
else:
	print("you did not get discount" )
        print("total bill is", price) 
        Print("paid bill is",price) 
      


Output:
 1000
 total bill is 1000
 Discount on bill amount is 100
 Paid bill is 900
 
 

	
