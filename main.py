from models.financeiro import Financeiro, FluxoDados
from storage.banco_json import BancoJSON
from pathlib import Path
import os


class App:
    def __init__(self, ):
        "Ainda não sei o que comentar"
        caminho = Path(r"C:\Users\davil\OneDrive\PYTHON\gestao_financeira\data\dadosfinanceiros.json")
        self.db = BancoJSON(caminho)
        self.financeiro = Financeiro(self.db)
        self.fluxodados = FluxoDados(self.db)
    def pergunta(self):
        """Reduzir as repetições aninhadas"""
        while True:
            try:
                resposta = int(input('\n\nOutra sequência numérica: 1(Sim) ou 2(Não): \n'))
            except ValueError:
                print('Entrada inválida')
                continue
            if resposta == 1:
                return 'continuar'
            elif resposta == 2:
                return 'Encerrar'
            else:
                print('RESPOSTA INVÁLIDA. TENTE NOVAMENTE')

    def espaco_linha(self, tipo_linha="-"):
        return f"{tipo_linha}" * 90
    
    def tabela_meses(self):                                 
        linhas = []
        for indice, mes in enumerate(self.db.dados.keys()):
            indice_formatado = f"{indice+1}."
            linhas.append(f"  {indice_formatado:<10} {mes} ")
        return "\n".join(linhas)
    
    def tabela_bancos(self):
        linhas = []
        bancos = self.fluxodados.lista_bancos()
        for indice, banco in enumerate(bancos):
            linhas.append(f"{indice+1}. {banco}")

        return "\n".join(linhas)

    def exibir_por_mes(self, tipo_moeda="R$"): 
        linhas = []
        indice_mes = self.escolher_mes_indice()
        lista_mes = self.fluxodados.lista_meses()
        mes_divida = lista_mes[indice_mes-1]
        linhas.append(f"Mês selecionado: {mes_divida:<10}")
        for key, value in self.db.dados[mes_divida].items():
            linhas.append(f"{key:<10}| {tipo_moeda} {value:<10}")
            
        linhas.append((f"Valor total {tipo_moeda} {self.financeiro.soma_financeiro_mes(mes_divida):.2f}".replace(".", ",")))
        return "\n".join(linhas)                          

    def exibir_por_banco(self, tipo_moeda="R$"):
        linhas = []
        indice_banco = self.escolher_banco_indice()
        banco_divida = self.fluxodados.lista_bancos()[indice_banco-1]
        for mes, bancos in self.db.dados.items():
            valor_formatado = f"{tipo_moeda} {bancos[banco_divida]:.2f}"
            linhas.append(f"{mes:<10} | {banco_divida:<10} | {valor_formatado:>10}")
    
        linhas.append(f"Valor total {tipo_moeda} {self.financeiro.soma_financeiro_bancos(banco_divida):.2f}".replace(".", ","))
        return "\n".join(linhas)


    def escolher_mes_indice(self):
        print(self.tabela_meses())
        while True:
            try:
                mes_escolhido = int(input("Escolha o índice do mês: "))
                if mes_escolhido > 12:
                    raise ValueError("Escolha um numero de 1 a 12.")
            except ValueError:
                print("Escolha um número de 1 a 12")
            else:
                return mes_escolhido
        
    def escolher_banco_indice(self):
        print(self.tabela_bancos())
        a = 1
        b = len(self.fluxodados.lista_bancos())
        while True:
            try:
                banco_escolhido = int(input("Escolha o índice do Banco: "))
                if banco_escolhido > b:
                    raise ValueError("")
            except ValueError:
                print(f"Escolha um número de {a} a {b}")
            else:
                return banco_escolhido

    def novo_valor(self):
        while True:
            try:
                novo_valor = float(input("Digite o novo valor: ")) 
            except ValueError:
                print("Valor inválido. Digite somente número. Se for com casa decimal, coloque o ponto.")
            else:
                return novo_valor


    def editar_valor(self):
        indice_mes = self.escolher_mes_indice()
        mes = self.fluxodados.lista_meses()[indice_mes-1]#list(self.db.dados.keys())
        indice_banco = self.escolher_banco_indice()
        banco = self.fluxodados.lista_bancos()[indice_banco-1]
        novo_valor = self.novo_valor()
        if novo_valor == 0.01:
            print("Atualização Cancelada! ")
        else:
            self.db.atualizar_item(mes, banco, novo_valor) 
        

    def tratamento_entrada_numerica(self, a=0, b=5, texto="Escolha a opção desejada: "):
        try:
            op = input(texto)
            if op != "q":
                op = int(op)
                parametro = [n for n in range(a, b+1)]
                if op not in parametro:
                    raise ValueError("Numero fora dos parâmetros do menu")
            elif op == "q":
                print()
                return f"quit"
        except ValueError:
            print(self.espaco_linha())
            print(f"Digite um número de {a} a {b}!")
            print(self.espaco_linha())
        else:
            return op

    def voltar(self):
        pass
            

    def menu(self):

        while True:
            
            print('Programa em funcionamento. ')
            print('1. Exibir.')
            print('2. Editar valor.')
            print('3. Adicionar/apagar banco.')
            print('4. N/D.')
            print('5. Sair.')
            print('0. Limpar terminal.')
         
            op = self.tratamento_entrada_numerica(0, 5)
            

            if op == 1:
                contador = 0
        
                while True:
                    if contador == 0:
                        limpar_terminal()
                    print("Menu de exibição: ")
                    print("1. Vizualizar dívididas por mês.")
                    print("2. Vizualizar dívididas por banco.")
                    print("3. Vizualizar todas as dívidas.")
                    print("4. Voltar.")
                    contador = 1
                    op_exibir = self.tratamento_entrada_numerica(1, 4)

                    if op_exibir == 1:
                        print(self.exibir_por_mes())

                    elif op_exibir == 2:
                        print(self.exibir_por_banco())
                        
                    elif op_exibir == 3:
                        print(self.financeiro.exibir_tudo(self.fluxodados.lista_meses()[0]))

                    elif op_exibir == "quit":
                        break

                    elif op_exibir == 4:
                        limpar_terminal()
                        break

                    if op_exibir in [1, 2, 3]:
                        print()
                        break

            elif op == 2:
                while True:
                    self.editar_valor()
                    print(self.financeiro.exibir_tudo(self.fluxodados.lista_meses()[0]))
                    continuidade = int(input("Deseja editar outro valor? S[1] ou N[2]\n"))
                    
                    if continuidade == 1:
                        continue
                    elif continuidade == 2:
                        break
                        
            
            elif op == 3:
                print("1. Adicionar Banco.\n2. Apagar Banco.\n3. Voltar.")
                op_alterar = self.tratamento_entrada_numerica(1, 3)
                if op_alterar == 1:
                    nome_banco = input("Digite o nome do banco que deseja adicionar: ").capitalize()
                    confirmacao = self.tratamento_entrada_numerica(1, 2, f"Tem certeza que deseja ADICIONAR o banco {banco_apagar}? Sim[1] Não[2] ")
                    if confirmacao == 1: 
                        self.db.adicionar_bancos(nome_banco)
                        print(self.financeiro.exibir_tudo(self.fluxodados.lista_meses()[0]))
                    elif confirmacao == 2:
                        print('OPERAÇÃO CANCELADA')

                elif op_alterar == 2:
                    banco_apagar = input("Digite o nome do banco que deseja apagar: ").capitalize()
                    confirmacao = self.tratamento_entrada_numerica(1, 2, f"Tem certeza que deseja APAGAR o banco {banco_apagar}? Sim[1] Não[2] ")
                    if confirmacao == 1:
                        self.db.apagar_bancos(banco_apagar)
                        print(self.financeiro.exibir_tudo(self.fluxodados.lista_meses()[0]))    
                    elif confirmacao == 2:
                        print("OPERAÇÃO CANCELADO")  

                elif op_alterar == 3:
                    limpar_terminal()
                    continue

                elif op_alterar == "quit":
                    break
                                

            elif op == 4:
                pass

            elif op == 5:
                break

            elif op == 0:
                limpar_terminal()



def limpar_terminal():
    os.system('cls')

if __name__ == "__main__":
    app = App()
    app.menu()


    