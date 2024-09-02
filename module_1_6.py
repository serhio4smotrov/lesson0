my_dict = {'ivan':1996,'kirill':1967,'vasiliy':1978}
print(my_dict)
print('ivan:',my_dict['ivan'],'mefodiy:',my_dict.get('mefodiy','нет такого имени'))
my_dict.update({'mefodiy':1954,'janna':2003})
print('kirill:',my_dict.pop('kirill'))
print(my_dict)
my_set = {1,1,1,1,1,4,4,False,'g','g',False}
print(my_set)
my_set.update({7,'q'})
my_set.remove('g')
print(my_set)