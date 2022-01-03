from odoo import fields, models, api, _
from odoo.exceptions import UserError
from datetime import date

class Activity(models.Model):
    _name = 'library.activity'
    _description = 'reader activity info'

    book_name = fields.Many2one('library.book',string='Book name')
    reader_name = fields.Many2one('library.user',string='Reader name')

    entry_time = fields.Date(string="Entry time", default=date.today())
    exit_time = fields.Date(string='Exit time', default=date.today())