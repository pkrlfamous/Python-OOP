'''open('test.txt','r') # to read file
open('test.txt','w') # to write or create a new file and overrides existing content of the file, so use a to append
open('test.txt','a') # to append to an existing file

open('test.txt','rb') # to read binary file (image, video)
open('test.txt','wb') # to write or create a new binary file (image, video) and overrides existing content of the file, so use a to append'''


# opening a file
# try:
#     f1 = open('test.txt','r')
#     for line in f1: # reading file line by line
#         print(line, end="")
# except FileNotFoundError as e:
#     print('File not found.')
# except PermissionError as e:
#     print('Permission denied to open the file')
# except Exception as e:
#     print('Something went wrong')



# reading a file with read()
f1 = open('test.txt','r')
# print(f1.read())

# reading a single line
# print(f1.readline())

# reading in a list
# print(f1.readlines())

'''
Context Managers (Recommended):
To ensure that a file is properly closed even if an exception occurs, it's recommended to use a context manager (with statement). The file will be automatically closed when the block is exited.
'''

# with open('testfile.txt', 'r') as f:
#     print(f.read())

# writing a file, it will create a new file and overrides the existing
# data of that file, be careful

f2 = open('test2.txt', 'w')
f2.write('1\n23')
# f2.writelines([''])


# using a to append to an existing file

f3 = open('test.txt', 'a')

f3.write('\nappended it to the file')

# writing from f1 to f4
f4 = open('test4.txt', 'w')
for line in f1:
    f4.write(line)


# We can open and manipulate binary files (e.g., images, videos) using binary modes ("rb", "wb", etc.).

# using 'rb' to read an image
f5 = open('flower.jpg', 'rb')

# reading a single and all the lines of the flower.jpb
# print(f5.readline())
# print(f5.readlines())

# creating a binary file with wb
f6 = open('flower2.jpg', 'wb')


# writing the lines of flower.jpg image to the flower2.jpg image
# for lines in f5:
#     f6.write(lines)

f6 = open('flower2.jpg', 'ab')


for lines in f5:
    f6.write(lines)


f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()