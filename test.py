from random_gen import LCG, XorShift, weighted_choice
rng = LCG(42)
vals = [rng.next_float() for _ in range(100)]
assert all(0 <= v < 1 for v in vals)
assert len(set(int(v*10) for v in vals)) > 5  # reasonable spread
r1 = rng.randint(1, 6); assert 1 <= r1 <= 6
c = rng.choice(["a","b","c"]); assert c in ["a","b","c"]
shuf = rng.shuffle([1,2,3,4,5])
assert sorted(shuf) == [1,2,3,4,5]
samp = rng.sample([1,2,3,4,5], 3)
assert len(samp) == 3 and len(set(samp)) == 3
xr = XorShift(42)
xvals = [xr.next_float() for _ in range(100)]
assert all(0 <= v <= 1 for v in xvals)
wc = [weighted_choice(["a","b"], [0.9, 0.1], LCG(i)) for i in range(100)]
assert wc.count("a") > wc.count("b")
print("random_gen tests passed")
