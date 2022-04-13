#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

#Pay attention to data types int/str/float*/ and variables
#Variables? 
print("Welcome to the Tip Calculator.")
bill = (float(input("What was the total Bill? $"))) #str
#print(bill)

tip = (int(input("What percentage tip would you like to give? 10, 12, or 15? (can input any int.): \n")))
#print(type(tip))

people = (int(input("How many people to split the bill? ")))
#print(type(people))

tip_per = round( bill * ( 1 + (tip / 100)) , 2)
#print(tip_per)

tip_split = round( tip_per / people , 2)
#print(tip_split)
print(f"Each person should pay: ${tip_split}")