import flask
import fraction_run

app = flask.Flask(__name__)

@app.route('/', methods=['POST'])
def fraction_api():
    data = flask.request.json
    value1 = data.get('value1')
    value2 = data.get('value2')
    operation = data.get('operation')
    result = fraction_run.compute_fraction(value1, value2, operation)
    context = {
        "equation": f"{value1} {operation} {value2}",
        "result": result
    }
    return flask.jsonify(**context)