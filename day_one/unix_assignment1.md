# GAIN 2021, Introductory Unix tutorial

## Common commands: 

Below you’ll see a list of commonly used UNIX commands. You might want to use this to take notes on commands as you work through the tutorial, or just as a checklist so that you know you’ve covered all the bases.

While getting used to the idea of these commands, it is useful to note that the up and down arrow keys scroll through recently used commands, and pressing the `tab` key completes the name of a file, directory, unix command, or piece of installed software. You will want to use `tab` heavily for two reasons. 1. it will save you most of your typing time, 2. autocomplete is more accurate than your  typing.

    ls          mkdir           cd          pwd
    cp          mv              rm          rmdir 		
    cat         less            head        tail
    grep        wc              uniq	    top

## `man` pages. 
For any Unix command (there are thousands) you can find the full information on that command by using  `man`. 

    $ man pwd

This will tell you what `pwd` does, command line options, etc. Here you will see the information on `pwd` displayed in a text viewer called `less`.  `man` pages are always opened with `less`, a command for text viewing you will use regularly. You can move forward one page at a time with the space bar, and exit `less` by typing `q`.

Next, look at:

    $ man wc

You will see that `wc` in its simplest invocation counts words characters and lines, but command line options allow more. Want to know how many lines of data are in a large file? 

    $ wc -l name_of_file.txt
Try:

    $ man grep

 Upon scrolling through the `grep` man page, you will see that `grep` has many command options and is a flexible, powerful, and commonly used text processing tool. Use the `man` command to explore the functionality and command line options of the common commands listed above.

## Directory navigation. 

You can move directly to your home directory from anywhere with the two shortcuts below.

    $ cd ~

    $ cd 

Moving up into unnamed directories is easy, as below.

To move up one directory:

    $ cd ../

To move up two directories, and so on:

    $ cd ../../



You can also move a file from your directory to any directory by displaying the whole path from root (starting with / which is the top of your directory tree. That is, all directories descend from root).

The following command would move a file into the directory Macintosh HD, which all Macs have:

    $ mv <filename> /Volumes/Macintosh\ HD

Note: there is a `\ ` before HD. This is because the directory name (“Machintosh HD”) has a space in it.

In general, when making and naming directories or files in unix, you will want to avoid using spaces because they require extra typing and the `\ ` needs to be used instead of just “ “. If you have been using spaces in file or directory names, you will quickly learn that it causes headaches. You will learn from experience that the spaces in file or directory names also interfere with the efficacy of using "tab complete".

What do you think the following command will do? Try it and find out:

    $ mv ../<filename> .

“.” Represents the current directory. Anytime you `cp` or `mv` something from some distant directory (or another computer for example) to the directory you are working in, you will use “.”  as the destination directory.

You have already seen the use of `ls -l`. You might have noticed that command reported file sizes in units that were not easy to interpret. 


Take some time to move around other directories, listing their content and moving to more distant directories. Familiarize yourself with how directories are listed and organized.

Use `cd` to enter a directory\
Use `cd ../` to go back a directory\
Use `cd` (with no arguments) to jump directly to your home directory, and\
Use `cd` to jump directly to root


To quickly remind yourself of where you are in a directory tree from anywhere on your system:

    $ pwd

## Stopping jobs, exiting programs in the terminal

It is often necessary to put a stop to things that are happening in the terminal, but the means to that end can be context dependent. Here are two simple options that usually work:

`^c` will cancel a process that is running (the “^” there represents the control key)

`^z` will cancel a job but store in the background. More on this later.

`q` exits a number of programs, including less and top

## basic process monitoring (more detail later)

    $ top

Will list processes running on your machine.

Open another terminal window (`command n`) and use `less` to look at the top of a text file. Type `top` in the other terminal and look for the line showing that less is running.


 ### Try some other useful commands:

    $ whatis date
    $ whatis grep
    $ whatis less 
    $ date
    $ whoami
    $ cal


## **Unix tutorials:** Complete the first 2-3 sections of each of the below tutorials. This will help you get up to speed and or solidify introductory Unix commands.

Lastly for our first day, work through the first two sections of this tutorial to reiterate your introduction.

Useful primer from [Unix and Perl to the Rescue](http://korflab.ucdavis.edu/Unix_and_Perl/current.html), by Bradnam and Korf. Work through the beginning unix sections this morning (U1-U30). 

Also, please have a look at the excellent [tutorial from software carpentry](http://swcarpentry.github.io/shell-novice/). This morning I suggest exploring 1 through 3.
