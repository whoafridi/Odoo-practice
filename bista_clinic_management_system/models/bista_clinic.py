import re
from odoo import models, fields, api , _
from odoo.exceptions import UserError

class Bista_Clinic(models.Model):
    _name = 'bista.clinic'
    _description = 'bista clinic info'

    name = fields.Char(string="Name", required=True)
    phone = fields.Char(string="Phone", required=True)
    email = fields.Char(string="Email")
    website = fields.Char(string="Website")
    logo = fields.Binary(string="Logo")

    employee = fields.One2many('bistaclinic.employee','clinic',string="Employee")
    doctor = fields.One2many('bistaclinic.doctor','clinic',string="Doctor")

    @api.onchange('email')
    def _onchange_email(self):
        if self.email and len(self.email) == 0:
            raise UserError(_("plaese type email"))
        elif self.email and len(self.email) != 0:
            pattern = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
            regex = re.search(pattern, self.email)
            print(regex)
            if not regex:
                raise UserError(_("Email not valid"))

    @api.model
    def create(self, values):
        print(values)
        if values['phone']:
            phone = values['phone']
            if phone in values.values():
                pattern = r"^(\+88)?01[15-9]\d{8}$"
                regex = re.match(pattern, phone)

            # method of regex object.
                if not regex:
                    raise UserError(_('Invalid phone'))
                if phone[0] == '+' and phone[1] == '8' and phone[2] == '8':
                    values['phone'] = phone
                else:
                    values['phone'] = '+88' + phone

        res = super(Bista_Clinic, self).create(values)
        return res