# Simulador de dado
import random

def jogar_dado():
    return random.randint(1, 6)

def main():
    print("Bem-vindo ao simulador de dado!")
    while True:
        resposta = input("Você quer jogar o dado? (sim/não): ").strip().lower()
        if resposta == 'sim':
            resultado = jogar_dado()
            print(f"Você jogou o dado e o resultado foi: {resultado}")
        elif resposta == 'não':
            print("Obrigado por jogar! Até a próxima.")
            break
        else:
            print("Resposta inválida. Por favor, responda 'sim' ou 'não'.")

if __name__ == "__main__":
    main()