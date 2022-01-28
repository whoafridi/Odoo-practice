from odoo import models, fields, api, _
from odoo.exceptions import UserError
import re
from datetime import date
 
class Bista_Clinic_Employee(models.Model):
    _name = 'bistaclinic.employee'
    _description = 'bista clinic employee info'

    employee_id = fields.Char(string="Employee ID", required=True)
    name = fields.Char(string="Name", required=True)
    designation = fields.Selection([('nurse','Nurse'),('admin','Admin'),('cleaner','Cleaner')])
    phone = fields.Char(string="Phone", required=True)
    email = fields.Char(string="Email")
    address = fields.Char(string="Address")
    birth_date = fields.Date(string="Birth date")
    create_date = fields.Date(string="Create date", readonly=True)

    clinic = fields.Many2one('bista.clinic',string="Clinic")



    @api.onchange('birth_date')
    def _onchange_birth_date(self):
        if self and self.birth_date:
            bdate = self.birth_date
            if bdate > self.birth_date.today():
                raise UserError("Future date can't be allowed")

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
        _id = ''
        if values['employee_id']:
            if values['designation'] == 'nurse':
                _id = 'NU - ' + values['employee_id']
                values['employee_id'] = _id
            if values['designation'] == 'admin':
                _id = 'AD - ' + values['employee_id']
                values['employee_id'] = _id
            if values['designation'] == 'cleaner':
                _id = 'CL - ' + values['employee_id']
                values['employee_id'] = _id
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

        res = super(Bista_Clinic_Employee, self).create(values)
        return res