# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class notice(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------
    _name = 'library.notice'
    _description = 'Notice of book'

    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic
    text = fields.Html("Text of notice")
    note = fields.Integer("Note / 5")
    active = fields.Boolean("Actif ?", default=True)

    #relational
    book_id = fields.Many2one("library.book", string="Book")

    #related
    book_cover=fields.Binary(related="book_id.image", string="book_cover")