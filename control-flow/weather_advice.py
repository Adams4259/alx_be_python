#Weather recommendation program

weather = input("What is the weather like today? (sunny/rainy/cold): ").lower()

if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
if weather == "rainy":
    print("Don't forget your umbrella and raincoat.")
if weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")