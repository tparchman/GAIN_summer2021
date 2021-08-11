#!/usr/bin/env python3

import sys
import re

SeqNo = 0
TEco = 0
TMse = 0
THin = 0

IN = open(sys.argv[1])
for Line in IN:
	Line = Line.strip("\n")
	if re.search("^>", Line):
		SeqNo += 1
	elif re.search("[ATCGN]", Line):
		Eco = len(re.findall("GAATTC", Line))
		Mse = len(re.findall("TTAA", Line))
		Hin = len(re.findall("AAGCTT", Line))
		TEco += Eco
		TMse += Mse
		THin += Hin

print("Total Number of Sequences: %d, EcoRI cut sites: %d, MseI cut sites: %d, HindIII cut sites: %d" % (SeqNo, TEco, TMse, THin))

IN.close()
