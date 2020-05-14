from models import Base, DATABASE_NAME
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine(f'sqlite:///{DATABASE_NAME}', echo=True)

    Base.metadata.create_all(engine)
