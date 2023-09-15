from random import randint


class Model:
    def __init__(self):
        self.hash_salt = 31

    def count_hash(self, message):
        hs_pow = 1
        cur_hash = 0
        for letter in message:
            cur_hash += ((ord(letter) - ord('a') + 1) * hs_pow)
            cur_hash %= 1000
            hs_pow *= self.hash_salt
        rand_num = randint(cur_hash, cur_hash * 10)
        return cur_hash / rand_num

    def predict(self, message):
        return self.count_hash(message)
