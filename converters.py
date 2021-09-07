def translator(text: str) -> str:
    symbols = (u"абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
               u"abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA")

    tr = {ord(a): ord(b) for a, b in zip(*symbols)}

    return text.translate(tr)


def convert_citizenship_to_database(citizenship: bool) -> str:
    if citizenship:
        citizenship = 'Russian citizenship'
    else:
        citizenship = 'Non russian citizenship'
    return citizenship


def convert_education_to_database(education: str) -> str:
    if education == '1':
        education = 'Secondary education'
        return education
    if education == '2':
        education = 'Incomplete higher education'
        return education
    if education == '3':
        education = 'University degree'
        return education
    else:
        return 'Not chosen'


def convert_name_to_database(name: str) -> str:
    name = translator(name)
    return name


def convert_middle_name_to_database(middle_name: str) -> str:
    middle_name = translator(middle_name)
    return middle_name


def convert_gender_to_database(gender: int):
    if gender == 1:
        gender = 'male'
        return gender
    if gender == 2:
        gender = 'female'
        return gender
    else:
        gender = 'not defined'
        return gender


def convert_comment_to_database(comment: str) -> str:
    comment = translator(comment)
    return comment


