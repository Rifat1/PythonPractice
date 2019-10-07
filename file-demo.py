

# # f=open('file-demo.txt','r')

# # print(f.mode)
# # f.close()
# # with open('file-demo.txt','r') as f:
# #     # for line in f:
# #     #     print(line,end='')
# #     sizeToRead=10
# #     f_content=f.read(sizeToRead)
# #     print(f.tell())
# #     # while len(f_content)>0:
# #     #     print(f_content,end='*')
# #     #     f_content = f.read(sizeToRead)

# with open('file-demo.txt','r') as rf:
#     with open('file-demo-copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)

    

# def gcd(m,n):
#     if m%n==0:
#         return n
#     else:
#         return gcd(n,m%n)
# print(gcd(537,44))
val=0
def pattern(n):
    
    if n==1:
        print(str(n))
    else:
        # val=1
        # print(str(n)*n , str(pattern(n-1)))
        return (pattern(n-1),print(str(n)*n))
        
pattern(8)
