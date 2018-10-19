# Hash Table experiments, created by Madeline Farina 10/19/18

# hash function is the key (int) modulo the table size (length of hash table)
# load factor = number of filled indices / length of table

from random import randint
import math

NUM_COLLISIONS = [0]
LOAD_FACTOR = [0]


def key_mod_hash(key, length_of_hash_table):
    index = key % length_of_hash_table
    return index


# square the key, then take middle digits modulo table size
def mid_digits_sqr_hash(key, length_of_hash_table):
    sqr_key = int(math.pow(key, 2))
    str_digits = str(sqr_key)

    if len(str_digits) > 2:
        mid_digits = str_digits[1:-1]
    else:
        mid_digits = str_digits

    return int(mid_digits) % length_of_hash_table


def create_open_addressing_hash_table(n):
    ls = [None] * n
    return ls


def load_factor_open_addr(hash_table):
    list_length = len(hash_table)
    filled_indices = 0
    for val in hash_table:
        if val is not None:
            filled_indices += 1
    return filled_indices / list_length


def load_factor_chaining(hash_table):
    list_length = len(hash_table)
    filled_indices = 0
    for val in hash_table:
        if len(val) > 0:
            filled_indices += 1
    return filled_indices / list_length


def create_chaining_hash_table(n):
    ls = [[] for _ in range(n)]  # list comprehension
    return ls


# generate index by putting key in hash function, check if array at index is available
# if available, place tuple of key and value at first list index
# if unavailable, increment counter variable and note current load factor then place
# at next available list index
def insertion_chaining(key, value, hash_table, hash_fn):
    global NUM_COLLISIONS
    global LOAD_FACTOR

    n = len(hash_table)
    index = hash_fn(key, n)

    if len(hash_table[index]) > 0:
        NUM_COLLISIONS.append(NUM_COLLISIONS[-1] + 1)
        LOAD_FACTOR.append(load_factor_chaining(hash_table))

    hash_table[index].append((key, value))

    return hash_table


def insert_chaining_key_mod(key, value, hash_table):
    return insertion_chaining(key, value, hash_table, key_mod_hash)


def insert_chaining_mid_digits(key, value, hash_table):
    return insertion_chaining(key, value, hash_table, mid_digits_sqr_hash)


# generate index by putting key in hash function, check if array at index is available
# if available, place tuple of key and value at index
# #if unavailable, increment counter variable and note current load factor then
def insertion_open_addr(key, value, hash_table, hash_fn):
    global NUM_COLLISIONS
    global LOAD_FACTOR

    n = len(hash_table)
    index = hash_fn(key, n)

    if hash_table[index] is None:  # if no collision
        hash_table[index] = (key, value)
    else:  # if collision
        NUM_COLLISIONS.append(NUM_COLLISIONS[-1] + 1)
        LOAD_FACTOR.append(load_factor_open_addr(hash_table))
        for idx in range(index + 1, 2 * n):
            new_idx = idx % n
            if hash_table[new_idx] is None:
                hash_table[new_idx] = (key, value)


def insert_open_addr_key_mod(key, value, hash_table):
    return insertion_open_addr(key, value, hash_table, key_mod_hash)


def insert_open_addr_mid_digits(key, value, hash_table):
    return insertion_open_addr(key, value, hash_table, mid_digits_sqr_hash)


def tests():
    # for i in range(10):
    #     random_key = randint(1, 1000)
    #     random_length = randint(1, 100)
    #     expected_res = random_key % random_length
    #     assert expected_res == key_mod_hash(random_key, random_length), 'key_mod_hash test failed'
    # print('key_mod_hash test passed')
    # for i in range(10):
    #     random_key = randint(10, 100)
    #     random_length = randint(10, 100)
    #     mid_digit = str(int(math.pow(random_key, 2)))[1:-1]
    #     expected_res = int(mid_digit) % random_length
    #     assert expected_res == mid_digits_sqr_hash(random_key, random_length), 'mid_digits_sqr_hash test failed'
    # print('mid_digits_sqr_hash test passed')
    # for i in range(10):
    #     random_int = randint(1, 10)
    #     print(create_chaining_hash_table(random_int))
    # for i in range(10):
    #     random_int = randint(1, 10)
    #     print(create_open_addressing_hash_table(random_int))

    # ls = [None, 1, 2, 3, 4]
    # print(load_factor_open_addr(ls))
    # ls2 = [[], [1], [1, 2, ], [1, 2, 3]]
    # print(load_factor_chaining(ls2))
    pass


# def insert_into_hash_tbl(hash_table, key, value, hash_fn, coll_res_fn):
#     idx = hash_fn(key)
#     coll_res_fn(idx, key, value)


if __name__ == '__main__':

    length_of_hash_table = [10, 20, 100]
    num_keys = 100

    for len_hash_tbl in length_of_hash_table:
        ht = create_chaining_hash_table(len_hash_tbl) # create chaining_table
        for _ in range(num_keys):
            random_key = randint(0, 3 * len_hash_tbl)
            insertion_chaining(???) # insert_key_mod table

    NUM_COLLISIONS = [0]
    LOAD_FACTOR = [0]

    for len_hash_tbl in length_of_hash_table:
        ht = create_chaining_hash_table(len_hash_tbl)
        for _ in range(num_keys):
            random_key = randint(0, 3 * len_hash_tbl)
            insertion_chaining(???)

    NUM_COLLISIONS = [0]
    LOAD_FACTOR = [0]

    for len_hash_tbl in length_of_hash_table:
        ht = create_open_addressing_hash_table(len_hash_tbl)
        for _ in range(num_keys):
            random_key = randint(0, 3 * len_hash_tbl)
            insertion_open_addr(???)

    NUM_COLLISIONS = [0]
    LOAD_FACTOR = [0]

    for len_hash_tbl in length_of_hash_table:
        ht = create_open_addressing_hash_table(len_hash_tbl)
        for _ in range(num_keys):
            random_key = randint(0, 3 * len_hash_tbl)
            insertion_open_addr(???)