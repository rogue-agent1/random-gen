#!/usr/bin/env python3
"""Random generator — numbers, strings, UUIDs, passwords, dice."""
import sys, random, string, uuid, hashlib
def password(length=16):
    chars = string.ascii_letters + string.digits + "!@#$%&*"
    return "".join(random.choice(chars) for _ in range(length))
def passphrase(words=4):
    w = ["correct","horse","battery","staple","alpha","bravo","charlie","delta","echo","foxtrot","gamma","hotel","india","juliet","kilo","lima","mike","november","oscar","papa","quantum","romeo","sierra","tango","uniform","victor","whiskey","xray","yankee","zulu"]
    return "-".join(random.choice(w) for _ in range(words))
def cli():
    if len(sys.argv) < 2: print("Usage: random_gen int|float|string|uuid|password|passphrase|dice [args]"); sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "int": lo, hi = int(sys.argv[2]) if len(sys.argv)>2 else 0, int(sys.argv[3]) if len(sys.argv)>3 else 100; print(random.randint(lo, hi))
    elif cmd == "float": print(f"{random.uniform(0, float(sys.argv[2]) if len(sys.argv)>2 else 1):.6f}")
    elif cmd == "string": n = int(sys.argv[2]) if len(sys.argv)>2 else 16; print("".join(random.choices(string.ascii_letters+string.digits, k=n)))
    elif cmd == "uuid": print(uuid.uuid4())
    elif cmd == "password": print(password(int(sys.argv[2]) if len(sys.argv)>2 else 16))
    elif cmd == "passphrase": print(passphrase(int(sys.argv[2]) if len(sys.argv)>2 else 4))
    elif cmd == "dice": n = int(sys.argv[2]) if len(sys.argv)>2 else 1; s = int(sys.argv[3]) if len(sys.argv)>3 else 6; rolls = [random.randint(1,s) for _ in range(n)]; print(f"  {rolls} = {sum(rolls)}")
    elif cmd == "hex": print(hashlib.sha256(str(random.random()).encode()).hexdigest()[:int(sys.argv[2]) if len(sys.argv)>2 else 32])
if __name__ == "__main__": cli()
