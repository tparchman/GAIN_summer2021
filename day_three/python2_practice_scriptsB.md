# Python assignment 3

## Topics to cover
- Working with files: Input/Output
- `for` loops, processing files one line at a time.

<p>&nbsp;</p>


### Here we will get comfortable reading IN and writing OUT. We are not literally reading in the contents of entire files at once, rather we are making connections (file objects or handles) between our program and these files. For this exercise you will need to use a `for` loop to read data in one line at a time. The python_2_primer.md and slides from class should help to get you started, as should the code illustrated below (which basically walks you through this.)
<p>&nbsp;</p>


Here we will get some practice reading from and writing to files. To do this, we are going to process a fasta file (no60_intron_IME_data.fasta; located in the day_three directory on course page) containing DNA sequence data for 59,260 intron sequences. Use `less` from the command line to have a look at this file to orient yourself. You should see that each DNA sequence has two lines of information: an id line that starts with `>` and the following line which has the nucleotide sequence.

**A.** Instead of hardcoding the file name into your script, use `sys.argv` to open a file object from the command line. Create python script in the same directory where you store the data file downloaded from the course page. When you run your script, it should look something like below:

    $ python myscript.py no60_intron_IME_data.fasta

To inspire confidence and success, we will walk you through what the top of your code should look like here:

    #!/usr/bin/env python3

    import sys
    IN = open(sys.argv[1], 'r')

The above code loads the `sys` library, and opens a file handle to the file (which is the second item in sys.argv, hence the 1st list element).

**B.** Use a for loop to work through this file one line at a time. When you do that, remember to strip the line ending from each line before doing anything else to it. To convince yourself this is working the way you intend, simply print each line. When you run your script, you should see thousands of lines from the file fly by on the screen.

Your `for` loop might look something like this:

    for Line in IN:
        Line_data = Line.strip("\n")


**C.** You have learned how to use the `len` function to calculate the length of a string. Each line in this file is read in as a string, so use `len` to obtain the length of each line in your loop.

**D.** Use an incrementer to count the number of lines in the file. If you initialize a variable, say CTR = 0, outside of your loop, you can add 1 each time through your loop to count the number of times through the loop. This is very useful and commonly done, and might look like the example below.

    CTR = 0
    for Line in IN:
        Line_data = Line.strip("\n")
        CTR += 1


**E.** Now you have written code to read data from a file, one line at a time, and to do some stuff. Now lets write some of that information to an external file. In this case, we can write information each time through the loop, so the file grows as we iterate. If you figured out how to calculate the length of each line above, and your incrementer is working, you could write the line number and the length of each line to a new file you create using something like below.

You'd want to create your outfile before  you start iterating through your for loop, so that code should come above, for e.g.:

    OUT = open("outfile.txt", "w")
    
    CTR = 0
    for Line in IN:
        Line_data = Line.strip("\n")
        CTR += 1

You could then write you your file each time through the loop by adding the below line under the CTR line above.

	OUT.write("Line number: %d,Line length: %d \n" % (CTR, Line_length))

If you play with OUT.write, you might see it like printing strings, but not digits or floats. The `%` operations above specify that both variables are digits, printing them inside the quotes, and the variables are listed in parentheses in order after the `%`.    