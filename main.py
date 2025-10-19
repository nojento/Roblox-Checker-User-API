import requests

def verificar_nome(usuario):
    url = f"https://api.roblox.com/users/get-by-username?username={usuario}"
    resposta = requests.get(url)

    if resposta.status_code != 200:
        return f"Erro ao verificar ({resposta.status_code})"

    dados = resposta.json()

    if "Id" not in dados:
        return f"O nome de usuário '{usuario}' disponivel"
    else:
        return f"O nome de usuário '{usuario}' já tem."

if __name__ == "__main__":
    while True:
        nome = input("Digite um nome de usuário para verificar (ou 'sair'): ").strip()
        if nome.lower() == "sair":
            break
        print(verificar_nome(nome))
        print()
