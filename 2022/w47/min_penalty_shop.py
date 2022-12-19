class Solution:
    def bestClosingTime(self, customers: str) -> int:
        customers = customers + "N"
        ones = [0] * len(customers)
        zeros = [0] * len(customers)
        if customers[-1] == 'Y':
            ones[-1] = 1
        for i in range(len(customers) - 2, -1, -1):
            if customers[i] == 'Y':
                ones[i] = ones[i + 1] + 1
            else:
                ones[i] = ones[i + 1]
        for i in range(1, len(customers)):
            if customers[i-1] == 'N':
                zeros[i] = zeros[i-1] + 1
            else:
                zeros[i] = zeros[i-1]
        # print(f"{ones=}")
        # print(f"{zeros=}")
        penalty = [one + zero for one, zero in zip(ones, zeros)]
        # print(penalty)
        index_min = min(range(len(penalty)), key=penalty.__getitem__)
        return index_min


s = Solution()
customers = "YYNY"
print(s.bestClosingTime(customers))
