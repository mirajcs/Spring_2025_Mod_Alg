from math import gcd



def order_of_element(a, m):
    """
    Compute the order of an element 'a' modulo 'm'.
    The order is the smallest positive integer n such that a^n ≡ 1 (mod m).
    """
    if gcd(a, m) != 1:
        return None  # Element must be coprime with m to have an order

    n = 1
    power = a % m  # Initial power

    while power != 1:
        power = (power * a) % m
        n += 1

        if n > m:  # Failsafe for infinite loops (shouldn't happen in a valid group)
            return None  h

    return n


a = int(input("Enter the element: "))
m = int(input("Enter the modulo (group order): "))

order = order_of_element(a, m)
if order:
    print(f"The order of {a} modulo {m} is {order}.")
else:
    print(f"{a} has no valid order modulo {m}.")

