from flask import Flask, request, render_template

from CustomerDetails import CustomerDetails
from randomforest import get_prediction
from preprocessing import get_preprocessed_array

app = Flask(__name__)

@app.route("/")
def guest_page():
    return render_template('employee.html')



@app.route("/guest/predict", methods=["POST"])
def predict_guest_score():
    customer_details = CustomerDetails(request.form)
    print(customer_details)
    preprocessed_values = get_preprocessed_array(customer_details)
    print(preprocessed_values)
    result = get_prediction([preprocessed_values])

    score_name = {
        0: 'Good',
        1: 'Poor',
        2: 'Standard'
    }
    creditScoreCategory=score_name[int(result)]
    return render_template('results.html',creditScoreCategory=creditScoreCategory)


@app.route('/test')
def hello_world():  # put application's code here
    res = get_prediction([[-0.93002131, 0.50495588, 1., 1., 0.53846154, 1.33333333,
                           1.22222222, 0.5, -0.77362409, 1., 2.15908509, 0.01118578,
                           - 1.22929936, 1.84838534, 0.29769982, -0.08668615, 0., 1.,
                           0., 1., -1., 1., 0., 0.,
                           0.]])

    score_name = {
        0: 'Good',
        1: 'Poor',
        2: 'Standard'
    }

    return score_name[int(res)]


if __name__ == '__main__':
    app.run()
