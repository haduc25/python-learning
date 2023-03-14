"""
Sản phẩm
    - Mã sp
    - Teeb sp
    - Giá

==================
Product
    - Id
    - Name
    - Price
    
==================
ProductManager
    - AddNewProduct
    - Remove
"""


class Product:
    def __init__(self, id, name, price):
        self._id = id
        self._name = name
        self._price = price

    def getId(self):
        return self._id

    def setId(self, id):
        self._id = id

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getPrice(self):
        return self._price

    def setId(self, price):
        self._price = price

    # show
    def show(self):
        print('Id: {0}, Name: {1}, Price: {2} '.format(
            self._id, self._name, self._price))


# sp = Product(10, 'A', 20)
# sp.show()
