from collections import namedtuple, Counter

Price = namedtuple('Price', ('items', 'price'))

prices = {
    "A": [Price(3, 130), Price(1, 50)],
    "B": [Price(2, 45), Price(1, 30)],
    "C": [Price(1, 20)],
    "D": [Price(1, 15)],
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    counter = Counter()
    for item in skus:
        if item not in prices:
            return -1

        counter.

