class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0

    def inc_progress(self, kata):
        possible_ranks = [value for value in range(-8,9) if (value != 0)]
        possible_progress = [value for value in range(0,101)]
        print("Level of given Kata: ", kata)
        print("Object stats before: ", self.rank, self.progress)
        if self.rank and kata not in possible_ranks or self.progress not in possible_progress:
            raise Exception("values out of range")
        if self.rank == 8:
            self.progress = 0
        else:
            if kata == self.rank - 1: #
                self.progress += 1
            if kata == -1 and self.rank == 1:
                self.progress += 1
            if kata == self.rank:
                self.progress += 3
            if kata > self.rank:
                if kata * self.rank < 0:
                    self.progress += 10 * ((kata - self.rank) - 1) ** 2
                else:
                    self.progress += 10 * (kata - self.rank) ** 2
        if self.progress >= 100:
            rank_before = self.rank
            self.rank += self.progress // 100
            rank_after = self.rank
            self.progress = self.progress % 100
            if rank_after * rank_before <= 0:
                self.rank += 1
        if self.rank > 8:
            self.rank = 8
        if self.rank == 8:
            self.progress = 0
        print("Object stats after: ", self.rank, self.progress)
        return self.rank, self.progress


user = User()
user.inc_progress(-7)
user.inc_progress(-4)
user.inc_progress(-3)
