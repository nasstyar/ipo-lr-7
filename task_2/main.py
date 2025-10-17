print ("start code") #вывод строки
import json
num = str(input("Введите номер квалификации: "))
file = "dump.json"
skills = False
with open(file, 'r', encoding='utf-8') as file:
    data = json.load(file)
    for skill in data:
        if skill.get("model") == "data.skill":
            skill_code = skill["fields"].get("code")
            skill_title = skill["fields"].get("title")
            skills = True
            # speciality_code = ""#jfnv ;ajsefv;ajefsv;bajefwb
            # speciality_title = "" #ajenv;ujefv
            # speciality_educational = "" #eugvaegbv;ae
            for profession in data:
                if profession.get("model") == "data.speciality":
                    speciality_code = profession["fields"].get("code")
                    if speciality_code in num:
                        speciality_title = profession["fields"].get("title")
                        speciality_educational = proffesion["fields"].get("c_type")
                        break
            break
if not skills:
    print("=============== Не найдено ===============")
else:
    print("=============== Найдено ===============")      
    print(f"{speciality_code} >> Специальность {speciality_title} , {speciality_educational}")
    print(f"{skill_code} >> Квалификация {skill_title}")  