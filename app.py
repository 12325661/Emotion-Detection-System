from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    # Get the user's input from the form
    code = request.form['code']

    # Run the Python code
    result = None
    try:
        result = eval(code)
    except Exception as e:
        result = str(e)

    # Render the results template
    return render_template('results.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)