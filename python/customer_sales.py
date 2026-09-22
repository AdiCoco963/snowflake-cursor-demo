# customer_sales.py

orders = [
    {"customer_id": 101, "amount": 1200},
    {"customer_id": 102, "amount": 500},
    {"customer_id": 101, "amount": 800},
    {"customer_id": 103, "amount": None},
]


def calculate_customer_sales(orders):
    customer_sales = {}

    for order in orders:
        customer_id = order["customer_id"]
        amount = 0 if order["amount"] is None else order["amount"]

        if customer_id not in customer_sales:
            customer_sales[customer_id] = 0

        customer_sales[customer_id] += amount

    return customer_sales


result = calculate_customer_sales(orders)

print(result)
