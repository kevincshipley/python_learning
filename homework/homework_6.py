# Write function tax that takes one argument.
# The argument will be a float representing a person's income.

# The function should calculate and return how much tax is owed as a float,
# based on the income argument. Do NOT format the return value.

# Only include the function definition in your submission.

def tax(income):

    # Taxable Income: Over $80,000
    if income > 80000:
        # Tax on this income: $17,550 plus 37 cents for each $1 over $80,000
        return float(17550 + .37 * (income - 80000))

    # Taxable Income: $37,001 – $80,000
    elif income < 80000 and income > 37000:
        # Tax on this income: $4,650 plus 30 cents for each $1 over $37,000
        return float(4650 + .30 * (income - 37000))

    # Taxable Income: $6,001 – $37,000
    elif income <= 37000 and income > 6000:
        # Tax on this income: 15 cents for each $1 over $6,000
        return float(.15 * (income - 6000))

    # Taxable Income: $0 – $6,000
    else:
        # Tax on this income: 0
        return float(income * 0)


