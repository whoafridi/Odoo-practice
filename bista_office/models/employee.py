from odoo import fields, models, api, _
from odoo.exceptions import UserError, Warning
from datetime import date
import re  

def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age 

class Employee(models.Model):
    _name = 'office.employee'
    _description = 'Employee model'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age',default=24)
    photo = fields.Binary(string='Image')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string='Gender')
    employee_dob = fields.Date(string="Date of Birth")
    employee_blood_group = fields.Selection(
    	[('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
     	('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],
    	string='Blood Group')
    is_regular = fields.Boolean(string="Is Regular on class", default=True)
    employee_description = fields.Text(string="Description of student")
    employee_salary = fields.Float(string="Salary")
    employee_html = fields.Html(string="Student html")
    employee_image = fields.Binary(string="Upload Student Image")
    phone = fields.Char(string="Type your phone",required=True)
    email = fields.Char(string="Email",required=True)
    
    @api.onchange('employee_dob')
    def onchange_employee_dob(self):
        if self and self.employee_dob:
            today = age(self.employee_dob)
            self.age = today
            
    @api.onchange('age')
    def onchange_age(self):
        if self.age < 24:
            raise UserError(_("You can't qualified"))
            
    @api.onchange('phone')
    def check_phone_number(self):
        if self.phone and len(self.phone) == 0:
            if len(self.phone) == 0:
                raise UserError(_("please type your number"))
        elif self.phone and len(self.phone) != 0:
            pattern = r'{a-zA-Z0-9}'
            regex = re.match(pattern,self.phone)
            if not regex:
                raise UserError(_("Phone number must be valid one"))
            elif len(self.phone) < 11:
                pattern2 = r'\0?[\d]{11}'
                regex2 = re.match(pattern2, self.phone)
                if not regex2:
                    raise UserError(_("Phone number must be 11 characters"))
            elif len(self.phone) > 11:
                pattern = r"\+?[\d]{3}-[\d]{10}"
                regex = re.match(pattern,self.phone)
                if not regex:
                    raise UserError(_('Invalid phone'))
    
    @api.onchange('email')	
    def check_email(self):
        if self.email and len(self.email) == 0:
            raise UserError(_("plaese type email"))
        elif self.email and len(self.email) != 0:
            pattern = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
            regex = re.search(pattern, self.email)
            print(regex)
            if not regex:
                raise UserError(_("Email not valid"))