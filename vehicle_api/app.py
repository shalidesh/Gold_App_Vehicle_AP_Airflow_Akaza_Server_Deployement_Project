from flask import Flask, request, jsonify
import pandas as pd
import os
import datetime
import pandas as pd
import pandas as pd
import socket
import jwt
from functools import wraps
from utils.unique_model_creation import unique_model_creation,model_mapping,upload_database,dataset_processing
from utils.input_data_validation import DatasetValidation,checkInputs,changeFuelType,changeCapacity
from utils.price_calculation import price_calculate
from constants.dataframes import honda_database,suzuki__database,nissan__database,toyota__database,micro__database,mitsubishi__database
# from dotenv import load_dotenv
# load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['USER'] = os.environ.get('USER')
app.config['PASSWORD'] = os.environ.get('PASSWORD')


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # Check for token in headers
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]

        if not token:
            return {
                "message": "Authentication Token is missing!",
                "data": None,
                "error": "Unauthorized"
            }, 401

        try:
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
        except Exception as e:
            return {
                "message": "Something went wrong",
                "data": None,
                "error": str(e)
            }, 500

        return f(*args, **kwargs)
    return decorated


@app.route("/login")
def login():
    auth=request.authorization

    if not auth:
        return "missing credentials", 401
    
    if auth.password != 'cdb123456':
            return f"invalid credentials", 401
    else:
        token=jwt.encode({'user':auth.username},app.config['SECRET_KEY'])
        return jsonify({'token':token})


@app.route('/predict', methods=['POST'])
@token_required
def predict_datapoint():
    try:
        ct = datetime.datetime.now()
        
        if request.method == 'POST':

            request_data = request.get_json(force=True) 

            if checkInputs(request_data):

                model=request_data.get('model').upper().strip() 
                manufacture = request_data.get('manufacture').upper().strip() 
                fuel=request_data.get('fuel').upper().strip() 
                transmission=request_data.get('transmission').upper().strip() 
                engine_capacity=request_data.get('engine_capacity').upper().strip() 
                yom=request_data.get('yom').strip() 

                fuel=changeFuelType(fuel)     
                engine_capacity= changeCapacity(engine_capacity) 

                if manufacture=="NISSAN":

                    mean_price=price_calculate(nissan__database,manufacture,model,fuel,transmission,yom,engine_capacity)

                    app.logger.info("success")
                    response = jsonify({
                                    "timestamps": ct,
                                    "Predicted_Price": str(mean_price),
                                    "host_id":socket.gethostname()
                                })
                    response.status_code = 200
                    return response    
                elif manufacture=="SUZUKI" or manufacture=="MARUTI":
                    mean_price=price_calculate(suzuki__database,manufacture,model,fuel,transmission,yom,engine_capacity)

                    app.logger.info("success")
                    response = jsonify({
                                    "timestamps": ct,
                                    "Predicted_Price": str(mean_price),
                                    "host_id":socket.gethostname()
                                })
                    response.status_code = 200
                    return response
                elif manufacture=="HONDA":
                    mean_price=price_calculate(honda_database,manufacture,model,fuel,transmission,yom,engine_capacity)

                    app.logger.info("success")
                    response = jsonify({
                                    "timestamps": ct,
                                    "Predicted_Price": str(mean_price),
                                    "host_id":socket.gethostname()
                                })
                    response.status_code = 200
                    return response
                elif manufacture=="TOYOTA":
                    mean_price=price_calculate(toyota__database,manufacture,model,fuel,transmission,yom,engine_capacity)

                    app.logger.info("success")
                    response = jsonify({
                                    "timestamps": ct,
                                    "Predicted_Price": str(mean_price),
                                    "host_id":socket.gethostname()
                                })
                    response.status_code = 200
                    return response
                elif manufacture=="MICRO":
                    mean_price=price_calculate(micro__database,manufacture,model,fuel,transmission,yom,engine_capacity)

                    app.logger.info("success")
                    response = jsonify({
                                    "timestamps": ct,
                                    "Predicted_Price": str(mean_price),
                                    "host_id":socket.gethostname()
                                })
                    response.status_code = 200
                    return response              
                elif manufacture=="MITSUBISHI":
                    mean_price=price_calculate(mitsubishi__database,manufacture,model,fuel,transmission,yom,engine_capacity)

                    app.logger.info("success")
                    response = jsonify({
                                    "timestamps": ct,
                                    "Predicted_Price": str(mean_price),
                                    "host_id":socket.gethostname()
                                })
                    response.status_code = 200
                    return response
                else:
                    app.logger.info("success")
                    response = jsonify({
                                    "timestamps": ct,
                                    "Predicted_Price": "try Valid Make"
                                })
                    response.status_code = 200
                    return response
            else:
                app.logger.info("input validation error")
                response = jsonify({
                            "timestamps":ct,
                            "Predicted_Price":0,
                            "host_id":socket.gethostname()
                        })
                response.status_code = 200
                return response
        else:
            app.logger.info("allowed only post request")
            response = jsonify({
                            "timestamps":ct,
                            "Predicted_Price":"allowed only post request",
                            "host_id":socket.gethostname()
                        })
            response.status_code = 500
            return response
        
    except Exception as e:
        app.logger.error("An error occurred during prediction: %s", str(e))
        response = jsonify({
            "error": str(e),
            "message": "An error occurred during prediction",
            "host_id":socket.gethostname()
        })
        response.status_code = 500
        return response



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8443))
    app.run(host='0.0.0.0', port=port,debug=True)    

