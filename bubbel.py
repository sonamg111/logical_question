list=[-2,45,0,11,9]
i=0
list_len=len(list):
while i<list_len:
	j=0
	while j<list_len:
		if list[i]<list[j]:
			c=list[i]
			list[i]=list[j]
			list[j]=c
		j=j+1
	i=i+1
print list	
