import os
import sys
from sqlalchemy import Table, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

favorite_planets = Table(
    'favorite_planets',
    dColumn(Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('planet_id', Integer, ForeignKey('planet.id'), primary_key=True)
)

# Tabla intermedia para la relación muchos a muchos entre usuarios y personajes favoritos
favorite_people = Table(
    'favorite_people',
    Column(Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('people_id', Integer, ForeignKey('people.id'), primary_key=True)
)

class User(Model):
    id = Column(Integer, primary_key=True)
    email = Column(String(250), unique=True, nullable=False)
    password = Column(String(80), nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    favorite_planets = relationship('Planet', secondary=favorite_planets, backref=backref('favorited_by_users', lazy='dynamic'))
    favorite_people = relationship('People', secondary=favorite_people, backref=backref('favorited_by_users', lazy='dynamic'))
    def __repr__(self):
        return '<User %r>' % self.email
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_active": self.is_active,
        }
    
class People(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    def __repr__(self):
        return '<People %r>' % self.name
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "eye_color": self.eye_color,
            "height": self.height,
        }
    
class Planet(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    def __repr__(self):
        return '<Planet %r>' % self.name
