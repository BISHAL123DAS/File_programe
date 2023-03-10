#--------------- write file in a python-------------

# n=open('input.txt','w') 
# n.write('i love anisha')
# # n.write("i wanna meet to you")
# n.close()
n2=open('input2.txt','w')
n2.write('i will')
n2.close()

#---------read the file-------


# f=open('input.txt')
# f1=f.read()
# print(f1)
# f.close()

# str=open('input2.txt')
# f2=str.read()
# print(f2)
# str.close()

# n3=open('input3.txt','w')
# n3.write('10 20 30 4050 50')
# n3.close()

# fq=open('input3.txt')
# fq2=fq.read()
# print(fq2)
# fq.close()

#  ------------sum of number in onother file'-------

# f=open('input3.txt')
# f1=f.readline().split()
# f.close()
# nums=[int(i)for i in f1]
# sum=0
# for i in nums:
#     sum+=i
# f2=open('output4.txt','w') 
# f2.write(str(sum))
# f2.close()   

# f=open('input3.txt','r')
# f1=f.readline().split()
# nums=[int(i)for i in f1]
# sum=0
# for i in nums:
#     sum+=i
# f2=open('input4.txt','w')
# f2.write(str(sum))    
# f2.close()

#-----this is the read the file-----

# str=open('output4.txt','r')
# f2=str.read()
# print(f2)
# str.close()

def fetch(l,ind):
    s=l[ind]
    return s
f=open('fp_input3.txt')
str1=f.readline()
f.close()
lst=str1.split()
f2=fetch(lst,3)
print(f2)   #this line can be make a error 
try:
    f2=fetch(lst,1)
    print(f2)
except:
    print(IndexError("index error"))
finally:    
    print('end') 
    f.close()       



# def fetch(l,ind):
#     s=l[ind]
#     return s

# # str1=f.readline()
# # f.close()
# # lst=str1.split()
# #f2=fetch(lst,3)
# #print(f2)   #this line can be make a error 
# try:
#     f=open('C:/Users/BISHAL/OneDrive/Desktop/python/filepython/input4.txt')
#     str1=f.readline()
#     f.close()
#     lst=str1.split()
#     f2=fetch(lst,3)
#     print(f2)
# except IndexError:
#     print("index error")
# except FileNotFoundError:
#     print("file not found")    
# finally:    
#     print('\nend\n') 
# #f.close()       


#------another-----
# def fetch(l,ind):
#     s=l[ind]
#     return s
# try:
#     res=10/0
#     f=open('C:/Users/BISHAL/OneDrive/Desktop/python/filepython/input4.txt')
#     str1=f.readline()
#     f.close()
#     lst=str1.split()
#     f2=fetch(lst,3)
#     print(f2)
# except IndexError:
#     print("index error")
# except FileNotFoundError:
#     print("file not found") 
# except ZeroDivisionError:
#     print("dividing zero")    
# finally:    
#     print('\nend\n') 
# #f.close()       

