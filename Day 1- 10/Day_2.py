# Tip calculater
print("welcome to tip calculater")
bill = float(input("what was the total bill? $"))
tip = int(input("what peercentege would you like to give? 10, 12, or 15?"))
people = int(input("how mony people are split the bill? $"))
tip_as_persent = tip / 100
totl_tip_amount = bill * tip_as_persent
total_bill = bill + totl_tip_amount
bill_pre_person = total_bill / people 
final_amount = round(bill_pre_person, 2)
print(f"each persen should pay ${final_amount}")