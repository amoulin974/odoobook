{
    'name': "library",

    'summary': """
        Application de gestion de livre""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Antoine Moulin",
    'website': "c2i-revision.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'services/library',
    'version': '16.0.1.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    'application': True,
    'license': "AGPL-3",
    # always loaded
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_menu.xml',
        'views/book_views.xml',
        'views/language_views.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/book_detail_template.xml',
        'views/book_list_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
# -*- coding: utf-8 -*-
