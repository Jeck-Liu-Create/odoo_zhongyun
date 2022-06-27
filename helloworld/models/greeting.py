from odoo import models, fields


class Greeting(models.Model):
    _name = "helloworld.greeting"
    _description = "greeting"
    message = fields.Char('问候语')