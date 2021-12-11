{	
    'name': 'Bista-office',
    'description':'this module is for @Bista Bangladesh office.',
    'version': '1.0',	
    'summary': 'Record all Information',	
    'author': 'whoRafi',	
    'sequence':2,
    'depends': ['base'], 
    'data': [  
        'security/ir.model.access.csv',
         'views/employee_view.xml',
        # 'views/teacher_view.xml'	
            ],	
    'license': 'AGPL-3',
    'installable': True,
    'application': False,	
    'auto_install': False
}