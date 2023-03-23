from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, product):
        pass

class Subject(ABC):
    def __init__(self):
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, product):
        for observer in self._observers:
            observer.update(product)

class Client(Observer):
    def __init__(self, name, iv):
        self._name = name
        self._iphonev = iv

    def update(self, product):
        if product.get_version() != self._version:
            self._version = product.get_version()
            print(f"{self._name}: The new iPhone  {self._version} is available!")
        
    def set_version(self, version):
        self._version = version

class Product:
    def __init__(self, name, available, version):
        self._name = name
        self._available = available
        self._version = version
        self._observers = []

    def get_name(self):
        return self._name

    def get_availability(self):
        return self._available

    def set_availability(self, available):
        self._available = available
        self.notify_observers(self)

    def get_version(self):
        return self._version

    def set_version(self, version):
        self._version = version
        self.notify_observers(self)

    def register_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, product):
        for observer in self._observers:
            observer.update(product)

class Store:
    def __init__(self):
        self._product = Product("iPhone", False, 1)

    def get_product(self):
        return self._product

    def set_product_version(self, version):
        self._product.set_version(version)

if __name__ == "__main__":
    store = Store()

    client1 = Client("JP",13)
    client2 = Client("Jaquim",13)

    product = store.get_product()
    client1.set_version(product.get_version())
    client2.set_version(product.get_version())
    product.register_observer(client1)
    product.register_observer(client2)

    store.set_product_version(14)

    product.remove_observer(client2)
    product.remove_observer(client1)

    store.set_product_version(15)
