def get_prime_numbers(val):
    
    if isinstance(val, int):
        if val > 1:
            prime_list = []
            for x in range(2, val+1):
                Prime = True
                for num in range(2, x):
                    if x % num == 0:
                        Prime = False
                if Prime:
                    prime_list.append(x)
        else:
            return 'Negatives or Zero not allowed'
    else:
        raise ValueError
    return prime_list


print(get_prime_numbers(56))
