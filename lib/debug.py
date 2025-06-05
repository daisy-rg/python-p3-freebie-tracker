

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Dev, Company, Freebie,Base


engine = create_engine('sqlite:///./sqlite/freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

print("\n👩‍💻 Devs:")
for dev in session.query(Dev).all():
    print(f"{dev.id} - {dev.name}")

print("\n🏢 Companies:")
for company in session.query(Company).all():
    print(f"{company.id} - {company.name} ({company.founding_year})")


print("\n🎁 Freebies:")
for freebie in session.query(Freebie).all():
    print(f"{freebie.item_name} (${freebie.value}) given by {freebie.company.name} to {freebie.dev.name}")

session.close()