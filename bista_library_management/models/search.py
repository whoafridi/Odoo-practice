from odoo import fields, models, api, _
from odoo.exceptions import UserError

class Search(models.Model):
    _name = 'library.search'
    _description = 'search info'

    book_name = fields.Many2one('library.book',string='Book name')
    reader_name = fields.Many2one('library.user',string='Reader name')
    branch_name = fields.Many2one('library.branch',string='Branch name')
    publisher = fields.Many2one('library.publisher',string='Publisher name')
    author = fields.Many2one('library.author',string='Author name')
    library = fields.Many2one('library.library',string='Library')
    librarian = fields.Many2one('library.librarian',string='Librarian')

    # show author details
    @api.multi
    def details_author(self):
        name = self.env['library.author'].search([('name','=',self.author.name)])
        for rec in name:
            message = f"Author name : {self.author.name} - Author ID: {self.author.author_id } - Book name : {self.author.book_name.name}"
            raise UserError(_(message))

    # show book details
    @api.multi
    def details_bookname(self):
        name = self.env['library.book'].search([('name','=',self.book_name.name)])
        for rec in name:
            message = f"Book name : {self.book_name.name} - Author name: {self.book_name.author.name} - Price : {self.book_name.price}"
            raise UserError(_(message))

    # show reader details
    @api.multi
    def details_reader(self):
        name = self.env['library.user'].search([('name','=',self.reader_name.name)])
        for rec in name:
            message = f"Reader name : {self.reader_name.name} - ID: {self.reader_name.user_id} - Email : {self.reader_name.email}"
            raise UserError(_(message))

    # show branch details
    @api.multi
    def details_branch(self):
        name = self.env['library.branch'].search([('name','=',self.branch_name.name)])
        for rec in name:
            message = f"Branch name : {self.branch_name.name} - Branch ID: {self.branch_name.branch_id} - Address : {self.branch_name.branch_address}"
            raise UserError(_(message))

    # show branch details
    @api.multi
    def details_publisher(self):
        name = self.env['library.publisher'].search([('name','=',self.publisher.name)])
        for rec in name:
            message = f"Publisher name : {self.publisher.name} - Publisher book name : {self.publisher.book_name.name} - Address : {self.publisher.address}"
            raise UserError(_(message))
    
    # show library details
    @api.multi
    def details_library(self):
        name = self.env['library.library'].search([('name.name','=',self.library.name.name)])
        for rec in name:
            message = f"Book name : {self.library.name.name} - Branch : {self.library.branch.name} - Quantity : {self.library.quantity}"
            raise UserError(_(message))

    # show librarian details
    @api.multi
    def details_librarian(self):
        name = self.env['library.librarian'].search([('name','=',self.librarian.name)])
        for rec in name:
            message = f"Librarian name : {self.librarian.name} - Id : {self.librarian.user_id} - Email : {self.librarian.email}"
            raise UserError(_(message))

    #show borrowhistory
    @api.multi 
    def show_borrowhistory(self):
        print('--- from self ---',self.book_name.name, self.reader_name.name, self.author.name)
        message = ''
        # book name, author name, reader name
        if self.book_name.name and self.reader_name.name and self.author.name:
            rec = self.env['library.borrowhistory'].search([
                ('borrow_book_title.name.name','=',self.book_name.name),('borrower_name.name','=',self.reader_name.name),
                ('borrow_book_title.author.name','=',self.author.name)])

        # book name/author and book/reader and author/reader                
        elif self.book_name.name and self.reader_name.name or self.book_name.name and self.author.name or self.reader_name.name and self.author.name:
            print("#### 1 ####")
            rec = self.env['library.borrowhistory'].search([
                '|','|',
                '&',('borrow_book_title.name.name','=',self.book_name.name),('borrower_name.name','=',self.reader_name.name),
                '&',('borrow_book_title.name.name','=',self.book_name.name),('borrow_book_title.author.name','=',self.author.name),
                '&',('borrower_name.name','=',self.reader_name.name),('borrow_book_title.author.name','=',self.author.name)])
        
        # book name or author or reader 
        elif self.book_name.name or self.author.name or self.reader_name.name:
            rec = self.env['library.borrowhistory'].search(['|','|',
                ('borrow_book_title.name.name','=',self.book_name.name),('borrow_book_title.author.name','=',self.author.name),
                ('borrower_name.name','=',self.reader_name.name)
                ])
            
        if rec:
            for i in rec:
                print(i.borrow_book_title.name.name,self)
                message += f"Book name : {i.borrow_book_title.name.name} - Borrower name : {i.borrower_name.name} - Branch name : {i.branch.name} - Quantity : {i.quantity}\n"
            raise UserError(_(message))
        else:
            raise UserError(_("Requested user not borrow any book"))
            

    # show activity
    @api.multi 
    def show_activity(self):
        print(self.book_name.name, self.reader_name.name)
        message = ''
        if self.book_name.name and self.reader_name.name:
            rec = self.env['library.activity'].search([
                    ('book_name.name','=',self.book_name.name),('reader_name.name','=',self.reader_name.name)
                    ])
        elif self.book_name.name or self.reader_name.name:
            print("### 2 ###")
            rec = self.env['library.activity'].search(['|',('book_name.name','=',self.book_name.name),
                ('reader_name.name','=',self.reader_name.name)])
    
        if rec:
                for i in rec:
                    print(i.book_name.name, self)
                    message += f"Book name : {i.book_name.name} - Reader name : {i.reader_name.name} - email : {i.reader_name.email} - exit time : {i.exit_time}\n"
                raise UserError(_(message))
        else:
                raise UserError(_("Requested user don't have any activity"))
    
    #show requested book
    @api.multi 
    def show_requestedbook(self):
        print(self.book_name.name, self.author.name, self.branch_name.name)
        message = ''
        # book and author and branch
        if self.book_name.name and  self.author.name and self.branch_name.name:
            print("#################### 1 ###################")
            rec = self.env['library.bookrequest'].search([('title.name','=',self.book_name.name),('author.name','=',self.author.name),('branch.name','=',self.branch_name.name)])

        # book/author and author/book and branch/author
        elif self.book_name.name and self.branch_name.name or self.book_name.name and self.author.name or self.author.name and self.branch_name.name:
            print("#################### 3 ###################")
            rec = self.env['library.bookrequest'].search([
                '|','|',
                '&',('title.name','=',self.book_name.name),('branch.name','=', self.branch_name.name),
                '&',('title.name','=',self.book_name.name),('author.name','=',self.author.name),
                '&',('author.name','=',self.author.name),('branch.name','=',self.branch_name.name)
                ])

        # book or author or branch
        elif self.book_name.name or self.author.name or self.branch_name.name:
            print("#################### 2 ###################")
            rec = self.env['library.bookrequest'].search([
                '|','|',
                ('title.name','=',self.book_name.name),
                ('author.name','=',self.author.name),('branch.name','=', self.branch_name.name)])
        
        if rec:
            for i in rec:
                message += f"Book name : {i.title.name} - Requested by : {i.requested_by.name} Author : {i.author.name}\n"
            raise UserError(_(message))
        else:
            raise UserError(_("user don't request any book"))      
