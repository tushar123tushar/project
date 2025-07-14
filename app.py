from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Save the data to a CSV file
        with open('users.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, password])

        return "✅ Login info saved successfully!"

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
