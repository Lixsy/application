from flask import Flask, render_template, request, g

import converters
from database import Base, SessionLocal, engine
from models import UserModel, IndividualInfoModel, PhoneNumberModel


class CustomException(Exception):
    def __init__(self, message: str):
        self.message = message


app = Flask(__name__)


def db_session(func):
    def wrapper():
        with SessionLocal() as session:
            g.session = session
            to_return = func()
            session.commit()
        return to_return

    return wrapper


Base.metadata.create_all(bind=engine)


@app.route('/')
def index():
    return render_template("picture.html")


def add_one_individual_to_database(name: str, middle_name: str, gender: int, citizenship: bool, phone: str,
                                   dateborn: str, education: str, comment: str):
    user_to_add = UserModel(name=converters.convert_name_to_database(name),
                            middle_name=converters.convert_middle_name_to_database(middle_name),
                            bornDate=dateborn, gender=converters.convert_gender_to_database(gender))

    g.session.add(user_to_add)
    g.session.flush()

    user_extra_info = IndividualInfoModel(user_id=user_to_add.user_id,
                                          education=converters.convert_education_to_database(education),
                                          comment=converters.convert_comment_to_database(comment),
                                          citizenship=converters.convert_citizenship_to_database(citizenship))

    g.session.add(user_extra_info)
    g.session.flush()

    users_phone = PhoneNumberModel(user_id=user_to_add.user_id, phone_number=phone)

    g.session.add(users_phone)
    g.session.flush()


@app.route('/api/users', methods=['POST'])
@db_session
def requests_from_front():
    print(request.json)
    name = request.json['name']
    middle_name = request.json['middle_name']
    gender = request.json['gender']
    citizenship = request.json['citizenship']
    phone = request.json['phone']
    dateborn = request.json['dateBorn']
    education = request.json['education']
    comment = request.json['comment']
    add_one_individual_to_database(name, middle_name, gender, citizenship, phone, dateborn, education, comment)
    return render_template("picture.html")


if __name__ == '__main__':
    app.run(debug=True)
