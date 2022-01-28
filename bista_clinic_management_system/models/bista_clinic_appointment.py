import datetime
from odoo import models, fields, api, _
from odoo.exceptions import UserError
import datetime

class Bista_Clinic_Appointment(models.Model):
    _name = 'bistaclinic.appointment'
    _description = 'bista clinic appointment info'

    @api.model
    def _default_phone(self):
        rec = self.env['bistaclinic.patient'].search([])
        for i in rec:
            return i.phone

    patient_name = fields.Char(string="Patient Name", required=True)
    patient_phone = fields.Char(string="Patient's phone",readonly=True, default=_default_phone) 
    doctor = fields.Many2one('bistaclinic.doctor',string="Doctor")
    
    diseases = fields.Many2many('bistaclinic.diseases',string="Diseases")
    appointment_date = fields.Datetime(string="Appointment date")
    appointment_fee = fields.Char(string="Appointment fee", default=500)
    duration = fields.Char(string="Duration")

    patient = fields.Many2one('bistaclinic.patient', string="Patient")

    @api.onchange('appointment_date')
    def _onchange_fee(self):
        if self and self.appointment_date:
            if (self.patient.create_date - self.appointment_date.now().date()).days <= 90:
                self.appointment_fee = 300

    @api.onchange('appointment_date')
    def _onchange_appointment_date(self):
        if self and self.appointment_date:
            appoint_date = self.appointment_date
            today = datetime.datetime.now()
            print('from appointmnet date ----', (appoint_date))
            print('from dae',today)
            if appoint_date < today :
                raise UserError("Previous date can't be allowed") 
     
    # show available doctor 
    @api.multi
    def show_available_doctor(self):
        message = ''
        name = self.env['bistaclinic.doctor'].search([])
        for rec in name:
            print(rec)
            message += f"Doctor name : {rec.name}\n"
        raise UserError(_(message))

      # show all sechedule
    @api.multi
    def show_all_sechedule(self):
        message = ''
        rec = self.env['bistaclinic.doctor'].search([('first_name','=',self.doctor.first_name)])
        for i in rec:
            print(i.appointment_slot.appointment_date)
            message += f"Appointment date/time: {i.appointment_slot.appointment_date}\n"
        raise UserError(_(message))