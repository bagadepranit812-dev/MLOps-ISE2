from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Student Performance Prediction</h1>
    <form action="/predict" method="POST">
        <label>Enter Student Marks (0-100):</label>
        <input type="number" name="marks" min="0" max="100" required>
        <button type="submit">Predict</button>
    </form>
    """


@app.route("/predict", methods=["POST"])
def predict():

    if request.is_json:
        data = request.get_json()
        marks = data.get("marks")
    else:
        marks = request.form.get("marks")

    try:
        marks = float(marks)
    except (TypeError, ValueError):
        return jsonify({"error": "Valid marks are required"}), 400

    if not 0 <= marks <= 100:
        return jsonify({"error": "Marks must be between 0 and 100"}), 400

    if marks >= 75:
        result = "Distinction"
    elif marks >= 60:
        result = "First Class"
    elif marks >= 40:
        result = "Pass"
    else:
        result = "Fail"

    return jsonify({
        "marks": marks,
        "prediction": result
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)