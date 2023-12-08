from flask import Flask, request, render_template

from CustomerDetails import CustomerDetails
from randomforest import get_prediction
from preprocessing import get_preprocessed_array
from customer_database import get_customer_details

app = Flask(__name__)


# Show home page
@app.route("/")
def home_page():
    return render_template('main.html')

# Show Existing customer Screen
@app.route("/customer_screen")
def show_customer_screen():
    return render_template('customer.html')

# Show guest user screen
@app.route("/guest_screen")
def show_guest_screen():
    return render_template('guest.html')

# Get input from existing customer
@app.route("/customer/predict", methods=["POST"])
def predict_customer_score():
    customer_id = request.form.get('customer_id')
    ssn = request.form.get('ssn')
    customer_details = get_customer_details(customer_id, ssn)
    creditScoreCategory = predict_score(customer_details)
    return render_template('results.html', creditScoreCategory=creditScoreCategory,
                           customer_details = customer_details)


# Get input from guest user
@app.route("/guest/predict", methods=["POST"])
def predict_guest_score():
    customer_details = CustomerDetails(request.form)
    creditScoreCategory = predict_score(customer_details)

    return render_template('results.html', creditScoreCategory=creditScoreCategory,
                           customer_details = customer_details)

# predict score based on customer details
def predict_score(customer_details: CustomerDetails):
    print(customer_details)
    preprocessed_values = get_preprocessed_array(customer_details)
    print(preprocessed_values)
    result = get_prediction([preprocessed_values])
    return result[0]

# check server health
@app.route('/health')
def hello_world():  # put application's code here
    return "Server is up"


if __name__ == '__main__':
    app.run()
