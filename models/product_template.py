# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import api, fields, models


class ProductLabelFields(models.Model):
    _inherit = 'product.template'

    lote = fields.Char('Lote')
    fecha_fab = fields.Date('Fecha de fabricación')
    fecha_ven = fields.Date('Fecha de vencimiento')
    peso = fields.Float('Peso kg')
    vida_util = fields.Char('Vida útil')
    footer = fields.Char('Pie de página')
