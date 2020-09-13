mores_code = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
              '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
              '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
              '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
              '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9'}


def parse_word(word):
    characters = word.split('0')
    new_charaters = []
    for character in characters:
        if character == '1':
            new_charaters.append('.')
        elif character == '111':
            new_charaters.append('-')
    return mores_code.get(''.join(new_charaters), '')


def parse_verse(verse):
    res_verse = []
    if '000' in verse:
        words = verse.split('000')
        for word in words:
            res_verse.append(parse_word(word))
    else:
        res_verse.append(parse_word(verse))
    return ''.join(res_verse)


def solution(text):
    if '0000000' in text:
        res = []
        verses = text.split('0000000')
        for verse in verses:
            res.append(parse_verse(verse))
        print(' '.join(res))
    else:
        print(parse_verse(text))


if __name__ == '__main__':
    solution('1010100011101110111000101010000000101110111011101110001010111011101110001010101110111')
    solution('101')
    solution('101010001110111011100010101')
    solution('10101')
    solution('')

