from odoo import models, fields

class BBiKommiauftragpos(models.Model):
    _name = "bbi.lager.kommiauftragpos"
    _description = "Eine Position im Kommiauftrag"
    kommiauftrag_id = fields.Many2one('bbi.lager.kommiauftrag', 'Aus Kommiauftrag', required = True)
    projekt = fields.Char(related='kommiauftrag_id.projekt_id',readonly=True,store=False)
    projektbez = fields.Char(related='kommiauftrag_id.kubez1',readonly=True,store=False,string="Proj.-Bez.1")
    artikel_id = fields.Many2one('bbi.lager.artikel', string="Artikel", required = True)
    scancode = fields.Char(related='artikel_id.scancode',readonly=True,store=False)
    kubez1 = fields.Char(related='artikel_id.kubez1',readonly=True,store=False,string="Artikel-Bez.1")
    kubez2 = fields.Char(related='artikel_id.kubez2',readonly=True,store=False,string="Artikel-Bez.2")
    soll = fields.Integer(required = True)
    ist = fields.Integer(required = True)
