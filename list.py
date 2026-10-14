list1=[34,5,6,7,89,4,3,5,6,]
list2=[4,5,6,7,8,45,56,6,]
list3=[4,5,6,"ganu",55.7,]
list4=[] #blank list create kr sakte hai
list4.append(45)
list2[4]=76 #update
print(list2,"updare value are present");
print(list1+list2,"joint kiya dono list ko")#add karge usmai
print(list4,"empty list ko 45 ki add kiya")
print(len(list2))
list3.extend(list2)
print(list3)
list1.sort()
print(list1)
