# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .production import *


def register():
    Pool.register(
        CreateProductionRequestStart,
        module='stock_supply_production_warehouse', type_='model')
    Pool.register(
        CreateProductionRequest,
        module='stock_supply_production_warehouse', type_='wizard')
