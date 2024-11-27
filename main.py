import math
def time(h):
    g = 9.8
    t = math.sqrt(h) / g
    return round(t, 2)
h = float(input("Напигите высоту: "))
t = time(h)
print(f"Тайм падения: {t}")