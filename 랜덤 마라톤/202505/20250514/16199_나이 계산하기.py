by, bm, bd = map(int, input().split())
ny, nm, nd = map(int, input().split())
year_age = ny - by
cnt_age = year_age + 1
age = year_age - 1 if (bm > nm or (bm >= nm and bd > nd)) else year_age
print(age)
print(cnt_age)
print(year_age)
