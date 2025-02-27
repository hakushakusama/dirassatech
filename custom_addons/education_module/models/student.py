from odoo import models, fields

class Student(models.Model):
    _name = 'education.student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
    elo_rating = fields.Integer(string='ELO Rating', default=1000)
