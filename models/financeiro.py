class Financeiro:
    """"recebe os dados necessários para realizar os cálculos"""
    def __init__(self, banco_dados):
        self.dados = banco_dados.dados

    def soma_financeiro_mes(self, escolha_mes="Janeiro"):
        "Soma as contas de um único mês"
        total_mes = sum(self.dados[escolha_mes].values())
        return total_mes
    
    def soma_financeiro_bancos(self, escolha_banco="Nubank"):
        "Soma todas as contas de um único banco"
        valor_total = 0
        for mes, contas in self.dados.items():
            valor_total += contas[escolha_banco]
        return valor_total
    
    def soma_financeiro_total(self):
        "Soma todas as contas disponiveis"
        total_total = 0
        for mes in self.dados.keys():
            total_total += sum(self.dados[mes].values())
        return total_total

    def exibir_tudo(self, mes):
        "Retorna todas as informações formatadas em texto"
        linhas = []
        # Cabeçalho (bancos)
        cabecalho = ""
        a = 17
        for contador, banco in enumerate(self.dados[mes].keys()):
            if contador != 0:
                cabecalho += f"|{banco:<17}"
            else:
                cabecalho += f"{'':<17}|{banco:<17}"
        linhas.append(cabecalho)
        # Linhas por mês
        for mes in self.dados.keys():
            linha = f"{mes:<17}"
            for valor in self.dados[mes].values():
                valor = float(valor)
                valor_formatado = f" {valor:.2f}".replace(".", ",")
                linha += f"|{valor_formatado:<17}"
            

            linhas.append(linha)
        valor_total = 1
        linhas.append(f"Valor total: {self.soma_financeiro_total()}")
        linhas.append(" ")

        return "\n".join(linhas)
    

    
class FluxoDados:
    """
    Classe responsável por fornecer informações estruturais dos dados,
    como listagem de meses e bancos disponíveis, sem realizar cálculos
    ou operações de persistência.
    """
    def __init__(self, banco_dados):
        self.dados = banco_dados.dados

    def lista_meses(self):
        meses = list(self.dados.keys())
        return meses
    
    def lista_bancos(self):
        lista = []
        for mes in self.lista_meses():
            for banco in self.dados[mes].keys():
                lista.append(banco)
        bancos = []
        for banco in lista:
            if banco not in bancos:
                bancos.append(banco)
        return bancos
