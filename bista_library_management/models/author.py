from odoo import fields, models, api, _
from odoo.exceptions import UserError

class Author(models.Model):
    _name = 'library.author'
    _description = 'author info'

    name = fields.Char(string='Author name', required= True)
    author_genre = fields.Selection([('science fiction','Science fiction'),('programming','Programming'),('thriller','Thriller'),('horror','Horror'),('historical','Historical')],string='Author written genre')
    author_id = fields.Char(string='Auhor_id')
    author_description = fields.Text(string='Author description')
    is_author = fields.Boolean(string="Author")

    book_name = fields.Many2one('library.book', string="Book")
    library_deatils = fields.Many2one('library.library', string="Library details")


    book_ids = fields.Many2many('library.book',string="Book list")

    books_name = fields.One2many('library.book','author', string="Books")


    # self.env['library.author'].search([('is_author','=',True)])
    @api.model
    def create(self, vals):
        print('create-----book name value',vals['book_name'])
        if vals['name']:
            vals['name'] = vals['name'].capitalize()
        if not vals['book_name']:
            raise UserError(_("please select the book name"))
        if not vals['author_id']:
            raise UserError(_("Required field"))
        if vals['author_id'].isdigit() == False:
            raise UserError(_("Id can't be character"))
        vals['author_genre'] = 'horror' if not vals['author_genre'] else vals['author_genre']
        vals['author_description'] = 'this is author description' if not vals['author_description'] else vals['author_description']

        res = super(Author,self).create(vals)
        return res
    
    @api.multi
    def check_name(self):
        au = self.env['library.author'].search([('is_author','=',True),('book_name.name','=','odoo'),('book_name.branch.name','=','Mohakhali')])
        for i in au:
            print(i.name, i.book_name.branch.name)
            if i.name == 'kafi' or i.name == 'Kafu':
                print('/--------/ /--------/ Find required things.')
                raise UserError(_("Find Kafi Branch from Mohakhali"))
    
    @api.multi
    def write(self, vals):
        # check id status
        print("write------book name value",vals)
        
        # if vals.get('author_id') == None:
        #      raise UserError(_("required auhtor id"))
        # if not vals['author_id']:
        #      raise UserError(_("auhtor id can't be empty"))

        print(self.book_name.name, self.book_name.book_id, self.book_name.branch.name)
        if self.book_name.name == 'React JS':
            print("got it")

        res = super(Author,self).write(vals)
        return res
    