from datetime import datetime

from sqlalchemy import Column, Integer, Float, Date

from conn_database import Base


class ScoreRecord(Base):
    __tablename__ = 'score_records'
    
    id = Column(Integer(), primary_key=True)
    created_at = Column(Date(), default=datetime.now().date())
    num_records = Column(Integer())
    num_coordinates = Column(Integer())
    percent_accuracy = Column(Float())
    percent_approximate = Column(Float())
    percent_inaccurate = Column(Float())
    response_rate = Column(Float())
    accuracy_rate = Column(Float())
    value_score = Column(Float())

    def __str__(self) -> str:
        return f"(created_at={self.created_at}, \
num_records={self.num_records}, num_assert_coordinates={self.num_coordinates}, \
accurate={self.percent_accuracy}%, approximate={self.percent_approximate}%, \
inaccurate={self.percent_inaccurate}%, response_rate={self.response_rate}%, \
accuracy_rate={self.accuracy_rate}%, score={self.value_score})"