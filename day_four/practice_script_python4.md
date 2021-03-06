# GAIN summer 2021, Python day 3, practice script 4

## Topics to cover
- Working with files: Input/Output
- `for` loops, processing files one line at a time.
- Regular expressions!
- `sys.argv`, `re.search`
<p>&nbsp;</p>

# Summarizing DNA sequence motifs in genomes‬‬‬‬‬‬
‬
Here we will work with DNA sequence data from several different species. These are coding DNA sequences, and happen to be from a bird (*Manacus vitellinus*; Manacus_vitellinus.gene.cds.fa.gz) and a pine (*Pinus taeada*; Pta.seq.uniq.gz). You can pull these from the course website (you will need to `gunzip` them). The data sets are either from whole genome or whole transcriptome sequencing projects, and represent most of the protein coding sequence.
<p>&nbsp;</p>

### **Task 1**: write a script that counts the number of restriction enzyme cut sites in the genome assemblies. For now, write the script to just process on file at a time. See below for a simple syntax example of how you might process multiple files at once by looping through `sys.argv`. We are going to look for three DNA sequence motifs that are represented by the exact DNA sequences:

- EcoRI cut site: GAATTC
- Mse1 cut site: TTAA
- HindIII cut site: AAGCTT

Print to screen or write to an outfile that contains a report with several features of this data set:

1. The total number of sequences in each file. (hint: Ctr += 1)

2. The number of EcoRI, MseI, and HindIII restriction enzyme cut sites. This will involve counting the number of exact matches for the cut site sequences in each line, and summing that over all of the lines. One of the slides from class has an example of how to keep count of multiple regular expression matches in a scalar, and another slide has an example of how to add these counts onto a total with each iteration through a for loop.
<p>&nbsp;</p>

**HINTS**

You will need to process 2 lines each round through a for loop. Below is a hint on how to do this:

	for Line in IN:
		Line = Line.strip("\n")
		Fasta = Line
	    Seq = IN.readline()
	    Seq = Seq.strip("\n")


<p>&nbsp;</p>

### **Extra optional task**: Modify you script to read in as many .fasta files as you want to feed it, and write a report file that summarizes the number of restriction enzyme cut sites as in A and the number of microsatellite repeats as in B for each input file. In this case, you want to be able to feed it the three data sets that I provided on the course website. So, you should be able to process from the command line as:

$ python cutsite_micro_multi_exportSSR.py Manacus_vitellinus.gene.cds.fa contorta_454.fa Pta.seq.uniq.fa

Because `sys.argv` is a list, you can easily loop through such a list to open and process as many files as you feed into that list. 

Here is some example syntax:

	for filename in sys.argv[1:]:
    	print(filename)
    	IN = open(filename, 'r')