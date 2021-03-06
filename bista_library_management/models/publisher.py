from dbm.ndbm import library
from odoo import models, fields

class Publisher(models.Model):
    _name = 'library.publisher'
    _decription = 'library publisher info'

    name = fields.Char(string="Publisher name", required=True)
    author = fields.Many2one('library.author', string='Author name')
    book_name = fields.Many2one('library.book', string='Book name')
    opening_time = fields.Selection([('9:00-7:00','9:00am-7:00pm'),('10:00-8:00','10:00am-8:00pm'),('11:00-9:00','11:00am-9:00pm')],string='Time for opening')
    address = fields.Char(string='Address of publisher')

    book_ids = fields.Many2many('library.book', string="All Books")

    books_name = fields.One2many('library.book','isbn_publisher', string="Books")

    library = fields.Many2one('library.library', string='Library name')