from num2words import num2words

from odoo import models, tools


class ResCurrency(models.Model):
    _inherit = "res.currency"

    def amount_to_text_vn(self, amount):
        lang = tools.get_lang(self.env)
        if lang and lang.iso_code == 'vi':
            return tools.ustr(' {amt_value} {amt_word}').format(
                amt_value=num2words(amount, lang='vi_VN'),
                amt_word='VND',
            )
        return self.amount_to_text(amount)
