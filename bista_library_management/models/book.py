from odoo import fields, models, api, _
from odoo.exceptions import UserError

def generate_id(author_gen):
    if author_gen == 'demo_genre':
        _id = '101202'
    elif author_gen == 'science fiction':
        _id = '101203'
    elif author_gen == 'programming':
        _id = '101204'
    elif author_gen == 'historical':
        _id = '101205'
    elif author_gen == 'horror':
        _id = '101206'
    elif author_gen == 'thriller':
        _id = '101207'
    
    return _id
            

class Book(models.Model):
    _name = "library.book"
    _description = "book info"
    
    
    name = fields.Char(string="Book name", required=True)
    book_id = fields.Char(string="Book ID")
    author_genre = fields.Selection([('demo_genre','Demo genre'),('science fiction','Science fiction'),('programming','Programming'),('thriller','Thriller'),('horror','Horror'),('historical','Historical')],string='Author written genre')
    email = fields.Char(string='Email')
    edition = fields.Char(string="Copyright Edition", required=True)
    price = fields.Float(string='Price', required=True)
    pages = fields.Integer(string='Number of pages')
    isbn_no = fields.Char(string='ISBN no')
    description = fields.Text(string="Description of books")
    is_available = fields.Boolean(string="Is available?")
    # relational fields
    author = fields.Many2one('library.author', string='Author name')
    branch = fields.Many2one('library.branch', string='Which Branch ?')
    isbn_publisher = fields.Many2one('library.publisher',string='ISBN publisher')


    @api.model
    def create(self, values):
        print("--///",values)
        values['author_genre'] = 'demo_genre' if not values['author_genre'] else values['author_genre']
        values['email'] = 'demo@gmail.com' if not values['email'] else values['email']
        values['pages'] = 0 if values['pages'] == 0 else values['pages']
        values['isbn_no'] = 'demo_isbn' if not values['isbn_no'] else values['isbn_no']
        values['description'] = 'this is demo description' if not values['description'] else values['description']
        if not values['author']:
            raise UserError(_("required author field"))
        if not values['branch']:
            raise UserError(_("please add the branch field"))
        if not values['isbn_publisher']:
            raise UserError(_("please select the isbn_publisher field"))
        
        # genereate book id using function
        if not values['book_id']:
            values['book_id'] = generate_id(values['author_genre'])
        
        res = super(Book, self).create(values)
        return res

    @api.multi
    def check_name(self):
        _name = self.env['library.book'].search(['|',('author.is_author','=',True),('name','=','odoo'),('branch.name','=','Lalmatia')])
        for rec in _name:
            message = f"Book - {rec.name}"
            raise UserError(_(message))

    @api.multi
    def write(self, values):
        print("==============\n",values)
        # check description status
        # if values.get('description') == None or values.get('isbn_no') == None:
        #     raise UserError(_("Required !"))
        # else:
        #     values['description'] = values['description']
        # # check isbn status
        # if not values.get('isbn_no'):
        #     values['isbn_no'] = '001-002-003-004'
        
        res = super(Book, self).write(values)
        return res