"""
Description:
Encrypt this!

You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

Your message is a string containing space separated words.
You need to encrypt each text in the message using the following rules:
The first letter needs to be converted to its ASCII code.
The second letter needs to be switched with the last letter
Keepin' it simple: There are no special characters in input.
Examples:
encrypt_this("Hello") == "72olle"
encrypt_this("good") == "103doo"
encrypt_this("hello world") == "104olle 119drlo"
"""

# my solution
def encrypt_this(text):
    encrypted_msg = ""
    for word in text.split():
        if len(word) == 1:
            encrypted_msg += str(ord(word[0])) + " "
        elif len(word) < 3:
            encrypted_msg += str(ord(word[0])) + (word[len(word) - 1]) + " "
        else:
            encrypted_msg += (
                str(ord(word[0]))
                + (word[len(word) - 1])
                + (word[2 : len(word) - 1] + word[1])
                + " "
            )
    return encrypted_msg.strip()

# print(encrypt_this("hello world"))


# code wars
def encrypt_this(text):
    result = []

    for word in text.split():
        # turn word into a list
        word = list(word)

        # replace first letter with ascii code
        word[0] = str(ord(word[0]))

        # switch 2nd and last letters
        if len(word) > 2:
            word[1], word[-1] = word[-1], word[1]

        # add to results
        result.append("".join(word))

    return " ".join(result)


print(encrypt_this("A wise old owl lived in an oak"))
