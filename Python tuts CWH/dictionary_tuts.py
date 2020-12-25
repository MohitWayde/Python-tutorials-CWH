#dictionary-key value pair
#list-mutable(can change)
#tuple-immutable(cannot change)

dict={"vegetable":"bhindi",
      "device":"mobile",
      "fruit":"aamba"}
print(type(dict))
print(dict["fruit"])
del dict["fruit"]
print(dict)
dict2=dict
del dict["vegetable"]
print(dict2)
print(dict)  #thus use copy function to copy ,not do like this

# get()
# update()
#items()#display all keys 
    