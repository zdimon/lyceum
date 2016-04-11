
##Path to the interpreter.

    #!/usr/bin/env python

If you see the error “: No such file or directory” (with nothing before the colon), 
it means that your shebang line has a carriage return at the end, 
presumably because it was edited under Windows (which uses CR,LF as a line separator).

To remove the Windows line endings, you can use. 


    sed -i -e 's/\r$//' filename

--------------tt.py---------------------
                       
    #!/usr/bin/env python


    def myfunc():
        print __name__
        print 'hello'


    if __name__ == '__main__':
        myfunc()nano 

###Execution

    root@python:~/7# ./tt.py
    __main__
    hello


###Importing

--------im.py----------------------

    from tt import myfunc
    myfunc()

### Output

    root@python:~/7# python im.py
    tt
    hello

##File manipulation

###Open, close, write, delete, update operation.


The syntax is:
**file_object = open(filename, mode)** where file_object is the variable to put the
file object.


The modes can be:

**'r'** when the file will only be read

**'w'** for only writing (an existing file with the same name will be erased)

**'a'** opens the file for appending; any data written to the file is automatically
added to the end. 

**'r+'** opens the file for both reading and writing.


    >>> f = open('tt.py', 'r')
    >>> print f

###Output

    <open file '1.md', mode 'r' at 0x7fe10821f420>


###Methods

    f.write("hello world")
    cont = f.read()
    f.read()
    f.readline()
    f.readlines()
    ['hello world in the new file', 'and another line']
    f.close()
    

### Looping over the file object


    file = open('newfile.txt', 'r')

    for line in file:
        print line,


    fh = open("hello.txt", "w")
    lines_of_text = ["a line of text", "another line of text", "a third line"]
    fh.writelines(lines_of_text)
    fh.close()

Another way of working with file objects is the With statement.

It is good practice to use this statement. 

With the "With" statement, you get better syntax and exceptions handling. 


    with open("newtext.txt") as file:	# Use file to refer to the file object
        data = file.read()
        do something with data


##Using OS library

    import os

### How to get current directory

    path = os.getcwd()
    print path

### Checking file and dir existence.

    os.path.isfile(filename)
    print(os.path.isdir("/home/el"))

### get file size
    statinfo = os.stat('index.rst')
    statinfo.st_size 


### Check if directory is empty

    if os.listdir(work_path) = []:
        print 'yes'
    else
        print 'no'

    print os.listdir('.')

### Output

    ['tt.py', 'test.py', 'im.py', 'tt.pyc', 'test.pyc', 't.py']

### Removing file or dir.

**os.remove(path)** will remove a file.

**os.rmdir(path)** will remove an empty directory.

**shutil.rmtree(/folder_name)** will delete a directory and all its contents.

### Recursively walk a directory


    root = '/root'
    # dirs are the directory list under dirpath
    # files are the file list under dirpath
    for dirpath, dirs, files in os.walk(root):
        for filename in files:
            fullpath = os.path.join(dirpath, filename)
            print fullpath







