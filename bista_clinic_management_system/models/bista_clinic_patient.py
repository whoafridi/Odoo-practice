import re
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class Bista_Clinic_Patient(models.Model):
    _name = 'bistaclinic.patient'
    _description = 'bista clinic patient info'

    patient_id = fields.Integer(string="Patient ID", required=True)
    first_name = fields.Char(string="First name", required=True)
    last_name = fields.Char(string="Last name")
    name = fields.Char(string="Name", compute="_compute_name", readonly=True)
    phone = fields.Char(string="Phone")
    address = fields.Char(string="Address")
    create_date = fields.Date(string="Create date", readonly=True)

    disases = fields.Many2many('bistaclinic.diseases',string="Diseases")
    appointment = fields.One2many('bistaclinic.appointment','patient', string="Clinic Appointment", readonly=True) 


    def _compute_name(self):
        for i in self:
            print(i)
            if not i.last_name:
                 i.name = i.first_name 
            else:
                 i.name = i.first_name + ' ' + i.last_name
    

    @api.model
    def create(self, values):
        print(values)
        _id = ''
        if values['patient_id']:
            patient = values['patient_id']
            if patient in values.values():
                if patient[2] == '-':
                    new_key = patient[0:2].upper() +' - '+ patient[3:]
                    values['patient_id'] = new_key
                elif patient[2] == ' ' and patient[3] == '-' and patient[4] == ' ':
                    values['patient_id'] = patient.upper()
                elif (patient[0] == 'p' or patient[0] == 'P') and (patient[1] == 't' or patient[1] == 'T'):
                    new_key = patient[0:2].upper() + ' - '+ patient[2:]
                    values['patient_id'] = new_key
                else:
                    _id = 'PT - ' + values['patient_id']
                    values['patient_id'] = _id
        
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

        res = super(Bista_Clinic_Patient, self).create(values)
        return res
