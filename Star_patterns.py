def display_menu():
    print('''
    [1]  -  square
    [2]  -  right_angle_triangle
    [3]  -  right_angle_triangle1
    [4]  -  mirror_right_angle_triangle
    [5]  -  equilateral_triangle
    [6]  -  diamond
    [7]  -  reverse_equilateral
    [8]  -  reverse_right_angle
    [9]  -  mirror_reverse_right_angle
    [10] -  arrow
    ''')


def get_input():
    n = int(input("Enter no of stars \n"))
    return n


def square():
    n = get_input()
    for i in range(0, n):
        for j in range(0, n):
            print("* ", end=" ")
        print("\r")


def right_angle_triangle():
    n = get_input()
    for i in range(0, n):
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


def right_angle_triangle1():
    n = get_input()


# Mirror Right angle Triangle

def mirror_right_angle_triangle():
    n = get_input()
    for i in range(1, n + 1):
        print("  " * (n - i) + "* " * i)


# Equilateral Triangle

def equilateral_triangle():
    n = get_input()
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)


# Diamond

def diamond():
    n = get_input()
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)
    for i in range(n, 0, -1):
        print(" " * (n - i) + "* " * i)


# Reverse equilateral

def reverse_equilateral():
    n = get_input()
    for i in range(n, 0, -1):
        print(" " * (n - i) + "* " * i)


# Reverse right angle

def reverse_right_angle():
    n = get_input()
    for i in range(n, 0, -1):
        print("* " * i)


# Mirror Reverse right angle

def mirror_reverse_right_angle():
    n = get_input()
    for i in range(n, 0, -1):
        print("  " * (n - i) + "* " * i)


# Arrow

def arrow():
    n = get_input()
    for i in range(1, n + 1):
        print("* " * i)
    for i in range(n - 1, 0, -1):
        print("* " * i)


if __name__ == "__main__":
    display_menu()
    choice = int(input("Enter your choice from the above Menu \n"))
    if choice == 1:
        square()
    elif choice == 2:
        right_angle_triangle()
    elif choice == 3:
        right_angle_triangle1()
    elif choice == 4:
        mirror_right_angle_triangle()
    elif choice == 5:
        equilateral_triangle()
    elif choice == 6:
        diamond()
    elif choice == 7:
        reverse_equilateral()
    elif choice == 8:
        reverse_right_angle()
    elif choice == 9:
        mirror_reverse_right_angle()
    elif choice == 10:
        arrow()
    else:
        print("Invalid entry")
