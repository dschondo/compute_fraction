import flask
import compute_fraction
import fraction

app = flask.Flask(__name__)    

@app.route('/', methods=['POST'])
def fraction_api():
    data = flask.request.json
    value1 = data.get('value1')
    value2 = data.get('value2')
    operation = data.get('operation')

    # Check for errors in inputs before computing
    if value1 is None or value2 is None or operation is None:
        errormessage = {
            "message": "The user did not supply all necessary command line arguments, need to input value1, value2, and operation of the form <fraction1> <operation> <fraction2>",
            "status_code": 400
        }
        return flask.jsonify(errormessage), 400
    if operation not in ['+', '-', '*', '/']:
        errormessage = {
            "message": f"The operation input: '{operation}' is not a valid math operand, please use one from the set: ['+', '-', '*', '/'].",
            "status_code": 400
        }
        return flask.jsonify(errormessage), 400

    # Use this try/except block to catch Exceptions thrown by the fraction class and use flask error messages
    try:
        fraction1 = fraction.Fraction(value1)
        fraction2 = fraction.Fraction(value2)
    except Exception:
        errormessage = {
            "message": "Invalid fraction input. Please use one of the forms with only valid integers: 1_1/2, 1/2, 1.",
            "status_code": 400
        }
        return flask.jsonify(errormessage), 400
    
    # Call the compute_fraction function from compute_fraction.py to do the math operation on the user input
    result = compute_fraction.compute_fraction(fraction1, fraction2, operation)

    # Return the starting equation and the result computed
    context = {
        "equation": f"{value1} {operation} {value2}",
        "result": str(result)
    }
    return flask.jsonify(**context)