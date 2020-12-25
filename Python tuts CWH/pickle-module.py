# 9-12-2020
# pickle module
# it is a file storing format (.pkl) which is used to store the data in binary format.
# Only readable by objects and its functions
import pickle

# how to create pickle
cars = ['Ferrari', 'BMW', 'Mercedes', 'Audi', 'Aston martin']
f = "mypickle.pkl"
f_obj = open(f,'wb')
mycar = pickle.dump(cars,f_obj)
f_obj.close()

# how to open pickle
fil = "mypickle.pkl"
fil_obj = open(fil,'rb')
mecars = pickle.load(fil_obj)
print(mecars)