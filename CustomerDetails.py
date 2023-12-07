import json
from dataclasses import dataclass

@dataclass
class CustomerDetails:

    monthly_inhand_salary : float
    num_bank_accounts: int
    num_credit_card : int
    interest_rate : float
    num_of_loan : int
    delay_from_due_date : int
    num_of_delayed_payment : int
    changed_credit_limit : float
    num_credit_inquiries : int
    credit_mix : str
    outstanding_debt : float
    credit_utilization_ratio : float
    credit_history_age : int
    payment_of_min_amount : str
    total_emi_per_month : float
    amount_invested_monthly : float
    monthly_balance : float
    payment_behaviour : str


