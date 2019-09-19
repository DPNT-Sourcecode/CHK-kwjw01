from collections import namedtuple, Counter

Price = namedtuple('Price', ('items', 'price'))

# we assume that in prices_map for every item there will be price for one piece
# we also assume that prices are sorted by items from biggest and it always worth to buy more items
prices_map = {
    'A': [Price(5, 200), Price(3, 130), Price(1, 50)],
    'B': [Price(2, 45), Price(1, 30)],
    'C': [Price(1, 20)],
    'D': [Price(1, 15)],
    'E': [Price(1, 40)],
    'F': [Price(3, 20), Price(1, 10)],
    'G': [Price(1, 20)],
    'H': [Price(10, 80), Price(5, 45), Price(1, 10)],
    'I': [Price(1, 35)],
    'J': [Price(1, 60)],
    'K': [Price(2, 150), Price(1, 80)],
    'L': [Price(1, 90)],
    'M': [Price(1, 15)],
    'N': [Price(1, 40)],
    'O': [Price(1, 10)],
    'P': [Price(5, 200), Price(1, 50)],
    'Q': [Price(3, 80), Price(1, 30)],
    'R': [Price(1, 50)],
    'S': [Price(1, 30)],
    'T': [Price(1, 20)],
    'U': [Price(4, 120), Price(1, 40)],
    'V': [Price(3, 130), Price(2, 90), Price(1, 50)],
    'W': [Price(1, 20)],
    'X': [Price(1, 90)],
    'Y': [Price(1, 10)],
    'Z': [Price(1, 50)],
}

ItemForFreeOffer = namedtuple('ItemForFreeOffer', ('items_needed', 'des_product', 'des_items'))

items_for_free = {
    'E': [ItemForFreeOffer(2, 'B', 1)],
    'N': [ItemForFreeOffer(3, 'M', 1)],
    'R': [ItemForFreeOffer(3, 'Q', 1)],
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    counter = Counter()
    for item in skus:
        if item not in prices_map:
            return -1

        counter[item] += 1

    for product, item_for_free_list in items_for_free.items():
        number_of_products = counter[product]
        for item_for_free in item_for_free_list:
            action_count = number_of_products // item_for_free.items_needed
            number_of_products -= action_count * item_for_free.items_needed
            counter[item_for_free.des_product] -= action_count * item_for_free.des_items

    total = 0
    for item, number_of_pieces in counter.items():
        prices = prices_map[item]

        while number_of_pieces > 0:
            price = next(p for p in prices if p.items <= number_of_pieces)
            total += price.price
            number_of_pieces -= price.items

    return total
