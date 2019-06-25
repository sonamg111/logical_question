kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
a=len(kitna_paisa_hai)
i=0
count=0
count1=0
count2=0
while i<a:
	if kitna_paisa_hai[i]>=10000000:
		count=count+1
	elif kitna_paisa_hai[i]>=100000 and kitna_paisa_hai[i]<=10000000:
		count1=count1+1
	else:
		count2=count2+1
	i=i+1
print count,"crorepati hai"
print count1,"lakhapati hai"
print count2,"diwale hai"
