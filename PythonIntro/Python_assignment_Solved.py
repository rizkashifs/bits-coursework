'''Question 1'''

def find_sum():
    input_num = input() 
    final_sum = 0

    for i in input_num:
        final_sum += int(i)

    return final_sum

print(find_sum())


'''Question 2'''

def check_armstrong(num,n):

    # check if the input is a positive number or not.

    assert num > 0 , "Number provided is not positive"

    temp_sum = 0

    for i in str(num):
        temp_sum += int(i)**n

    if temp_sum == num:
        return True
    else:
        return False

print(check_armstrong(153,3))


'''Question 3'''

def check_palindrome(input_str):

    if input_str[::-1] == input_str:
        return True
    else:
        return False

print(check_palindrome(input_str="malayalam"))


'''Question 4'''

def count_frequency(input_list):

    freq_dict = {}

    for i in input_list:
        try:
            freq_dict[i] += 1
        except:
            freq_dict[i] = 1

    return freq_dict

print(count_frequency(input_list=[1,4,5,7,5,4,2,1,0,5,7,4,5]))


'''Question 5'''

def find_prime_numbers(num):

    prime_num = []

    for i in range(2,num//2):
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            prime_num.append(i)
    return prime_num

prime_factr = []

def find_prime_factors(n):

    global prime_factr

    for i in find_prime_numbers(n):

        if n % i == 0:
            prime_factr.append(i)
            find_prime_factors(n//i)
            break
    else:
        prime_factr.append(n)

    return prime_factr

print(find_prime_factors(100))


'''Question 6'''

def calculate_factorial(num):

    if num == 1:
        return 1
    else:
        return num * calculate_factorial(num-1)

def calculate_binomial_coefficient(n,r):

    return calculate_factorial(n) / (calculate_factorial(r) * calculate_factorial(n-r))
    
print(calculate_binomial_coefficient(6,2))


'''Question 7'''

def linear_search(input_array,x):

    for i in input_array:
        if i == x:
            return True
        else:
            pass
    return False

def binary_search(input_array,x):
    # as the array is sorted
    mid_index = len(input_array)//2
    mid_value = input_array[mid_index]
    
    if x == mid_value:
        return True

    elif len(input_array) == 1:
        return False

    elif x < mid_value:
        return binary_search(input_array[:mid_index],x)

    else:
        return binary_search(input_array[mid_index:],x)

print(linear_search([1,4,7,9,12,16,45,66,89,104], 45))
print(binary_search([1,4,7,9,12,16,45,66,89,104], 9))


'''Question 8'''

def count_word_frequencies(file_name):
    # file_name should be something like 'myfile.txt' or the file location with name.
    with open(file_name, mode='r') as f:

        all_text = f.readlines()

    word_frequency_dict = {}

    for i in all_text:
        try:
            word_frequency_dict[i] += 1

        except:
            word_frequency_dict[i] = 1

    three_most_frequernt_words = list(zip(*sorted(word_frequency_dict.items(),key = lambda x : x[1] , reverse=True)[:3]))[0]    

    return word_frequency_dict, three_most_frequernt_words

print(count_word_frequencies("./mytextfile.txt"))