from dbm.ndbm import library
from odoo import fields, models, api, _
from odoo.exceptions import UserError
from datetime import datetime
import re

class User(models.Model):
    _name = 'library.user'
    _description = 'library user info'

    book_name = fields.Many2one('library.book',string="Book name")
    name = fields.Char(string='Name', required=True)
    email = fields.Char(string="Email")
    user_id = fields.Char(string="User ID")
    phone = fields.Char(string='Phone')
    date_of_joining = fields.Datetime(string="Date of joining")

    book_ids = fields.Many2many('library.book',string="Book list") 

    reader_name = fields.One2many('library.borrowhistory','borrower_name',string='Borrower name')
    library = fields.Many2one('library.library',string="Library name")


    @api.model
    def create(self,values):

        res = super(User, self).create(values)
        return res

    @api.multi
    def write(self, values):
        print('-----\n', values)
        rec = self.env['library.user'].search([('book_name.is_available','=',True)])
        for i in rec:
            print("--------",i.book_name.name, i.book_name.author.name)

        res = super(User, self).write(values)
        return res
    
    @api.onchange('date_of_joining')
    def change_id(self):
        self.user_id = ''
        if self and self.date_of_joining:
            year = self.date_of_joining.year
            month = self.date_of_joining.month
            day = self.date_of_joining.day
            self.user_id = str(day) + str(month) + str(year)

    @api.onchange('phone')
    def check_phone_number(self):
        if self.phone and len(self.phone) == 0:
            raise UserError(_("please type your number"))

        elif self.phone and len(self.phone) != 0:
            pattern = r'{a-zA-Z0-9}'
            regex = re.match(pattern, self.phone)
            pattern2 = r'\0?[\d]{11}'
            regex2 = re.match(pattern2, self.phone)
            if not regex2:
                raise UserError(_("Phone number must be valid one"))
            elif len(self.phone) < 11:
                pattern2 = r'\0?[\d]{11}'
                regex2 = re.match(pattern2, self.phone)
                if not regex:
                    raise UserError(_("Phone number must be 11 characters"))
            elif len(self.phone) > 11:
                pattern = r"\+?[\d]{3}-[\d]{10}"
                regex = re.match(pattern, self.phone)

            # method of regex object.
                if not regex:
                    raise UserError(_('Invalid phone'))

    @api.onchange('email')
    def check_email(self):
        if self.email and len(self.email) == 0:
            raise UserError(_("plaese type email"))
        elif self.email and len(self.email) != 0:
            # pattern = "^[_a-z0-9]+[\._-]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
            pattern = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")
            regex = re.fullmatch(pattern, self.email)
            print(regex)
            if not regex:
                raise UserError(_("Email not valid"))