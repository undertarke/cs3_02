
arrChar = ["car", "bat", "card", "man", "women", "bag", "bimbim"]

# ca => car, card
# ba => bat, bag

getChar = input("Nhập từ muốn kiếm: ")


matching_words = [word for word in arrChar if word.startswith(getChar)]

matching_words = []
# O(N)
for word in arrChar:
    if word.startswith(getChar):
        matching_words.append(word)

# Display the matching words
if matching_words:
    print(f"Các từ bắt đầu bằng '{getChar}': {', '.join(matching_words)}")
else:
    print(f"Không có từ nào bắt đầu bằng '{getChar}'")

    # Cấu trúc Trie

    #  root = {
    #     "c": {
    #         "a": {
    #             "t": {

    #                 "endWord": True
    #             },
    #             "endWord": False
    #         },
    #         "endWord": False
    #     },

    #     "b": {
    #         "a": {
    #             "n": {
    #                 "a": {
    #                     "n": {
    #                         "a": {
    #                             "endWord": True
    #                         },
    #                         "endWord": False
    #                     },
    #                     "endWord": False
    #                 },
    #                 "endWord": False
    #             },

    #             "t": {
    #                 "m": {
    #                     "a": {
    #                         "n": {
    #                             "endWord": True
    #                         },
    #                         "endWord": False
    #                     },
    #                     "endWord": False
    #                 },
    #                 "endWord": False
    #             },
    #             "endWord": False
    #         },

    #         "endWord": False
    #     },

    #     "o": {
    #         "b": {
    #             "a": {
    #                 "m": {
    #                     "a": {
    #                         "endWord": True
    #                     },
    #                     "endWord": False
    #                 },
    #                 "endWord": False
    #             },
    #             "endWord": False
    #         },
    #         "endWord": False
    #     },
    #     "a": {},

    # }
# *** L
root = {
    "c": {
        "a": {
            "r": {
                "is_end_of_word": True
            },
            "t": {
                "is_end_of_word": True
            },
            "is_end_of_word": False
        },
        "is_end_of_word": False
    },
    "is_end_of_word": False
}

# ["car", "bat", "card", "man", "women", "bag", "bimbim"]
# c a

print(root["c"]["a"])
