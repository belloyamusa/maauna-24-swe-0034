from flask import Flask, render_template, request, redirect
from models import Business

app = Flask(__name__)

businesses = []
recent_stack = []

@app.route('/')
def home():
    return render_template(
        'index.html',
        businesses=businesses,
        recent=recent_stack[-5:]
    )

@app.route('/add', methods=['GET', 'POST'])
def add_business():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        category = request.form['category']

        new_business = Business(name, location, category)

        businesses.append(new_business)
        recent_stack.append(new_business)

        return redirect('/')

    return render_template('add.html')

if __name__ == "__main__":
    app.run(debug=True)
