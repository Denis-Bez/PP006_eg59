from spam_list import spam_filter

import re

def start():
    text = "Zimerlfe"
    for spam_text in spam_filter:
        print(spam_text)
        # if re.search(spam_text, text):
        #     print("Searched!")


if __name__ == "__main__":
    start()