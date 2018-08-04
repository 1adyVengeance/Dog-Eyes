from random import randint
from time import mktime
from math import log10
from setting import INITIAL_VALUES
import datetime


def main():
    # time = time_maker('2018-1-1 00:00:00', '2030-1-1 23:59:59')

    for i in range(100):
        # print(score_maker())
        print(region_maker())


def time_maker(begin, end):
    """
    make a random date
    :param begin: beginning of date
    :param end: end of date
    :return: a random date whose type is the datetime
    """
    def trans(time):
        time_list = time.split(' ')
        time_tuple = tuple(time_list[0].split('-') + time_list[1].split(':'))

        time_tuple = tuple(map(int, time_tuple))

        return mktime(time_tuple+(0, 0, 0))

    # translate into a string date
    time0 = randint(trans(begin), trans(end))
    time0 = datetime.datetime.fromtimestamp(time0)
    time0 = time0.strftime(r'%Y-%m-%d %H:%M:%S')

    return time0

#
# def type_maker(n, str0=0):
#     if str0 == 0:
#         return '原料编号%s' % n
#     else:
#         return str0
#
#
# def taste_maker(n, str0=0):
#     if str0 == 0:
#         return '口味编号%s' % n
#     else:
#         return str0
#
#
# def material_maker(n, str0=0):
#     if str0 == 0:
#         return '原料编号%s' % n
#     else:
#         return str0
#
#
# def recipe_maker():
#     return None


def price_maker(low, high):
    """
    make a random price
    :param low: low value
    :param high: high value
    :return: integer price
    """
    return randint(low, high)


def score_maker():
    """
    make a score based on the formula: score = 5 x log10( )
    :return: a float score
    """
    score = log10(randint(1, 100)) * 5

    return round(score, 1)


def region_maker():
    """
    make a place
    :return: a str place
    """
    places = INITIAL_VALUES.get('PLACES')

    return places[randint(0, len(places))-1]


def good_maker(good_num,  price_region, time_region):
    """
    create a good
    :param good_num: the number of the good
    :param price_region: the price region of the good
    :param time_region: the date region of the good
    :return: a dict good
    """
    good_dict = {
        'name': '商品编号%s' % good_num,
        'price': price_maker(price_region[0], price_region[1]),
        'score': score_maker(),
        'place': region_maker(),
        'sold_time': time_maker(time_region[0], time_region[1])
    }

    return good_dict


if __name__ == '__main__':
    main()
