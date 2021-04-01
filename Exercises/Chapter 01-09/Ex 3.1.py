cp = 24.95
afterDisc = 0.6 * cp
copies = 60
shipping = 3 + (0.75*copies-1)
totalprice = (afterDisc * copies) + shipping
print(totalprice)