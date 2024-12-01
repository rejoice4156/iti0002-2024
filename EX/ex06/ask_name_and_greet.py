"""Ask name and greet."""


def ask_name_and_greet():
    """
    Ask for the user's name and greet them.

    The user has to enter his/her name. The function prints the greeting.

    Regular greeting: Hi, [name]. Would you like to have a Hamburger?
    [name] is capitalized, meaning first letter is capital, the rest is lower.

    If the name is Thanos (case-insensitive, so thanos and THANOS also count):
    Get out of here, Thanos! Nobody wants to play with you!
    """
    name = input("What is your name: ")
    if name.lower() == "thanos":
        print("Get out of here, Thanos! Nobody wants to play with you!")
    else:
        print(f"Hi, {name.capitalize()}. Would you like to have a Hamburger?")


if __name__ == '__main__':
    ask_name_and_greet()
