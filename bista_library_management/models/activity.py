from odoo import fields, models, api, _
from odoo.exceptions import UserError
from datetime import datetime

class Activity(models.Model):
    _name = 'library.activity'
    _description = 'reader activity info'

    book_name = fields.Many2one('library.book',string='Book name')
    reader_name = fields.Many2one('library.user',string='Reader name')

    entry_time = fields.Datetime(string="Entry time", default=datetime.today())
    exit_time = fields.Datetime(string='Exit time', default=datetime.today())

    @api.multi
    def read_book(self):
        t = (self.exit_time -self.reader_name.date_of_joining).days
        #rec = self.env['library.activity'].search([('exit_time.days','=','reader_name.date_of_joining.days')])
        print('-----',(self.exit_time - self.reader_name.date_of_joining).days)
        if(t>=30):
            print('------',self.reader_name.name, self.book_name.name)