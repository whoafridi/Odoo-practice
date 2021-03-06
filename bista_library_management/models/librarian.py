from odoo import fields, models, api, _
from datetime import date
from odoo.exceptions import UserError
import re

class Librarian(models.Model):
    _name = 'library.librarian'
    _description = 'librarian info'

    name = fields.Char(string='Librarian name', required=True)
    email = fields.Char(string="Email")
    user_id = fields.Char(string="Librarian ID")
    phone = fields.Char(string='Phone')
    date_of_joining = fields.Date(string="Date of joining", default=date.today())

    library = fields.Many2one('library.library', string='Library')

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
            pattern = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
            #  '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'
            regex = re.search(pattern, self.email)
            print(regex)
            if not regex:
                raise UserError(_("Email not valid"))