from odoo import models, fields

class BBiKommiauftrag(models.Model):
    _name = "bbi.lager.kommiauftrag"
    _description = "Eine idee, wie kommisionierungsaufträge laufen könnten"
    _rec_name = 'projekt_id'
    projekt_id = fields.Char(required = True , string = 'Projektreferenz, Kostenstelle')
    kommiauftragpos_ids = fields.One2many('bbi.lager.kommiauftragpos', 'kommiauftrag_id', 'Kommiauftrag Positionen', copy=True)
    kubez1 = fields.Char()
    kubez2 = fields.Char()
    state = fields.Selection([('1', 'wird angelegt'),
        ('2', 'Freigabe für Beschaffung'),
        ('3', 'Freigabe für Kommissionierung'),
        ('4', 'Teilkommissioniert'),
        ('5', 'Vollständig Kommisioniert')],
        required = True,
        default = "1")
    montagesoll = fields.Date(required = True)

    def eine_methode(self):
        print('aloa')
        #print(self.id)

    #geht mit state=1 rein per default constrait
    def action_kommiauftrag_changeState(self):
        print(self.state)
        if self.state == "1":
            self.state="2"
        elif self.state == "2":
            self.state="3"
        elif self.state == "3":
            self.state="4"
        elif self.state == "4":
            self.state="5"
        elif self.state == "5":
            self.state="4"

    def action_kommiauftrag_1(self):
        print('aloa')
