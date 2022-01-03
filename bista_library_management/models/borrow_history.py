from odoo import fields, models, api, _
from odoo.exceptions import UserError
import re

class BorrowHistory(models.Model):
    _name = 'library.borrowhistory'
    _description = 'librarian info'

    borrow_book_title = fields.Many2one('library.library',string="Borrow book name")
    borrower_id = fields.Char(string="Borrower ID")
    borrower_name = fields.Many2one('library.user',string="Borrower name")
    borrower_email = fields.Char(string="Borrower email", required=True)
    borrower_phone = fields.Char(string="Borrower phone", required=True)
    quantity = fields.Integer(string='Quantity', required=True)
    price = fields.Float(string="Price", required=True)
    pages = fields.Integer(string="Pages", required=True)
    edition = fields.Selection([('first','First'),('second','Second'),('third','Third')],string="Edition", required=True)



    @api.model
    def create(self, vals):

        if not vals['borrow_book_title']:
            raise UserError(_("select boook title done"))
        
        res = super(BorrowHistory, self).create(vals)
        return res

    @api.onchange('edition')
    def change_id(self):
        id = ''
        if self and self.edition == 'first':
            id = '001'
            self.borrower_id = id
        elif self and self.edition == 'second':
            id = '002'
            self.borrower_id = id
        elif self and self.edition == 'third':
            id = '003'
            self.borrower_id = id

    @api.onchange('borrower_phone')
    def check_phone_number(self):
        if self.borrower_phone and len(self.borrower_phone) == 0:
            raise UserError(_("please type your number"))

        elif self.borrower_phone and len(self.borrower_phone) != 0:
            pattern = r'{a-zA-Z0-9}'
            regex = re.match(pattern, self.borrower_phone)
            pattern2 = r'\0?[\d]{11}'
            regex2 = re.match(pattern2, self.borrower_phone)
            if not regex2:
                raise UserError(_("Phone number must be valid one"))
            elif len(self.borrower_phone) < 11:
                pattern2 = r'\0?[\d]{11}'
                regex2 = re.match(pattern2, self.borrower_phone)
                if not regex:
                    raise UserError(_("Phone number must be 11 characters"))
            elif len(self.borrower_phone) > 11:
                pattern = r"\+?[\d]{3}-[\d]{10}"
                regex = re.match(pattern, self.borrower_phone)

            # method of regex object.
                if not regex:
                    raise UserError(_('Invalid phone'))

    @api.onchange('borrower_email')
    def check_email(self):
        if self.borrower_email and len(self.borrower_email) == 0:
            raise UserError(_("plaese type email"))
        elif self.borrower_email and len(self.borrower_email) != 0:
            pattern = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
            regex = re.search(pattern, self.borrower_email)
            print(regex)
            if not regex:
                raise UserError(_("Email not valid"))



