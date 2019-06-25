elements_list=[23,14,56,12,19,9,15,25,31,42,43]
index=0
elements_len=len(elements_list)
even_sum=0
odd_sum=0
average=0
average1=0
while index<elements_len:
	if elements_list[index]%2==0:
		even_sum=even_sum+elements_list[index]
	else:
		odd_sum=odd_sum+elements_list[index]
	index=index+1
average=even_sum/elements_len
average1=odd_sum/elements_len
print odd_sum
print even_sum
print average
print average1
