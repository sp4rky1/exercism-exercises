def to_rna(strands):
    complements = {'G': 'C',
                   'C': 'G',
                   'T': 'A',
                   'A': 'U'}
    result = ''
    for strand in strands:
        result += complements[strand]
    return result
        
