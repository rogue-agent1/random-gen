#!/usr/bin/env python3
"""Random number generators. Zero dependencies."""

class LCG:
    """Linear Congruential Generator."""
    def __init__(self, seed=42, a=1664525, c=1013904223, m=2**32):
        self.state = seed; self.a = a; self.c = c; self.m = m
    def next_int(self):
        self.state = (self.a * self.state + self.c) % self.m; return self.state
    def next_float(self): return self.next_int() / self.m
    def randint(self, lo, hi): return lo + self.next_int() % (hi - lo + 1)
    def choice(self, seq): return seq[self.next_int() % len(seq)]
    def shuffle(self, lst):
        lst = lst[:]
        for i in range(len(lst)-1, 0, -1):
            j = self.next_int() % (i+1)
            lst[i], lst[j] = lst[j], lst[i]
        return lst
    def sample(self, seq, k):
        pool = list(seq); result = []
        for _ in range(k):
            idx = self.next_int() % len(pool)
            result.append(pool.pop(idx))
        return result

class XorShift:
    def __init__(self, seed=42):
        self.state = seed if seed else 1
    def next_int(self):
        x = self.state
        x ^= (x << 13) & 0xFFFFFFFF
        x ^= x >> 17
        x ^= (x << 5) & 0xFFFFFFFF
        self.state = x & 0xFFFFFFFF
        return self.state
    def next_float(self): return self.next_int() / 0xFFFFFFFF

def weighted_choice(items, weights, rng=None):
    import random
    r = (rng.next_float() if rng else random.random()) * sum(weights)
    cumsum = 0
    for item, w in zip(items, weights):
        cumsum += w
        if r <= cumsum: return item
    return items[-1]

if __name__ == "__main__":
    rng = LCG(12345)
    print([rng.next_float() for _ in range(5)])
