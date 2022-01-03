from odoo import fields, models, api, _
from odoo.exceptions import UserError

class Activity(models.Model):
    _name = 'library.search'
    _description = 'search info'

    book_name = fields.Many2one('library.book',string='Book name')
    reader_name = fields.Many2one('library.user',string='Reader name')
    branch_name = fields.Many2one('library.branch',string='Branch name')
    publisher = fields.Many2one('library.publisher',string='Publisher name')
    author = fields.Many2one('library.author',string='Author name')
    library = fields.Many2one('library.library',string='Library')
    librarian = fields.Many2one('library.librarian',string='Librarian')