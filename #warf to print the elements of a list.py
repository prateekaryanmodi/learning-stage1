#warf to print the elements of a  list
list_1= ["a","b","c","d","e"]
def  elem(mylist,idx=0):
    if idx==len(mylist):
        return
    print(mylist[idx],idx)
    elem(mylist,idx+1)
elem(list_1)