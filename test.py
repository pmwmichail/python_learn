# -*- coding: cp1251 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import *


if __name__ == '__main__':
    # Открываем базу данны[
    engine = create_engine(f'sqlite:///{DATABASE_NAME}')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Делаем тестовые запросы
    len1 = len(session.query(Student).join(ExamRecord).all())
    len2 = len(session.query(ExamRecord).join(Exam).filter(Exam.discipline.like('Math')).all())
    len3 = len(session.query(ExamRecord).join(Exam).join(Staff).filter(Staff.last_name.like('Gavrilova')).all())

    # Печатаем результат для проверки
    print(len1 * len2 * len3)
