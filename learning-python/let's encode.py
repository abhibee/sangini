#let's encode
sentence = input('please enter a sentence: ')

number_difference = 13
print("you entered ",sentence)


def encode(sentence, number_to_add) :
    sentence_chars = list(sentence)
    encoded_sentence = ''
    for character in sentence_chars:
        encoded_character_int = ord(character) + number_to_add
        encoded_sentence = encoded_sentence + chr(encoded_character_int)

    return encoded_sentence


def decode(sentence,number_to_reduce):
    sentence_chars = list(sentence)
    decoded_sentence = ''
    for character in sentence_chars:
        decoded_character_int = ord(character) - number_to_reduce
        decoded_sentence = decoded_sentence + chr(decoded_character_int)

    return decoded_sentence


def newEncodeDecode(message, num_diff):
    output = ""
    for letter in message.upper():
        if letter.isupper():
            value = ord(letter) + num_diff
            letter = chr(value)
            if not letter.isupper():
                value -= 26
                letter = chr(value)
        output += letter

    return output


encoded_sentence = encode(sentence, number_difference)
print("encoded sentence ",encoded_sentence)

decoded_sentence = decode(encoded_sentence, number_difference)
print("decoded sentence ",decoded_sentence)

print("")
print("")
print("encoded---->",newEncodeDecode(sentence,number_difference))
print("decoded---->",newEncodeDecode(newEncodeDecode(sentence,number_difference),number_difference))