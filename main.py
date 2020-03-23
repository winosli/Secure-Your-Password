import requests
import hashlib
import sys
from time import time

def request_api_data(query):
    url = 'https://api.pwnedpasswords.com/range/' + str(query)
    res = requests.get(url)
    if res.status_code != 200:
        #raise RuntimeError(f'Error occur {res.status_code}, check the API and try again')
        print('Error occur - Check your internet connection!')
        sys.exit()
        #print(res)
    return res

#request_api_data(1234)

def count_passwords(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def get_sha1(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper() # hashing must be with encode utf-8
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    #print(first5_char,tail)
    #print(response)
    return count_passwords(response, tail)

def main(args):
    t1 = time()
    for password in args:
        count = get_sha1(password)
        if count:
            print(f'{password} was found {count} times - better to find another password')

        else:
            print(f'{password} was not found - that\'s great!')
    t2 = time()
    total_sec = round(t2 - t1, 2)
    print(f'Completed in {total_sec} sec')
    pass

if __name__ == "__main__":
    print('Check your Password Security in a secure way')
    is_checking = True
    while(is_checking):
        print('***')
        pass_to_check = input('\nEnter password for checking\n')
        if (pass_to_check.lower() == "exit"):
            sys.exit()
        else:
            main([str(pass_to_check)])
