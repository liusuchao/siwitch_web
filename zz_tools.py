import random
import string

def get_random(count, str):
	sa = []
	for i in range(count):
		sa.append(random.choice(str))
	salt = ''.join(sa)
	return sa


def write_list(file, list):
	file_object = open(file, 'w')
	file_object.writelines(list)


a = []
for i in range(5):
	a.append(str(i)+'\n')
write_list('a.txt',a)

try : 
	s = None
	if s is None:
		print(s)
		raise NameError
	print (len(s))
except Exception as err:
	print (err)
	print (type(err))
	print ('fdfafaf')
