from odoo import models, fields

class Teacher(models.Model):
    _name = 'education.teacher'
    _description = 'Teacher'

    name = fields.Char(string='Name', required=True)
    subject = fields.Char(string='Subject', required=True)
