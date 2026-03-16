lst=['apple','banana','mango']
print("length of the list is:",len(lst))
print(lst[0])
print(lst[1])
print(lst[2])
print(lst[-1])
lst.append('grapes')
print(lst)
lst.remove('banana')
print(lst)
lst.sort()
lst.pop(-1)
print(lst)
lst.reverse()
print(lst)
my_dict={'name':'mini','age':20,'city':'islamabad'}
print(my_dict['name'])
print(my_dict['age'])
print(my_dict['city'])
my_dict['age']=21
print(my_dict)
my_dict['city']='Lahore'
print(my_dict)
def test(list):
    result={}
    for item in list:
     result [item [0]]=item[1:]
    return result
my_list=[[1,'sara','grade2'],[2,'nimra','grade4'],[3,'esha ','grade 8']]
print(test(my_list))




