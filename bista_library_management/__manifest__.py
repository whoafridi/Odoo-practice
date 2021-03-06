{
    'name': 'Bista-library-management',
    'description': 'this module is for @Bista library management.',
    'version': '1.0',
    'summary': 'Record all Information',
    'author': 'Rafi',
    'sequence': 2,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/book_view.xml',
        'views/library_branch_view.xml',
        'views/author_view.xml',
        'views/publisher_view.xml',
        'views/book_request_view.xml',
        'views/librarian_view.xml',
        'views/library_view.xml',
        'views/user_view.xml',
        'views/borrow_history_view.xml',
        'views/activity_view.xml',
        'views/search_view.xml'
    ],
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False
}
