from odoo import models, fields

class Question(models.Model):
    _name = 'education.question'
    _description = 'Question'

    name = fields.Char(string='Question', required=True)
    difficulty = fields.Integer(string='Difficulty', required=True)
    answer = fields.Text(string='Answer', required=True)
