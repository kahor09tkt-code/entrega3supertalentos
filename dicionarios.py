 #LISTA DE EXERCÍCIOS
# Dicionários em Python

# Questão 1
# {} é a forma literal de criar um dicionário.
# dict() é o construtor da classe e também permite criar dicionários.
# Para um dicionário vazio, os dois produzem o mesmo resultado.

produto = {
    "nome": "Notebook",
    "preco": 4500.00,
    "estoque": 10
}

print("\nQuestão 1")
print(produto)


# Questão 2
# O acesso com colchetes gera KeyError quando a chave não existe.
# O método get() permite informar um valor padrão.

usuario = {"nome": "Ana", "nivel": "Admin"}

print("\nQuestão 2")

try:
    print(usuario["email"])
except KeyError as erro:
    print(f"KeyError: {erro}")

print(usuario.get("email", "Não informado"))


# Questão 3

notas = {
    "Matemática": 8.5,
    "História": 7.0
}

notas["Física"] = 9.0
notas["História"] = 7.5

print("\nQuestão 3")
print(notas)


# Questão 4
# del remove uma chave e não retorna o valor.
# pop() remove a chave e retorna o valor removido.

cliente = {
    "id": 1024,
    "nome": "Carlos",
    "ativo": True
}

id_removido = cliente.pop("id")

print("\nQuestão 4")
print(f"ID removido: {id_removido}")
print(f"Cliente atualizado: {cliente}")


# Questão 5

config = {
    "tema": "escuro",
    "notificacoes": True,
    "volume": 80
}

item_removido = config.popitem()

print("\nQuestão 5")
print(f"Item removido: {item_removido}")
print(f"Config após popitem(): {config}")

config.clear()

print(f"Config após clear(): {config}")


# Questão 6

def verificar_chave(dicionario, chave):
    if chave in dicionario:
        return f"A chave '{chave}' existe no dicionário."
    return f"A chave '{chave}' não existe no dicionário."


usuario = {
    "nome": "Ana",
    "nivel": "Admin"
}

print("\nQuestão 6")
print(verificar_chave(usuario, "nome"))
print(verificar_chave(usuario, "email"))


# Questão 7

estoque = {
    "banana": 50,
    "maca": 30,
    "laranja": 25
}

print("\nQuestão 7")

for fruta in estoque.keys():
    print(fruta.upper())


# Questão 8

quantidade_total = sum(estoque.values())

print("\nQuestão 8")
print(f"Quantidade total de frutas em estoque: {quantidade_total}")


# Questão 9

print("\nQuestão 9")

for fruta, quantidade in estoque.items():
    print(f"Temos {quantidade} unidades de {fruta} em estoque.")


# Questão 10

empresa = {
    "TI": {
        "gerente": "Rafael",
        "funcionarios": ["Marcos", "Beatriz"]
    },
    "RH": {
        "gerente": "Juliana",
        "funcionarios": ["Sofia", "Renata"]
    }
}

segundo_funcionario_ti = empresa["TI"]["funcionarios"][1]

print("\nQuestão 10")
print(segundo_funcionario_ti)


# Questão 11

numeros = [1, 2, 3, 4, 5]

quadrados = {
    numero: numero ** 2
    for numero in numeros
}

print("\nQuestão 11")
print(quadrados)


# Questão 12

idades = {
    "Alice": 22,
    "Bob": 17,
    "Carlos": 29,
    "Daniel": 15
}

maiores_de_idade = {
    nome: idade
    for nome, idade in idades.items()
    if idade >= 18
}

print("\nQuestão 12")
print(maiores_de_idade)


# Questão 13
# update() altera o dicionário original.
# O operador | cria um novo dicionário.
# Quando uma chave se repete, prevalece o valor do dicionário da direita.

d1 = {
    "a": 1,
    "b": 2
}

d2 = {
    "b": 9,
    "c": 4
}

d1.update(d2)

print("\nQuestão 13")
print(f"d1 após update(): {d1}")

d1_original = {
    "a": 1,
    "b": 2
}

d3 = d1_original | d2
print(f"d3 (operador |): {d3}")


# Questão 14

configs = {
    "tema": "claro"
}

idioma = configs.setdefault("idioma", "pt-br")

print("\nQuestão 14")
print("Valor retornado:", idioma)
print("Configs atualizado:", configs)

