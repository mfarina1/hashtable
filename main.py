# hash function is the key (int) modulo the table size (length of hash table)
# load factor = number of filled indices / length of table

from random import randint
import math


def key_mod_hash(key, length_of_hash_table):
    index = key % length_of_hash_table
    return index


# square the key, then take middle digits modulo table size
def mid_digits_sqr_hash(key, length_of_hash_table):
    sqr_key = int(math.pow(key, 2))
    mid_digits = str(sqr_key)[1:-1]
    return int(mid_digits) % length_of_hash_table


def create_open_addressing_hash_table(n):
    ls = [None] * n
    return ls


def create_chaining_hash_table(n):
    ls = [[]] * n
    return ls


def tests():
    for i in range(10):
        random_key = randint(1, 1000)
        random_length = randint(1, 100)
        expected_res = random_key % random_length
        assert expected_res == key_mod_hash(random_key, random_length), 'key_mod_hash test failed'
    print('key_mod_hash test passed')
    for i in range(10):
        random_key = randint(10, 100)
        random_length = randint(10, 100)
        mid_digit = str(int(math.pow(random_key, 2)))[1:-1]
        expected_res = int(mid_digit) % random_length
        assert expected_res == mid_digits_sqr_hash(random_key, random_length), 'mid_digits_sqr_hash test failed'
    print('mid_digits_sqr_hash test passed')


if __name__ == '__main__':
    tests()
