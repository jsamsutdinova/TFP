import json


class Bouquet():
    def __init__(self, shared_state):
        self._shared_state = shared_state

    def operation(self, unique_state):
        u = json.dumps(unique_state)
        print(f"Добавим атрибут ({u}).", end="\n")


class BouquetFactory():

    def __init__(self, init_bouquet):
        self._bouquets = {}
        for state in init_bouquet:
            self._bouquets[self.get_key(state)] = Bouquet(state)

    def get_key(self, state):
        return "".join((state))

    def get_flyweight(self, shared_state):
        key = self.get_key(shared_state)

        if not self._bouquets.get(key):
            self._bouquets[key] = Bouquet(shared_state)

        return self._bouquets[key]

    def add_attribute(self, attribute_name):
        flowers = self.get_flyweight([attribute_name])
        flowers.operation([attribute_name])

    def list_flyweights(self):
        count = len(self._bouquets)
        print(f"Букет состоит из {count} элементов:")
        print("\n".join(map(str, self._bouquets.keys())), end="\n")


if __name__ == "__main__":
    flowers1 = BouquetFactory(["Розы", "Герберы"])
    flowers1.add_attribute("Personal Lenta")
    flowers1.list_flyweights()

    flowers2 = BouquetFactory(["Гартензии", "Тюльпаны", "Ирисы"])
    flowers2.add_attribute("Wrapping Paper")
    flowers2.list_flyweights()

