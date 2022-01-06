import re
from odoo import fields, models, api, _
from odoo.exceptions import UserError
from datetime import date

class BookRequest(models.Model):
    _name = 'library.bookrequest'
    _description = 'book request info'

    title = fields.Many2one('library.book', string='Requested book title', required=True)
    author = fields.Many2one('library.author',string='Requested book Author name')
    author_genre = fields.Selection([('science fiction','Science fiction'),('programming','Programming'),('thriller','Thriller'),('horror','Horror'),('historical','Historical')],string='Author written genre')
    #relational field
    branch = fields.Many2one('library.branch',string='Which branch ?')
    publisher = fields.Char(string='Requested publisher name')
    edition = fields.Char(string='Requested book edition')
    #relational field
    requested_by = fields.Many2one('library.user',string='Requested by')
    state = fields.Selection([('requested','Requested'),('done','Done')], required=True)
    date = fields.Date(string="Date of Requesting", default=date.today())

    @api.model
    def create(self,values):
        if not values['branch']:
            raise UserError(_("please select the branch!"))
        
        if values['state'] == 'done':
            raise UserError(_("You can't select done"))

        res = super(BookRequest, self).create(values)
        return res

    @api.multi
    def write(self, values):
        print('-----\n', values)

        # check the requested book
        requested_book = self.env['library.bookrequest'].search([('title.is_available','!=',True)])
        for rec in requested_book:
            print('----requested book----',rec.title.name, rec.author)
        res = super(BookRequest, self).write(values)
        return res
