sabbir = [1, 2, 3, 4, 5]

# ana = len(sabbir)

# while ana > 0:
#     print sabbir[-ana]
#     ana -= 1

# first you have to define the list of "Sabbir"
# and then make another variable that is different from sabbir, that says how
# many elements are in Sabbir you can do this while using the funtion of size
# - do to this you can just "len" - and then define what list
# then we use the the while loop, and you print what list and the decrement
# and finally you say how much you want to decrement from the varible

sabbir.append("honey")

print sabbir

# append adds elements to the end, and does not distrupt the list

sabbir.insert(2, "fhkdsjf")

print sabbir

# inster insert the element in the index indicated

sabbir.pop()

print sabbir

# pop takes off the element from the end of the list

sabbir.remove(sabbir[1])

print sabbir

# removes the element that is specified in index
# append is to pop
# as instert is to remove
