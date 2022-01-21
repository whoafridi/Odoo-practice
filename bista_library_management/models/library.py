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
    publisher = fields.Many2one('library.publisher', string='Publisher')

    book_ids = fields.Many2many('library.book', string="Book list")
    author_ids = fields.Many2many('library.author', string="Author list")
    publications_ids = fields.Many2many('library.publisher', string="Publisher list")

    librarian = fields.One2many('library.librarian','library', string="librarian")
    book_name = fields.One2many('library.book','library', string="Book details")
    author_name = fields.One2many('library.author','library_deatils', string="Author details")
    publisher_name = fields.One2many('library.publisher','library', string="Publisher detais")
    reader_name = fields.One2many('library.user','library', string="Reader details")


    @api.multi
    def check_notavailable(self):
        notavailablebook_name = self.env['library.library'].search([('name.is_available','!=',True)])
        price = 0
        for rec in notavailablebook_name:
            print('----book name------',rec.name.name,'---publisher name--', rec.name.isbn_publisher.name,'---author name--', rec.author.name,'---price--', rec.name.price,'\n')
            price += rec.name.price
        print('total price :',price)
    

    @api.multi
    def check_requestedbook(self):
        requested_book = self.env['library.bookrequest'].search([('state','=','requested')])
        for rec in requested_book:
            print('----requested book----',rec.title.name,'---name----', rec.requested_by.name, '----author name----',rec.author, '----publisher name----',rec.publisher,'\n')

    @api.multi
    def check_available(self):
        availablebook_name = self.env['library.library'].search([('name.is_available','=',True)])
        for rec in availablebook_name:            
            print('-----found book name----',rec.name.name, rec.name.isbn_publisher.name, rec.author.name)
            print('-----found book name----',rec.name.isbn_publisher.address, rec.author.author_description) 

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
        # check if book not available
        notavailablebook_name = self.env['library.library'].search([('name.is_available','!=',True)])
        for rec in notavailablebook_name:
            print('-----not found book name------',rec.name.name)
        
        # check if book not available
        availablebook_name = self.env['library.library'].search([('name.is_available','=',True)])
        for rec in availablebook_name:            
            print('-----found book name----',rec.name.name, rec.name.isbn_publisher.name, rec.author.name)
            print('-----found book name----',rec.name.isbn_publisher.address, rec.author.author_description)        

        res = super(Library, self).write(values)
        return res
