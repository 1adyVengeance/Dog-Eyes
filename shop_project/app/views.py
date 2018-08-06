from flask import Blueprint, render_template, request, jsonify
from dataMaker.data_maker import good_maker

import datetime

api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('')
def home():
    return render_template('index.html')


@api_blueprint.route('/api/<price_low>/<price_high>/<date_low>/<date_high>/<num>/<t_num>/')
def get_api(price_low, price_high, date_low, date_high, num, t_num):
    if request.method == 'GET':

        num = int(num)
        t_num = int(t_num)

        # 商品种类必须大于等于 1
        if t_num < 1:
            return jsonify('Good type must more than one')

        # 单次获取商品数不得大于 1 万
        if num > 10000:
            return jsonify('Good number must be lower than 10000')

        date_low = date_low + ' 08:00:00'
        date_high = date_high + ' 21:00:00'

        # 检查日期是否溢出
        try:
            low = datetime.datetime.strptime(date_low, '%Y-%m-%d %H:%M:%S')
            high = datetime.datetime.strptime(date_high, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            return jsonify('DateError')

        # 检查日期是否区间是否正确
        if low > high:
            temp = date_low
            date_low = date_high
            date_high = temp

        price_region = [price_low, price_high]
        price_region = list(map(lambda x: int(x), price_region))

        if price_region[0] > price_region[1]:
            temp = price_region[0]
            price_region[0] = price_region[1]
            price_region[1] = temp

        date_region = [date_low, date_high]

        goods = []
        for i in range(num):
            goods.append(good_maker(t_num, price_region, date_region))

        ctx = {
            'code': 200,
            'goods': goods
        }

        return jsonify(ctx)
