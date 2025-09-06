# 1. Verificar se um número é perfeito
def numero_perfeito(n):
    soma = sum(i for i in range(1, n) if n % i == 0)
    return soma == n

# 2. Contar palavras em um texto
def contar_palavras(texto):
    palavras = texto.split()
    dicionario = {}
    for p in palavras:
        dicionario[p] = dicionario.get(p, 0) + 1
    return dicionario

# 3. Lista de primos entre dois números
def primos_entre(a, b):
    def eh_primo(x):
        if x < 2: return False
        for i in range(2, int(x**0.5)+1):
            if x % i == 0: return False
        return True
    return [n for n in range(a, b+1) if eh_primo(n)]

# 4. Fatorial recursivo
def fatorial(n):
    if n == 0: return 1
    return n * fatorial(n-1)

# 5. Contar linhas, palavras e caracteres em arquivo
def analisar_arquivo(nome):
    with open(nome, "r", encoding="utf-8") as f:
        texto = f.read()
    linhas = texto.count("\n") + 1
    palavras = len(texto.split())
    caracteres = len(texto)
    return linhas, palavras, caracteres

# 6. Verificar palíndromo
def eh_palindromo(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# 7. Sequência de Fibonacci
def fibonacci(n):
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

# 8. Sorteio de nomes
import random
def sorteio(nomes):
    return random.choice(nomes)

# 9. CRUD com dicionário
def crud():
    contatos = {}
    while True:
        print("\n1-Adicionar 2-Remover 3-Atualizar 4-Listar 5-Sair")
        op = input("Opção: ")
        if op == "1":
            nome = input("Nome: ")
            tel = input("Telefone: ")
            contatos[nome] = tel
        elif op == "2":
            nome = input("Nome: ")
            contatos.pop(nome, None)
        elif op == "3":
            nome = input("Nome: ")
            if nome in contatos:
                contatos[nome] = input("Novo telefone: ")
        elif op == "4":
            for n, t in contatos.items():
                print(n, t)
        elif op == "5":
            break

# 10. CRUD com arquivo
import json
def crud_arquivo(arquivo="contatos.json"):
    try:
        with open(arquivo, "r") as f:
            contatos = json.load(f)
    except:
        contatos = {}
    while True:
        print("\n1-Adicionar 2-Remover 3-Atualizar 4-Listar 5-Sair")
        op = input("Opção: ")
        if op == "1":
            nome = input("Nome: ")
            tel = input("Telefone: ")
            contatos[nome] = tel
        elif op == "2":
            nome = input("Nome: ")
            contatos.pop(nome, None)
        elif op == "3":
            nome = input("Nome: ")
            if nome in contatos:
                contatos[nome] = input("Novo telefone: ")
        elif op == "4":
            for n, t in contatos.items():
                print(n, t)
        elif op == "5":
            with open(arquivo, "w") as f:
                json.dump(contatos, f)
            break

# 11. Ordenar lista de tuplas
def ordenar(lista):
    return sorted(lista, key=lambda x: (-x[2], x[1], x[0]))

# 12. Subconjuntos que somam alvo
def subconjuntos(nums, alvo):
    res = []
    def backtrack(i, atual, soma):
        if soma == alvo:
            res.append(list(atual))
        if soma >= alvo or i == len(nums):
            return
        atual.append(nums[i])
        backtrack(i+1, atual, soma+nums[i])
        atual.pop()
        backtrack(i+1, atual, soma)
    backtrack(0, [], 0)
    return res

# 13. Maior subsequência crescente contínua
def maior_subseq(lista):
    maior, atual = 1, 1
    for i in range(1, len(lista)):
        if lista[i] > lista[i-1]:
            atual += 1
            maior = max(maior, atual)
        else:
            atual = 1
    return maior

# 14. Rotacionar matriz 90°
def rotacionar(matriz):
    n = len(matriz)
    return [[matriz[n-1-j][i] for j in range(n)] for i in range(n)]

# 15. Elemento majoritário
def majoritario(lista):
    contagem = {}
    for num in lista:
        contagem[num] = contagem.get(num, 0) + 1
        if contagem[num] > len(lista)//2:
            return num
    return None
