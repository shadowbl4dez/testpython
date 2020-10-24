def hello_func(*args):
    if len(args) == 3:
        s1 = args[0]
        s2 = args[1]
        s3 = args[2]
        if s1 != "" and s2 != "" and s3 != "":
            return Satz_studieren3(s1, s2, s3)
    if len(args) == 2:
        s1 = args[0]
        s2 = args[1]
        if s1 != "" and s2 != "":
            return Satz_studieren2(s1, s2)
    if len(args) == 1:
        s1 = args[0]
        if s1 != "":
            return Satz_studieren(s1)
    if len(args) == 0:
        return Nichts()


def Nichts():
    return "Ich studiere nichts!"


def Satz_studieren(s2):
    return "Ich studiere {}!".format(s2.upper())


def Satz_studieren2(s1, s2):
    return "Ich studiere {} und {}!".format(s1.upper(), s2.upper())


def Satz_studieren3(s1, s2, s3):
    return "Ich studiere {}, {} und {}!".format(s1.upper(), s2.upper(), s3.upper())


studium = ["Python", "FlagFootball", "Mechatronik"]
print(hello_func(*studium))
#
# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# kurse = ["Mechanik", "Digitaltechnik"]
# infos = {"name": "Luca", "alter": "19"}
#
# student_info(*kurse, **infos)

print("")

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    if not 1 <= month <= 12:
        return "Ungueltiger Monat"
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]


print(days_in_month(2000, 2))
