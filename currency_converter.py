
def convert_to_euro(rupees):
   
    exchange_rate = 90 
    euros = rupees / exchange_rate
    return round(euros, 2)


money_in_inr = 4500
money_in_eur = convert_to_euro(money_in_inr)

print("\n--- Europe Trip Budget Calculator ---")
print(f"Amount in Indian Rupees: ₹{money_in_inr}")
print(f"Amount in Euros: €{money_in_eur}")
