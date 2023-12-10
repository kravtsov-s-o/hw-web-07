from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:pass@localhost:5432/hw_web_07"
engine = create_engine(db_url)

DBSession = sessionmaker(bind=engine)
db_session = DBSession()
