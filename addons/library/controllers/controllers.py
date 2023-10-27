# -*- coding: utf-8 -*-
from odoo import http


class Books(http.Controller):
    @http.route('/library/allbooks', type='http', auth='public', website=True)
    def index(self, **kwargs):
        Book = http.request.env["library.book"]
        books = Book.search([])
        return http.request.render(
            "library.book_list_template",
            {"books": books}
        )
    @http.route("/library/allbooks/<model('library.book'):book>", type='http', auth="public", website=True)
    def detail(self, book):
        return http.request.render(
            "library.book_detail_template",
            {"book": book}
        )
