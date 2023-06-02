
from flask import Flask, jsonify, request

app = Flask(__name__) # Flask obj

tasks =[{'id' : 1, 'name' : 'Rohit Sharma', 'contact' : '91*******0', 'done' : False}, {'id' : 2, 'name' : 'Savita', 'contact' : '94*******8', 'done' : False}]

@app.route('/add-data', methods = ['POST']) 
def add_task():
    if not request.json:
        return(jsonify({
            'status' : 'ERROR',
            'message' : 'Please provide data'         
        }, 400))
    
    task = {'id' : tasks[-1]['id']+1, 
            'name' : request.json['name'], 
            'contact': request.json.get('contact', ''),
            'done': False}
    
    tasks.append(task)
    return(jsonify({
            'status' : 'SUCCESS',
            'message' : 'Task added successfully'         
        }))

    # method that returns json structure
    
@app.route('/get-data') 

def get_task():
    return(jsonify({
            'status' : 'SUCCESS',
            'data' : tasks         
        }))


if __name__ == "__main__":
    app.run(debug = True, port=9090)

