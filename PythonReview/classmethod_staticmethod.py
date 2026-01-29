##class Book:
    ##TYPES = ("hardcover", "paperback", "ebook")

     ##def __init__(self, name, book_type, weight):
        ## self.name = name
        ## self.book_type = book_type
         ##self.weight = weight

     ##def __repr__(self):
         ##return f"<Book('{self.name}', '{self.book_type}', {self.weight})g>"
    
    ## @classmethod
     ##def hardcover(cls, name, page_weight):
         ##return cls(name, cls.TYPES[0], page_weight + 100)
    
     ##@classmethod
     ##def paperback(cls, name, page_weight):
         ##return cls(name, cls.TYPES[1], page_weight + 50)
 ##book = Book.hardcover("Harry Potter",  1.5)   

 ##light = Book.paperback("Ring of the powers", 1.5)   

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        return cls(f"{store.name} - franchise")
        # Return another store, with the same name as the argument's name, plus " - franchise"

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return f"{store.name}, total stock price: {store.stock_price()}"
    
    
store = Store("Test")
store2 = Store("Amazon")
store2.add_item("Keyboard", 160)

amazon_franchise = Store.franchise(store2)
print(amazon_franchise.name)