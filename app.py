from flask import Flask, render_template

app = Flask(__name__)

@app.route("/logika")
def hello_world():
    return render_template("index.html")
@app.route("/")
def log():
    return render_template("logika.html")
if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)

