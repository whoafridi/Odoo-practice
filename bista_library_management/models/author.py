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
    def check_mark(self):
        au = self.env['library.author'].search([('is_author','=',True),('book_name','=','React JS')])
        for i in au:
            print(i)
            if i.name == 'Mahmud':
                print('got mahmud')
    
    @api.multi
    def write(self, vals):
        # check id status
        print("write------book name value",vals)
        
        if vals.get("author_id") == None:
            raise UserError(_("required auhtor id"))
        # if vals.get('book_name') == None:
        #     raise UserError(_("required book_name"))

        print(self.book_name.name, self.book_name.book_id, self.book_name.branch.name)
        if self.book_name.name == 'React JS':
            print("got it")
        
        au = self.env['library.author'].search([('is_author','=',True)])
        for i in au:
            #print(i.name)
            if i.name == 'Mahmud':
                print('Got it')

        res = super(Author,self).write(vals)
        return res
    