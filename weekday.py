from datetime import date

nazvy_dni = [
  "pondělí",
  "úterý",
  "středa",
  "čtvrtek",
  "pátek",
  "sobota",
  "neděle"
]

DAYS_IN_MONTH = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAYS_BEFORE_MONTH = [-1]

dbm = 0
for dim in DAYS_IN_MONTH[1:]:
  DAYS_BEFORE_MONTH.append(dbm)
  dbm += dim
del dbm, dim

def is_leap_year(year):
  return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def days_before_year(year):
  y = year - 1
  return y * 365 + y // 4 - y // 100 + y // 400

def days_before_month(year, month):
  return DAYS_BEFORE_MONTH[month] + (month > 2 and is_leap_year(year))

def to_ordinal(year, month, day):
  return days_before_year(year) + days_before_month(year, month) + day

def day_of_week(year, month, day):
  return to_ordinal(year, month, day) % 7

if __name__ == "__main__":
  assert is_leap_year(2000)
  assert not is_leap_year(1900)
  assert is_leap_year(2004)
  # print(DAYS_IN_MONTH, DAYS_BEFORE_MONTH)
  print(nazvy_dni[day_of_week(2018, 11, 8) - 1])