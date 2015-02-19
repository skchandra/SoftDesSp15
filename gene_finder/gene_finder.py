# -*- coding: utf-8 -*-
"""
Created on Mon, Jan 26, 2015

SHIVALI CHANDRA

"""
from amino_acids import aa, codons, aa_table
import random
from load import load_seq

def shuffle_string(s):
    """Shuffles the characters in the input string"""
    return ''.join(random.sample(s,len(s)))

def get_complement(nucleotide):
    """Returns the complementary nucleotide
    >>> get_complement("A")
    'T'
    >>> get_complement("C")
    'G'"""
    if nucleotide == 'A':
        return 'T' 
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence

    >>> get_reverse_complement("ATGCCCGCTTT")
    'AAAGCGGGCAT'
    >>> get_reverse_complement("CCGCGTTCA")
    'TGAACGCGG'"""
    rev_dna = (dna[::-1])
    rev_comp_dna = []
    for c in rev_dna:
        rev_comp_dna.append(get_complement(c))
    return ''.join(rev_comp_dna)

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    Adding unit test to ensure that it returns the entire string if no frame stop codon
    >>> rest_of_ORF("ATGTGAA")
    'ATG'
    >>> rest_of_ORF("ATGAGATAGG")
    'ATGAGA'
    >>> rest_of_ORF("ATGAGATACCCC")
    'ATGAGATACCCC'
    """
    for i,n in enumerate(dna):
        if n == 'T':
            codon = dna[i:i+3]
            if i%3 == 0 and (codon == 'TAG' or codon == 'TGA' or codon == 'TAA'):
                dna = dna[0:i]
    return dna

def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
        added another unit test to check a non-nested ORF example
    >>> find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")
    ['ATGCATGAATGTAGA', 'ATGTGCCC']
    >>> find_all_ORFs_oneframe("ATGATGATGTGA")
    ['ATGATGATG']
    """
    x = 0 
    orfs = []
    length = len(dna)
    while x < length:
        if dna[x:x+3] == 'ATG':
            orf = rest_of_ORF(dna[x:])
            x = x + len(rest_of_ORF(dna[x:]))
            orfs.append(orf)
        else:
            x += 3
    return orfs

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs

    >>> find_all_ORFs("ATGCATGAATGTAG")
    ['ATGCATGAATGTAG', 'ATGAATGTAG', 'ATG']
    """
    orfl = []
    orfl.extend(find_all_ORFs_oneframe(dna))
    orfl.extend(find_all_ORFs_oneframe(dna[1:]))
    orfl.extend(find_all_ORFs_oneframe(dna[2:]))
    return orfl

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """
    orfbs = []
    orfbs.extend(find_all_ORFs(dna))
    orfbs.extend(find_all_ORFs(get_reverse_complement(dna)))
    return orfbs

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    """
    both_s = find_all_ORFs_both_strands(dna)
    return max(both_s,key=len)

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    longl = []
    for i in range(num_trials):
        dna = shuffle_string(dna)
        longl.append(longest_ORF(dna))
    return max(longl,key=len)

def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment

        >>> coding_strand_to_AA("ATGCGA")
        'MR'
        >>> coding_strand_to_AA("ATGCCCGCTTT")
        'MPA'
    """
    amino_acid = []
    for i in range(0,len(dna)-2,3):
        codon = dna[i:i+3]
        if codon in aa_table: 
            amino_acid.append(aa_table[codon])
    return ''.join(amino_acid)

def gene_finder(dna):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    longest = len(longest_ORF_noncoding(dna,150))
    all_orfs = find_all_ORFs_both_strands(dna)
    aa_list = []
    for n in all_orfs:
        if len(n) > longest:
            aa_list.append(coding_strand_to_AA(n))
    return aa_list

dna = load_seq("./data/X73525.fa")
print gene_finder(dna)

if __name__ == "__main__":
    import doctest
    doctest.testmod()