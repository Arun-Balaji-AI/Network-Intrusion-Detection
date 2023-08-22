from flask import Flask ,render_template, request
from Detector import detect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.post('/checker')
def checker():
    data = request.form
    data = dict(data)
    print(data['service'])
    answer = detect(data)
    return render_template("output.html",input = data, answer = answer[0])

if __name__ == "__main__":
    app.run(debug=True)