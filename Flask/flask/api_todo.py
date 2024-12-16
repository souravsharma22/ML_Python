from flask import Flask,jsonify,request

'''Creating a instance of the flask class'''

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this flask workshop.\njust need to save changes"

@app.route("/index")
def index():
    return "this is the new index page"

items=[
    {'id':1,'name':'item1','descreiption':'This is item number one'},
    {'id':2,'name':'item2','descreiption':'This is item number two'},
    {'id':3,'name':'item3','descreiption':'This is item number Three'}
    ]
#retrive all items
@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)

#retireve a specific item
@app.route('/items/<int:item_id>',methods=['GET'])
def get_items_id(item_id):
    item = next((item for item in items if item['id']==item_id),None)
    if item is None:
        return jsonify({'error':"Item not found"})
    return jsonify(item)

#creating a new task
@app.route('/items' , methods=['POST'])
def create_items():
    if not request.json or not 'name' in request.json:
        return jsonify({'error':"Item not found"})
    new_item = {
        'id':items[-1]['id']+1 if items else 1,
        'name':request.json['name'],
        'description':request.json['description']
    }
    items.append(new_item)
    return jsonify(new_item)

# updating an existing item
@app.route('/items/<int:item_id>' , methods=['PUT'])
def update_items(item_id):
    item = next((item for item in items if item['id']==item_id),None)
    if item is None:
        return jsonify({'error':"Item not found"})
    item['name']=request.json.get('name',item['name'])
    item['description']=request.json.get('description',item['description'])
    return jsonify(item)

#deleting  an item
@app.route('/items/<int:item_id>' , methods=['DELETE'])
def delete_items(item_id):
    global items
    items = [item for item in items if item['id']!=item_id]
    return jsonify({'RESULT':"Item deleted"})

if __name__=="__main__":
    app.run(debug=True)