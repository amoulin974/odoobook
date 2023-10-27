# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

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


    def _check_isbn(self):
        self.ensure_one()  # vérifie que quel self contient 1 seul record.
        total = 0
        digits = [int(x) for x in str(self.isbn)]
        if len(digits) == 13:
            for index, digit in enumerate(digits[:12]):
                if (index % 2) == 0:
                    total += digit
                else:
                    total += digit * 3

        reste = total % 10
        cleTheorique = 10 - reste if reste != 0 else 0
        return digits[-1] == cleTheorique

    def button_check_isbn(self):
        for book in self:
            if not book.isbn:
                raise (ValidationError("Please provide an ISBN for this book"))
            if book.isbn and not book._check_isbn():
                raise ValidationError("%s isbn is invalid" % (book.isbn))