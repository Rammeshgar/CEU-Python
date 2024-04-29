#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Wellcome to tip calculater!")
bill = float(input("What is total bill? $\n"))
tip = float(input("Choose your tip: 10%, 15%, or 20%!\n"))
group = int(input("Payment be devided by how many people?\n"))
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
finalisedtip = tip / 100 * bill
totalbill = finalisedtip + bill
perperson = round(totalbill / group, 2)

print(f"Total bill = {totalbill}, Total tip = {finalisedtip}, Per person = {perperson}")