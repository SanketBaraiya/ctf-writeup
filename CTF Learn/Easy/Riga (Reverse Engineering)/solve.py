import string

pickles0 = [
    0x9F, 0xAE, 0x9C, 0xB6, 0xBD, 0xB9, 0xEF, 0xEB, 0xE6,
    0x9E, 0xB9, 0xEC, 0xB3, 0xB9, 0xE3, 0xB9, 0xBB, 0xA8,
    0x89, 0xE3, 0xBD, 0xEF, 0xBB, 0x96, 0xB9, 0xED, 0xE3,
    0x89, 0xB9, 0xE4
]

r = ""

a = string.printable
for x in pickles0:
    t = (x ^ 0xCB) - 17

    if chr(t) in a:
        r += chr(t)
    else:
        p = chr(t ^ 97)
        if p in a:
            r += p
        else: r += " " + hex(t) + " "

print(r)