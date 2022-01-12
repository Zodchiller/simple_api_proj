from flask import Flask, jsonify, request
import json
app = Flask(__name__)

@app.route('/home/', methods=['GET', 'POST'])
def welcome():
    return "Welcome"

@app.route('/json', methods=['GET', 'POST'])
def welcomeHome():
    if request.is_json:
        req = request.get_json()
        return jsonify(req), 200
    else:
        return "Request was not in JSON format.", 400
#This route is used to append a new recipe to the file
@app.route('/disp', methods=['GET', 'POST'])
def add_recipie():
    with open('/mnt/c/pyProj2/files/data.json', 'r') as f:
        req = f.read()
    if not req:
        info = [req]
    else:
        for i in info:
            #Check if the recipe is already on the list
            if i['name'] == req['name']:
                return 'This entry already exists',200

        info.append(req)
    with open('/mnt/c/pyProj2/files/data.json', 'w') as f:
        f.write(json.dumps(info, indent=4))
    return jsonify(req)

#Route to add a new recipe, using both GET and POST methods as
#we are accessing and posting data
@app.route('/updt', methods = ['GET', 'POST'])
def update_recipe():
    #Grab entry from command line
    req = json.loads(request.data)
    #storage place for new, updated list
    updated = []
    with open('/mnt/c/pyProj2/files/data.json', 'r') as f:
        data = f.read()
        info = json.loads(data)
    for i in info:
        #same data except for the entry getting updated
        if i['name'] == req['name']:
            updated.append(req)
        else:
            updated.append(i)

    with open('/mnt/c/pyProj2/files/data.json', 'w') as f:
        f.write(json.dumps(info, indent=4))

    return jsonify(updated)

#This route spits out the entire file in JSON format
@app.route('/list', methods=['GET', 'POST'])
def listing():
    with open('/mnt/c/pyProj2/files/data.json', 'r') as f:
        data = f.read()
        info = json.loads(data)
    return jsonify(info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
