class EmptyInventoryError(ValueError):
    "If you try to buy something but there's none left!"
    pass


class Product:
    inventory = 0
    reviews = []

    def __init__(self, name, desc, seller, price):
        self.name = name
        self.desc = desc
        self.seller = seller
        self.price = price

    def __str__(self):
        return f'{self.name}:\n{"-"*(len(self.name)+1)}\nSeller: {self.seller}, Price: {str(self.price)} \nDesc: {self.desc}'

    @property
    def available(self):
        return bool(self.inventory)


class Review:
    def __init__(self, desc, user, product):
        self.desc = desc
        self.user = user
        self.product = product.name

    def __str__(self):
        return f'{self.user}\'s review of {self.product}: {self.desc}'


class User:
    def __init__(self, id, name):
        self.name = name
        self.id = id
        self.reviews = []

    def __str__(self):
        return f'Name: {self.name}, Products reviewed: {", ".join(set(map(lambda x: x.product, self.reviews)))}'

    def sell_product(self, product_name, desc, price):
        product = Product(product_name, desc, self.name, price)
        product.inventory += 1
        return product

    @staticmethod
    def buy_product(product):
        assert isinstance(product, Product)
        if product.inventory:
            product.inventory -= 1
        else:
            raise EmptyInventoryError(f'There are no {product.name}s left')

    def write_review(self, comment, product):
        assert isinstance(product, Product)
        review = Review(comment, self.name, product)
        self.reviews.append(review)
        product.reviews.append(review)
        return review


if __name__ == '__main__':
    brianna = User(1, 'Brianna')
    mary = User(2, 'Mary')

    keyboard = brianna.sell_product(
        'Keyboard', 'A nice mechanical keyboard', 100)
    print(keyboard.available)  # => True
    mary.buy_product(keyboard)
    print(keyboard.available)  # => False
    review = mary.write_review('This is the best keyboard ever!', keyboard)
    print(review in mary.reviews)  # => True
    print(review in keyboard.reviews)  # => True
    print(keyboard)
    print(mary)
    print(review)
