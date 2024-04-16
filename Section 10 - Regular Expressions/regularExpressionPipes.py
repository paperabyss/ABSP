import re

series = "Xenoblade Chronicles 1, Xenoblade Chronicles X, Xenoblade Chronicles2, Xenoblade Chronicles 3, Xenogears, Xenosaga"

xenoRegex = re.compile(r'Xeno(blade|gears|saga)')
mo = xenoRegex.search(series)
print(mo)
