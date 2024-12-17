import calendar

def is_leap_year(year):
    return ((year%4==0 and year%100!=0) or (year%400 == 0))

year_is = 1900
res = is_leap_year(year_is)
print(f"{year_is} is leap year : {res}")

def is_leap(year):
    return calendar.isleap(year)
year  = 2024
res = is_leap(year)
print(f"{year} is leap year : {res}")

def leap_year(year):
    res = lambda year : (year%4==0 and year%100!=0) or (year%400 == 0)
    print(res)
    return res

list_year = [1990,1989,2024,2000,2010]
answer = 0
for ele in list_year:
    if calendar.isleap(ele):
        answer += 1
print(f"Count of leap years : {answer} ")
if answer == 0 :
    print("No leap year")
