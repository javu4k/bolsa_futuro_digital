"""
nome = "Carlos"
idade = 30
salario = 1250.75

print(type(nome))  # Saída: <class 'str'>
print(type(idade))  # Saída: <class 'int'>
print(type(salario))  # Saída: <class 'float'>

numero1 = 10
numero2 = 5

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
"""

# ex_1
first_name = "Júlia"
idade = 21
altura = 1.70
tem_animal = True

print("Meu nome é: ", first_name)
print("Minha idade é: ", idade)
print("Minha altura é: ", altura)
print("Tenho animal de estimação: ", tem_animal)

# ex_2
valor1 = 10
valor2 = 5

soma = valor1 + valor2
subtracao = valor1 - valor2
multiplicacao = valor1 * valor2
divisao = valor1 / valor2

print("Soma: ", soma)
print("Subtração: ", subtracao)
print("Multiplicação: ", multiplicacao)
print("Divisão: ", divisao)

# ex_3
nome_produto: str = "Mouse Logitech"
preco_produto: float = 29.90
qtd_estoque: int = 33
disponivel_venda: bool = True

print(
    "Produto: ",
    nome_produto,
    " Preço: ",
    preco_produto,
    " Estoque: ",
    qtd_estoque,
    " Disponível: ",
    disponivel_venda,
)

# ex_4
saldo_bancario: float = 500.00
valor_deposito: float = 150.00

saldo_bancario += valor_deposito

valor_saque: float = 50.00

saldo_bancario -= valor_saque

print("Saldo bancário atual: R$", saldo_bancario)
