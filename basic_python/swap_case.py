def swap_case(s):
    s = [c.upper() if c.islower() else c.lower() for c in s]
    return "".join(s)