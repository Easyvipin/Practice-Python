# Program to decrypt ceaser cipher

text = input("Message > ").upper()

abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

for i in range(28):
    decrypt = ""
    for l in text:
        if l in abc:
            pos_let = abc.index(l)
            new_pos = (pos_let - i) % len(abc)
            decrypt += abc[new_pos]
        else:
            descrypt+= l
    msj = (f"ROT-{i}:", decrypt)
    print(msj)