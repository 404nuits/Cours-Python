def encode(chaine, decalage):
    new_chaine = ""
    for lettre in chaine:
        new_chaine += chr(ord(lettre) + decalage)
    return new_chaine

def decode(chaine, decalage):
    new_chaine = ""
    for lettre in chaine:
        new_chaine += chr(ord(lettre) - decalage)
    return new_chaine