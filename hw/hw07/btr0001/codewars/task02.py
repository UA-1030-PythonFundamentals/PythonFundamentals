def distance(x1, y1, x2, y2):
    # Your code here
    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)
    return round(dist, 2)