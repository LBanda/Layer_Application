from flask import Flask, request
from flask_restful import Resource, Api

from repository.item_repository import ItemRepository


class ItemResource(Resource):

    def get(self):
        return ItemRepository().get_all()

    def post(self):
        item = request.get_json()
        return ItemRepository().add(item)

    def delete(self, sku):
        return ItemRepository().delete(sku)
