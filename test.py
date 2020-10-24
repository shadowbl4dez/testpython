greeting = "Hello"

name = "world"

name = name.replace("world", "Augsburg")

message = f"{greeting} {name.upper()}!"

print(message)

print("")

num_1 = float("123")
num_2 = int("321")

print(num_1 + num_2)

print("")

kurse_semester1 = ["Technische Mechanik", "Mathematik", "Physik", "Digitaltechnik", "Elektrotechnik", "Konstruktion",
                   "Englisch"]
kurse_semester2 = ["Werkstofftechnik", "Physik Praktikum", "Mathematik"]

kurse_semester1.insert(6, "Informatik")

pop = kurse_semester2.pop()

kurse_semester1.extend(kurse_semester2)

kurse1_sortiert = sorted(kurse_semester1)

for index, kurs in enumerate(kurse1_sortiert, start=1):
    print(index, kurs)

print("")

print("1 " + pop)

print("")

for index, s2 in enumerate(kurse_semester2, start=1):
    print(index, s2)

print("")

print("Englisch" in kurse_semester1)

print("")

kurse_semester1_schoen = ", ".join(kurse_semester1)

print(kurse_semester1_schoen)

print("")

liste1 = {"alpha", "beta", "gamma"}
liste2 = {"omega", "alpha", "zeta"}

liste = sorted(liste1.union(liste2))

for index, listee in enumerate(liste, start=1):
    print(index, listee)
