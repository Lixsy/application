from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from password import password, pg_user, pg_port, pg_host, db_name
import converters

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{pg_user}:{password}@{pg_host}:{pg_port}/{db_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class UserModel(db.Model):
    __tablename__ = 'main_info'
    __table_args__ = {"schema": "soloviev"}
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    middle_name = db.Column(db.String(), nullable=False)
    bornDate = db.Column(db.String(), nullable=False)
    gender = db.Column(db.String(), nullable=False)


class IndividualInfoModel(db.Model):
    __tablename__ = "extra_info"
    __table_args__ = {"schema": "soloviev"}

    user_id = db.Column(db.Integer, db.ForeignKey('soloviev.main_info.user_id'), primary_key=True, index=True)
    education = db.Column(db.String())
    comment = db.Column(db.String())
    citizenship = db.Column(db.String())


db.create_all()


@app.route('/')
def index():
    return render_template("picture.html")


def add_one_individual_to_database(name: str, middle_name: str, gender: int, citizenship: bool, dateborn: str,
                                   education: str, comment: str):
    user_to_add = UserModel(name=converters.convert_name_to_database(name),
                            middle_name=converters.convert_middle_name_to_database(middle_name),
                            bornDate=dateborn, gender=converters.convert_gender_to_database(gender))

    db.session.add(user_to_add)
    db.session.commit()

    user_extra_info = IndividualInfoModel(user_id=user_to_add.user_id,
                                          education=converters.convert_education_to_database(education),
                                          comment=converters.convert_comment_to_database(comment),
                                          citizenship=converters.convert_citizenship_to_database(citizenship))

    db.session.add(user_extra_info)
    db.session.commit()


@app.route('/api/users', methods=['POST'])
def requests_from_front():
    name = request.json['name']
    middle_name = request.json['middle_name']
    gender = request.json['gender']
    citizenship = request.json['citizenship']
    dateborn = request.json['dateBorn']
    education = request.json['education']
    comment = request.json['comment']
    add_one_individual_to_database(name, middle_name, gender, citizenship, dateborn, education, comment)
    return render_template("picture.html")


if __name__ == '__main__':
    app.run(debug=True)
