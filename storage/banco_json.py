from pathlib import Path
import json


class BancoJSON:
    def __init__(self, arquivo):
        self.path = Path(arquivo)
        self.dados = self._carregar()
        print("DEBUG - caminho do arquivo:", self.path.resolve())
        print("DEBUG - existe?", self.path.exists())

        

    def _carregar(self):
        """Carrega o conteúdo do arquivo JSON ou cria lista vazia."""
        
        if self.path.exists():
            with self.path.open("r", encoding="utf-8") as arq:
                return json.load(arq)
        return self.estrutura_dados()

    def atualizar_item(self, mes="Janeiro", banco="Nubank", novo_valor=0):
        self.dados[mes][banco] = float(novo_valor)
        self._salvar()

    def adicionar_bancos(self, banco_novo):
        for mes in self.dados:
            self.dados[mes][banco_novo] = 0
        self._salvar()

    def apagar_bancos(self, banco_apagar):
        for mes in self.dados:
            del self.dados[mes][banco_apagar]
        self._salvar()
    
    def _salvar(self):
        """Salva os dados no arquivo JSON"""
        with self.path.open("w", encoding="utf-8") as arq:
            json.dump(self.dados, arq, indent=4, ensure_ascii=False)
            self.dados

    def dadostotais(self):
        "Usado apenas para teste de manipulação de dados"
        meses = list(self.dados.keys())
        print(self.dados)
        print()
        for mes in meses:
            novo_nome = f"{mes}/2026"
            self.dados[novo_nome] = self.dados[mes]
            del self.dados[mes]
        self._salvar()

    def estrutura_dados(self):
        """Coleta os dados"""
        meses = [
            'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 
            'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
            ]
        
        modelos_bancos = {
            "Nubank":0,
            "Click": 0,
            "Amazon": 0,
            "Inter": 0,
        }

        dados_gerais = {}
        for mes in meses:
            dados_gerais[mes] = modelos_bancos.copy()

        return dados_gerais

