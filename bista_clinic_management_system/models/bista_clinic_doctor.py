import re
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class Bista_Clinic_Doctor(models.Model):
    _name = 'bistaclinic.doctor'
    _description = 'bista clinic doctor info'

    doctor_id = fields.Char(string="Employee ID", required=True)
    first_name = fields.Char(string="First name", required=True)
    last_name = fields.Char(string="Last name")
    name = fields.Char(string="Name", compute="_compute_name", readonly=True)
    phone = fields.Char(string="Phone", required=True)
    email = fields.Char(string="Email")
    address = fields.Char(string="Address")
    birth_date = fields.Date(string="Birth date")
    create_date = fields.Date(string="Create date", readonly=True)
    clinic = fields.Many2one('bista.clinic',string="Clinic")
   
    appointment_slot = fields.Many2many('bistaclinic.appointment',string="Appointment slot")

    def _compute_name(self):
        for i in self:
            if not i.last_name:
                i.name = i.first_name 
            else:
                i.name = i.first_name + ' ' + i.last_name
                  
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
        if values['doctor_id']:
            doctor = values['doctor_id']
            if doctor in values.values():
                if doctor[2] == '-':
                    new_key = doctor[0:2].upper() +' - '+ doctor[3:]
                    values['doctor_id'] = new_key
                elif doctor[2] == ' ' and doctor[3] == '-' and doctor[4] == ' ':
                    values['doctor_id'] = doctor.upper()
                elif (doctor[0] == 'd' or doctor[0] == 'D') and (doctor[1] == 't' or doctor[1] == 'T'):
                    new_key = doctor[0:2].upper() + ' - '+ doctor[2:]
                    values['doctor_id'] = new_key
                else:
                    _id = 'DT - ' + values['doctor_id']
                    values['doctor_id'] = _id

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

        res = super(Bista_Clinic_Doctor, self).create(values)
        return res