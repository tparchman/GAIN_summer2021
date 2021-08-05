# Unix primer 2

## Topics to cover

- .bash_profile or .zshrc
- text viewing and in terminal text editors
- compression, decompression
- more Unix commands, redirection
- process monitoring
- introduction to `grep`
- package installation

<p>&nbsp;</p>

## 1. `zsh` or `bash` profile

You can can customize the way a command works from shell by creating an **alias**. For example, the below command will change things so that when you type `ls`, your terminal will call `ls -lh`

    $ alias ls = 'ls -lh'

When you do this, it will only work from within a single terminal session. Once you get more comfortable in Unix, you will likely want to customize the behavior of your shell uniformly. This can easily be done by modifying a file, .profile, .zhsrc or .bash_profile, that depends on the terminal your system uses that resides in your home directory. Id suggest the following alias's, or atleast this is what I use.

    # helpful alias collection
    alias python='python3'
    alias ll="ls -laF"
    alias ls="ls -F"
    alias rm="rm -i"
    alias mv="mv -i"
    alias cp="cp -i"
   

The alias collection above has some useful features. `ll` and `ls`, when typed, will give you more complete, and/or more readable information. `rm`, `mv`, and `cp` have the `-i` option added, which is HIGHLY HIGHLY recommended. This will change the behavior of `rm`, `mv`, or `cp` to always ask if you are sure you want to remove a file, or overwrite a file with the same name in terms of `cp` and `mv`.

Since most of you are using newer apple mac laptops, you will be using the zsh terminal by default. IF you like this alias collection or want something similar, you can set in your .zshrc file as follows. These live in a hidden file in your home directory (.zshrc, the "." in front of a file hides the file from showing up with normal use of `ls`). If you have such a profile file, set alias as above within that file. 

Go to your home directory:

    $ cd ~

View hidden files:

    $ ls .*

If you dont have .bash_profile or .profile, lets make, and open with bbedit:

    $ touch .zshrc
    $ open -a bbedit .zshrc

Copy and paste the alias settings ("helpful alias settings") above into `.zshrc`, and save. OR you can just download the `.zshrc` file from under day_one in the course repository and move to your home directory (note the `.` at the beginning of the file means it will not appear with a simple use of the `ls` command)

Then, 

    $ source .zshrc

Once you quit and restart your terminal app, your new alias settings should be working, but test this out to be sure. Make a test.txt file, and use `rm` to remove it. If things are correct, you should be prompted by the terminal with "remove test.txt?". Type Y to remove, N to leave alone. Note, these settings will protect from terrible very bad accidents.
<p>&nbsp;</p>


## 2. Text viewing *OR* text editing within the terminal

### Text viewers for quickly looking at small sections of files

We will make common use of text viewers such as `less`, `head`, `tail` or `more`; especially `less`. Why would we just want to "look" and not "open" large text files? Large amounts of data stored in text are often beyond the memory capacity of GUI programs, and most of what we will work with will be far too large to "look" at anyway. `less` will allow you to have a peak at a file to understand its structure, which is ultimately what you will need to write code to manipulate and extract information. 

As `man` pages are by default viewed with `less`, look at the man page for `less` for guidance on how to control this text viewer.

    $ man less

You will use `less` regularly, a few tips:
- `q` quits
- `spacebar` moves one page forward
- `b` moves one page back
- `/` allows search, `/123` will go to instances of "123".
- after first match is found, `n` will go to the next match.

Use `less` to have a look at the top of sample_passerina.fastq file I have under day_one on the course page. You will see that DNA sequence data from an Illumina machine is stored in a structured and simple format with 4 lines of data per sequence (ID line, DNA sequence, Quality ID, quality score).

### In terminal text editors

To access and edit text *within* the terminal, there are many editors (`vim`, `emacs`, etc.) you can use. For this course, I suggest `nano`, which will be avaialable on your system. Why would you want to use a keyboard controlled only in-terminal text editor instead of something like TextWrangler? Once you start working on remote servers, the time and place for such usage will become more clear. For now, just know it exists as an option, but do not make your life harder by trying to write your first bash or python programs in `nano`.
<p>&nbsp;</p>

## 3. Compression and decompression using gzip and gunzip

Compression and de-compression are regular activities associated with large text data files, so get comfortable with it. `gzip` is a command for compressing and decompressing files. 

The compressed .gz file can be easily decompressed.

    $ gunzip sample_passerina.fastq.gz

The below command will create the compressed file "sample_passerina.fastq".

    $ gzip sample_passerina.fastq

