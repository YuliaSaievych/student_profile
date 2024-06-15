# import SQLAlchemy
#
# db = SQLAlchemy()
#
# class Student(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(50), nullable=False)
#     last_name = db.Column(db.String(50), nullable=False)
#     email = db.Column(db.String(100), unique=True, nullable=False)
#     age = db.Column(db.Integer, nullable=False)
#     major = db.Column(db.String(100), nullable=False)
#
#     def __init__(self, first_name, last_name, email, age, major):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.age = age
#         self.major = major
