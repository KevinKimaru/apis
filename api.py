from flask import Flask, jsonify, request
from peewee import IntegrityError

from users_model import User

app = Flask(__name__)

@app.route('/')
@app.route('/all',methods=['GET'])
def all():
    #User.create(names="Lawrence", email="law@game.com", age=18)
    users = User.select()
    users_list = []
    for item in users:
        users_list.append({"id": item.id, "names": item.names, "email":item.email, "age":item.age})
    return jsonify(users_list)

@app.route("/user/<int:id>", methods=["GET"])
def fetch_user(id):
    item = User.get(User.id == id)
    return jsonify({"id": item.id, "names": item.names, "email":item.email, "age":item.age})

@app.route('/save', methods=['POST'])
def save():
    if request.method == 'POST':
        names = request.form["names"]
        email = request.form["email"]
        age = request.form["age"]
        try:
            User.create(names=names, email=email, age=age)
        except IntegrityError:
            return jsonify({"response":"saved"})
    else:
        return jsonify({"response":"no data was sent"})

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    if request.method == 'POST':
        names = request.form["names"]
        email = request.form["email"]
        age = request.form["age"]
        user = User.get(User.id == id)
        user.names = names
        user.email = email
        user.age = age
        user.save()
        return jsonify({"response": "Updated Successfully"})
    else:
        return jsonify({"response":"Failed to update"})

@app.route("/delete/<int:id>", methods=["DELETE"])
def delete(id):
    if request.method == 'DELETE':
        user = User.get(User.id == id)
        user.delete_instance()
        return jsonify({"response": "Deleted successfully"})
    else:
        return jsonify({"response": "Failed to Delete"})

if __name__ == '__main__':
    app.run(host="0.0.0.0")