All .txt files in a directory can be compressed (or decompressed) using a wildcard, `*` with this command. Note the below command would compress, one by one, all files ending in .txt. `*` will make your life easier.

    $ gzip *.txt 

`tar` is a unix command with more flexibility for compressing directories. We will learn more about this later.

`*` will make your life easier, and you will learn to use it in many contexts. Here is another simple example for now, which would copy all of the files starting with BS_1287 and ending in fastq.gz to a specified directory

    $ cp BS_1287*fastq.gz data_for_BS1287/

## 4. stdout, redirection (`>`)

**stdout** (standard out) is normally printed to screen when Unix commands are executed. The `cat` command below will print the entire contents of passerina.fastq to screen.

    $ cat passerina.fastq

That doesn't seem very useful in most cases. Instead, we can redirect the output of any Unix command to a file simply by using redirection. Here are some simple examples.

The below command will concatenate the data from all files in a directory ending in data.txt into one file.

    $ cat *data.txt > all_data_in_directory.txt

The use of `>>` below will write the contents of newdata.txt to the end of all_data_in_directory.

    $ cat newdata.txt >> all_data_in_directory.txt

Redirection of `ls -lh` below simply sends all that information on files in the directory to a text file.

    $ ls -lh > directory_contents.txt

The use of `grep` below will send all lines containing a match to "BS_1287" to a new file.

    $ grep "BS_1287" data_all_inds.txt > data_for_ind_BS1287.txt

## 5. Basic process monitoring 
*This is a simple start, as you use more Unix, your knowledge should expand*

`top` will display information on processes running on the machine you are logged into. Try it, read the output carefully. Doesnt matter what directory you call it from.

    $ top

`ps` will show your active process ids. Try it.

    $ ps aux | grep tparchman

If you have mutliple processes running, and want to kill one, use `kill` followed by the process ID, which you can locate with `top` or `ps`

    $ kill 9031

## 6. Regular expressions and text extraction with `grep`

`grep` is a powerful regular expression engine, among the most commonly used commands for data science. You can explore the examples below using sample_passerina.fastq, available under week1 on the [course github page](https://github.com/tparchman/BIOL792). This is an increbily versatile command, so we better learn more. In it simplest invocation, `grep` with output every line in a file that matches the specified pattern.

Since fastq files have a standard four line format (ID starting with @, DNA sequence, quality id starting with +, and quality score), we know that every sequence has a line starting with @ associated with it. 

We could write all of teh ID lines to a separate file:

$ grep "^@" -c sample_passerina.fastq > idlines.txt

We can cound the number of sequences:

$ grep "^@" -c sample_passerina.fastq

We can print the line with a match, plus any number of lines following it:

grep "^@" -A 1 sample_passerina.fastq

SDN_AM_43432 is the ID of a specific bird represented in this data set. How many DNA sequences do we have for this bird?

$ grep "SDN_AM_43432" -c sample_passerina.fastq



## 7. Package installation

This is a bit extra for what we are doing in the GAIN module, but I thought I would add it here as a guide for those interested. For installing on your personal mac computers, `brew` will be your most convenient option. I would stress here that this type of package installer/manager makes accomplishing these tasks in the Unix OS incredibly easy.

**B. Unix on Mac Unix systems**

`homebrew` manages and installs packages on Mac OS Unix. 
To install brew (homebrew):

    $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

`brew` is pretty easy to use. To look at a list of commands and their uses:

    $ brew help

To search for an installable program:

    $ brew search

To install a package:

    $ brew install packagename

As a simple example, lets install a more useful version of `top`, `htop`, that has some expanded information and visuals. Using brew is quite easy, as you can see.

    $ brew install htop

A more detailed, yet basic, tutorial can be found below. As with the above, carefully review before using.

- https://wpbeaches.com/installing-homebrew-on-macos-big-sur-11-2-package-manager-for-linux-apps/

**B. Linux distributions:**

`apt` is a package management system for most Linux distributions. It facilitates the installation, management, updates, and removal of software. Using apt-get requires superuser privileges (`sudo`), and will require password entry.


You can find useful tutorials on `apt` and `apt-get` below. We suggest reviewing information, and familiarizing yourself with `sudo` carefully before using.

- https://phoenixnap.com/kb/how-to-use-apt-get-commands
- https://itsfoss.com/apt-get-linux-guide/
- https://www.control-escape.com/linux/lx-swinstall.html


To install software using `apt-get`:

    $ sudo apt-get install <package_name>

To remove software using `apt-get`:

    $ sudo apt-get remove <package_name> 

Note, the above doesnt remove configuration files associated with a package. To remove the package along and configuration files:

    $ sudo apt-get purge <package_name> 




