# def hello_func(*args):
#     if len(args) == 3:
#         s1 = args[0]
#         s2 = args[1]
#         s3 = args[2]
#         if s1 != "" and s2 != "" and s3 != "":
#             return Satz_studieren3(s1, s2, s3)
#     if len(args) == 2:
#         s1 = args[0]
#         s2 = args[1]
#         if s1 != "" and s2 != "":
#             return Satz_studieren2(s1, s2)
#     if len(args) == 1:
#         s1 = args[0]
#         if s1 != "":
#             return Satz_studieren(s1)
#     if len(args) == 0:
#         return Nichts()
#
#
# def Nichts():
#     return "Ich studiere nichts!"
#
#
# def Satz_studieren(s2):
#     return "Ich studiere {}!".format(s2.upper())
#
#
# def Satz_studieren2(s1, s2):
#     return "Ich studiere {} und {}!".format(s1.upper(), s2.upper())
#
#
# def Satz_studieren3(s1, s2, s3):
#     return "Ich studiere {}, {} und {}!".format(s1.upper(), s2.upper(), s3.upper())
#
#
# studium = ["Python", "FlagFootball", "Mechatronik"]
# print(hello_func(*studium))
#
# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# kurse = ["Mechanik", "Digitaltechnik"]
# infos = {"name": "Luca", "alter": "19"}
#
# student_info(*kurse, **infos)

# print("")
#
# month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
#
# def is_leap(year):
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
#
#
# def days_in_month(year, month):
#     if not 1 <= month <= 12:
#         return "Ungueltiger Monat"
#     if month == 2 and is_leap(year):
#         return 29
#     return month_days[month]
#
#
# print(days_in_month(2000, 2))


class Angestellte:
    anzahl_v_a = 0
    gm = 1.06

    def __init__(self, vorname, nachname, gehalt):
        # x = list()
        self.ganzername = vorname + " " + nachname
        self.gehalt = gehalt
        self.email = vorname + "." + nachname + "@firma.com"
        # x.append(self.ganzername)
        # x.append(self.gehalt)
        # x.append(self.email)
        Angestellte.anzahl_v_a += 1

    def infos(self):
        return "{} {} {}€".format(self.ganzername, self.email, self.gehalt)

    def erhoehung(self):
        self.gehalt = int(self.gehalt * self.gm)

        # for a2 in x:
        #     y = x.index(a2)
        #     print(y, a2)


ang_1 = Angestellte("Luca", "Bultmann", 10000)
ang_2 = Angestellte("Nils", "Just", 15000)
ang_3 = Angestellte("Felix", "Stachiw", 40000)
ang_4 = Angestellte("Niklas", "Just", 21000)
print(Angestellte.anzahl_v_a)
# print(infos1(ang_1))

# print(ang_1.infos())
# a1 = ang_1.infos().split()
# a1 = a1[0] + " " + a1[1], a1[2], a1[3]
# # print(a1)
# for a11 in a1:
#     print(a11)
