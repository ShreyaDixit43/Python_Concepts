# reading a file
# f = open('myfile.txt', 'r')
# # print(f)
# text = f.read()
# print(text)
# f.close()

#writing a file
#
# f = open('myfile2.txt', 'w')
# f.write("hello ! have some patience everything will work")
# f.close()

#append a file

# f = open('myfile3.txt','a')
# f.write("hello world!")
# f.close()

#if we do not want to use f.close() then use like this

# with open('myfile.txt','a')  as f:
#     f.write("Hey Im inside with")

#methods

#readline()
# f = open('myfile.txt','r')
# i = 0
# while True:
#     i = i + 1
#     line = f.readline()
#     if not line:
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print("marks of students {i} in Maths is :{m1}")
#     print("marks of students {i} in science is :{m2}")
#     print("marks of students {i} in sst is :{m3}")
#
#     if not line:
#         break
#     print(line)

#writelines()
# f = open('myfile2','w')
# lines = ['line1\n','line2\n','line3\n']
# f.writelines(lines)
# f.close()

# #seek()
# with open('file.txt','r') as f:
#     print(type(f))
#     #move to the 10th byte in the file
#     f.seek(10)
#
#     #Read the next 5 bytes
#     data = f.read(5)
#     print(data)

#tell()
# with open('file.txt','r') as f:
#     print(type(f))
#     #move to the 10th byte in the file
#     f.seek(10)
#
#     #Read the next 5 bytes
#     print(f.tell())
#     data = f.read(5)
#     print(data)

#truncate()
with open('sample.txt','w') as f:
    f.write('hello world')
    f.truncate(5)

with open('sample.txt','r') as f:
    print(f.read())
