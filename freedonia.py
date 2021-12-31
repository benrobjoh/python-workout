def calculate_tax(amount, province, hour):
    tax = {
        'chico': 0.5,
        'groucho': 0.7,
        'harpo': 0.5,
        'zeppo': 0.4
    }
    return amount * (1 + tax[province.lower()] * (hour / 24.0))