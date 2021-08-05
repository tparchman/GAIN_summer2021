# GAIN summer 2021, Unix practice tutorial 2

**download or be prepared to use the below files from day_one/:**
passerina_sample.fastq.gz, yeast_genome.gff


## 1. Process monitoring and control, running jobs in the background.

`jot`  is a Unix command for generating strings of numbers, among other things. Use `man` to read up on `jot`. Reminder on navigating file viewing in `less`: `q` to exit, space bar will skip through the file one terminal window sized page at a time, `b` to scroll backwards. Try the following command which will print 100 random numbers:

    $ jot -r 100

You will notice that this command will print the numbers to the screen. 

- Now, increase the number of random numbers until you get to a number of replicates (think millions or more) that takes your computer an appreciable amount of time to complete. 

- Generating a long string of random numbers is useful, but you would probably rather write those numbers to file than print to screen. Modify the command above to write those numbers into a new file (which you can name whatever you want).

If you have successfully sent the numbers into a file, and if your `jot` command was still set to a very high number, then you’ve probably noticed that you can’t do anything else with your Terminal window while it’s busy working on your command. Use `^c` to stop it printing to that file, and then execute the commands again with an `&` at the end:


    $ jot –r 100000000000 > rand.numbers.txt &

The `&` will cause the job to run in the background. Thus, you will have the normal prompt back in your terminal window, and if you exit the window you will not affect the job. For big jobs that take a long time, running in the background is essential. 

What if you had the job running in the background, but you realized that you wanted to kill the process anyway? Mistakes happen a lot during the debugging process, and we assure you that you will commonly need to kill jobs (sometimes many at once).  `^c` will not work for that. Execute your `jot` command again, with the high number of replicates and running in the background. Now, use process control commands to see which jobs are running and to kill `jot`. (hint: There are multiple ways to do this, think `top`, `ps`, and `kill`)


**Note** if you inadvertently made numerous very large files as part of this exercise, be sure to remove them to reclaim disc space.

## 2. Extracting fields and sorting (`cut`, `sort`, `uniq`)

Some useful Unix commands for extracting and organizing information from text, using the yeast_genome.gff file in the [day_one page](https://github.com/tparchman/GAIN_summer2021/tree/main/day_one).

`cut`: can be used to extract fields (similar to columns in a data frame) from files. For example, the command below will extract fields 3-5 from the file `yeast_genome.gff`. In this case the delimiter, which is `tab`, is detected by default (delimiter can be specified with `- d` option). 

    $ cut -f 3-5 yeast_genome.gff > feature_info.txt


`sort` will sort lines. The action above extracted information on annotated features in the yeast genome and their coordinates. Try the below use of `sort` and inspect the output.

    $ sort feature_info.txt > sorted_feature_info.txt

`uniq` will output the unique lines in a file. Lets say we just wanted a list of the categories of genomic features represented in the yeast_genome.gff file (contained in field 3). Note what happens if you pipe the output of `cut` straight into `uniq` without using `sort`.

    $ cut -f 3 yeast_genome.gff | sort | uniq

## 3. Using Unix to explore features of a file of Illumina DNA sequencing data.

Within the directory you cloned from github for this module, make a new directory entitled "my_GAIN_Unix_Python".

Inside this directory, make three other directories (using `mkdir`) named:
- data
- scripts
- resources

locate the example file “sample_passerina.fastq.gz” from the day_one directory, and use the command line to move it into the data directory you made above. 

### Compression: 
You will notice that this file has the extension .gz and is compressed. For working with large files, you will often want to compress and decompress files using unix commands. This is much faster than one of your apple or Microsoft programs, and can be used to compress or decompress many files simultaneously.

Look at the `man` page for `gzip` and then use the correct command to decompress this file. Then, figure out how to quickly recompress the file to convince yourself that you know how to use gzip. Notice how simple and convenient this is. 

Note that if you had a directory full of 500 large .fastq files, and you wanted to compress them all at once. Very easy using a wildcard (`*`), but could take some time, so you'd want to run in the background.

    $ gzip *fastq &


## Text processing tutorial/exercises: 
This file contains raw data from an Illumina sequencer in .fastq format. Each DNA sequence is represented by four lines. An id line, which starts with “@”, followed by a line with DNA sequence, followed by another id line for the quality score, which starts with “+”, followed by quality scores for each base (dont worry about the quality score encoding for now). Note that this is a small example file. A typical file from a single lane of Illumina sequencing could contain up to 2,000,000,000 DNA sequences. That means 8,000,000,000 lines, and a very large file size. It turns out “clicking” on such files and trying to open them with your favorite text editor will not work, and is likely to crash the software and perhaps your laptop. Why would you want to try to “look” at 300 million DNA sequences anyway?

Imagine that this is data that you just got back from whatever facility you paid to do your  sequencing. The first thing you are going to want to do is look at it. Follow the steps below to use some Unix tools to learn more about this data set.

**A**. Use `man` to refresh your memory about `less`, `wc`, `grep`, `head` and `split`.

**B**.  Use `less` to look into the example file and familiarize yourself as to what these files look like (remember: exit less by typing q).

    $

**C**. Use `wc` to output 1.) the number of characters in the file and 2.) the number of lines in the file. 

    $

**D**. Now you might want to peel off just a bit of that data so that you can look at it in even more detail, maybe run it through some preliminary analyses. Now use some of the tools that you’ve learned to take the first 2,000 DNA sequences of that data file and write them to a new file (there are 4 lines per read, so that will correspond to taking the first 8000 lines). (hint: look at the `man` page for `head`, remember what ">" does.) 

    $
	
**E**. Use `man` to remind yourself of some of the command line options for `grep`. `grep` is a powerful regular expression engine, among the most commonly used commands for data science. This is a versatile command, so we better learn more. In it simplest invocation, `grep` with output every line in a file that matches the specified pattern.

Since fastq files have a standard four line format (ID starting with @, DNA sequence, quality id starting with +, and quality score), we know that every sequence has a line starting with @ associated with it. 

We can count the number of sequences (there is one ID line per sequence; ^ denotes beginning of line anchor):

    $ grep "^@" -c sample_passerina.fastq

We could write all of the ID lines to a separate file:

    $ grep "^@" sample_passerina.fastq > idlines.txt


We can print the line with a match, plus any number of lines following it:

    $ grep "^@" -A 1 sample_passerina.fastq

SDN_AM_43432 is the ID of a specific bird represented in this data set. How many DNA sequences do we have for this bird?

    $ grep "SDN_AM_43432" -c sample_passerina.fastq


**F**. This file contains DNA sequence data for 192 different individual birds. Lets say you want to know how many reads are present for a certain individual. Use `grep` to count the number of sequences for the individual named "NVP_CY_48147". You will notice here that you only need to count the id lines.

**G.** Use a similar command to extract all of the data for the same individual and write to a file. 

Hints: 
- Look at the man page and learn how to grab the 3 lines following each match (each DNA sequence entry in this file has 4 lines associated with it, starting with the id line.)
- use redirection to write STDOUT to a new file.
    






	
