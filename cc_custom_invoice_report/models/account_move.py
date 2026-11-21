# -*- coding: utf-8 -*-
from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    amount_in_words = fields.Char(
        string="Amount in Words",
        compute='_compute_amount_in_words',
        store=True,
        help="Automated textual amount representation for official printed reports."
    )

    @api.depends('amount_total', 'currency_id')
    def _compute_amount_in_words(self):
        for move in self:
            currency_name = move.currency_id.name or 'USD'
            move.amount_in_words = self._convert_amount_to_words(move.amount_total, currency_name)

    def _convert_amount_to_words(self, amount, currency_name='USD'):
        amount = round(amount, 2)
        units = int(amount)
        cents = int(round((amount - units) * 100))

        if currency_name in ('SAR', 'SAR '):
            unit_str = f"{units} Riyal" if units == 1 else f"{units} Riyals"
            sub_str = f"{cents} Halala" if cents == 1 else f"{cents} Halalas"
        elif currency_name == 'EUR':
            unit_str = f"{units} Euro" if units == 1 else f"{units} Euros"
            sub_str = f"{cents} Cent" if cents == 1 else f"{cents} Cents"
        elif currency_name == 'GBP':
            unit_str = f"{units} Pound" if units == 1 else f"{units} Pounds"
            sub_str = f"{cents} Penny" if cents == 1 else f"{cents} Pence"
        else:
            unit_str = f"{units} Dollar" if units == 1 else f"{units} Dollars"
            sub_str = f"{cents} Cent" if cents == 1 else f"{cents} Cents"

        if cents > 0:
            return f"{unit_str} and {sub_str}"
        return unit_str
