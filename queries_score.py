from sqlalchemy import select

from conn_database import Session
from schema_score import ScoreRecord


def insert_data():
    # INSERTAR
    from data_score import data_score
    
    with Session() as session:
        score_data = ScoreRecord(**data_score)
        session.add(score_data)
        session.commit()

def get_all_data() -> None:
    # CONSULTAR TODOS LOS REGISTROS
    with Session() as session:
        score_data_list = session.query(ScoreRecord).all()
        for data in score_data_list:
            print(data)

def get_data_date(date_rec):
    # CONSULTAR UN REGISTRO
    with Session() as session:
        stmt = select(ScoreRecord).where(ScoreRecord.created_at == date_rec)
        data_list = session.scalars(stmt).all()
        if data_list:
            for data in data_list:
                if data:
                    print(data)
        else:
            print("No data")
    
def get_last_data():
    # CONSULTAR ULTIMO REGISTRO
    with Session() as session:
        stmt = select(ScoreRecord).order_by(ScoreRecord.id.desc())
        score_data_lst = session.scalars(stmt).all()
        print(list(score_data_lst)[0])
  
