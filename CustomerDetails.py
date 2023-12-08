from pandas import Series


class CustomerDetails:

    def __int__(self, cust_series: Series):
        self.monthly_inhand_salary = float(cust_series.get('monthly_inhand_salary', 0))
        self.num_bank_accounts = int(cust_series.get('num_bank_accounts', 0))
        self.num_credit_card = int(cust_series.get('num_credit_card', 0))
        self.interest_rate = float(cust_series.get('interest_rate', 0))
        self.num_of_loan = int(cust_series.get('num_of_loan', 0))
        self.delay_from_due_date = int(cust_series.get('delay_from_due_date', 0))
        self.num_of_delayed_payment = int(cust_series.get('num_of_delayed_payment', 0))
        self.changed_credit_limit = float(cust_series.get('changed_credit_limit', 0))
        self.num_credit_inquiries = int(cust_series.get('num_credit_inquiries', 0))
        self.credit_mix = cust_series.get('credit_mix', '')
        self.outstanding_debt = float(cust_series.get('outstanding_debt', 0))
        self.credit_utilization_ratio = float(cust_series.get('credit_utilization_ratio', 0))
        self.credit_history_age = int(cust_series.get('credit_history_age', 0))
        self.payment_of_min_amount = cust_series.get('payment_of_min_amount', '')
        self.total_emi_per_month = float(cust_series.get('total_emi_per_month', 0))
        self.amount_invested_monthly = float(cust_series.get('amount_invested_monthly', 0))
        self.monthly_balance = float(cust_series.get('monthly_balance', 0))
        self.payment_behaviour = cust_series.get('payment_behaviour', '')

    def __init__(self, form):
        self.monthly_inhand_salary = float(form.get('monthly_inhand_salary', 0))
        self.num_bank_accounts = int(form.get('num_bank_accounts', 0))
        self.num_credit_card = int(form.get('num_credit_card', 0))
        self.interest_rate = float(form.get('interest_rate', 0))
        self.num_of_loan = int(form.get('num_of_loan', 0))
        self.delay_from_due_date = int(form.get('delay_from_due_date', 0))
        self.num_of_delayed_payment = int(form.get('num_of_delayed_payment', 0))
        self.changed_credit_limit = float(form.get('changed_credit_limit', 0))
        self.num_credit_inquiries = int(form.get('num_credit_inquiries', 0))
        self.credit_mix = form.get('credit_mix', '')
        self.outstanding_debt = float(form.get('outstanding_debt', 0))
        self.credit_utilization_ratio = float(form.get('credit_utilization_ratio', 0))
        self.credit_history_age = int(form.get('credit_history_age', 0))
        self.payment_of_min_amount = form.get('payment_of_min_amount', '')
        self.total_emi_per_month = float(form.get('total_emi_per_month', 0))
        self.amount_invested_monthly = float(form.get('amount_invested_monthly', 0))
        self.monthly_balance = float(form.get('monthly_balance', 0))
        self.payment_behaviour = form.get('payment_behaviour', '')
