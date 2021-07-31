# GAIN summer 2021, Python day III, practice script 3 

## Topics to cover
- Working with files: Input/Output
- More with lists
- `sys.argv`, `re.search`
- `for` loops, processing files one line at a time.

<p>&nbsp;</p>


### Today we will work a bit more with lists, input/output, and will get introduced to using regular expressions for pattern matching and extraction.  The python_3_primer.md and slides from class should help to get you started.

<p>&nbsp;</p>

1.) Read in the input file genenames.txt line by line, and add the values from the second "column" of each line to a list. This file has two columns, the second of which lists gene names. Print the list to check that your script has worked. The output should be the second "column" of the file genenames.txt.

**Hints**: You will need to use two lists, the first of which will be created by splitting each line into an list so that you can work on it. 2. You will need to ‘add’ elements to the second list (using `.append`) with each iteration of a while loop.

<p>&nbsp;</p>


2.) Here we will get process some information from a DNA sequence data. Here we are going to process a fasta file (no60_intron_IME_data.fasta) containing DNA sequence data for 59,260 intron sequences You will need to calculate some summary information for each sequence, and to write that information to a file that you are going to create in your script. 

Instead of hardcoding the file name into your script, use `sys.argv` to open a file object from the command lineWrite to an output file: 

- A. the id lines 

- B. the length of each sequence 

- C. the GC content of each sequence (remember, GC content is simply the proportion of bases in a DNA sequence that are either G or C). 

- DLastly have your program print to screen the number of DNA sequences (use incrementing, e.g., TotalSeq += 1, for each time you process a DNA sequence) in the no60_intron_IME_data.fasta file and the average GC content over all of the sequences.**

**Hints:**

1). Use a `for` loop to process the file one line at a time. You may want to remove the line endings, but then you can accomplish your goals by just working with each line as a string. 

Your `for` loop might look something like this:

    for Line in IN:
        Line_data = Line.strip("\n")

2). If you remember, `str.count('G')`, for example, can be used to count the number of Gs in a string of DNA sequence data. 

We did something like this yesterday with something like:

    DNA='ATCCCGGGCCGGGCCCAA'
    NumberG = DNA.count('G')

3). `+=` will be useful, as you will want to keep a running total of a few variables each iteration through your for loop in order to get the total counts of C and G and the total equence length necessary for calculating the GC content for ALL sequences in the file together. 

You could do this with code such as below:

    CTR = 0
        for Line in IN:
            Line_data = Line.strip("\n")
            CTR += 1

4).Each ID line starts with a ">". You will not want to perform any calculations on this line. Hence you will need to recognize lines that start with ">".  A regular expression can do that for you. Maybe something like:

    if re.search("^>", Line_data):
        #do something if the line matches the id line format
    elif re.search("^[ACTG]", Line_data)

For lines that start with A, T, C, or G, you will want to do something else.
