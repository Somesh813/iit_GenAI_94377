numbera=input("Enter the numbers=")
number_list=numbera.split(",")
even_count=0
odd_count=0
for num in number_list:
    if int (num)%2==0:
        even_count+=1
    else:
        odd_count+=1
print("Number of even numbers=",even_count)
print("Number of odd numbers=",odd_count)    
