
#################### - Function definations 

def get_principal():
    while True: 
        variable = input("Please enter the loan principal amount($): ")
        if variable >= -1: 
            return get_principal
        else: 
            print("Please re-enter the loan principal amount($): ")
            # except ValueError:
            return 
################- Variable 

principal = float(get_principal())

annual_rate = get_annual_rate(float)

years = get_years(int)

monthly_payment = calculate_monthly_payment(principal, annual_rate, years)


################## - Testing area - remove in final


get_principal()








########################


print("##################################")
print("##                              ##")
print("##      Welcome to loan         ##")
print("##     Payment Calculator!      ##")
print("##                              ##")
print("##################################")



