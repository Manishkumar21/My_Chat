def delete(index):
    if len(add_user['friend'][index])==0:
        print "You have no friend currently"
    counter=1
    for temp in add_user['friend'][index]:
        print"\n\t%d\t%s" % (counter,temp)
        counter=counter+1
    select_friend = raw_input("\nSelect a friend :\t")
    select_friend = int(select_friend)
    i=len(add_user['friend'][index])
    if i==0:
        print "You have No friend to Delete\n"
    else:
        temp1 = select_friend
        temp=0
        lis=[]
        while temp1<len(add_user['friend'][index]):
            add_user['friend'][index][temp1-1] = add_user['friend'][index][temp1]
            temp1=temp1+1
        temp1=1
        while temp < len(add_user['friend'][index])-1:
            lis.append(add_user['friend'][index][temp])
            print "\n\t%d\t%s"%(temp1,add_user['friend'][index][temp])
            temp=temp+1
            temp1=temp1+1
        add_user['friend'][index]=lis
    return    add_user['friend'][index]