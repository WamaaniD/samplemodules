from odoo import fields, models

class GoldCrestProfile(models.Model):
    _name = 'gold.connect'
	
    name = fields.Char(string='goldCrest')
    email = fields.Char(string='Email')
    phone = fields.Char('Phone')
	
	  