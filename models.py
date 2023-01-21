from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy import create_engine

from app import actions, prices_cleaned

engine = create_engine('postgresql://postgres:my_password@localhost/actions_db')
Base = declarative_base()

class Action(Base):
	__tablename__ = 'actions'

	id = Column(Integer(), primary_key=True)
	name = Column(String(50), nullable=False)
	price =  Column(Float(), nullable=False)
	date =  Column(DateTime(), default=datetime.now())

	def __str__(self):
		return f'Action name: {self.name}\nPrice: {self.price}\nDate: {self.date}'


Session = sessionmaker(engine)
session = Session()

if __name__ == '__main__':

	Base.metadata.drop_all(engine)
	Base.metadata.create_all(engine)

	for a, i in enumerate(prices_cleaned):
		action = Action(name=actions[a], price=prices_cleaned[a])
		session.add(action)
		session.commit()