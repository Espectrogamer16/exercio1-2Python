import re
import os
#codigo versão 2.0 realizado 30/09/2026
pasta_atual = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(pasta_atual, "preproinsulin-seq.txt")

with open(caminho_arquivo, "r") as arquivo:
    conteudo = arquivo.read()

print(conteudo)

limpeza = re.sub(r"ORIGIN|//|\d+|\s+", "", conteudo)
print("Sequencia um pouco mais limpa: ")
print(limpeza)
print("Tamanho da sequencia: ")
print(len(limpeza))

# Esta variável armazena a sequência completa da pré-proinsulina humana
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
                "reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

#eu vou amazenar as partes restantes da sequência da insulina

lsIsulin = "malwmrllpllallalwgpdpaaafvnqh"
aIsulin = "lcgshlvealylvcgergffytpktr"
bIsulin = "reaedlqvgqvelgggpgagslqplaleg"
cIsulin = "slqkrgiveqcctsicslyqlenycn"

insulin = (lsIsulin + aIsulin)

print("Sera aqui mostrado a sequencia incial da insulina: ")
print(insulin)

print("Sera aqui mostrado a sequencia final da insulina:",insulin + bIsulin + cIsulin)