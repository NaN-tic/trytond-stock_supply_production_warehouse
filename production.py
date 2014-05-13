#The COPYRIGHT file at the top level of this repository contains the full
#copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['CreateProductionRequestStart', 'CreateProductionRequest']
__metaclass__ = PoolMeta


class CreateProductionRequestStart:
    __name__ = 'production.create_request.start'

    warehouses = fields.Many2Many('stock.location', None, None, 'Warehouses',
        domain=[
            ('type', '=', 'warehouse'),
            ])


class CreateProductionRequest:
    __name__ = 'production.create_request'

    @property
    def _requests_parameters(self):
        res = super(CreateProductionRequest, self)._requests_parameters
        if self.start.warehouses:
            res.update({
                    'warehouses': self.start.warehouses
                    })
        return res
