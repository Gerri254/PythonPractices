def calculate_total_cost(item_price, tax_rate, discount_percentage=0):
    tax_amount = item_price * (tax_rate / 100)
    discounted_price = item_price - (item_price * discount_percentage)
    total_cost = discounted_price + tax_amount
    return total_cost

def main():
    # Input item price, tax rate, and discount percentage from the user
    item_price = float(input("Enter the item price: "))
    tax_rate = float(input("Enter the tax rate (%): "))
    discount_percentage = float(input("Enter the discount percentage (%): "))

    # Calculate the total cost using the function
    total_cost = calculate_total_cost(item_price, tax_rate, discount_percentage)

    # Display the total cost
    print("The total cost of the item after tax and discount is:", total_cost)

if __name__ == "__main__":
    main()


# Use of while function

def get_positive_integer():
    """
    Prompt the user to input a positive integer and return it.
    """
    while True:
        try:
            num = int(input("Please enter a positive integer: "))
            if num > 0:
                return num
            else:
                print("Please enter a positive integer greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")

def main():
    # Get a positive integer from the user
    positive_integer = get_positive_integer()
    print("You entered:", positive_integer)

if __name__ == "__main__":
    main()
