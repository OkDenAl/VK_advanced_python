class CustomList(list):
    def count_sum(self):
        return sum(self)

    def __neg__(self):
        res = []
        for i in self:
            res.append(-i)
        return CustomList(res)

    def __add__(self, other):
        res = []
        num_of_iter = max(len(self), len(other))
        for i in range(num_of_iter):
            if i >= len(self):
                res.append(other[i])
                continue
            if i >= len(other):
                res.append(self[i])
                continue
            res.append(self[i] + other[i])
        return CustomList(res)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        res = []
        num_of_iter = max(len(self), len(other))
        for i in range(num_of_iter):
            if i >= len(self):
                res.append(-other[i])
                continue
            if i >= len(other):
                res.append(self[i])
                continue
            res.append(self[i] - other[i])
        return CustomList(res)

    def __rsub__(self, other):
        return -self + other

    def __eq__(self, other):
        return self.count_sum() == other.count_sum()

    def __ne__(self, other):
        return self.count_sum() != other.count_sum()

    def __le__(self, other):
        return self.count_sum() <= other.count_sum()

    def __lt__(self, other):
        return self.count_sum() < other.count_sum()

    def __ge__(self, other):
        return self.count_sum() >= other.count_sum()

    def __gt__(self, other):
        return self.count_sum() > other.count_sum()

    def __str__(self):
        values = ""
        elem_sum = 0
        for i in self:
            values += str(i) + " "
            elem_sum += i
        return f"List's elements: {values}\nSum: {elem_sum}"
