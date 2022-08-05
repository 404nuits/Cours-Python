from tkinter import *
import cesar

fenetre = Tk()
fenetre.title('Code de César')
fenetre.geometry("450x250")

texte_a_convertir = StringVar(fenetre)
texte_converti = StringVar(fenetre)

def conversion():

    # Récupère le texte qui est dans input_text
    texte_clair = texte_a_convertir.get()

    # Converti le texte avec cesar.encode
    texte_encode = cesar.encode(texte_clair, 9)

    # Affiche le texte input_resultat
    texte_converti.set(texte_encode)
    

# Texte demande input
test_text = Label(fenetre, text = "Donnez-moi une phrase à encoder")
test_text.pack()

# Ici
ici_text = Label(fenetre, text = "Ici")
ici_text.pack(side=LEFT,fill=BOTH)

# Zone de texte entrée
input_text = Entry(fenetre, textvariable=texte_a_convertir)
input_text.pack(side=LEFT)

# Bouton
bouton_conversion = Button(fenetre, text="Convertir", command=conversion)
bouton_conversion.pack(side=LEFT, padx=30)

# Zone de texte sortie
input_resultat = Entry(fenetre, textvariable=texte_converti)
input_resultat.pack(side=RIGHT)

# Résultat
resultat_text = Label(fenetre, text = "Résultat ⏩")
resultat_text.pack(side=RIGHT,fill=BOTH)


# Permet d'afficher la fenetre
fenetre.mainloop()
