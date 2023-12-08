from CustomerDetails import CustomerDetails

# Data Preprocessing steps along with one hot encoding
def get_preprocessed_array(customer_details: CustomerDetails):
    preprocessed_values = []
    preprocessed_values.append(customer_details.monthly_inhand_salary)
    preprocessed_values.append(customer_details.num_bank_accounts)
    preprocessed_values.append(customer_details.num_credit_card)
    preprocessed_values.append(customer_details.interest_rate)
    preprocessed_values.append(customer_details.num_of_loan)
    preprocessed_values.append(customer_details.delay_from_due_date)
    preprocessed_values.append(customer_details.num_of_delayed_payment)
    preprocessed_values.append(customer_details.changed_credit_limit)
    preprocessed_values.append(customer_details.num_credit_inquiries)
    preprocessed_values.append(customer_details.outstanding_debt)
    preprocessed_values.append(customer_details.credit_utilization_ratio)
    preprocessed_values.append(customer_details.credit_history_age)
    preprocessed_values.append(customer_details.total_emi_per_month)
    preprocessed_values.append(customer_details.amount_invested_monthly)
    preprocessed_values.append(customer_details.monthly_balance)

    payment_behaviour = customer_details.payment_behaviour
    if "small_value" in payment_behaviour:
        preprocessed_values.append(0)
        preprocessed_values.append(0)
        preprocessed_values.append(1)
    elif "medium_value" in payment_behaviour:
        preprocessed_values.append(0)
        preprocessed_values.append(1)
        preprocessed_values.append(0)
    else:
        preprocessed_values.append(1)
        preprocessed_values.append(0)
        preprocessed_values.append(0)

    if "low_spent" in payment_behaviour:
        preprocessed_values.append(0)
        preprocessed_values.append(1)
    else:
        preprocessed_values.append(1)
        preprocessed_values.append(0)

    if customer_details.credit_mix == "bad":
        preprocessed_values.append(1)
        preprocessed_values.append(0)
        preprocessed_values.append(0)
    elif customer_details.credit_mix == "good":
        preprocessed_values.append(0)
        preprocessed_values.append(1)
        preprocessed_values.append(0)
    else:
        preprocessed_values.append(0)
        preprocessed_values.append(0)
        preprocessed_values.append(1)

    if customer_details.payment_of_min_amount == "yes":
        preprocessed_values.append(0)
        preprocessed_values.append(1)
    else:
        preprocessed_values.append(1)
        preprocessed_values.append(0)

    return preprocessed_values
