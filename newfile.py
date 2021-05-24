price=int(input())
if 1000<=price<2000:
	print('total bill is',price)
	print('Discount on bill amount is',(10*price)/100)
	print('paid bill is',price-(price*10)/100)
elif 2000<=price<3000:
	print('total bill is',price)
	print('Discount on bill amount is',(20*price)/100)
	print('paid bill is',price-(20*10)/100)
elif 3000<=price<5000:
	print('total bill is',price)
	print('Discount on bill amount is',(10*price)/100)
	print('paid bill is',price-(price*10)/100)		
elif price>=5000:
	print('total bill is',price)
	print('Discount on bill amount is',(10*price)/100)
	print('paid bill is',price-(price*10)/100)	
else:
	print('you did not purchase enough to get discount' )
	