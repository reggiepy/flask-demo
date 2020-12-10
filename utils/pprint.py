# coding=utf-8

"""
@author: Reggie
@time:   2018/07/15 21:17
"""


def pprint(msg):
    import json
    p_msg = json.JSONEncoder(ensure_ascii=False, indent=4)
    ret = p_msg.encode(msg)
    print('*-' * 50, '\n')
    print(ret)
    print('\n', '*-' * 50)
    return ret


def main():
    msg = {
        "unit_name": "亨鑫宾馆",
        "orginal_id": "62290011",
        "org_code": "91622924MA734590314",
        "industry_id": 9,
        "unit_type_id": 1,
        "region_id": 3195,
        "address": "城关镇河北新区马家路",
        "tel": "18009300958",
        "online_status": 1,
        "control_center_tel": "5671555",
        "control_center_video_url": "www.xxxx.com",
        "responsible_man_name": "马亨",
        "responsible_man_id": "000000000000000000",
        "responsible_man_tel": "12345678901",
        "fire_manager_name": "未录入",
        "fire_manager_id": "000000000000000000",
        "fire_manager_tel": "12345678901",
        "assist_fire_manager_name": "未录入",
        "assist_fire_manager_id": "000000000000000000",
        "assist_fire_manager_tel": "12345678901",
        "legal_person_name": "未录入",
        "legal_person_id": "000000000000000000",
        "legal_person_tel": "12345678901",
        "staff_count": "20",
        "established_time": "2017-01-01 00:00:00",
        "superior_unit_name": "未录入",
        "admin_unit_name": "未录入",
        "economic_type_id": 4,
        "fixed_assets": 0,
        "area": 500,
        "building_area": 1800,
        "online_date": "2017-11-09 00:00:00",
        "supervise_level_id": 2,
        "supervise_type_id": 1,
        "fire_center_id": 6229001,
        "map_lng": "103.571",
        "map_lat": "35.4892",
        "svg_file": ""
    }
    print(pprint(msg))


if __name__ == '__main__':
    main()
