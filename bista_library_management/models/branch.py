from odoo import fields, models, api

class Branch(models.Model):
    _name = 'library.branch'
    _description = 'library branch info'

    name = fields.Char(string="Branch name", required=True)
    branch_address = fields.Char(string='Branch address')
    division = fields.Selection([('dhaka','Dhaka'),('chittagong','Chittagong'),('rangpur','Rangpur'),('sylhet','Sylhet'),('barishal','Barishal')], string='Division')
    contact = fields.Char(string="Contact details")
    email = fields.Char(string='Email')
    branch_id = fields.Char(string='Branch ID')

    @api.multi
    def check_author(self):
        rec = self.env['library.borrowhistory'].search([('branch.name','=',self.name)])
        for i in rec:
            print('----book name----', i.borrow_book_title.name.name,'----author name----', i.borrow_book_title.author.name,'----borrower name----',i.borrower_name.name,'---- email ----', i.borrower_name.email,'\n')

    @api.onchange('division')
    def change_id(self):
        id = ''
        if self and self.division == 'dhaka':
            id = '101'
            self.branch_id = id
        elif self and self.division == 'chittagong':
            id = '202'
            self.branch_id = id
        elif self and self.division == 'rangpur':
            id = '303'
            self.branch_id = id
        elif self and self.division == 'sylhet':
            id = '404'
            self.branch_id = id
        elif self and self.division == 'barishal':
            id = '505'
            self.branch_id = id