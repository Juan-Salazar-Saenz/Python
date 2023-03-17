import string

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s


def f(x):
    x = normalize(x)
    quitar = string.punctuation + "¡" + "¿"
    texto = ""
    for i in (x):
        if i != " ":
            if not i in (quitar):
                texto = texto + i
    return (texto.upper() == texto[::-1].upper())
