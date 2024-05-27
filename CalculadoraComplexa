import math

def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro: Divisão por zero"
    return x / y

def potencia(x, y):
    return x ** y

def raiz_quadrada(x):
    if x < 0:
        return "Erro: Raiz quadrada de número negativo"
    return math.sqrt(x)

def logaritmo(x, base=10):
    if x <= 0:
        return "Erro: Logaritmo de número não positivo"
    return math.log(x, base)

def porcentagem(x, y):
    return (x / 100) * y

def menu():
    print("\nCalculadora Complexa")
    print("Escolha a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potência")
    print("6. Raiz Quadrada")
    print("7. Logaritmo")
    print("8. Porcentagem")
    print("9. Sair")

def main():
    while True:
        menu()
        escolha = input("Digite sua escolha (1/2/3/4/5/6/7/8/9): ").strip()

        if escolha == '9':
            print("Obrigado por usar a calculadora. Até a próxima!")
            break

        if escolha in ['1', '2', '3', '4', '5']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                print(f"Resultado: {num1} + {num2} = {adicao(num1, num2)}")
            elif escolha == '2':
                print(f"Resultado: {num1} - {num2} = {subtracao(num1, num2)}")
            elif escolha == '3':
                print(f"Resultado: {num1} * {num2} = {multiplicacao(num1, num2)}")
            elif escolha == '4':
                print(f"Resultado: {num1} / {num2} = {divisao(num1, num2)}")
            elif escolha == '5':
                print(f"Resultado: {num1} ^ {num2} = {potencia(num1, num2)}")

        elif escolha == '6':
            num = float(input("Digite o número: "))
            print(f"Resultado: √{num} = {raiz_quadrada(num)}")

        elif escolha == '7':
            num = float(input("Digite o número: "))
            base = input("Digite a base do logaritmo (pressione Enter para base 10): ").strip()
            base = float(base) if base else 10
            print(f"Resultado: log{base}({num}) = {logaritmo(num, base)}")

        elif escolha == '8':
            num1 = float(input("Digite o valor: "))
            num2 = float(input("Digite a porcentagem: "))
            print(f"Resultado: {num2}% de {num1} = {porcentagem(num1, num2)}")

        else:
            print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    main()