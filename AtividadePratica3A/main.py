
import argparse
import os
import re
import sys
import unittest


match    = 2
mismatch = -1
gap      = -2
seq1     = 'E'
seq2     = 'E'


arq = open("arqExemplo.fasta")
header = arq.readline()
seq1 = seq1 + str(arq.readline()).rstrip()
header2 = arq.readline()
seq2 = seq2 + str(arq.readline()).rstrip()

#print(seq1)
#print(seq2)

def comparaTamanho(u, v):
 if (len(u) != len(v)):
      raise ValueError('As sequencias precisam ser do mesmo tamanho!')
      return False
 return True

def crie_matriz_nula(n_linhas, n_colunas, valor):

	    matriz = [] # lista vazia
	    for i in range(n_linhas):
	        # cria a linha i
	        linha = [] # lista vazia
	        for j in range(n_colunas):
	            linha.append(valor)

	        matriz.append(linha)
	
	    return matriz
#print(matriz)

def create_score_matrix(rows, cols):

    matriz = crie_matriz_nula(len(seq1),len(seq2),0)

    # Fill the scoring matrix.
    max_score = 0
    max_pos   = None    # The row and columbn of the highest score in matrix.
    for i in range(1, rows):
        for j in range(1, cols):
            score = calc_score(matriz, i, j)
            if score > max_score:
                max_score = score
                max_pos   = (i, j)

            matriz[i][j] = score

    assert max_pos is not None, 'the x, y position with the highest score was not found'

    return matriz, max_pos

def calc_score(matrix, x, y):
    if(seq1[x - 1] == seq2[y - 1]):
      similarity = match
    else:
       similarity = mismatch
    #similarity = match if seq1[x - 1] == seq2[y - 1] else mismatch
    diag_score = matrix[x - 1][y - 1] + similarity
    up_score   = matrix[x - 1][y] + gap
    left_score = matrix[x][y - 1] + gap

    return max(0, diag_score, up_score, left_score)

def print_matrix(matrix):
    for row in matrix:
        for col in row:
            print('{0:>4}'.format(col))
        print()

def alignment_string(aligned_seq1, aligned_seq2):
    idents, gaps, mismatches = 0, 0, 0
    alignment_string = []
    for base1, base2 in zip(aligned_seq1, aligned_seq2):
        if base1 == base2:
            alignment_string.append('|')
            idents += 1
        elif '-' in (base1, base2):
            alignment_string.append(' ')
            gaps += 1
        else:
            alignment_string.append(':')
            mismatches += 1

    return ''.join(alignment_string), idents, gaps, mismatches

def traceback(score_matrix, start_pos):
    END, DIAG, UP, LEFT = range(4)
    aligned_seq1 = []
    aligned_seq2 = []
    x, y         = start_pos
    move         = next_move(score_matrix, x, y)
    while move != END:
        if move == DIAG:
            aligned_seq1.append(seq1[x - 1])
            aligned_seq2.append(seq2[y - 1])
            x -= 1
            y -= 1
        elif move == UP:
            aligned_seq1.append(seq1[x - 1])
            aligned_seq2.append('-')
            x -= 1
        else:
            aligned_seq1.append('-')
            aligned_seq2.append(seq2[y - 1])
            y -= 1

        move = next_move(score_matrix, x, y)

    aligned_seq1.append(seq1[x - 1])
    aligned_seq2.append(seq1[y - 1])

    return ''.join(reversed(aligned_seq1)), ''.join(reversed(aligned_seq2))


def next_move(score_matrix, x, y):
    diag = score_matrix[x - 1][y - 1]
    up   = score_matrix[x - 1][y]
    left = score_matrix[x][y - 1]
    if diag >= up and diag >= left:     # Tie goes to the DIAG move.
        return 1 if diag != 0 else 0    # 1 signals a DIAG move. 0 signals the end.
    elif up > diag and up >= left:      # Tie goes to UP move.
        return 2 if up != 0 else 0      # UP move or end.
    elif left > diag and left > up:
        return 3 if left != 0 else 0    # LEFT move or end.
    else:
        # Execution should not reach here.
        raise ValueError('invalid move during traceback')


if(comparaTamanho(seq1,seq2)):
  rows = len(seq1) 
  cols = len(seq2)
  # Initialize the scoring matrix.
  matriz, start_pos = create_score_matrix(rows, cols)
  print(matriz,start_pos)

seq1_aligned, seq2_aligned = traceback(matriz, start_pos)
alignment_str, idents, gaps, mismatches = alignment_string(seq1_aligned, seq2_aligned)
alength = len(seq1_aligned)
print()
print(' Identities = {0}/{1} ({2:.1%}), Gaps = {3}/{4} ({5:.1%})'.format(idents,
alength, idents / alength, gaps, alength, gaps / alength))
print()


