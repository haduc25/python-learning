from Product import Product


class ProductManager:
    _listProduct = []

    def generateId(self):
        maxId = 1

        if len(self._listProduct) > 0:
            maxId = self._listProduct[0].getId()

            # Tìm max
            for x in self._listProduct:
                if maxId < x.getId():
                    maxId = x.getId()
            maxId += 1
        return maxId

    # create new product
    def input(self):
        id = self.generateId()
        name = input('Tên sản phẩm: ')
        price = float(input('Giá sản phẩm: '))

        product = Product(id, name, price)

        self._listProduct.append(product)

    # show
    def showAllProduct(self):
        for x in self._listProduct:
            x.show()

    # find by id
    def findById(self, id):
        product = None
        for x in self._listProduct:
            if x.getId() == id:
                product = x
                break

        return product

    # find by name
    def findByName(self, keyword):
        listProduct = []
        for x in self._listProduct:
            if x.upper() == keyword.upper():
                listProduct.append(x)

        return listProduct

    # delete by id
    def deleteById(self, id):
        for x in self._listProduct:
            if x.getId() == id:
                self._listProduct.remove(x)
                return True
        return False

    # update
    def update(self, id):
        product = self.findById(id)

        if product == None:
            return False

        name = input('Tên sản phẩm: ')
        price = float(input('Giá sản phẩm: '))

        product.setName(name)
        product.setPrice(price)

        return True

    # sort
    def sortById(self):
        self._listProduct.sort(key=lambda x: x.getId(), reverse=False)

    def sortByName(self):
        self._listProduct.sort(key=lambda x: x.getName(), reverse=False)

    # get all product
    def getAllProduct(self):
        return self._listProduct


#################################################################
lstPro = ProductManager()
lstPro.input()
lstPro.input()
# lstPro.findById(1)
# foundResult = lstPro.findById(10)
foundResult = lstPro.findById(1)
if foundResult != None:
    print('=====FOUND=====')
    foundResult.show()
    print('===============')
else:
    print('dont have this id')

lstPro.showAllProduct()
