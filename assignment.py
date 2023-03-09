from datetime import datetime, timedelta

def calculate_subscription(expiry_date, months_to_buy, monthly_cost):
    # Convert expiry date string to datetime object
    expiry_date = datetime.strptime(expiry_date, "%d/%m/%Y")

    # Calculate the date of the farthest possible billing cycle
    if expiry_date.day <= 28:
        billing_cycle = datetime(expiry_date.year, expiry_date.month, 28)
    else:
        next_month = expiry_date.replace(day=28) + timedelta(days=4)
        billing_cycle = datetime(next_month.year, next_month.month, 28)

    # Calculate the new expiry date by adding months_to_buy to billing_cycle
    new_expiry = billing_cycle + relativedelta(months=months_to_buy)

    # Calculate the cost of subscription
    whole_months_cost = months_to_buy * monthly_cost
    remaining_days = (new_expiry - billing_cycle).days
    daily_cost = monthly_cost / 30
    remaining_days_cost = remaining_days * daily_cost
    cost = whole_months_cost + remaining_days_cost

    # Format the new_expiry date string as dd/mm/yyyy
    new_expiry_str = new_expiry.strftime("%d/%m/%Y")
   
    return (new_expiry_str, round(cost, 2))
