import re

arq = open("toxins_3-5.fna","r")
seq = ""
header = arq.readline()
arqSaida = open("mRNA_toxins.fna","w")
for linha in arq:
    if (linha.startswith(">lcl")):
        dna = re.sub("T","U",seq)
        mRna=dna[::-1]
        arqSaida.write(header+mRna+"\n")
        header = linha
        seq = ""
        print (mRna)
    else:
      seq = seq+linha.rstrip()

dna = re.sub("T","U",seq)
mRna=dna[::-1]
print (mRna)
arqSaida.write(header+mRna+"\n")        
arqSaida.close()