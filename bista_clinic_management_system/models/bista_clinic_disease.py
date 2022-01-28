from odoo import models, fields

class Bista_Clinic_Diseases(models.Model):
    _name = 'bistaclinic.diseases'
    _description = 'bista clinic diseases info'

    name = fields.Char(string="Diseases Name", required=True)
    description = fields.Char(string="Description of diseases")
    
    specialized_doctor = fields.Many2many('bistaclinic.doctor',string="Specialized doctor")
 