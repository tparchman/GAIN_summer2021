# GAIN summer 2021, Python primer I

## Topics to cover

- Getting started
- First python program
- Variables: strings and pythons
- The interactive prompt

# Why Python ?

The idea of this course is to introduce scientists without any, or much, prior programming experience to a language that can be useful for their needs. The choice of the first programming language to learn may not be as important as you think; once you have learned one, learning additional languages will be much much easier, and you are nearly guaranteed to utilize additional languages at some point in your career. Nonetheless, the two scripting languages that have been most heavily used in bioinformatics and data science are **Perl** and **Python**. There are a number of reasons that Python has become the ideal language to learn first for data science:

- It is one of the most common languages used in biology and other fields of science. Thus, you will be able to find a lot of documentation, guidance, examples, and opinion on the web.
- It has excellent capabilities for manipulating text, suiting it well to bioinformatics and data science.
- It uses consistent syntax, which makes learning specific code relatively easy.
- It has many built in libraries to facilitate common tasks.
- Python is very widely used, across science and inustry. 

<p>&nbsp;</p>

# Getting started with Python. 

## Topics to cover
- installing/updating python
- writing your first python script(s), `print` statements
- working with strings and integers
- controlling float precision
- using the interactive prompt to test code in the terminal
- `help()` and `dir()`

<p>&nbsp;</p>

# 1. Installing/updating to python 3 current version
We are going to start slow and basic with Python, attempting to insure that everyone stays on board. First we are going to make sure everyone has the most recent version installed on their machine. While doing this, we are going to take a slight detour to learn how incredibly easy it can be to download and install packages for Unix commands or programs that are not installed in the base system. For this, we will demonstrate the use of `brew`, which is command line utility for locating, downloading, and installing Unix packages on Mac computers.

First check to see if you have python3 installed.  Open the shell and type

    $ python --version

If you get anyting that looks like version 2 not 3 or if you get an error that you dont have python. Then you will need to install version 3.


## Installing or updating Python on Mac Unix using homebrew

If you have already installed Homebrew - you dont need to do this. Check if you have it:

    $ which brew
  
If you dont have `brew`, then:

    $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Then install python3 

    $ brew install python3

