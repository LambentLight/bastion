from .filesystem import *
from bastion.validators import validate_yes_no


# Make a new file system, i.e., format the disk so that it
# is ready for other file system operations.
class MKFS():
    def __init__(self, shell):
        self.shell = shell
        self.file_system = self.shell.file_system

    def run(self):
        self.file_system.initialize()


# Open a file with the given <flag>, return a file
# descriptor <fd> associated with this file.
# <flag>: 1: "r"; 2: "w"
# The current file offset will be 0 when the file is opened.
# If a file does not exist, and it is opened for "w", then
# it will be created with a size of 0. This command should
# print an integer as the fd of the file.
# Example: open foo w shell returns SUCCESS, fd=5
class Open():
    def __init__(self, shell, filename, flag):
        self.shell = shell
        self.file_system = self.shell.file_system

        # Arguments
        self.filename = filename
        self.flag = flag

    def run(self):
        return


# Read <size> bytes from the file associated with <fd>, from
# current file offset. The current file offset will move forward
# <size> bytes after read.
# Example: read 5 10 shell returns the contents of the file
# (assuming it has been written)
class Read():
    def __init__(self, shell, fd, size):
        self.shell = shell
        self.file_system = self.shell.file_system

        # Arguments
        self.fd = fd
        self.size = size

    def run(self):
        return


# Write <string> into file associated with <fd>, from current
# file offset. The current file offset will move forward the
# size of the string after write. Here <string> must be formatted
# as a string. If the end of the file is reached, the size of the
# file will be increased.
# Example: write 5 "hello, world"
class Write():
    def __init__(self, shell, fd, string):
        self.shell = shell
        self.file_system = self.shell.file_system

        # Arguments
        self.fd = fd
        self.string = string

    def run(self):
        return


# Move the current file offset associated with <fd> to a new file
# offset at <offset>. The <offset> means the number of bytes from
# the beginning of the file.
# Example: seek 5 10
class Seek():
    def __init__(self, shell, fd, offset):
        self.shell = shell
        self.file_system = self.shell.file_system

        # Arguments
        self.fd = fd
        self.offset = offset

    def run(self):
        return


# Close the file associated with <fd>.
# Example: close 5
class Close():
    def __init__(self, shell, fd):
        self.shell = shell
        self.file_system = self.shell.file_system

        # Arguments
        self.fd = fd

    def run(self):
        return


# Create a sub-directory <dirname> under the current directory.
# Example: mkdir foo
class MKDIR():
    def __init__(self, shell, dirname):
        self.shell = shell
        self.file_system = self.shell.file_system

        # Arguments
        self.dirname = dirname

    def run(self):
        # TODO: check name for '..' and say "mkdir: ..: File exists"

        # Check if directory already exists
        if self.shell.current_directory.find_child(self.dirname) is not None:
            print('mkdir: ' + self.dirname + ': File exists')
            return

        new_directory = Directory(self.shell.current_directory, self.dirname)  # create new directory
        self.shell.current_directory.add_child(new_directory)
        return


# Remove the sub-directory <dirname>.
# Example: rmdir foo
class RMDIR():
    def __init__(self, shell, dirname):
        self.shell = shell
        self.file_system = self.shell.file_system

        # Arguments
        self.dirname = dirname

    def run(self):
        # TODO: check name for '..' and say "rmdir: ..: Directory not empty"

        deletion = self.shell.current_directory.find_child(self.dirname)
        if deletion is None:
            print('rmdir: ' + self.dirname + ': No such file or directory')
            return

        self.shell.current_directory.children.remove(deletion)
        return


# Change the current directory to <dirname>.
# Example: cd ../../foo/bar
class CD():
    def __init__(self, shell, dirname):
        self.shell = shell
        self.file_system = self.shell.file_system

        # Arguments
        self.dirname = dirname

    def run(self):
        if self.dirname == '..':
            if self.shell.current_directory.parent is None:  # Directory is root
                return
            else:
                self.shell.current_directory = self.shell.current_directory.parent
                return

        move = self.shell.current_directory.find_child(self.dirname)
        if move is None:
            print('cd: ' + self.dirname + ': No such file or directory')
            return

        self.shell.current_directory = move
        return


# Show the content of the current directory. No parameters
# need to be supported.
class LS():
    def __init__(self, shell):
        self.shell = shell
        self.file_system = self.shell.file_system

    def run(self):
        for child in self.shell.current_directory.children:
            print child.name
        return


# Show the content of the file.
# Example: cat foo
class CAT():
    def __init__(self, shell, filename):
        self.shell = shell
        self.file_system = self.shell.file_system

        # Arguments
        self.filename = filename

    def run(self):
        return


# List the contents of the current directory in a
# tree-format. For each file listed, its date file
# size should be included.
# To understand this command better, you may refer
# to this command output under the command line shell
# in a Windows system.
class Tree():
    def __init__(self, shell):
        self.shell = shell
        self.file_system = self.shell.file_system

    def run(self):
        self.tree_print(self.shell.current_directory, 0)

        return

    # TODO: get tab prints to go on the same line
    def tree_print(self, directory, level):
        # tree_print iterates through each child.
        for child in directory.children:

            # if file, print based on level
            if isinstance(child, File):
                for i in range(0, level):
                    print('\t')
                print child.name

            # if directory, print based on level, call tree_print(directory, level+1)
            if isinstance(child, Directory):
                for i in range(0, level):
                    print('\t')
                print child.name
                self.tree_print(child, level+1)


# Import a file from the host machine file system to
# the current directory.
# Example: import /d/foo.txt foo.txt
class Import():
    def __init__(self, shell, srcname, destname):
        self.shell = shell
        self.file_system = self.shell.file_system

        # Arguments
        self.srcname = srcname
        self.destname = destname

    def run(self):
        return


# Export a file from the current directory to the host
# machine file system.
# Example: export foo.txt /d/foo.txt
class Export():
    def __init__(self, shell, srcname, destname):
        self.shell = shell
        self.file_system = self.shell.file_system

        self.srcname = srcname
        self.destname = destname

    def run(self):
        return
