def encode(chaine, decalage):
    
    debut = 97
    fin = 122
    
    new_chaine = ""
    for lettre in chaine:
        temp1 = ord(lettre)
        
        decale = temp1 + decalage
        
        if decale > fin:
            decale = decale - 26
        
        temp2 = chr(decale)
        new_chaine += temp2
    return new_chaine

def decode(chaine, decalage):
    new_chaine = ""
    for lettre in chaine:
        new_chaine += chr(ord(lettre) - decalage)
    return new_chaine
