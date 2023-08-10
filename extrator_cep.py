endereco = "Rua das Florestas 54, apartamento 555, Limoeiro, Minas Gerais, MG, 23446-699"

import re
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco)

if (busca):
    cep = busca.group()
    print(cep)