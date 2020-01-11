


class Random:
    x = 2
    def next_random(self):
        self.x = (self.x * 13 + 17) % 101
        return self.x


r = Random()


a = [r.next_random() for _ in range(100)]
print(a)