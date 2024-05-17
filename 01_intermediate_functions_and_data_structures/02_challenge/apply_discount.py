def apply_discount(products, minimum_price, discount_rate):
    # return [(p["name"], p["price"]*(1-discount_rate/100)) 
    #         for p in products if p["price"]*(1-discount_rate/100)>=minimum_price]
    products_tupple = [(p["name"], p["price"]*(1-discount_rate/100)) for p in products]
    return list(filter(lambda p: p[1]>=minimum_price, products_tupple))