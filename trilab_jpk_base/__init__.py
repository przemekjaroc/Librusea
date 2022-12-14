# -*- coding: utf-8 -*-

from odoo import api, SUPERUSER_ID
from . import models


PARAMETER = 'trilab_jpk_base.taxoffice_loaded'


def post_init_handler(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    if not env['ir.config_parameter'].get_param(PARAMETER, False):
        env['jpk.taxoffice'].load_from_xml()
        env['ir.config_parameter'].set_param(PARAMETER, True)

    # hide main menu icon
    menu_data = env['ir.model.data'].search([['name', '=', 'jpk_main_menu'],
                                             ['module', '=', 'trilab_jpk_base'],
                                             ['model', '=', 'ir.ui.menu']])
    if menu_data:
        menu_item = env['ir.ui.menu'].browse([menu_data.res_id])
        menu_item.write({'active': False})


def uninstall_handler(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['ir.config_parameter'].set_param(PARAMETER, False)
