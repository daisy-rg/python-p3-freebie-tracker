#!/usr/bin/env python3
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.dev import Dev
from models.company import Company
from models.freebie import Freebie

engine = create_engine("sqlite:////home/moringa/Development/Code/Lesson/freebie_tracker/sqlite/freebie.db")
Session = sessionmaker(bind=engine)
session = Session()


dev1 = Dev(name="Yaska")
company1 = Company(name="OpenAI", founding_year=2015)
freebie1 = Freebie(item_name="Sticker", value=5, dev=dev1, company=company1)

session.add_all([dev1, company1, freebie1])
session.commit()

devs = session.query(Dev).all()
companies = session.query(Company).all()
freebies = session.query(Freebie).all()

print(f"Devs: {[dev.name for dev in devs]}")
print(f"Companies: {[company.name for company in companies]}")
print(f"Freebies: {[freebie.item_name for freebie in freebies]}")


# Script goes here!
