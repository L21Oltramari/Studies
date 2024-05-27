#JogoDaVelha
from random import randrange

# Função para exibir o tabuleiro
def display_board(board):
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print("|   " + "   |   ".join(row) + "   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

# Função para atualizar o tabuleiro com a jogada
def enter_move(board, move, sign):
    row, col = divmod(move - 1, 3)
    board[row][col] = sign

# Função para obter os movimentos livres no tabuleiro
def make_list_of_free_fields(board):
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ["X", "O"]:
                free_fields.append((row, col))
    return free_fields

# Função para verificar se há um vencedor
def victory_for(board, sign):
    # Checar linhas e colunas
    for idx in range(3):
        if all(board[idx][col] == sign for col in range(3)) or all(board[row][idx] == sign for row in range(3)):
            return True
    # Checar diagonais
    if all(board[idx][idx] == sign for idx in range(3)) or all(board[idx][2-idx] == sign for idx in range(3)):
        return True
    return False

# Função para a jogada do computador
def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    move = free_fields[randrange(len(free_fields))]
    board[move[0]][move[1]] = 'X'

# Função principal para gerenciar o jogo
def jogodavelha():
    board = [['1', '2', '3'], ['4', 'X', '6'], ['7', '8', '9']]
    display_board(board)

    while True:
        # Movimento do usuário
        move = int(input("Digite seu movimento: "))
        if move < 1 or move > 9:
            print("Movimento inválido. Tente novamente.")
            continue
        row, col = divmod(move - 1, 3)
        if board[row][col] in ['X', 'O']:
            print("Movimento inválido. Tente novamente.")
            continue
        enter_move(board, move, 'O')
        display_board(board)
        if victory_for(board, 'O'):
            print("Você ganhou!")
            break
        if len(make_list_of_free_fields(board)) == 0:
            print("Empate!")
            break

        # Movimento do computador
        draw_move(board)
        display_board(board)
        if victory_for(board, 'X'):
            print("O computador ganhou!")
            break
        if len(make_list_of_free_fields(board)) == 0:
            print("Empate!")
            break

jogodavelha()