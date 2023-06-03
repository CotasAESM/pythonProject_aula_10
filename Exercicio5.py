def transcrever_para_rna_complementar(dna):
    rna = ""
    complemento = {"G": "C", "C": "G", "T": "A", "A": "U"}

    for nucleotideo in dna:
        if nucleotideo in complemento:
            rna += complemento[nucleotideo]
        else:
            rna += nucleotideo

    return rna

dna = str(input("Digite a cadeia DNA: "))
rna = transcrever_para_rna_complementar(dna)
print(rna)
