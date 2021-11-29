{	
    'name': 'School-management',
    'description':'this module is for school management.',
    'version': '1.0',	
    'summary': 'Record all Information',	
    'category': 'Tools',	
    'author': '@Rafi',	
    'depends': ['base'], 
    'data': [  
        'security/ir.model.access.csv',
        'views/student_view.xml',
        'views/teacher_view.xml'	
            ],	
    'license': 'AGPL-3',
    'installable': True,
    'application': False,	
    'auto_install': False
}