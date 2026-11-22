# 1.
def from_1_to_n(n):
    if n < 1:
        return
    from_1_to_n(n - 1)
    print(n, end=" ")


# 2.
def from_a_to_b(a, b):
    print(a, end=" ")
    if a == b:
        return
    if a < b:
        from_a_to_b(a + 1, b)
    else:
        from_a_to_b(a - 1, b)


# 3.
def is_power_of_two(n):
    if n == 1:
        return True
    if n < 1 or n % 2 != 0:
        return False
    return is_power_of_two(n // 2)


# 4.
def sum_digits(n):
    if n < 10:
        return n
    return (n % 10) + sum_digits(n // 10)


# 5.
def print_digits_reverse(n):
    print(n % 10, end=" ")
    if n >= 10:
        print_digits_reverse(n // 10)


# 6.
def print_digits_forward(n):
    if n >= 10:
        print_digits_forward(n // 10)
    print(n % 10, end=" ")


if __name__ == "__main__":
    print("1) Від 1 до 5:")
    from_1_to_n(5)

    print("\n\n2) Від 5 до 1:")
    from_a_to_b(5, 1)

    print("\n\n3) Точна степінь двійки (8 та 3):")
    print("YES" if is_power_of_two(8) else "NO")
    print("YES" if is_power_of_two(3) else "NO")

    print("\n4) Сума цифр 179:")
    print(sum_digits(179))

    print("\n5) Цифри 179 справа наліво:")
    print_digits_reverse(179)

    print("\n\n6) Цифри 179 зліва направо:")
    print_digits_forward(179)
    print()