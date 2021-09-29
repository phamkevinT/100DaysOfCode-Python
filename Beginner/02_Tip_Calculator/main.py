print("Welcome to the Tip Calculator.");

bill = float(input("What was the total bill? "));

tip = int(input("What percent tip would you like to give? "));

people = int(input("How many people to split the bill between? "));

tip_as_percent = tip / 100.0;

tip_amount = bill * tip_as_percent;

total_bill =  bill + tip_amount;

bill_per_person = total_bill / people;

final_total = round(bill_per_person, 2)

print(f"Each person should pay ${final_total}");
