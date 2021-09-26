from odoo import models, fields

class BBiLagerArtikel(models.Model):
    _name = "bbi.lager.artikel"
    _description = "Das entspräche dem derzeitigen scanbaren teil im lager"
    _rec_name = 'scancode'
    kommiauftragpos_ids = fields.One2many("bbi.lager.kommiauftragpos", "artikel_id", string="Positionen in Kommiaufträgen")
    scancode = fields.Char(required = True , string = 'Scancode der Schütte')
    kubez1 = fields.Char()
    kubez2 = fields.Char()
    category = fields.Char(required = True)
    file = fields.Char()
    #roterpunkt = fields.Selection([
    #    ('count', 'Zählen'),
    #    ('redDot', 'Roter Punkt'),
    #],
    #    required = True,
    #    string = 'Roter Punkt',
    #    default='count',)
    #bewertung = fields.Monetary()
