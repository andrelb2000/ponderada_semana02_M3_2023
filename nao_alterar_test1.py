import exercicio1

# test para conta_palavras_unicas
def test_conta_palavras_unicas():
    assert exercicio1.conta_palavras_unicas("banana") == 1
    assert exercicio1.conta_palavras_unicas("banana maçã") == 2
    assert exercicio1.conta_palavras_unicas("banana maçã maçã") == 2
    assert exercicio1.conta_palavras_unicas("banana maçã maçã maçã maçã maçã maçã maçã maçã maçã maçã maçã maçã maçã") == 2

