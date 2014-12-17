from openerp.osv import fields,osv
from openerp import tools

 
class account_check(osv.osv):
    _name = "account.check"
    _inherit = 'account.check'
    _description = "Account Check"
    _columns = {
	'warehouse_id': fields.many2one('stock.warehouse','Warehouse'),
	}
 
account_check()
