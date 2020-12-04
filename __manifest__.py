# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Gold Crest',
    'version' : '1.1',
    'summary': 'Loan Repayments Monitoring',
    'sequence': 2,
    'description': """  
Monitoring Loan Payments
====================
The specific and easy-to-use loan repayment monitoring system in Odoo allows you to keep track of your payments, even when you are not an accountant. It provides an easy way to follow up on your loan clients.

You could use this simplified accounting in case you work with an (external) account to keep your books, and you still want to keep track of payments. This module also offers you an easy method of registering payments, without having to encode complete abstracts of account.
    """,
    'category': 'Finance',
    'website': 'https://www.goldconnect.com',
    'images' : ['images/accounts.jpeg','images/bank_statement.jpeg','images/cash_register.jpeg','images/chart_of_accounts.jpeg','images/customer_invoice.jpeg','images/journal_entries.jpeg'],
    'depends' : ['base'],
    'data': [ "views/goldcrest_views.xml",
              "security/ir.model.access.csv"],
    'demo': [],

    'installable': True,
    'application': True,
    'auto_install': False,
}
