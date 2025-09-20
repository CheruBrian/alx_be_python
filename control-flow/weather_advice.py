#pront user for weather input 
weather = input("What`s the weather like today? (sunny/rainy/cold): ").lower()

#provide clothing recomedation based on input 
if weather == "sunny":
  print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
  print("Dont`t forget your umbrella and a raincoat.")
elif weather == 'cold":
print("make sure to wear a warm coat and a scarf.")
else:
print("Sorry, I dont`t have recommendation for this weather.")
