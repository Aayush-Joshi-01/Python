def JTOI():
    with open('WORDS.TXT', 'r') as file:
        text = file.read()
    corrected_text = text.replace('J', 'I')
    print('Corrected content:')
    print(corrected_text)


JTOI()
