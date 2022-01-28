{
    'name': 'Bista Clinic Management System',
    'description': 'this module is for Bista Clinic Management System',
    'version': '1.0',
    'sequence': 3,
    'summary': 'Record all Information about doctor/clinic',
    'category': '',
    'author': 'bista_test',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/bista_clinic_view.xml',
        'views/bista_clinic_employee_view.xml',
        'views/bista_clinic_doctor_view.xml',
        'views/bista_clinic_patient_view.xml',
        'views/bista_clinic_disease_view.xml',
        'views/bista_clinic_appointment_view.xml',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False
}
