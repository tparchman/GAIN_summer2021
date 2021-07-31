# GAIN summer 2021; Python practice script 2A

## Topics to cover
- More string operations
- lists
- conditionals
- for loops

<p>&nbsp;</p>


## 1. This problem involves working with a DNA sequence that has some information in front of it. To start your program, type (or copy) this line into your program and assign it to a string.

    DNA_Info = 'SAMPLE_110 Pop3 atatctcgcggggtttatatatattatttaaa'

A. Get rid of everything other than the DNA sequence (using `str.replace`), and save this to another string.




B. Change the DNA sequence string to contain uppercase rather than lower case. 

C. Count the number of Gs, Cs, Ts, and As in the DNA sequence, calculate and print out the GC content of the sequence (Number of C and G bases divided by total sequence length)
<p>&nbsp;</p>


## 2. Here we are going to practice manipulating a simple list. Execute the tasks for each letter in one script and provide informative print statements to track your progress. Lets start with a single scalar:

    DNA_Seq = 'A,C,G,T,A,A,A,T,G,C,C,A,T,G,C,C,G,G,A,A,T,C,G,A,T,T,T'

<p>&nbsp;</p>

A. Work with DNA_Seq above, which is currently a string. Often you will read in large files of ',' separated values one line at a time. One way to extract items from that line (or the thousands that may follow) is to split the string based on ',' and create a list out of the line. This way, you can easily use list indeces to work on specified “columns” of data, or you can loop through the list with something like `for` in order to perform the same task on each list element. Use `str.split` to turn this string into an list where each element is something contained between the commas. Note that if you were to try to use `list()` to convert the string to a list, you would end up with commas as additional list elements.

B. Note that `.join` is the opposite of `str.split`, and can be used to turn an list back into a string. The syntax is a bit different for `.join`, where the delimiter must be specified before the `.`. This is a task you might routinely encounter. Use `.join` to turn the list you made above back into a comma delimited string.

C. Lets go back to the list you made in A. Add the additional list, specified below, to the end of the first list (essentially, concatenate the two DNA sequences together.

    SeqList2 = ['A','T','A','T','A','T','A','T','A','T','A','T','A','T','A','T','A','T','A','T','A','T']

D. Make a new list that only contains the first 10 bases of the list you made in C.
<p>&nbsp;</p>




## 3. Lets try something else with lists, `for`, and some conditional statements.

A. Make a list simple list of integers, starting with 1 and going to 100
    
    NumList=list(range(1,100))


B. Using a `for` loop, print each value, a comma, the value multiplied by 2, a comma, and the element that value occupies in the list. Each line of output should look like (for the first element, 1):

## 1, 2, 0, 
<p>&nbsp;</p>

Hints: 

	 
- You will want to increment a variable each time through the loop to record array index. See the last section of the primer for this week for an example. This is done using something like `CTR+=1` So, each time through `for` the value of CTR will grow by one. By initializing `CTR=0` outside the loop, and incrementing it inside the loop, you can correctly associate each run through the list with the correct list index (e.g., the first time through the list).



