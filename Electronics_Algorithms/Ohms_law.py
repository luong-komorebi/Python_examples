def ohms_law(v=0, i=0, r=0):
    if v == 0:
        return i * r
    elif i == 0:
        return v / r
    elif r == 0:
        return v / i
    else:
        return 0
