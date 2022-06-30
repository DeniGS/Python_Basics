yard_sq_meters = float(input())
price_per_sqm = 7.61
total_price = yard_sq_meters * price_per_sqm
discount = total_price * 0.18
final_price = total_price - discount

print(f"The final price is: {final_price} lv.")

print(f"The discount is: {discount} lv.")