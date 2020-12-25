import json


class Bouquet():
    def __init__(self, flowers):
        self._flowers = flowers

    def operation(self, attribute):
        u = json.dumps(attribute)
        print(f"Добавим атрибут ({u}).", end="\n")


class BouquetFactory():

    def __init__(self, init_bouquet):
        self._bouquets = {}
        for flower in init_bouquet:
            self._bouquets[self.get_key(flower)] = Bouquet(flower)

    def get_key(self, flower):
        return "".join((flower))

    def get_attribute(self, attribute):
        key = self.get_key(attribute)

        if not self._bouquets.get(key):
            self._bouquets[key] = Bouquet(attribute)

        return self._bouquets[key]

    def add_attribute(self, attribute_name):
        flowers = self.get_attribute([attribute_name])
        flowers.operation([attribute_name])

    def list_flowers(self):
        count = len(self._bouquets)
        print(f"Букет состоит из {count} элементов:")
        print("\n".join(map(str, self._bouquets.keys())), end="\n")


if __name__ == "__main__":
    flowers1 = BouquetFactory(["Розы", "Герберы"])
    flowers1.add_attribute("Personal Lenta")
    flowers1.list_flowers()

    flowers2 = BouquetFactory(["Гартензии", "Тюльпаны", "Ирисы"])
    flowers2.add_attribute("Wrapping Paper")
    flowers2.list_flowers()

