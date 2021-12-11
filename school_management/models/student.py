from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning
from datetime import date
import re  
import datetime

def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age  

def year(y):
	y = datetime.datetime
	print(y)
	return y    

class Student(models.Model):
	_name = 'school.student'
	_description = 'Students info'

	name = fields.Char(string='Name', required=True)
	age = fields.Integer(string='Age')
	photo = fields.Binary(string='Image')
	gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string='Gender')
	student_dob = fields.Date(string="Date of Birth")
	student_blood_group = fields.Selection(
    	[('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
     	('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],
    	string='Blood Group')
	is_regular = fields.Boolean(string="Is Regular on class", default=True)
	std_description = fields.Text(string="Description of student")
	salary = fields.Float(string="Salary")
	std_html = fields.Html(string="Student html")
	std_image = fields.Binary(string="Upload Student Image")
	average_mark = fields.Float(string="Average mark",required=True)
	phone = fields.Char(string="Type your phone",required=True)
	email = fields.Char(string="Email",required=True)
	admission_date = fields.Date(string='Admission date')
	semester = fields.Selection([('04','Summer'),('05','Fall'),('06','Spring')],string="Semester")
	roll = fields.Char(string='Your roll')
	department = fields.Selection([('01','CSE'),('02','BBA'),('03','EEE'),('04','CE'),('05','ICT'),('06','ICE'),('07','CoE')],string='Department')
	std_id = fields.Char(string='ID No.')

	@api.onchange('student_dob')
	def onchange_student_dob(self):
		if self and self.student_dob:
			today = age(self.student_dob)
			self.age = today

	@api.onchange('age')
	def onchange_age(self):
		if self.age < 0:
			raise UserError(_('Tumi to mayer pet e acho'))

	@api.multi
	def check_mark(self):
		if self.average_mark and self.average_mark < 40.00:
			raise UserError(_("you failed to qualify next class"))
	
	@api.onchange('phone')
	def check_phone_number(self):
		if self.phone and len(self.phone) == 0 :
			raise UserError(_("please type your number"))
				
		elif self.phone and len(self.phone) != 0:
			pattern = r'{a-zA-Z0-9}'
			regex = re.match(pattern,self.phone)
			pattern2 = r'\0?[\d]{11}'
			regex2 = re.match(pattern2, self.phone)
			if not regex2:
				raise UserError(_("Phone number must be valid one"))
			elif len(self.phone) < 11:
				pattern2 = r'\0?[\d]{11}'
				regex2 = re.match(pattern2, self.phone)
				if not regex:
					raise UserError(_("Phone number must be 11 characters"))
			elif len(self.phone) > 11:
				pattern = r"\+?[\d]{3}-[\d]{10}"
				regex = re.match(pattern,self.phone)
			
			# method of regex object.    
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


	@api.onchange('admission_date')
	def change_roll(self):
	 	if self and self.admission_date:
			 date = self.admission_date.year
			 self.std_id = date

	@api.onchange('roll')
	def chnage_(self):
		if self and self.roll:
			sem = ''
			if len(self.roll) == 0:
				raise UserError(_("please type a roll number"))
			elif len(self.roll) == 1:
				sem = self.std_id +  '000' + self.roll
				self.std_id = sem
			elif len(self.roll) == 2:
				sem = self.std_id +  '00' + self.roll
				self.std_id = sem
			elif len(self.roll) == 3:
				sem = self.std_id +  '0' + self.roll
				self.std_id = sem
			elif len(self.roll) == 4:
				sem = self.std_id + self.roll
				self.std_id = sem

	@api.onchange('semester')
	def change_semester(self):
		std_id = ''
		if self and self.semester:
			if self.semester == '04':
				std_id = '12' + self.std_id
				self.std_id = std_id
			elif self.semester == '05':
				std_id = '24' + self.std_id
				self.std_id = std_id
			elif self.semester == '06':
				std_id = '36' + self.std_id
				self.std_id = std_id
	
	@api.onchange('department')
	def change_department(self):
		std_id = ''
		if self and self.department:
			if self.department == '01':
				std_id = '11' + self.std_id
				self.std_id = std_id
			elif self.department == '02':
				std_id = '22' + self.std_id
				self.std_id = std_id
			elif self.department == '03':
				std_id = '33' + self.std_id
				self.std_id = std_id
			elif self.department == '04':
				std_id = '44' + self.std_id
				self.std_id = std_id
			elif self.department == '05':
				std_id = '55' + self.std_id
				self.std_id = std_id
			elif self.department == '06':
				std_id = '66' + self.std_id
				self.std_id = std_id
			elif self.department == '07':
				std_id = '77' + self.std_id
				self.std_id = std_id