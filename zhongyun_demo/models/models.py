import string
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class ZyStatistics(models.Model):
    # 中运物流统计业务
    _name = 'zy.statistics'  
    _description = 'Business Statistics'
    # 继承消息部分
    _inherit = ['mail.thread', 'mail.activity.mixin'] # track_visibility

    # 字段 单据编号 必填项
    document_sequence = fields.Char('单据编号', required=True)

    # 跟踪字段 
    is_done_track_onchange = fields.Boolean(
        string='是否完成？', default=False, tracking=True)
    name_track_always = fields.Char(string="track_name", tracking=True)
    
    # 字段 运输物料名称 
    transport_material_name = fields.Char('运输物料名称')

    # 字段 供应商
    supplier = fields.Char('发货人（供应商）')

    # 字段 发货时间 
    # 字段 出厂时间 
    delivery_date = fields.Date('发货时间')
    manufacture_date = fields.Date('出厂时间')

    # float digits
    # field tutorial
    net_weight = fields.Float(string='净重', digits=(10,2))
    primary_weight = fields.Float(string='原发数', digits=(10,2))

    # 字段 运输单位
    transport_company = fields.Char(string='运输单位')

    # 发货地点
    delivery_location = fields.Char(string='发货地点')
    
    # 起运地
    port_shipment = fields.Char(string='起运地')

    # 止运地
    stop_shipment = fields.Char(string='止运地')

    # 燃油车车号
    fuel_car_number = fields.Char(string='燃油车车号')

    # 电动汽车承运单位
    electric_car_transport_company = fields.Char(string='电动汽车承运单位')

    # 备注
    remarke = fields.Text('备注')


    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'Description must be unique'),
    ]

    @api.constrains('delivery_date', 'manufacture_date')
    def _check_date(self):
        for data in self:
            if data.delivery_date >= data.manufacture_date:
                raise ValidationError(
                    "data.manufacture_date  > data.delivery_date"
                )
