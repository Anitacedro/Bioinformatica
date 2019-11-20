import re

arq = open("toxins.fna")
seq = ""
header = arq.readline()
arqSaida = open("toxins_3-5.fna","w")
for linha in arq:
    if (linha.startswith(">lcl")):
        dna = re.sub("T","X",seq)
        dna = re.sub("A","K", dna)
        dna = re.sub("C","Y",dna)
        dna = re.sub("G","J",dna)

        dna = re.sub("X","A",dna)
        dna = re.sub("K","T",dna)
        dna = re.sub("Y","G",dna)
        dna = re.sub("J","C",dna)

        dnar=dna[::-1]
        print(dnar)
        arqSaida.write(header+dnar+"\n")
        header = linha
        seq = ""
    else:
      seq = seq+linha.rstrip()

dna = re.sub("T","X",seq)
dna = re.sub("A","K", dna)
dna = re.sub("C","Y",dna)
dna = re.sub("G","J",dna)
dna = re.sub("X","A",dna)
dna = re.sub("K","T",dna)
dna = re.sub("Y","G",dna)
dna = re.sub("J","C",dna)

dnar=dna[::-1]
print(dnar)
arqSaida.write(header+dnar+"\n")        
arqSaida.close()