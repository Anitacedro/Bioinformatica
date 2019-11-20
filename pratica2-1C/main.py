import re
arq = open("mRNA_toxins.fna")
seq = ""
amino = []
header = arq.readline()
arqSaida = open("toxins.faa","w")
alfabetoAminoacido = {
"UUU":"phenylalanine",
"UUC":"leucine",
"UUA":"leucine",
"UUG":"leucine",
"CUU":"leucine",
"CUC":"leucine",
"CUA":"leucine",
"CUG":"leucine",
"AUU":"isoleucine",
"AUC":"isoleucine",
"AUA":"isoleucine",
"AUG":"methionine",
"GUU":"valine",
"GUC":"valine",
"GUA":"valine",
"GUG":"valine",
"UCU":"Serine",
"UCC":"Serine",
"UCA":"Serine",
"UCG":"Serine",
"CCU":"Proline",
"CCC":"Proline",
"CCA":"Proline",
"CCG":"Proline",
"ACU":"Threonine",
"ACC":"Threonine",
"ACA":"Threonine",
"ACG":"Threonine",
"GCU":"Alanine",
"GCC":"Alanine",
"GCA":"Alanine",
"GCG":"Alanine",
"UAU":"Tyrosine",
"UAC":"Tyrosine",
"UAA":"Stop",
"UAG":"Stop",
"CAU":"Histidine",
"CAC":"Histidine",
"CAA":"Glutamine",
"CAG":"Glutamine",
"AAU":"Asparagine",
"AAC":"Asparagine",
"AAA":"Lysine",
"AAG":"Lysine",
"GAU":"Aspartic acid",
"GAC":"Aspartic acid",
"GAA":"Glutamic acid",
"GAG":"Glutamic acid",
"UGU":"Cysteine",
"UGC":"Cysteine",
"UGA":"Stop",
"UGG":"Tryptophan",
"CGU":"Arginine",
"CGC":"Arginine",
"CGA":"Arginine",
"CGG":"Arginine",
"AGU":"Serine", 
"AGC":"Serine",
"AGA":"Arginine",
"AGG":"Arginine",
"GGU":"Glycine",
"GGC":"Glycine",
"GGA":"Glycine",
"GGG":"Glycine"
}
for linha in arq:
    if (linha.startswith(">lcl")):
        mRna = re.sub("T","U",seq)
        #print(mRna)
        aminoacido=mRna[::-1]
        aminoacidotres = re.findall('.{1,3}', aminoacido)
        
        for sequencia in aminoacidotres:
          #print(sequencia)
          for chave,valor in alfabetoAminoacido.items():
            #print(sequencia)
            if(sequencia in chave):
              amino.append(valor+",")
          
        
        arqSaida.write(header+str(amino)+"\n")
        header = linha
        seq = ""
        
    else:
      seq = seq+linha.rstrip()


mRna = re.sub("T","U",seq)
aminoacido=mRna[::-1]
aminoacidotres = re.findall('.{1,3}', aminoacido)
for sequencia in aminoacidotres:
   for chave,valor in alfabetoAminoacido.items():
      if(sequencia in chave):
        amino.append(valor+",")
        header = linha
arqSaida.write(header+str(amino)+"\n")        
arqSaida.close()
