from datetime import date

def calculate_age(date_of_birth):
    year, month, day = map(int, date_of_birth.split('-'))
    current_date = date.today()
    age = current_date.year - year
    if current_date.month < month or (current_date.month == month and current_date.day < day):
        age -= 1
    
    return age

class calculate_kcal:
    @staticmethod
    def calculate_kcal(weight, height, date_of_birth, lifestyle, sex):
        age = calculate_age(date_of_birth)
        print(age)

        if sex == 'Kobieta': 
            
            kcal = (655 + float(9.6 * float(weight)) + float(1.85 * float(height )) - float(4.7 * float(age)))* float(lifestyle)
            print("KOBIETA")
            return round(kcal, 2)
           
        else:
            kcal = (66.5 + float(13.7 * float(weight)) + float(5 * float(height) ) - float(6.8 * float(age)))* float(lifestyle)
            print("CHŁOP")
            return round(kcal, 2)