# File Read-Write operation in Pyhton :
# File-Open()
# File- Read(): r
# File- Write(): w
# File- Read-Write: w+
# File- Append: a
# File- Close()
# Now Let's Start our File operations............
print(".......File Related Operations in Python........")
file_ = 'file_operations.txt'


# ... Read & Write - Mode('r+') of the File: ...
f_cmd_prs = open(file_, 'r+')  # opening ftext-ile read('r') along with write('w') mode
f_cmd_prs.write("For R+ mode, this is the another Line is written. ")
# print("In R+ Mode:", f_cmd_prs.read())
f_cmd_prs.close()

# ... Write Mode within File ...
f_cmd_prs = open(file_, 'w')  # opening file in write('w')-mode
# The below line will be newly written within the text-file('file_operations.txt')
# no_chars-variable(below) stores total how many letters/characters  and white space are available
no_chars = f_cmd_prs.write("Hello, This is the 1st Line in File (May be overwritten). \n")

# Now Terminate File-ops (closing the file)
f_cmd_prs.close()

# ...Append-Mode (write after existed line & don't overwrite) File ...
f_cmd_prs = open(file_, 'a')  # opening file in read('r')-mode
f_cmd_prs.write("This Line is appended after the existed Line(if any) of the File.")
f_cmd_prs.close()

# ....Opening File in Read Mode....
f_cmd_prs = open(file_, 'r')  # opening file in read('r')-mode
print("File Reading Mode-read():\n", f_cmd_prs.read())
f_cmd_prs.close()


# ..............Now shortcut technique applying with files..........
print("\n\t========= All Lines as a list(not Recommended) readlines()=======")
f_cmd_prs = open(file_, 'r')  # opening file in read('r')-mode
f_cmd_prs.seek(0)  # Takes Line form 0-th(initial character)
print(f_cmd_prs.readlines())

print("\n\t========= All Lines in a new line using loops =======")
f_cmd_prs.seek(0)  # Takes Line form 0-th(initial character): Needed when return empty list
for single_line in f_cmd_prs:
    print(single_line)
f_cmd_prs.close()

print("\n\t ======Without File closing and opening facilities: with open technique======\n")
with open(file_, 'r') as f_ops:
    lines_ = f_ops.read()
    print(lines_)