tema = configs.setdefault("tema", "escuro")

print("Valor retornado:", tema)
print("Configs final:", configs)


# Questão 15
# defaultdict(list) cria automaticamente uma lista vazia para cada
# nova chave, então não é necessário verificar se a inicial já existe.

from collections import defaultdict

nomes = [
    "Ana",
    "Bruno",
    "Beatriz",
    "Carlos",
    "Camila",
    "Ana"
]

agrupado = defaultdict(list)

for nome in nomes:
    inicial = nome[0]
    agrupado[inicial].append(nome)

print("\nQuestão 15")
print(dict(agrupado))


# Questão 16

servidores = [
    "servidor1",
    "servidor2",
    "servidor3"
]

status_servidores = dict.fromkeys(servidores, "online")

print("\nQuestão 16")
print(status_servidores)


# Questão 17

campos = [
    "nome",
    "cargo",
    "salario"
]

valores = [
    "Mariana",
    "Analista",
    6200.00
]

funcionario = dict(zip(campos, valores))

print("\nQuestão 17")
print(funcionario)


# Questão 18
# sorted(agenda.items()) ordena alfabeticamente pelas chaves.
# A ordem correta é Gabriel, Kahor e Vinicius.

agenda = {
    "Vinicius": 40,
    "Kahor": 25,
    "Gabriel": 31
}

agenda_por_chave = sorted(agenda.items())

print("\nQuestão 18")
print(agenda_por_chave)


# Questão 19

agenda_por_idade = sorted(
    agenda.items(),
    key=lambda item: item[1]
)

print("\nQuestão 19")
print(agenda_por_idade)


# Questão 20

mapa = {
    "A": 1,
    "B": 2,
    "C": 3
}

mapa_invertido = {
    valor: chave
    for chave, valor in mapa.items()
}

print("\nQuestão 20")
print(mapa_invertido)


# Questão 21

cotacao_moedas = {
    "USD": 4.95,
    "EUR": 5.35,
    "GBP": 6.20,
    "ARS": 0.015
}

moeda_mais_valorizada = max(
    cotacao_moedas,
    key=cotacao_moedas.get
)

moeda_menos_valorizada = min(
    cotacao_moedas,
    key=cotacao_moedas.get
)

print("\nQuestão 21")
print(f"Moeda mais valorizada: {moeda_mais_valorizada}")
print(f"Moeda menos valorizada: {moeda_menos_valorizada}")


# Questão 22
# A comparação com == verifica se os dois dicionários possuem
# exatamente as mesmas chaves associadas aos mesmos valores.
# A ordem de inserção não interfere no resultado.

dicionario_1 = {
    "nome": "Ana",
    "idade": 22
}

dicionario_2 = {
    "idade": 22,
    "nome": "Ana"
}

print("\nQuestão 22")
print(dicionario_1 == dicionario_2)


# Questão 23

texto = "sol lua estrela sol estrela sol"
frequencia = {}

for palavra in texto.split():
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1

print("\nQuestão 23")
print(f"Frequência (manual): {frequencia}")


# Questão 24

d_loja1 = {
    "notebook": 5,
    "teclado": 12,
    "mouse": 20
}

d_loja2 = {
    "mouse": 15,
    "monitor": 7,
    "teclado": 8
}

produtos_em_comum = d_loja1.keys() & d_loja2.keys()

print("\nQuestão 24")
print(produtos_em_comum)


# Questão 25
# Um dicionário é um objeto do Python.
# JSON é um formato textual usado para armazenar e transmitir dados.
# Em JSON, True vira true, False vira false e None vira null.

import json

dados_cliente = {
    "nome": "Lucas",
    "vip": True,
    "compras": None
}

dados_json = json.dumps(
    dados_cliente,
    ensure_ascii=False,
    indent=4
)

print("\nQuestão 25")
print(dados_json)


# Questão final

inventario = {
    "P001": {
        "nome": "Mouse Gamer",
        "preco": 150.00,
        "quantidade": 30,
        "categoria": "Periféricos"
    },
    "P002": {
        "nome": "Teclado Mecânico",
        "preco": 350.00,
        "quantidade": 8,
        "categoria": "Periféricos"
    },
    "P003": {
        "nome": "Monitor 24pol",
        "preco": 899.90,
        "quantidade": 4,
        "categoria": "Monitores"
    },
    "P004": {
        "nome": "Cadeira Gamer",
        "preco": 1200.00,
        "quantidade": 2,
        "categoria": "Móveis"
    }
}


