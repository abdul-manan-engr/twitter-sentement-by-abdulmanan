import flask
from flask import request, jsonify
from functions import *


app = flask.Flask(__name__)




@app.route("/", methods=["POST"])
def print_piped():
    if request.form['mes']:
        msg = request.form['mes']
        x_input = str(msg)
        print(x_input)
        x_input, pred_class, pred_proba = make_prediction(x_input)
        flask.render_template('predictor.html',
                                chat_in=x_input,
                                prediction=pred_class,
                                probability=pred_proba)
    return jsonify(pred_class)

@app.route("/", methods=["GET"])
def predict():
    
    print(request.args)
    if(request.args):
        x_input, pred_class, pred_proba = make_prediction(request.args['chat_in'])
        pred_proba=pred_proba.split(" ")
        pred_proba=[float(b) for b in pred_proba if len(b) > 1]
        pred_proba=sorted(pred_proba)
        return flask.render_template('predictor.html',
                                chat_in=x_input,
                                prediction_class=pred_class,
                                prediction_prob=pred_proba[-1])
    
    else: 
        return flask.render_template('predictor.html',
                                     chat_in=" ",
                                     prediction_class=" ",
                                     prediction_prob=" ")


if __name__=="__main__":
    # For local development:
    # app.run(debug=True)
    # For public web serving:
    # app.run(host='0.0.0.0')
    app.run()
