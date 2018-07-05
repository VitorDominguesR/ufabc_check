# coding:utf8


import re

obrigatorias_file = open("limitadas.txt", "w")

with open("ufabc_materias_eng_info", "r", encoding='utf8') as materias_enginfo:
        #print(repr(materias_enginfo.read()))
        match = re.findall("\w+.+\n-\n[0-9]+\n\w+.+", materias_enginfo.read())
        for item in match:
            print(item)
            cod_mat = bytearray(item,'latin1').decode('latin1').split('\n')
            cod, mat = cod_mat[0]+cod_mat[1]+ cod_mat[2], cod_mat[3]
            obrigatorias_file.write("{0};{1}\n".format(cod, mat))

obrigatorias_file.close()

