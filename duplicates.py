n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
i=0
list_len=len(n)
new_list=[]
count=0
while i<list_len:
	j=i+1
	while j<list_len:
		if n[i]==n[j]:
			count=count+1
			if count>=1:
				if (n[i]) not in new_list:
					new_list.append(n[i])
			j=j+1
	i=i+1
print new_list
