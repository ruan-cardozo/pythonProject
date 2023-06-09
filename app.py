from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Add(Resource):
    def get(self):
        num1 = int(request.args.get('num1'))
        num2 = int(request.args.get('num2'))
        result = num1 + num2
        return jsonify({'result': result})


class Subtract(Resource):
    def get(self):
        num1 = int(request.args.get('num1'))
        num2 = int(request.args.get('num2'))
        result = num1 - num2
        return jsonify({'result': result})


class Multiply(Resource):
    def get(self):
        num1 = int(request.args.get('num1'))
        num2 = int(request.args.get('num2'))
        result = num1 * num2
        return jsonify({'result': result})


class Division(Resource):

    def get(self):
        num1 = int(request.args.get('num1'))
        num2 = int(request.args.get('num2'))
        result = num1 / num2
        return jsonify({'result': result})


api.add_resource(Add, '/Add')
api.add_resource(Subtract, '/Subtract')
api.add_resource(Multiply, '/multiply')
api.add_resource(Division, '/division')

if __name__ == '__main__':
    app.run()