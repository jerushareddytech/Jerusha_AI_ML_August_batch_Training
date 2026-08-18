# Q3 - Shopping Cart with Default & Mutable Pitfall


# ============================================================
# Part A - Spot the Bug
# ============================================================

def add_item_bug(item, cart=[]):
    cart.append(item)
    return cart


print("Part A - Mutable Default Argument Bug")

print(add_item_bug("apple"))
print(add_item_bug("banana"))
print(add_item_bug("milk", cart=["bread"]))
print(add_item_bug("eggs"))

# Expected output:
# ['apple']
# ['apple', 'banana']
# ['bread', 'milk']
# ['apple', 'banana', 'eggs']
#
# Explanation:
# The default list cart=[] is created only once when the
# function is defined. Therefore, calls that do not provide
# a cart reuse the same list.


# ============================================================
# Part B - Correct Way to Fix It
# ============================================================

def add_item(item, cart=None):
    if cart is None:
        cart = []

    cart.append(item)
    return cart


print("\nPart B - Fixed Function")

print(add_item("apple"))
print(add_item("banana"))

# Each call without a cart gets a fresh list.


# ============================================================
# Part C - Complete Shopping Cart
# ============================================================

def create_cart(owner, discount=0):
    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }


def add_to_cart(cart, name, price, qty=1):
    item = {
        "name": name,
        "price": price,
        "qty": qty
    }

    cart["items"].append(item)


def update_price(price_tuple, new_price):
    try:
        price_tuple[1] = new_price
    except TypeError:
        print("TypeError: Tuple elements cannot be modified.")


def calculate_total(cart):
    total = 0

    for item in cart["items"]:
        total += item["price"] * item["qty"]

    discount_amount = total * cart["discount"] / 100
    final_total = total - discount_amount

    return final_total


# ============================================================
# Demonstration for Two Different Customers
# ============================================================

cart1 = create_cart("Jerusha", discount=10)

add_to_cart(cart1, "Laptop", 50000, 1)
add_to_cart(cart1, "Mouse", 1000, 2)

cart2 = create_cart("Anjali", discount=5)

add_to_cart(cart2, "Keyboard", 2000, 1)
add_to_cart(cart2, "Headphones", 3000, 2)


print("\nPart C - Shopping Cart 1")
print(cart1)
print("Final Total:", calculate_total(cart1))

print("\nPart C - Shopping Cart 2")
print(cart2)
print("Final Total:", calculate_total(cart2))


# ============================================================
# Tuple Immutability Demonstration
# ============================================================

price_tuple = ("Laptop", 50000)

print("\nTuple before modification:", price_tuple)

update_price(price_tuple, 45000)

print("Tuple after attempted modification:", price_tuple)


# ============================================================
# Discussion Points
# ============================================================

# 1. Why is discount=0 safe but cart=[] dangerous?
#
# discount=0 is safe because integers are immutable.
# A new integer value can be assigned without changing a
# shared mutable object.
#
# cart=[] is dangerous because a list is mutable.
# The same default list can be reused between function calls,
# causing items from one call to appear in another call.


# 2. What is the difference between rebinding and mutating?
#
# Rebinding means making a variable refer to a different object.
# Example:
# x = [1, 2]
# x = [3, 4]
#
# Mutating means changing the existing object itself.
# Example:
# x = [1, 2]
# x.append(3)


# 3. Which of these are mutable?
#
# list  -> Mutable
# tuple  -> Immutable
# dict   -> Mutable
# set    -> Mutable
# str    -> Immutable
# int    -> Immutable


# 4. When you pass a list into a function and modify it,
#    do changes reflect outside? Why?
#
# Yes. A list is mutable, and the function receives a reference
# to the same list object. Therefore, modifications made to the
# list inside the function can be seen outside the function.
