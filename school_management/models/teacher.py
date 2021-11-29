from odoo import models, fields

class Teacher(models.Model):
    _name = 'school.teacher'

    name = fields.Char(string="Teacher name", required=True)
    age = fields.Integer(string="Age")
    gender = fields.Selection([('male','Male'),('female','Female'),('others','Others')],string='Gender',default="Others")
    joining_date = fields.Datetime(String='Joining Date',default=fields.Datetime.now(),required=True)
    teacher_courses = fields.Selection([('oop','OOP')],string='Select course',required=True)
    teacher_blood_group = fields.Selection(
    	[('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
     	('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],
    	string='Blood Group')