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

if __name__ == "__main__":
  print(nazvy_dni[date.today().weekday()])