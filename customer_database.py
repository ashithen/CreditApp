import pandas as pd

from CustomerDetails import CustomerDetails

customer_df = pd.read_csv('customer_details.csv')


def get_customer_details(customer_id, ssn):
    try:
        cdf = customer_df[(customer_df['Customer_ID'] == customer_id) &
                          (customer_df['SSN'] == ssn)].iloc[0]
        customer_details = CustomerDetails(cdf)
        return customer_details

    except Exception as error:
        print(error)
        return None
