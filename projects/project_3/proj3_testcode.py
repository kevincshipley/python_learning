print("Credit Card Entry")
print("-----------------------------------------------------------------------"
      "---------")

# Your test code should include a loop that prompts for a credit card number
# or q to quit.
card_num = input("Enter credit card number (q to quit): ")

# If the user types q, the loop should be terminated.
while card_num != "q":
    
    # If the user enters a credit card number, print a statement whether it is
    # valid and prompt for another credit card number.
    if is_valid_CC(card_num):
        print("{} is valid.".format(card_num))
    else:
        print("{} is invalid".format(card_num))

    card_num = input("Enter credit card number: ")

print("Routing Number Entry")
print("-----------------------------------------------------------------------"
      "---------")

# Do the same for routing numbers - Include loop that prompts for a routing
# number or q to quit.

# If the user enters a routing number, print a statement whether it is valid
# and prompt for another routing number.

# If the user types q, the loop should be terminated.
