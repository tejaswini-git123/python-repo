from collections import OrderedDict

def merge_the_tools(string, k):
   for index in range(0,len(string),k):
    print(''.join(OrderedDict.fromkeys(string[index:index+k]).keys()))

merge_the_tools('abcdefghij', 3)