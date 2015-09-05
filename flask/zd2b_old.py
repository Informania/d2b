from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html');


@app.route("/distanser")
def category():
    return render_template('produkter.html', category="cat");

@app.route ("/produkter")
def products():
	return render_template('produkter.html', category="none");

if __name__ == "__main__":
    app.run(debug=True)
