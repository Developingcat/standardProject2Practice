print("##################################")
print("##                              ##")
print("##      Welcome to loan         ##")
print("##     Payment Calculator!      ##")
print("##                              ##")
print("##################################")






################- Variable 


principal = float(input("Enter the loan principal amount($): "))

annual = float(input("Enter the annual interest rate: (in %, e.g, 5.0 for 5%, or 6.5 for 6.5% ): "))

years = int(input("Enter the amount of years: "))


# For reference strong credits to the pink one; interest_rate = intrest / 100 / 12, months = loan * 12, and then an if else for if there's interest 

annual_rate = annual / 100 / 12
months = years * 12

# Note to self, work on the math before tommorrow, use as a study guide reference 

if annual_rate > 0:
    monthly_payment = (principal * annual_rate) / (1 -(1 + annual_rate) ** -months) # Try to keep the formula in mind,
else:
    monthly_payment = principal / months 

total_payment = monthly_payment * months  

print("Loan Payment Summary!")
print("=====================")
print(f"Loan Principal: ${principal}")
print("========---------")
print(f"Annual Interest Rate!: ${annual}")
print("========---------")
print(f"Loan Term: {years} years")
print("========---------")
print(f"Total Payment: ${total_payment:.2f}")
################## - Testing area - remove in final












########################





