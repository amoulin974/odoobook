# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class language(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------
    _name = 'library.language'
    _description = 'Language of book'

    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic
    name = fields.Char("text")
    flag = fields.Binary("Flag")

    # Relational
    book_ids = fields.Many2many(
        "library.book",
        string="Language's book"
    )