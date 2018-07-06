#coding: latin1

import xml.etree.cElementTree as ET

tree = ET.parse('ficha.xml')

root = tree.getroot()

obrigatorias = {}
limitadas_dict = {}

with open('obrigatorias.txt', 'r') as obrig_file:
    for line in obrig_file.readlines():
        cod, mat = line.decode('utf8').split(';')
        obrigatorias[cod] = mat.strip()

with open('limitadas.txt', 'r', ) as limitadas:
    for line in limitadas.readlines():
        cod, mat = line.decode('utf8').split(';')
        limitadas_dict[cod] = mat.strip()

materias_covalidadas = ["BCL0308-15", "BCL0306-15", "BIJ0207-15", "BIL0304-15", "ESTA003-17", "ESTI016-17", "ESTO011-17"]

for materia in materias_covalidadas:
    try:
        obrigatorias.pop(materia)
    except:
        limitadas_dict.pop(materia)


discp_feitas = {}

for child in root.findall('Disciplina'):
    cod_discp_feita = child.find('codigo').text
    nome_discp_feita = child.find('disciplina').text
    if (cod_discp_feita in obrigatorias.keys() or nome_discp_feita in obrigatorias.values()) and child.find('situacao').text != "Reprovado":
        #print(child.find('disciplina').text)
        discp_feitas[cod_discp_feita] = nome_discp_feita
    elif (cod_discp_feita in limitadas_dict.keys() or nome_discp_feita in limitadas_dict.values()) and child.find('situacao').text != "Reprovado":
        #print(child.find('disciplina').text)
        discp_feitas[cod_discp_feita] = nome_discp_feita
    elif child.find('situacao').text != "Reprovado":
        print("Nao consta: %s"%nome_discp_feita)


discp_feitas_count = 0

print("Discp Feitas")
for key, value in discp_feitas.items():
    print("%s %s"%(key, value))
    discp_feitas_count +=1
print("Total: %s" %discp_feitas_count)


print("\nDisciplinas obrigatorias nao feitas")
count=0
for key, value in obrigatorias.items():
    if key not in discp_feitas.keys() and value not in discp_feitas.values():
        print("%s %s" % (key, value))
        count+=1

print("Total: %s" %count)

print("\nDisciplinas limitadas nao feitas")
count = 0
for key, value in limitadas_dict.items():
    if key not in discp_feitas.keys() and value not in discp_feitas.values():
        print("%s %s" % (key, value))
        count += 1

print("Total: %s" %count)