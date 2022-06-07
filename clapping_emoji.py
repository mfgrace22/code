
def main():
    clapping_emoji = " \U0001F44F "  # unicode for clapping emoji
    user_input = input(">>> ")
    print(clapping_emoji.join(user_input.split()) + clapping_emoji)

if __name__ == "__main__":
    main()
