from db.database_engine import DatabaseEngine as db
from db.product import Product


class ProductHandler:
    def __init__(self):
        self.__name = None
        self.__id = None

    def set_name(self, name):
        self.__name = name

    def print(self):
        print("id: %d\nname: %s" % (self.__id, self.__name))

    def add(self):
        session = db.create_session()
        p = Product(name =self.__name)
        session.add(p)
        session.commit()

    def update(self):
        session = db.create_session()
        product = session.query(Product).filter(Product.id == self.__id).first()
        product.name = self.__name
        session.commit()

    def find_by_name(self):
        session = db.create_session()
        product = session.query(Product).filter(Product.name == self.__name).first()
        if product is not None:
            self.__id = product.id
        else:
            self.__id = 0
            self.__name = ''

    def delete(self):
        session = db.create_session()
        product = session.query(Product).filter(Product.name == self.__name).first()
        session.delete(product)
        session.commit()


if __name__ == "__main__":
    p = ProductHandler()
    
    p.set_name("VULCAN")
    p.add()

    p.set_name("VULCAN_1")
    p.add()
    
    p.set_name("VULCAN")
    p.find_by_name()
    p.print()

    p.delete()
    p.find_by_name()
    p.print()
    
    p.set_name("VULCAN_1")
    p.find_by_name()
    p.print()
    p.set_name("LUNA")
    p.update()
