from odoo import fields, models, api, _
from odoo.exceptions import UserError

class Library(models.Model):
    _name = 'library.library'
    _description = 'library info'

    name = fields.Many2one('library.book',string='Book title')
    author = fields.Many2one('library.author', string='Author name')
    author_genre = fields.Selection([('science fiction','Science fiction'),('programming','Programming'),('thriller','Thriller'),('horror','Horror'),('historical','Historical')],string='Author written genre')
    
    edition = fields.Char(string="Copyright Edition", required=True)
    price = fields.Float(string='Price', required=True)
    pages = fields.Integer(string='Number of pages')
    quantity = fields.Integer(string='Number of books')
    description = fields.Text(string='Book description')
    # relational field
    branch = fields.Many2one('library.branch', string='Which Branch ?')

    @api.model
    def create(self, values):
        print("--///",values)
        values['author_genre'] = 'programming' if not values['author_genre'] else values['author_genre']
        values['description'] = 'this is demo description' if not values['description'] else values['description']
        if not values['author']:
            raise UserError(_("required author field"))
        if not values['name']:
            raise UserError(_("please verify the author!"))
        if not values['branch']:
            raise UserError(_("please select the branch!"))
        
        res = super(Library, self).create(values)
        return res

    @api.multi
    def write(self, values):
        print('---', values)
        if values['pages'] == 0:
            raise UserError(_("Pages can't be empty"))
        if values['quantity'] ==0:
            raise UserError(_("Quantity can't be empty"))

        res = super(Library, self).write(values)
        return res
