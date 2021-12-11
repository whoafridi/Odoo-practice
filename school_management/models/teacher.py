from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning
from datetime import date

def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

class Teacher(models.Model):
    _name = 'school.teacher'
    _description = "Teachers Info"

    name = fields.Char(string="Teacher name", required=True)
    age = fields.Integer(string="Age")
    gender = fields.Selection([('male','Male'),('female','Female'),('others','Others')],string='Gender')
    joining_date = fields.Date(String='Joining Date',required=True)
    teacher_courses = fields.Selection([('oop','OOP'),('swe','SWE'),('ai','AI')],string='Select course',required=True)
    teacher_blood_group = fields.Selection(
    	[('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
     	('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],
    	string='Blood Group')
    is_regular = fields.Boolean(string="Is Regular on class", default=False)
    teacher_description = fields.Text(string="Description of teacher")
    teacher_salary = fields.Float(string="Salary",default=20000,required=True)
    salary = fields.Float(string="Gross Salary",required=True)
    teacher_html = fields.Html(string="Student html")
    teacher_image = fields.Binary(string="Upload Student Image")
    salary_bonus = fields.Float(string="Bonus",required=True)
    teacher_exp = fields.Selection([('0','0 yrs'),('1','1 yrs'),('2','2 yrs'),('3','3 yrs')],string="Please select your experience")
    service_year = fields.Integer(string="Teacher Service year")

    @api.onchange('teacher_exp')
    def salary_onchange(self):
        salary = 0
        if self and self.teacher_exp:
            if self.teacher_exp == '0':
                salary = salary + 100
                self.salary_bonus = salary
            elif self.teacher_exp == '1':
                salary = salary + 200
                self.salary_bonus = salary
            elif self.teacher_exp == '2':
                salary = salary + 300
                self.salary_bonus = salary
            else:
                salary = salary + 500
                self.salary_bonus = salary

    @api.onchange('salary_bonus')
    def salary_change(self):
        teacher_salary = 0
        if self and self.salary_bonus:
            teacher_salary = self.salary_bonus + self.teacher_salary 
            self.salary = teacher_salary


    @api.onchange('age')
    def onchage_age(self):
        if self.age < 0:
            raise UserError(_("Zero can't be taken"))
        elif self.age > 0 and self.age <=24:
            raise UserError(_("This isn't an age of teaching/ No experiecne"))


    @api.onchange('joining_date')
    def joini(self):
        if self and self.joining_date:
            active_date = age(self.joining_date)
            self.service_year = active_date


    @api.multi
    def check_status(self):
        raise UserError(_('I am fron button action'))