def adicionar_produto(
    inventario,
    id_prod,
    nome,
    preco,
    quantidade,
    categoria
):
    if id_prod in inventario:
        inventario[id_prod]["preco"] = preco
        inventario[id_prod]["quantidade"] += quantidade
        inventario[id_prod]["nome"] = nome
        inventario[id_prod]["categoria"] = categoria

        print(
            f"Produto {id_prod} atualizado com sucesso."
        )
    else:
        inventario[id_prod] = {
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade,
            "categoria": categoria
        }

        print(
            f"Produto {id_prod} adicionado com sucesso."
        )


def realizar_venda(
    inventario,
    historico_vendas,
    id_prod,
    qtd_venda,
    cliente
):
    if id_prod not in inventario:
        print(
            f"Erro: o produto {id_prod} não existe no inventário."
        )
        return False

    produto = inventario[id_prod]

    if qtd_venda <= 0:
        print(
            "Erro: a quantidade da venda deve ser maior que zero."
        )
        return False

    if produto["quantidade"] < qtd_venda:
        print(
            "Erro: estoque insuficiente para "
            f"{produto['nome']} "
            f"(disponível: {produto['quantidade']})."
        )
        return False

    valor_bruto = produto["preco"] * qtd_venda

    if valor_bruto > 500:
        valor_final = valor_bruto * 0.90
    else:
        valor_final = valor_bruto

    produto["quantidade"] -= qtd_venda

    id_venda = f"V{len(historico_vendas) + 1:03d}"

    historico_vendas[id_venda] = {
        "cliente": cliente,
        "id_produto": id_prod,
        "produto": produto["nome"],
        "quantidade": qtd_venda,
        "valor_bruto": valor_bruto,
        "valor_final": valor_final
    }

    print(
        f"Venda registrada: {qtd_venda}x "
        f"{produto['nome']} para {cliente} "
        f"- Total: R$ {valor_final:.2f}"
    )

    return True


def gerar_relatorio_critico(inventario):
    return {
        id_prod: dados.copy()
        for id_prod, dados in inventario.items()
        if dados["quantidade"] < 5
    }


def calcular_faturamento_e_destaque(historico_vendas):
    if not historico_vendas:
        return 0.0, None

    faturamento_total = sum(
        venda["valor_final"]
        for venda in historico_vendas.values()
    )

    unidades_por_produto = {}

    for venda in historico_vendas.values():
        id_produto = venda["id_produto"]
        quantidade = venda["quantidade"]

        unidades_por_produto[id_produto] = (
            unidades_por_produto.get(id_produto, 0)
            + quantidade
        )

    destaque = max(
        unidades_por_produto,
        key=unidades_por_produto.get
    )

    return faturamento_total, destaque


historico_vendas = {}

print("\nQuestão final")

realizar_venda(
    inventario,
    historico_vendas,
    "P002",
    2,
    "Fernanda"
)

realizar_venda(
    inventario,
    historico_vendas,
    "P001",
    1,
    "Ricardo"
)

realizar_venda(
    inventario,
    historico_vendas,
    "P004",
    5,
    "Marcelo"
)

relatorio_critico = gerar_relatorio_critico(inventario)

faturamento, destaque = calcular_faturamento_e_destaque(
    historico_vendas
)

print("\nInventário atualizado:")
print(inventario)

print("\nRelatório crítico de reposição:")
print(relatorio_critico)

print(f"\nFaturamento total: R$ {faturamento:.2f}")
print(f"Produto mais vendido (em unidades): {destaque}")


# Informação extra
# copy() faz uma cópia rasa e mantém a referência dos objetos internos.
# deepcopy() copia também os objetos internos.

import copy

orig = {
    "lista": [1, 2]
}

copia_rasa = orig.copy()
copia_rasa["lista"].append(3)

print("\nInformação extra")
print("orig após copy() + append:", orig)

orig2 = {
    "lista": [1, 2]
}

copia_profunda = copy.deepcopy(orig2)
copia_profunda["lista"].append(3)

print("orig2 após deepcopy() + append:", orig2)
