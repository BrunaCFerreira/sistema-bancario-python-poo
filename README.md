# 🏦 Sistema Bancário em Python 

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![POO](https://img.shields.io/badge/POO-Fundamentos-blue?style=for-the-badge)
![DIO](https://img.shields.io/badge/DIO-Bootcamp-000000?style=for-the-badge)

Este projeto foi desenvolvido como um desafio prático de código para consolidar os fundamentos de **Orientação a Objetos (POO)** em Python. 

A proposta inicial faz parte da trilha de aprendizado da plataforma DIO. O objetivo foi construir toda a lógica matemática e de negócios do zero, transformando um diagrama UML em um sistema funcional rodando diretamente no terminal. O foco absoluto aqui foi garantir que a comunicação entre as classes e os objetos ocorresse de forma perfeita e segura.

## 📋 Requisitos do Desafio (Modelagem UML)
O desafio exigia a criação de um sistema bancário procedural para o paradigma de Orientação a Objetos, respeitando rigorosamente a seguinte modelagem:

* **Classe `Cliente` e `PessoaFisica`:** Criar uma classe base para clientes com capacidade de armazenar múltiplas contas e realizar transações. A classe filha `PessoaFisica` deve conter CPF, nome e data de nascimento.
* **Classe `Conta` e `ContaCorrente`:** O banco deve possuir uma classe base de conta, contendo agência, número, saldo e vínculo com um cliente. A classe filha `ContaCorrente` deve implementar as regras de negócio de limite de saque diário (3 saques) e limite de valor por saque (R$ 500,00).
* **Classe `Historico`:** Uma classe dedicada a armazenar a lista de todas as transações realizadas em uma conta específica.
* **Interface `Transacao` (Polimorfismo):** Uma classe abstrata que define um contrato obrigatório (método `registrar`) para as classes filhas `Saque` e `Deposito`, forçando-as a calcular as operações e anotar no histórico da conta.

```mermaid
classDiagram
    class Transacao {
        <<interface>>
        +registrar(conta: Conta)
    }

    class Deposito {
        -valor: float
    }

    class Saque {
        -valor: float
    }

    class Historico {
        +adicionar_transacao(transacao: Transacao)
    }

    class Conta {
        -saldo: float
        -numero: int
        -agencia: str
        -cliente: Cliente
        -historico: Historico
        +saldo(): float
        +nova_conta(cliente: Cliente, numero: int): Conta
        +sacar(valor: float): bool
        +depositar(valor: float): bool
    }

    class ContaCorrente {
        -limite: float
        -limite_saques: int
    }

    class Cliente {
        -endereco: str
        -contas: list
        +realizar_transacao(conta: Conta, transacao: Transacao)
        +adicionar_conta(conta: Conta)
    }

    class PessoaFisica {
        -cpf: str
        -nome: str
        -data_nascimento: date
    }

    Transacao <|.. Deposito
    Transacao <|.. Saque
    Conta <|-- ContaCorrente
    Cliente <|-- PessoaFisica
    Historico o-- "*" Transacao : -transacoes
    Conta *-- "1" Historico : -historico
    Cliente "1" -- "*" Conta : -contas / -cliente
    Cliente ..> Transacao : realiza


## 🚀 Funcionalidades do Sistema
O sistema simula as operações básicas de um caixa eletrônico real:
* `[nu]` **Novo Usuário:** Cadastro de clientes (Pessoa Física). O sistema barra CPFs duplicados.
* `[nc]` **Nova Conta:** Criação de conta corrente vinculada obrigatoriamente a um usuário existente.
* `[d]` **Depositar:** Adiciona saldo de forma segura (barrando valores negativos) e registra no histórico.
* `[s]` **Sacar:** Valida o saldo, o limite do saque e o limite de operações diárias antes de liberar o dinheiro.
* `[e]` **Extrato:** Lista cronologicamente todas as movimentações e exibe o saldo final.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python
* **Paradigma:** Programação Orientada a Objetos (POO)
* **Ambiente:** Visual Studio Code / Terminal

## 💻 Como executar
1. Clone este repositório na sua máquina local.
2. Abra o terminal na pasta raiz do projeto.
3. Execute o comando: `python sistema_bancario.py`
