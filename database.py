from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://wihlgozthhtylu:f69667341e61e429a9494a2f7021531b3395e8ece2825bfb832aafbdccde099b@ec2-44-205-64-253.compute-1.amazonaws.com:5432/d2imevpii1l1ff",
                       echo=True
                       )

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)
