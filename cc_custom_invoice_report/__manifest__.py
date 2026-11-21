# -*- coding: utf-8 -*-
{
    'name': 'Corporate Custom Invoice PDF Reports',
    'version': '17.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Professional executive invoice layout with custom header/footer, amount in words, and clean A4 paperformat.',
    'description': """
Corporate Custom Invoice PDF Reports
====================================
Transform your standard Odoo customer invoices and vendor bills into beautifully formatted, executive-grade PDF documents.

Key Features:
-------------
* Elegant corporate header and footer with company branding, tax registration, and contact details
* Dynamic Amount in Words conversion (Riyals/Halalas, Dollars/Cents, Pounds/Pence)
* Custom high-resolution A4 paperformat with optimized printing margins (12mm)
* Itemized line breakdown showing discounts, taxes, and net subtotals with high clarity
* Dual support for English and bilingual invoice layouts
* Zero external third-party dependencies; fully compatible with Odoo Community and Enterprise
    """,
    'author': 'CODCrafters, Usman Ghias',
    'website': 'https://usmanghias.co.uk',
    'support': 'support@codcrafters.org',
    'license': 'OPL-1',
    'price': 14.00,
    'currency': 'EUR',
    'depends': ['account', 'sale'],
    'data': [
        'reports/report_paperformat.xml',
        'reports/report_header.xml',
        'reports/report_invoice_template.xml',
        'reports/report_action.xml',
    ],
    'images': [
        'static/description/banner.png',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