**For more depth on homebrew and using the `brew` command to install and update packages in your Unix system, see section 7 of  [unixII_primer.md](https://github.com/tparchman/GAIN_summer2021/tree/main/day_one/unixII_primer.md).


### Python downloads, also useful potentially 
Go to python.org and download the latest release

    https://www.python.org/downloads/mac-osx


## Installing or updating Python on Ubuntu
It is probably already installed but if not try with the package manager `apt-get`

    $ sudo apt-get install python idle
<p>&nbsp;</p>
	
# 2. Writing your first python program

As with shell scripts, the first line of python scripts should be the shebang followed by the location of python:

    #!/usr/local/bin/python3

If you are unsure where you installed python3, you can easily figure out where it is:

    $ which python3


As covered in Haddock and Dunn, pg 127, you can also use the below as your first line. This allows you to send script to `env` first, which should then locate python3, wherever it resides.

    #!/usr/bin/env python3

Either of the above will do, and are important **IF** or when you wish to convert your scripts to executable. If you want to do this, change the file mode: 

    $ chmod u+x first_python.py

And run as follows:

    $ ./first_python.py

## Your first simple program, using a `print` statement.

Sending information from your python scripts to stdout is accomplished with the `print` statement. Our first script will simply illustrate how we print specified text, and will serve to convince you that writing python code might not be that hard. Use `touch` to make a blank text file, but give it a `.py` extension as is customary for python scripts. This script needs only two simple parts. First, your customary first line that should go in all of your scripts, which should be:

    #!/usr/bin/env python3
Or the path to the specific location where python lives:

    #!/usr/local/bin/python3

To illustrate the use of `comment` text, marked with `#`, lets add a comment that is for you to read, not python. 

    #this is a comment: testing my first program with a simple print statement

Note the line above will not be part of the interpreted code. Instead, you can make use of `#` to leave annotations for yourself or others in your code to explain what you are doing.

Now lets add a print statement:

    print("Im ready to learn python, and this is my first step")

You can now run your program in two ways. Simply (which we strongly recommend for this class):

    $ python3 first_script.py 

Or, change to executable, then run:

    $ chmod u+x first_script.py
    $ ./first_script.py

If all is in order, "Im ready to learn python, and this is my first step" should print to the screen, and you are ready for more.
<p>&nbsp;</p>

# `#`: comment character, annotating your code.
Anytime you use `#`, the rest of the line will be 'commented out'. This means python won't interpret what you write, and that you can write notes or annotations on what your code is doing, to help yourself and others. Make heavy use of this, and when you go back to old or strange code, you will know why you did what you did. When others make good use of this, you can learn more about why/how they did what they did. Use `#` frequently, especially in the early phases of learning python.

In example code below and in other primers, I have put comments to describe some code using `#`.

    print ("This is python code")  # this is a comment to describe the left

<p>&nbsp;</p>

# 3. Working with scalars (strings, integers, floats, etc.)
Chapter 8 of Haddock and Dunn does a nice job of walking you through a script that codes and performs various actions on strings and integers (both types of scalar variables). Lets use that example to cover a few aspects of working with strings and integers in python, including:

- some useful built-in string functions
- basic mathematical operations
- using the interactive prompt to test simple code, get help, etc. (`help()`, `dir()`)
- controlling string formatting with `%`
<p>&nbsp;</p>

## 3A. Strings 
Strings can be specified and assigned easily within scripts as below. Note that `"` or `'` can be used to enclose strings, and strings not enclosed will return undefined.

    Team = "lakers"
    Seq_one = "actgaaa"
    Seq_two = "ATCGAA"
    Seq3 = 'atcGGGC'

Strings can be concatenated with `+`:

    Seq_one_two = Seq_one + Seq_two
    print("concatenation example: ", Seq_one_two)

Strings can be repeated with `*`:

    Seq_one_times3 = Seq_one * 3
    print("repeat by multiplier example: ", Seq_one_times3)



### Python has a diverse array of string methods (these are built in functions), that allow efficient work with strings. A few examples below will illustrate the syntax for using these methods.
<p>&nbsp;</p>

`str.upper()` will convert string to uppercase:

    Seq_one_big = Seq_one.upper()

`str.lower()` will convert string to lowercase:

    Seq_one_lower = Seq_one_big.lower()

`str.replace()` will replace a specified character with a different specified character. The code below will replace "a" with "g":

    NewSeq_one = Seq_one.replace("a","g")
    print ("Use of str.replace: ", NewSeq_one)

 `str.count()` will return a count of occurences for a specific character:

    Counta_Seq_one = Seq_one.count("a")
    print ("Use of str.count: ", Counta_Seq_one) 

 `str.isalnum()` will return *True* if all characters are alphanumeric, *False* if not.

    Seq_one_alphanum_test = Seq_one.isalnum()
    print ("Use of str.isalnum: ", Seq_one_alphanum_test)

<p>&nbsp;</p>

## 3B. Basic mathematical operations
Basic mathematical operations work mostly as expected, and can be usefully tested using interactive prompt from the terminal (see below).  


| Arithmetic | Operators |
| ----------- | --------- |
| +  |  Addition |
| - |   Subtraction |
| * |   Multiplication |
| / |   Division |
| // |  Floor Division |
| % |   Modulo |
| ** |   Power |


<p>&nbsp;</p>

Comparison operators, such as those listed below, can return boolean values in some statements (True or False; 1 or 0). You will find yourself making regular use of these in conditional statements, such as `if`, `if else`, etc.

| Comparison | Operators |
|---------- | ---------- |
|==  | Equal To |
|>   | Greater Than |
|>=  | Greater Than or Equal To |
|<   | Less Than |
|<=  | Less Than or Equal To |
|!=  | Not Equal |

<p>&nbsp;</p>

Most basic mathematical operations work in an unsurprsing manner.

    Num1 = 5
    Num2 = 7
    Sum = Num1 + Num2
    Prod = Num1 * Num2
    Dif = Num1 - Num2
    Div = Num1 / Num2
    Mod = Num2 % Num1
    print (Sum, Prod, Dif, Div, Mod)

If you use the code above in a script, or more efficiently, test it out with the interactive prompt (see below), the print statement should illustrate the expected behavior of the math statements above. **Note that "Div" (5/7) returns a float with many digits past the decimal (0.7142857142857143). This is an overkill level of precision for some uses, and you will often want to control float precision for tidiness.** We will cover that type of control below.

<p>&nbsp;</p>

# 4. Strings, Scalars, and Integers. How to specify, how to know what a scalar variable is.

## 4A. Checking variables
If you arent sure whether a variable is an integer, string, or float, you can easily check using the `type()` function.

    Var = 1.2
    type(Var)     # will return <class 'float' >

    Var = 12
    type(Var)     # will return <class 'int'>

    Seq = 'atcgaaa'
    type(Seq)       # will return <class 'str'>

If you want to change among variables, you have some options with the `float`, `int`, and `str` functions.

    Var = 1.2
    Svar = str(Var)      # makes Svar="1.2", a string
    type(Svar)
    Nvar = float(Svar)      # makes Nvar=1.2, a float

## 4B. `%` operator: controlling format of scalars in print statements 

### In print statements, the first `%` is used as a placeholder that denotes what type of variable is to be specified:  **%d for integer, %f for float, and %s for string**. After the quoted statement, the second `%` is used before the variable name is provided in (). %f is also used to specify the number of digits after a decimal (see below).

Have a look at the examples in Haddock and Dunn. Here are a few more. The first uses a string assigned to the variable name within the print statement.

    Name='Lebron'
    print("38 points, 10 assists, 16 rebounds for %s" %(Name))
    # will print: 38 points, 10 assists, 16 rebounds for Lebron

The example below stores three integers. They are each separately printed within quotes in the print statement, using `%d` notation for each. Note, that the order of those variables is then 

    P=38
    A=10
    R=16
    print("%d points, %d assists, %d rebounds for Lebron" %(P, A, R))
    # will print "38 points, 10 assists, 16 rebounds for Lebron"


In python, floats can be represented with full precision, or controlled to a set number of positions. The latter will often be desirable to keep things tidy. The statements below will print 0.6666666666666666.

    Prod = 2/3
    print ("2/3 should equal roughly %.3f" % (Prod))
    # This will print "2/3 should equal roughly 0.667"

# 5. `input()` allows user input
Use of this function allows user input from the command line while a program is being exectuted. For example, the with the code below in a script, 'enter value between 1 and 10:' will be printed to the terminal, and a value entered can then be assigned to that variable within the program.

    X = input('enter a value between 1 and 10')
    print("The entered value was " + X)

# 6. A useful feature of python is the interactive prompt, which you can invoke by simply typing python (or python3, depending on your set up), as below. The interactive prompt can be used to test statements or blocks of code outside of your scripts, and/or to get help (`help()`, `dir()`)

    [tparchman@Thomass-MacBook-Pro python1]$ python
    Python 3.8.5 (default, Aug 16 2020, 12:28:59) 
    [Clang 9.0.0 (clang-900.0.39.2)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 

 You can usefully use the interactive prompt to test statements or operations while you are writing scripts. Some find it useful to keep the interactive prompt open next to their text editors while writing python code (Haddock and Dunn page ). Follow the example below, which demonstrates the use of +=.  

    >>> a = 7
    >>> a += 7
    >>> a
    14  

Here is another example, where I am demonstrating string assignment, and the use of `str.replace`:

    >>> Seq='ATCGGGGGGG'
    >>> Rep_Seq = Seq.replace('G','T')
    >>> print(Rep_Seq)
    ATCTTTTTTT

Finally, have a look at what happens when the code you are trying ISN'T right. Below, a string is not formatted correctly in the variable assingment statement.

    >>> Seq= ATCGCCCCC
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    NameError: name 'ATCGCCCCC' is not defined

In another example, I forgot to place parentheses around the variable which I am sending to the `print` function. Note here that the `^` is helpfully placed as a suggestion of where the error is coming from, and the correct syntax is suggested in the `SyntaxError` statement.

    >>> print Rep_Seq
    File "<stdin>", line 1
    print Rep_Seq
          ^
    SyntaxError: Missing parentheses in call to 'print'. Did you mean print(Rep_Seq)?

Note, for the examples shown above in sections 3A and 3B could be tested using the interactive prompt.
<p>&nbsp;</p>

### 5B. The interactive prompt is also useful for using `help()` and `dir()`. Try these with a few functions, you will quickly see the usefulness.
<p>&nbsp;</p>

### `help()` will print manual page descriptions of the function placed in parentheses. 

    >>> help(print)

    Help on built-in function print in module builtins:

    print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

<p>&nbsp;</p>

### `dir()` returns all properties and methods associated with the specified variable. Below the function is being used with a string.
    Name='Costanza'
    dir(str)
    ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']


<p>&nbsp;</p>
<p>&nbsp;</p>


# Python documentation and other useful resources. 

I strongly recommend you explore several of the below resources and tutorials.

[Python documentation](https://www.python.org/doc/)

[Python for Biologists](https://pythonforbiologists.com/introduction)

[Learn Python Interactive - has built in interpretter](https://www.learnpython.org/)

[Python guru - excellent, also has built in interpretter](https://thepythonguru.com/)

<p>&nbsp;</p>

### If you are using Haddock and Dunn text, be aware that it is based on python2, and there are some important differences between python2 and python3 (syntax changes that will require slight modification of book examples)

1. print statements in python3 should use (). 
2. `raw_input()` has become just `input()`