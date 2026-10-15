from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    card = request.form.get("card-number", "").replace(" ", "")
    name = request.form.get("card-name", "")
    expiry = request.form.get("expiry", "")
    cvv = request.form.get("cvv", "")
    print("\nCAPTURED", flush=True)
    print(f"Card:   {card}", flush=True)
    print(f"Name:   {name}", flush=True)
    print(f"Expiry: {expiry}", flush=True)
    print(f"CVV: {cvv}", flush=True)

    return "OK - check your terminal"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
