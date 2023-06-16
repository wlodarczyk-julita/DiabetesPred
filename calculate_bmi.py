from datetime import date

def calculate_age(date_of_birth):
    year, month, day = map(int, date_of_birth.split('-'))
    current_date = date.today()
    age = current_date.year - year
    if current_date.month < month or (current_date.month == month and current_date.day < day):
        age -= 1
    
    return age
class calculate_bmi:
    @staticmethod
    def calculate_bmi(weight, height):
        height = float(height)/100
        bmi = float(weight) / (float(height) ** 2)
        return round(bmi, 2)
    
    def describe_bmi(bmi, date_of_birth, sex):
        age = calculate_age(date_of_birth)

        if (sex == 'Mężczyzna'):
            if(age<=24):
                if(bmi<20):
                    return 'Niedowaga'
                elif (bmi>=20 and bmi <25):
                    return 'Waga w normie'
                elif (bmi>=25 and bmi <30):
                    return 'Nadwaga'
                elif (bmi>=30 and bmi <40):
                    return 'Otyłość'
                else:
                    return 'Skrajna otyłość'
            elif(age>=25 and age<34):
                if(bmi<21):
                    return 'Niedowaga'
                elif (bmi>=21 and bmi <26):
                    return 'Waga w normie'
                elif (bmi>=26 and bmi <31):
                    return 'Nadwaga'
                elif (bmi>=31 and bmi <41):
                    return 'Otyłość'
                else:
                    return 'Skrajna otyłość'
            elif(age>=34 and age<44):
                if(bmi<22):
                    return 'Niedowaga'
                elif (bmi>=22 and bmi <27):
                    return 'Waga w normie'
                elif (bmi>=27 and bmi <32):
                    return 'Nadwaga'
                elif (bmi>=32 and bmi <42):
                    return 'Otyłość'
                else:
                    return 'Skrajna otyłość'
            elif(age>=44 and age<54):
                if(bmi<23):
                    return 'Niedowaga'
                elif (bmi>=23 and bmi <28):
                    return 'Waga w normie'
                elif (bmi>=28 and bmi <33):
                    return 'Nadwaga'
                elif (bmi>=33 and bmi <43):
                    return 'Otyłość'
                else:
                    return 'Skrajna otyłość'
            elif(age>=54 and age<64):
                if(bmi<24):
                    return 'Niedowaga'
                elif (bmi>=24 and bmi <29):
                    return 'Waga w normie'
                elif (bmi>=29 and bmi <34):
                    return 'Nadwaga'
                elif (bmi>=34 and bmi <44):
                    return 'Otyłość'
                else:
                    return 'Skrajna otyłość'
            else:
                if(bmi<25):
                    return 'Niedowaga'
                elif (bmi>=25 and bmi <30):
                    return 'Waga w normie'
                elif (bmi>=30 and bmi <35):
                    return 'Nadwaga'
                elif (bmi>=35 and bmi <45):
                    return 'Otyłość'
                else:
                    return 'Skrajna otyłość'
        else: 
            if(age<=24):
                if(bmi<19):
                    return 'Niedowaga'
                elif (bmi>=19 and bmi <24):
                    return 'Waga w normie'
                elif (bmi>=24 and bmi <29):
                    return 'Nadwaga'
                elif (bmi>=29 and bmi <39):
                    return 'Otyłość'
                else:
                    return 'Skrajna otyłość'
            elif(age>=25 and age<34):
                if(bmi<20):
                    return 'Niedowaga'
                elif (bmi>=20 and bmi <25):
                    return 'Waga w normie'
                elif (bmi>=25 and bmi <30):
                    return 'Nadwaga'
                elif (bmi>=30 and bmi <40):
                    return 'Otyłość'
                else:
                    return 'Skrajna otyłość'
            elif(age>=34 and age<44):
                if(bmi<21):
                    return 'Niedowaga'
                elif (bmi>=21 and bmi <26):
                    return 'Waga w normie'
                elif (bmi>=26 and bmi <31):
                    return 'Nadwaga'
                elif (bmi>=31 and bmi <41):
                    return 'Otyłość'
                else:
                    return 'Skrajna otyłość'
            elif(age>=44 and age<54):
                if(bmi<22):
                    return 'Niedowaga'
                elif (bmi>=22 and bmi <27):
                    return 'Waga w normie'
                elif (bmi>=27 and bmi <32):
                    return 'Nadwaga'
                elif (bmi>=32 and bmi <42):
                    return 'Otyłość'
                else:
                    return 'Skrajna otyłość'
            elif(age>=54 and age<64):
                if(bmi<23):
                    return 'Niedowaga'
                elif (bmi>=23 and bmi <28):
                    return 'Waga w normie'
                elif (bmi>=28 and bmi <33):
                    return 'Nadwaga'
                elif (bmi>=33 and bmi <43):
                    return 'Otyłość'
                else:
                    return 'Skrajna otyłość'
            else:
                if(bmi<24):
                    return 'Niedowaga'
                elif (bmi>=24 and bmi <29):
                    return 'Waga w normie'
                elif (bmi>=29 and bmi <34):
                    return 'Nadwaga'
                elif (bmi>=34 and bmi <44):
                    return 'Otyłość'
                else:
                    return 'Skrajna otyłość'