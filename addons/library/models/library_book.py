# -*- coding: utf-8 -*-

from odoo import models, fields, api


class book(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------
    _name = 'library.book'
    _description = 'Book of library'

    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic
    name = fields.Char("Title")
    isbn = fields.Char("Isbn")
    active = fields.Boolean("Actif ?", default=True)
    date_published = fields.Date(string="Publish date")
    image = fields.Binary("Cover")

