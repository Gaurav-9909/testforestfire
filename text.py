from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask!"

print("Before app.run()")

if __name__ == "__main__":
    print("Starting server...")
    app.run(debug=True)