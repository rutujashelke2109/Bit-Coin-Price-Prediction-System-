from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load(r'C:\RUTUJA\bitcoin_price_prediction.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction_text = ""

    if request.method == 'POST':
        try:
            a = float(request.form['open_close'])
            b = float(request.form['low_high'])
            c = int(request.form['quarter_end'])

            cus_input = np.array([[a, b, c]])
            result = model.predict(cus_input)
            prediction = int(round(result[0]))

            if prediction == 0:
                prediction_text = "Price goes DOWN"
            elif prediction == 1:
                prediction_text = "Price goes UP"
            else:
                prediction_text = "Cannot predict"

        except Exception as e:
            prediction_text = f"Error: {e}"

    return render_template('index.html', prediction=prediction_text)


if __name__ == '__main__':
    app.run(debug=True)
