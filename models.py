from sqlalchemy import Column, Integer, String, ForeignKey

from database import Base


class UserModel(Base):
    __tablename__ = 'main_info'
    __table_args__ = {"schema": "soloviev"}
    user_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    middle_name = Column(String, nullable=False)
    bornDate = Column(String, nullable=False)
    gender = Column(String, nullable=False)


class IndividualInfoModel(Base):
    __tablename__ = "extra_info"
    __table_args__ = {"schema": "soloviev"}

    user_id = Column(Integer, ForeignKey('soloviev.main_info.user_id'), primary_key=True, index=True)
    education = Column(String)
    comment = Column(String)
    citizenship = Column(String)


class PhoneNumberModel(Base):
    __tablename__ = "phone_number"
    __table_args__ = {"schema": "soloviev"}

    user_id = Column(Integer, ForeignKey('soloviev.main_info.user_id'), primary_key=True, index=True)
    phone_number = Column(String)
