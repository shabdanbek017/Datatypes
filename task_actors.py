#Задача: Анкета актеров
actor1_name    = "Leonardo DiCaprio"
actor1_country = "США"
actor1_birth   = 1974

actor2_name    = "Brad Pitt"
actor2_country = "США"
actor2_birth   = 1963

actor3_name    = "Асель Садвакасова"
actor3_country = "Казахстан"
actor3_birth   = 1985

actor4_name    = "Санжар Мади"
actor4_country = "Казахстан"
actor4_birth   = 1986

years = [2026, 2000, 1990]

print("======= Анкета актеров ======")
old26 = "Возраст в 2026:"
old20 = "Возраст в 2000:"
old90 = "Возраст в 1990:"

print(f"Leonardo DiCaprio(USA) \n {old26} {years[0] - actor1_birth} \n {old20} {years[1] - actor1_birth} \n {old90} {years[2] - actor1_birth} ")
print(f" Возраст в месяцах (на 2026): {(years[0] - actor1_birth) * 12} \n")

print(f"Brad Pitt(USA) \n {old26} {years[0] - actor2_birth} \n {old20} {years[1] - actor2_birth} \n {old90} {years[2] - actor2_birth}")
print(f" Возраст в месяцах (на 2026): {(years[0] - actor2_birth) * 12} \n")

print(f"Асель Садвакасова(KZ) \n {old26} {years[0] - actor3_birth} \n {old20} {years[1] - actor3_birth} \n {old90} {years[2] - actor3_birth}")
print(f" Возраст в месяцах (на 2026): {(years[0] - actor3_birth) * 12} \n")

print(f"Санжар Мади(KZ) \n {old26} {years[0] - actor4_birth} \n {old20} {years[1] - actor4_birth} \n {old90} {years[2] - actor4_birth}")
print(f" Возраст в месяцах (на 2026): {(years[0] - actor4_birth) * 12} \n")

print("\n ======== Итоги ====== ")
print(f"Суммарный возраст в 2026 году:{sum([52,63,41,40])} \n Средний возраст 2026 году: {sum([52,63,41,40]) / 4}")
print(f"Разница между самым старшим и самым младшим (2026):{max(52,63,41,40) - min(52,63,41,40)}")
print(f"Самый старший:{max(52,63,41,40)} \n Самый младший:{min(52,63,41,40)}")
print("====== Отчет ======  \n В 2026 году 4 актёра имеют средний возраст 49.0 лет. Самый старший — Brad Pitt (63), самый младший — Санжар Мади (40).")