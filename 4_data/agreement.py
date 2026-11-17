"""Reproduce the inter-coder agreement reported in Section 4.3.

usage: python3 agreement.py          (run from this folder; needs numpy)
Reads reliability_levels.csv (independent codings of levels A-D, before consensus).
"""
import csv, random
from kalpha import kalpha


def rows(name):
    with open(name, encoding='utf-8') as f:
        return list(csv.DictReader(f))


def boot(units, level, n=4000, seed=1):
    random.seed(seed)
    vals = []
    for _ in range(n):
        smp = [random.choice(units) for _ in units]
        try:
            a = kalpha(smp, level)
            if a == a:
                vals.append(a)
        except ZeroDivisionError:
            pass
    vals.sort()
    return vals[int(.025 * len(vals))], vals[int(.975 * len(vals)) - 1]


def dcat(v):  # expected targeting: 0 = no estimate; categories 4-5 reckons, 3 possible, 1-2 not
    v = int(v)
    return None if v == 0 else ('reckons' if v >= 4 else 'possible' if v == 3 else 'not')


# unit order in which the bootstrap intervals of the paper were drawn (fixed seed)
ORDER = ['R1', 'R2', 'C1', 'C2', 'C3', 'R3', 'R4', 'R5', 'C4', 'C5', 'M1', 'R6', 'R7', 'R8', 'C6', 'C7', 'C8', 'M2', 'C9', 'C10']
lv = sorted(rows('reliability_levels.csv'), key=lambda r: ORDER.index(r['pseudonym']))
print('Levels (two coders, 20 organizations)')
for area, name in (('A', 'knowledge'), ('B', 'information acquisition'), ('C', 'risk practice')):
    u = [[int(r[f'first_{area}']), int(r[f'second_{area}'])] for r in lv]
    lo, hi = boot(u, 'ordinal')
    print(f'  {name:24s} alpha (ordinal) = {kalpha(u, "ordinal"):.2f}  [{lo:.2f}, {hi:.2f}]  identical {sum(a == b for a, b in u)}/20')
u = [[dcat(r['first_D']), dcat(r['second_D'])] for r in lv]
lo, hi = boot(u, 'nominal')
print(f'  {"expected targeting":24s} alpha (nominal, categories) = {kalpha(u, "nominal"):.2f}  [{lo:.2f}, {hi:.2f}]')

