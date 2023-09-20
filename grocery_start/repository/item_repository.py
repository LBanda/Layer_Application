from csv import DictReader


class ItemRepository:

    def __init__(self, filename):
        self.items = []
        with open(filename, "r") as f:
            reader = DictReader(f)
            for row in reader:
                self.items.append(row)

    def get_all(self):
        return self.items

    def get_by_sku(self, sku):
        for item in self.items:
            if item["sku"] == sku:
                return item
        return None

    def add(self, item):
        self.items.append(item)

    def delete(self, sku):
        for i, item in enumerate(self.items):
            if item["sku"] == sku:
                del self.items[i]
                return
        return None
