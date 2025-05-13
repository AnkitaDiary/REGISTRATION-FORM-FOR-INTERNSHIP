from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def form():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    full_name = request.form['fullName']
    age = request.form['age']
    email = request.form['email']
    description = request.form['description']
    domain = request.form.get('domain')
    companies = request.form.getlist('companies')
    duration = request.form.get('duration')

    # Save to CSV (append mode)
    with open("submissions.csv", "a") as file:
        file.write(f"{full_name},{age},{email},{domain},{','.join(companies)},{duration}\n")

    # Pass data to success page
    return render_template('success.html', data=request.form)

if __name__ == '__main__':
    app.run(debug=True)
