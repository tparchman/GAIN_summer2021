#!/usr/bin/env python3


#1.
DNA_Info = 'SAMPLE_110 Pop3 atatctcgcggggtttatatatattatttaaa'

#A. replace sample info with nothing
DNA = DNA_Info.replace('SAMPLE_110 Pop3 ','' )
print(DNA)

#B. convert to uppercase
U_DNA=DNA.upper()
print(U_DNA)

#C. count number of each base, print GC content
NumberA = U_DNA.count('A')
NumberC = U_DNA.count('C')
NumberG = U_DNA.count('G')
NumberT = U_DNA.count('T')

#note, SeqLength must be float for math to work
SeqLength = float(len(U_DNA))
print('Sequence Length:', SeqLength)
GC = (NumberG + NumberC)/ SeqLength

print(GC)


#2.
#A. convert string to list
DNA_Seq = 'A,C,G,T,A,A,A,T,G,C,C,A,T,G,C,C,G,G,A,A,T,C,G,A,T,T,T'
DNA_List = DNA_Seq.split(',')

#B. Join list back into String
DNA_string = ','.join(DNA_List)
type(DNA_string)

#C. Append two lists

SeqList2 = ['A','T','A','T','A','T','A','T','A','T','A','T','A','T','A','T','A','T','A','T','A','T']
CatList = DNA_List + SeqList2
print(CatList)

# D. Make a new list that contains only the first 10 elements of SeqList2

ShortList = SeqList2[:9]
print(ShortList) 

#3. Using a `for` loop, print each value, a comma, the value multiplied by 2, a comma, the element that value occupies in the list, a comma. Each line of output should look like (for the first element, 1):

NumList=list(range(1,100))
CTR = 0
for Num in NumList:
	Num2 = Num * 2
	print(Num,Num2,CTR)
	CTR += 1	

	
	