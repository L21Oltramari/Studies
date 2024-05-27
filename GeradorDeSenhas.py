import secrets
import string

def gerar_senha():
    comprimento_minimo = 8
    caracteres = string.ascii_letters + string.digits + string.punctuation
    while True:
        senha = ''.join(secrets.choice(caracteres) for i in range(comprimento_minimo))
        if (any(c.islower() for c in senha)
                and any(c.isupper() for c in senha)
                and any(c.isdigit() for c in senha)
                and any(c in string.punctuation for c in senha)):
            return senha

def main():
    try:
        senha = gerar_senha()
        print("A senha gerada é:", senha)
    except ValueError:
        print("Ocorreu um erro ao gerar a senha.")

if __name__ == "__main__":
    main()