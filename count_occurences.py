char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
a=len(char_list)
i=0
new_list=[]
while i<a:
	j=0
	count=0
	while j<a:
		if char_list[i]==char_list[j]:
			count=count+1
		j=j+1
	if([char_list[i],count]) not in new_list:
		new_list.append([char_list[i],count])
	i=i+1
print new_list
