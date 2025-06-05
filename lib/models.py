from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref,Session
from sqlalchemy.orm import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base()

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())
    freebies = relationship("Freebie", back_populates="company")

    @classmethod
    def oldest_company(cls, session:Session):
        return session.query(cls).order_by(cls.founding_year).first()

    def give_freebie(self, session:Session, dev:"Dev", item_name:str, value:int):
        freebie = Freebie(name=item_name, value=value, dev=dev, company=self)
        session.add(freebie)
        session.commit()

   

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())
    freebies = relationship("Freebie", back_populates="dev")



    def received_one(self, item_name: str):
        for freebie in self.freebies:
            if freebie.name == item_name:
                return True
        return False

    @property
    def companies(self):
        return list({freebie.company for freebie in self.freebies})

    def give_away(self, session:Session, new_dev:"Dev", freebie:"Freebie"):
        if freebie in self.freebies:
            freebie.dev = new_dev
            session.add(freebie) 
            session.commit()

 
class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer, primary_key=True)
    item_name = Column(String) 
    
    dev_id = Column(Integer, ForeignKey('devs.id'))
    company_id = Column(Integer, ForeignKey('companies.id'))

    dev = relationship('Dev', back_populates='freebies')
    company = relationship('Company', back_populates='freebies')

    def __repr__(self):
        return f"<Freebie #{self.id} {self.item_name}>"