user_sequence = input('Enter DNA sequence of 10 pairs: ')

perfect_sequence = 'AACCTTGGAA'
cancerous_sequence1 = 'AACCAAGGAA' # AA instead of TT at [4-5]
cancerous_sequence2 = 'AACCTTGCAA' # C instead of G at [7]

dna_to_binary = {
    'A': 0b00,  # A -> 00
    'C': 0b01,  # C -> 01
    'G': 0b10,  # G -> 10
    'T': 0b11   # T -> 11
}

if user_sequence == perfect_sequence:
    print("No mutations!")

def convert_sequence_to_binary(sequence):
    return ''.join([dna_to_binary[base] for base in sequence])

print(convert_sequence_to_binary(user_sequence))



