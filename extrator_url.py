import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
        self.indice_interrogacao = self.acha_indice_interrogacao()

    def sanitiza_url(self, url):
        if (type(url) == str):
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not (self.url):
            raise ValueError("A URL está vazia")
        else:
            padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
            match = padrao_url.match(self.url)

            if not (match):
                raise ValueError("A URL não é válida")

    def acha_indice_interrogacao(self):
        return self.url.find("?")

    def get_url_base(self):
        url_base = self.url[:self.indice_interrogacao]
        return url_base

    def get_url_parametro(self):
        url_parametro = self.url[self.indice_interrogacao + 1:]
        return url_parametro

    def get_valor_parametro(self, busca_parametro):
        indice_parametro = self.get_url_parametro().find(busca_parametro)
        indice_valor = indice_parametro + len(busca_parametro) + 1
        indice_e_comercial = self.get_url_parametro().find("&", indice_valor)

        if (indice_e_comercial == -1):
            valor = self.get_url_parametro()[indice_valor:]
        else:
            valor = self.get_url_parametro()[indice_valor:indice_e_comercial]

        return valor

    def converte_moeda(self):
        valor_dolar = 5.50
        moeda_origem = self.get_valor_parametro("moedaOrigem")
        quantidade = self.get_valor_parametro("quantidade")

        if (moeda_origem == "real"):
            conversao = f"{round(((int(quantidade)) * valor_dolar), 2)} dólares"
        else:
            conversao = f"{round(((int(quantidade)) / valor_dolar), 2)} reais"

        return conversao

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return "URL: " + self.url + "\n" + "Base: " + self.get_url_base() + "\n" + "Parâmetros: " + self.get_url_parametro()

    def __eq__(self, other):
        return self.url == other.url

extrator_url = ExtratorURL("https://bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")
print(f"Tamanho da URL: {len(extrator_url)}")
print(extrator_url)
valor = extrator_url.get_valor_parametro("moedaOrigem")
print("-------------------------------------------------------------------------------------------")
print(f"Valor procurado: {valor}")
print("-------------------------------------------------------------------------------------------")
conversao = extrator_url.converte_moeda()
print(f"Conversão: {conversao}")