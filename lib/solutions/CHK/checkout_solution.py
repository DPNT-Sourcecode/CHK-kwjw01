from collections import namedtuple, Counter

Price = namedtuple('Price', ('items', 'price'))

# we assume that in prices_map for every item there will be price for one piece
# we also assume that prices are sorted by items from biggest and it always worth to buy more items
prices_map = {
    'A': [Price(3, 130), Price(1, 50)],
    'B': [Price(2, 45), Price(1, 30)],
    'C': [Price(1, 20)],
    'D': [Price(1, 15)],
}

ItemForFreeOffer = namedtuple('ItemForFreeOffer', ('items_needed'))

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    counter = Counter()
    for item in skus:
        if item not in prices_map:
            return -1

        counter[item] += 1

    total = 0
    for item, number_of_pieces in counter.items():
        prices = prices_map[item]

        while number_of_pieces > 0:
            price = next(p for p in prices if p.items <= number_of_pieces)
            total += price.price
            number_of_pieces -= price.items

    return total

