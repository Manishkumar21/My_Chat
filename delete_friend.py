#from add_friend import friends
def delete(friends):

    if len(friends)==0:
        print "You have no friend currently"
    counter=1
    for temp in friends:
        print"\n\t%d\t%s" % (counter,temp.name)
        counter=counter+1
    select_friend = raw_input("\nSelect a friend :\t")
    select_friend = int(select_friend)
    i=len(friends)
    if i==0:
        print "You have No friend to Delete\n"
    else:
        temp1 = select_friend
        temp=0
        lis=[]
        while temp1<len(friends):
            friends[temp1-1] = friends[temp1]
            temp1=temp1+1
        temp1=1
        while temp < len(friends)-1:
            lis.append(friends[temp])
            print "\n\t%d\t%s"%(temp1,friends[temp])

            friends=lis

    return friends