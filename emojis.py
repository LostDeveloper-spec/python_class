def main():
    emoji_map = {
        ":thumbs_up:": "\U0001F44D",
        ":thumbsup:": "\U0001F44D",
        ":smile:": "\U0001F604",
        ":tada:": "\U0001F389",
        ":heart:": "\u2764\ufe0f",
        ":grinning:": "\U0001F600",
        ":wink:": "\U0001F609",
        ":cry:": "\U0001F622",
        ":laughing:": "\U0001F606",
        # more space
    }

    text = input("Input: ")

    for code, emoji_char in emoji_map.items():
        text = text.replace(code, emoji_char)

    print("Output:", text)

main()