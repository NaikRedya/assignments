def sr(st):
   rst=''
   index = len(st)
   while index>0:
      rst+=st[index-1]
      index=index-1
   return rst
print(sr('1234abcd'))
