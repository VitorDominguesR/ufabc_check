# coding:utf8


import re

obrigatorias_file = open("limitadas.txt", "w")

with open("ufabc_materias_eng_info", "r") as materias_enginfo:
        string = materias_enginfo.read().replace("\r\n"," ")
        #print(string)
        match = re.split("([0-9]{1,2}\s){4}[0-9]{2}\s", string)
        for item in match:
            #print(item)
            try:
                cod = re.match("\w{4}\d{3}\s-\s\d{2}", item).group(0).strip().replace(" ","")
                #print(cod)
                name_mat = re.sub("\w{4}\d{3}\s-\s\d{2}|((\d{1,2}\s){3}\d)", "", item).strip()
                #print(name_mat)

                #print("%s %s" % (cod, name_mat))
                obrigatorias_file.write("%s;%s\n" % (cod, name_mat))

            except Exception as e:
                pass
            # cod_mat = bytearray(item,'latin1').decode('latin1').split('\n')
            # try:
            #     cod, mat = cod_mat[0]+cod_mat[1]+ cod_mat[2], cod_mat[3:]
            # except:
            #     cod, mat = cod_mat[0] + cod_mat[1] + cod_mat[2], cod_mat[3]

obrigatorias_file.close()

