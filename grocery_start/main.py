from flask import Flask, request
from flask_restful import Resource, Api

from controller.item_resource import ItemResource


app = Flask(__name__)
api = Api(app)


api.add_resource(ItemResource, "/item")


if __name__ == "__main__":
    app.run()