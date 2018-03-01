# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['StockSupplyStart', 'StockSupply']


class StockSupplyStart:
    __metaclass__ = PoolMeta
    __name__ = 'stock.supply.start'

    warehouses = fields.Many2Many('stock.location', None, None, 'Warehouses',
        domain=[
            ('type', '=', 'warehouse'),
            ])


class StockSupply:
    __metaclass__ = PoolMeta
    __name__ = 'stock.supply'

    @property
    def _production_parameters(self):
        parameters = super(StockSupply, self)._requests_parameters
        if self.start.warehouses:
            parameters['warehouses'] = self.start.warehouses
        return parameters
