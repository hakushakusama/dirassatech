{
    'name': 'Education Module',
    'version': '1.0',
    'summary': 'Educational module with question bank and ELO system',
    'author': 'Your Name',
    'category': 'Education',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/question_view.xml',
        'views/student_view.xml',
        'views/teacher_view.xml',
    ],
    'installable': True,
    'application': True,
}
