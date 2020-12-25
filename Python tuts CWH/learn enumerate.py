# 26-10-2020
# enumerate-The enumerate() function assigns an index to each item in an iterable object 
# that can be used to reference the item later.

learning = ["web development","flutter","django",
            "flask","machine learning","artificial intellegence"]
for index,item in enumerate(learning):
    if index % 2 != 0:
        print(f"i want to learn all but for enumerate :{item}")