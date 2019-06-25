elements_list=[23,14,56,12,19,9,15,25,31,42,43]
index=0
elements_len=len(elements_list)
even_count=0
odd_count=0
even_sum=0
odd_sum=0
while index<elements_len:
	if elements_list[index]%2==0:
		even_count=even_count+1
		even_sum=even_sum+elements_list[index]
	else:
		odd_count=odd_count+1
		odd_sum=odd_sum+elements_list[index]
	index=index+1
print even_count
print odd_count
print even_sum
print odd_sum
