import flask
import fraction_run

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
            "message": "did not supply all necessary command line arguments, need value1, value2, and operation",
            "status_code": 400
        }
        return flask.jsonify(errormessage), 400
    if operation not in ['+', '-', '*', '/']:
        errormessage = {
            "message": "operation is not a valid math operand, please use one from the set: ['+', '-', '*', '/']",
            "status_code": 400
        }
        return flask.jsonify(errormessage), 400

    result = fraction_run.compute_fraction(value1, value2, operation)
    context = {
        "equation": f"{value1} {operation} {value2}",
        "result": result
    }
    return flask.jsonify(**context)