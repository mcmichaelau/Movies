from flask import Flask, render_template, request

app = Flask(__name__)

# Create a dictionary to store the available seats
seats = {"A1": False, "A2": False, "A3": False, "B1": False, "B2": False, "B3": False}

@app.route("/")
def index():
    return render_template("index.html", seats=seats)

@app.route("/reserve", methods=["POST"])
def reserve():
    seat = request.form["seat"]
    if seats[seat] == False:
        seats[seat] = True
        message = "Seat reserved successfully!"
    else:
        message = "Sorry, this seat is already reserved."
    return render_template("index.html", seats=seats, message=message)

if __name__ == "__main__":
    app.run(debug=True)
