 import exercicio2

# função test para is_anagram
def test_is_anagram():
    assert exercicio2.is_anagram("banana", "banana") == True
    assert exercicio2.is_anagram("banana", "maçã") == False
    assert exercicio2.is_anagram("amor", "roma") == True
    assert exercicio2.is_anagram("pedra", "padre") == True
    assert exercicio2.is_anagram("pedra", "pedro") == False
    assert exercicio2.is_anagram("perda", "pedra") == True
    assert exercicio2.is_anagram("perda", "pedro") == False
    assert exercicio2.is_anagram("perda", "padre") == True