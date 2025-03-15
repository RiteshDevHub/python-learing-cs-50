import emoji
print(emoji.__version__)  # Should print the version if correctly installed

def main():
    text = input("Input: ")
    emojized_text = emoji.emojize(text, language="alias")  # Enables alias support
    print("Output:", emojized_text)

main()