from flask import Flask, request, jsonify

app = Flask(__name__)

FULL_NAME = "aishwarya_s"
DOB = "01012003"
EMAIL = "your_email@vitstudent.ac.in"
ROLL_NUMBER = "YOURROLL123"

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "API is working ✅",
        "info": "Use POST /bfhl with JSON { 'data': [...] }"
    }), 200

@app.route('/bfhl', methods=['POST'])
def bfhl():
    try:
        data = request.json.get("data", [])
        even_numbers, odd_numbers, alphabets, special_characters = [], [], [], []
        sum_numbers, concat_string = 0, ""

        for item in data:
            if item.isdigit():
                num = int(item)
                sum_numbers += num
                (even_numbers if num % 2 == 0 else odd_numbers).append(item)
            elif item.isalpha():
                alphabets.append(item.upper())
                concat_string += item
            else:
                special_characters.append(item)

        concat_string = "".join(
            c.upper() if i % 2 == 0 else c.lower()
            for i, c in enumerate(concat_string[::-1])
        )

        response = {
            "status": "success",
            "is_success": True,
            "user_id": f"{FULL_NAME.lower()}_{DOB}",
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "data_processed": {
                "odd_numbers": odd_numbers,
                "even_numbers": even_numbers,
                "alphabets": alphabets,
                "special_characters": special_characters,
                "sum": str(sum_numbers),
                "concat_string": concat_string
            }
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"status": "error", "is_success": False, "error": str(e)}), 400
