def afficher_plateau(plateau):
    for row in plateau:
        print('|'.join(row))
        print('-' * 5)

def verifier_victoire(plateau, joueur):
    for i in range(3):
        if all([case == joueur for case in plateau[i]]):
            return True
        if all([plateau[j][i] == joueur for j in range(3)]):
            return True
    if all([plateau[i][i] == joueur for i in range(3)]) or all([plateau[i][2-i] == joueur for i in range(3)]):
        return True
    return False

def jeu_morpion():
    plateau = [[' ' for _ in range(3)] for _ in range(3)]
    joueurs = ['X', 'O']
    tour = 0

    while True:
        afficher_plateau(plateau)
        joueur = joueurs[tour % 2]
        mouvement = input(f'Joueur {joueur}, entrez votre mouvement (ligne,colonne) : ')
        ligne, colonne = map(int, mouvement.split(','))

        if plateau[ligne][colonne] != ' ':
            print('Case déjà occupée, veuillez choisir une autre case.')
            continue

        plateau[ligne][colonne] = joueur
        if verifier_victoire(plateau, joueur):
            afficher_plateau(plateau)
            print(f'Le joueur {joueur} a gagné !')
            break

        tour += 1

        if tour == 9:
            afficher_plateau(plateau)
            print('Match nul!')
            break

if __name__ == '__main__':
    jeu_morpion()
