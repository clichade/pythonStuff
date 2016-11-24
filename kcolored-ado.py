movies = [["movA", 23], ["movB", 56], ["movC", 72],["Fightclub",["Edward norton","Brad Pitt"]]]

"""""
Esto son comentarios
"""""
def show(lista):
    for mov in lista:
        if isinstance(mov, list):
            show(mov)
        else:
            print mov

# /print (len(movies))
show(movies)
