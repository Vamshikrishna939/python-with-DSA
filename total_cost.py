def is_calculate(cart):
    cost=0 
    for item in cart:
       cost+=item["price"] * item ["quantity"]
       return cost


cart = [
              { "name":"apple","price":50,"quantity":3},
              { "name":"banana","price":10,"quantity":2} ]
print(is_calculate(cart))
             