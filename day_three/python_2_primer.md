# Python primer II, GAIN Summer 2021, day 3. 

## Topics to cover
- lists
- conditional statements: `if`, `else`, and `elif`
- `for` loops
- working with files (input/output)
- introduction to libraries (`import`, `sys`)

## Helpful materials:
- Haddock and Dunn chapter 9 and Chapter 10 pdfs (Haddock_Dunn_Chap10.pdf
Haddock_Dunn_Chap9.pdf)
- [Python for biologists](https://pythonforbiologists.com/introduction) tutorial sections:

  - [printing and manipulating text](https://pythonforbiologists.com/printing-and-manipulating-text)
  - [lists and loops](https://pythonforbiologists.com/lists-and-loops)
  - [working with files](https://pythonforbiologists.com/working-with-files)
<p>&nbsp;</p>

# 1. Lists
Lists store vectors of information, and you will commonly use them. The are convenient because they can be used with loops to execute the same blocks of code on each element.

Hardcoding lists within your scripts is good for learning, although once you start working with real data you will learn to build lists quickly on the fly. To build lists, we enclose the set in brackets. The contents of a list can be a mixture of data types, although you will usually work with lists of only one type (strings, integers, floats)

    NameList = ['Jim', 'Bob', 'Amy', 'Beth']    # list of strings
    NumList = [9, 28, 18, 83, 85]   # list of integers

List elements are accessed by their indices, 0 coming before the first list element. Rather than thinking of each element as matching its index, think of the indeces as representing the boundaries between elements. (see page 159 of Haddock and Dunn for explanation)

    List=('a', 'b', 'c', 'd', 'e')
    print(List[0])  # will print a
    print(List[2])  # will print c
 
List elements are accessed by their indices, -1 is the last list element.

    List=('a', 'b', 'c', 'd', 'e')
    print(List[-1])  # will print e
    print(List[-3:-1])  # will print ('c', 'd') 

Specifying ranges of elements is done using `:`, with indices corresponding to boundaries between elements (see page 159 of Haddock and Dunn for explanation).

    print(List[0:3])  # will print ('a', 'b', 'c')
    print(List[1:4]) # will print ('b', 'c', 'd')
    print(List[-3:]) # will print ('c', 'd', 'e')

Note, that information from strings can be similarly extracted. One difference is that you can not modify a portion of a string, but you can modify portions of a list.

    Names = "TomJoshTrevor"
    print(Names[0:3]) # prints 'Tom'
    print(Names[7:]) # prints 'Trevor'

## Useful functions for working with lists:

`list()` translates a string into a list. This is useful because lists are easy to iterate through, e.g., by using `for`

    NumString="1234533324555434343"
    NumList=list(NumString)    

`.split` splits a string by specified delimiters. This is common when you have a line of data (tab or comma delimited) and you want to make that line into a list that can be worked wiht efficiently.

    Temp="65,76,77,77,65,67,65,45,45,90,91,91"
    List_Temp= Temp.split(",")

`.join()` "joins" elements of a list into a string. Delimiter, if used, is supplied before `.join`

    Bases=['A', 'G', 'G', 'C', 'TTT', 'ATC']
    ''.join(Bases) # no delimiter, creates 'AGGCTTTATC'
    ','.join(Bases) # comma delimiter, creates 'A,G,G,C,TTT,ATC'
    String=','.join(Bases[0:4]) # comma delimiter, sends to variable String

Note that strings and lists store information in a similar manner (See Haddock and Dunn pg 164)

`range()` generates lists of integers based on starting, ending, and interval values. The simplist use is to make a list of integers with specified start and stop points. Notice that the list will end ONE integer before the stop point.

    RanList = list(range(0,9))   
    print(RanList) # [0, 1, 2, 3, 4, 5, 6, 7, 8]

Another value can be added to specify interval between integers.

    RanList = list(range(0,20,2))
    print(RanList) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

`.append()` used to add elements to the end of an list

    Breeds=['labrador', 'golden', 'flatcoat', 'chesapeake']
    Breeds.append('curlycoat') #adds 'curlycoat')

Joining two lists together is very simple, just use `+`

    List1 = ["a", "b" , "c"]
    List2 = [1, 2, 3]

    List3 = List1 + List2
    print(list3)

`del()` removes any specified elements from a list
    
    del(Breeds[:2]) #removes the first two elements

`.reverse()` reverses a list. **Note, this function doesn't return a value, it just reverses the existing list.**
 
    Bases=['A', 'G', 'G', 'T', 'T', 'T']
    Bases.reverse()
    print(Bases) # ['T', 'T', 'T', 'G', 'G', 'A']

Reversing strings is a bit less straight forward. The text below looks funny, but it does the job of reversing the string Seq. You might learn more about the meaning of the syntax later if you learn about 'slicing'.

    Seq='ATCGGGGGG'
    Rev = Seq[::-1]

# 2. `if`, `else`, `elif`

Comparison operators, such as those listed below, will return boolean values in some statements (True or False; 1 or 0). You will find yourself making regular use of these in **conditional statements**, such as `if`, `else`, and `elif`.
<p>&nbsp;</p>

| Operators | Meaning |
|---------- | ---------- |
|==  | Equal To |
|>   | Greater Than |
|>=  | Greater Than or Equal To |
|<   | Less Than |
|<=  | Less Than or Equal To |
|!=  | Not Equal |
<p>&nbsp;</p>

Logical operators, as listed below are also useful in conditional statements.

| Operator | True if |
|---------- | ---------- |
|and  | Equal To |
|or  | Greater Than |
|not  | Greater Than or Equal To |
|(not A) or B | Less Than |
|not (A or B)| Less Than or Equal To |
<p>&nbsp;</p>

### `if` is used prior to a condition being stated, and code under `if` must be indented:
    X = 4
    if (X > 3):
        print("%d is greater than 3" % (X))

### `else` is used following `if` as below
    if (X >= 3):
        print("%d is greater than or equal to 3" % (X))
    else:
        print("%d is less than 3" % (X))

### `elif` is used when multiple conditions follow the initial `if`
    Y = 3
    if (Y > 3):
        print("%d is greater than 3" % (Y))
    elif (Y == 3):
        print("%d equals 3" % (Y))
    else:
        print("%d is less than 3" % (Y))

# 3. `for`

### `for` can be used with lists, dictionaries, and even strings at some points. Unlike the conditional statements above, `for` is used to loop (or iterate) through a data structure, executing the same block of code on each item. Python uses indentation in an inflexible manner (other languages often use curly brackets with indentation optional) to set apart code inside `for` loops. **Once a loop is initiated, the code within the loop must be indented.** A common error in your python code will come from incorrect indentation. 
<p>&nbsp;</p>

### Below is an example of using `for` to loop through a string. The code below should print each base in the DNA string on its own line of output.

    DNA = "ATCGGGAAACC"
    for Seq in DNA: 
        print(Seq)

### You will often use `for` to loop through lists. The syntax is similar to above. Lets make a list of numbers and loop through it.

    RanList = list(range(0,100))   
    for Num in RanList:
        if Num%10==0:
            print ("multiple of 10: ", Num)

Notice above we are doing three things. 
- First, we are making a list of integers from 0 through 100. 
- We are then looping through that list with `for`. Note that the statement "for Num in RanList" uses an already named list. Because you are looping through that list, you need to name each element so that it can be referred to within your loop. You can name it whatever you want, here I used "Num". 
- We then put a conditional statement to print something only if that condition is met.
- `%` is the modulo operator. It returns the *remainder* of division. So 10%10 = 0, 20%10 = 0, etc., but 5%10=5.

### While looping through data structures, we will often want to use an incrementer or counter, to keep track of how far we have gone, how far we should go, or how many times we have encountered a particular object. The `+=` tool from last week can be very helpful for this.
    num_a = 0
    num_c = 0
    num_g = 0
    num_t = 0
    DNA_seq = "ATCGGGAAACCTTAAGCTAAA"
    for base in DNA_seq:
        if (base=="A"):
            num_a += 1
        elif (base=="C"):
            num_c += 1
        elif (base=="G"):
            num_g += 1
        else:
            num_t += 1
    
    print("There are %d A bases" % (num_a))        
    print("There are %d C bases" % (num_c))        
    print("There are %d G bases" % (num_g))        
    print("There are %d T bases" % (num_t))        

### Here is an example of how to simply increment a counter to keep track of how far you have gone through a list. If you start with zero, you will essentially be tracking correct list indices (because the first list element is 0)

    List=['1','2','3','4','5','6','7','8','9','10']
    CTR = 0
    for Num in List:
        print("List index is :", CTR)
        CTR += 1    


# 4. Working with Files

For almost every task you attempt with Python, you will need to 1) open and read data from existing text files; and 2) write the products of your code to new text files. Sometimes you will work with one file at a time, while other tasks will involve reading and writing to very large numbers of files. As hopefully you will see here, Python makes all of the above fairly straightforward. 
<p>&nbsp;</p>

## I. Input

Input involves several steps

- assigning the name of the file to a variable (based on its location), and opening a connection to the file (creating a file object with `open()`)
- reading the contents of the file (`.read`)
<p>&nbsp;</p>

### `open()`, along with the `r` (read) argument, can be used to open a connection (also could be called a file handle) to files stored on your computer. 

<p>&nbsp;</p>

### This can be done by 'hardcoding' the name of a file or files into your code:

If the file is in your working directory:

    IN_file=open('data.txt', 'r')

Of course, you can also use an absolute path:

    IN_file=open('/working/parchman/data.txt', 'r')

## ** Perhaps more usefully, file names can be processed from command line arguments. This is often advantageous in that the same script can be used to process different files or different sets of files without. Let's walk through how to do this below, while also giving you a preview of using python libraries/modules. 
<p>&nbsp;</p>

Command line arguments can be accessed from you code using `sys.argv`. Once you have imported the `sys` library, `sys.argv` will essentially be a list of command line arguments. `IMPORTANT NOTE`: the [1:] below skips the first argument, which is the script itself.

    import sys
    for Arg in sys.argv[1:]:       
        print(Arg)

If you had placed just the above in a script, executed that script as below:

    $ python argtest.py Lebron AD Westbrook

You should see Lebron, AD and Westbrook printed consecutively to the screen

From here, you can see that using the `open()` function to make file objects from filenames listed in sys.argv is an efficient way to access files in your code. For most cases, this strategy will be more efficient and useful than hardcoding file names into your scripts.

    import sys
    IN = open(sys.argv[1], 'r') 
    
If you provide a file name as an argument, `sys.argv[1]`, as above, the second element of that list will be the file name (remember that list indexing in Python begins with zero). So if you ran the code below, the file `data.txt` would be opened and assigned to `IN`.

	python3 read_file.py data.txt
	
	import sys
	IN = open(sys.argv[1], 'r')

<p>&nbsp;</p>

### There are a number of ways you can read data from a file object.

**What you will most often want to do is loop over the file object to read each line one at a time from the file. In other words, we will run all of our commands on the first row of the file, then we will run all of our commands on the second row, and so on. This is memory efficient, fast, and leads to simple code:**

    for Line in IN:
        print (Line)

**Once you start processing files one line at a time,  you will realize that line ending characters (`\n`) often get in the way, and can be most effectively dealt with by removing them right off the bat. We can use the `.strip` function to do this as below.**

    IN_data = IN.strip("\n")


### Another way of doing this, following Haddock and Dunn:

    IN_Name = "data.txt"
    IN = open(IN_Name, 'r')
    LineNumber = 0  ## setting to 0 to count lines while looping through the file. 

    for Line in IN:
	    Line = Line.strip('\n') #### critical, removing line ending
	    print(LineNumber, ":", Line)
	
	    LineNumber += 1 ## incrementing LineNumber to count runs through loop
	
    IN.close() #closing IN, see below.

## II. Output

Opening a file for output, and writing to that file (as opposed to printing the output to the terminal using `print`), works similarly to the examples above and also uses `open()`. With this function, we use either the "r", "w", and "a" arguments for the `open()` function to specify read, write, or append actions. For writing output from your code, we will use "w" or "a".


    OUT = open("outfile.txt", "w")
    OUT.write("Here is the data my python code processed \n")

The `.write` function above works similarly to `print`. Hence, you can write strings of text, variables, and even  variables processed by functions. A few examples below. Two important points about `.write` in how it differs from `print`. `.write()` is picky about what it will write out, preferring strings, and requiring some specific notation (examples below). Also, while `print` automatically appends line endings to statements, `.write` does not. Thus, you will need to add line endings.

    OUT.write("Here is the data my python code processed \n") # string of text, note line ending added

    OUT.write("Data: %d %f" % (VarA, VarB)) # string and variables
    OUT2.write("Data %s \n" % (Line))
    OUT3.write("%d\n" % (VarName))

Strings can be written using just a variable name, but Python doesnt like lists

    OUT4.write(Name + "\n")
	
Finally, note that you can control output with `print` as well by using unix redirect (`>`), if you only need to send output to one file.

    $ python myscript.py > output.txt

## III. Closing file connections 

It may take some experience before you realize that closing file connections when you are done with them is good form. While learning and writing straightforward scripts, you may not encounter problems when you fail to close file handles, but that will change as you ramp up what you are doing. Nonetheless, get in the habit of doing this now, and try not to forget. It is simple using the `.close()` function. While you are learning python, you will commonly want to these commands towards the end of your scripts.

    IN.close()
    OUT.close()


## IV. Processing lines, one at a time

The code below gives an example of looping through every line in a file.

	for Line in InFile:
		Line = Line.strip('\n') #removing line ending
		


### splitting a line into a workable list, extracting a range of values

After removing line endings, you will often want to split the line (which is read in as a string) into a list using `.split()`. Once the line is split, you can work on each element separately using list notation or you can loop through the list with another for loop.

    LineNumber = 0
	for Line in InFile:
		Line = Line.strip('\n')
		ElementList = Line.split('\t') #tab delimited text.
        OUT1.write(str(ElementList[1:5]))
		LineNumber += 1     # incrementing lines to keep track.

## V. Introduction to regular expressions
Thus far, we have used tools that allow pattern recognition as a basis for completing some task or file manipulation in both Unix (e.g., `grep`, `sed`, `tr`, `awk`) and Python (`str.count()`). However, our use of these tools has largely involved searching for fixed patterns. While working with biological data, and really any other form of big data, we will encounter many problems that will require more flexible match patterns. 

We will start working with regular expressions using the `re` module. As hinted above with `sys`, modules/libraries will play a major role in enabling your python code. We will cover that in more detail in a few weeks, and we will get into more detail on regular expressions next week. First, lets introduce pattern matching for regular expressions using `re` (which stands for regular expression).

To use functionality in the `re` module in your code, you want to add a line near the top of your script (just after your shebang line) that uses the `import` function. 

    import re

In general, `re` requires you to specify a pattern to match, followed by a string to match the pattern in. There are numerous functions built into `re`, but lets start here with `re.search`, which simply returns a true/false based on whether the match occurs in the string or not. The general idea is as follows:

    re.search(pattern, string)

We can search a specified string, using an `if` statement as an example of how to control our code based on the presence or absence of matches:

    Seq = "ATCGGGGCCTAGAAT"
    if re.search("TAG", Seq):
        print("Stop codon (TAG) found.\n")


The `^` character can be used to anchor the pattern at the beginning of the string, and the `$` anchors the pattern at the end
    
    Seq = "ATCGGGGCCTAGAAT"
    if re.search("^A", Seq):
        print("Seq begins with A.\n")

    Seq = "ATCGGGGCCTAGAAT"
    if re.search("T$", Seq):
        print("Seq ends with T.\n")
    else:
        print("Seq does not end with T.\n")

This is just a taste to get you started. We will cover more depth on working with regular expressions next week.


