from listmodule import ListMethods
from dictmodule import DictMethods

l = [1,2,3]
l_obj = ListMethods(l)
print(l_obj.l)
l_obj.append_list("s")
print(l_obj.l)
y = l_obj.copy_list()
print(l_obj.l)
print(y)



## Jan 30 Polymorphism Video doubts clearing section This project