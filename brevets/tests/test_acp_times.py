"""
Nose tests for acp_times.py

Write your tests HERE AND ONLY HERE.
"""

from acp_times import open_time, close_time
import arrow
import nose    # Testing framework
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

def check_brevets(checkpoint_dict, dist, start_time):
    for km, time_tuple in checkpoint_dict.items():
        checkpoint_open, checkpoint_close = time_tuple
        assert open_time(km, dist, start_time) == checkpoint_open
        assert close_time(km, dist, start_time) == checkpoint_close

def test_brevet1():
    start_time = arrow.get("2023-02-22 00:00", "YYYY-MM-DD HH:mm")
    dist = 200
    checkpoints = {
        0: (start_time, start_time.shift(hours=1)),
        50: (start_time.shift(hours=1, minutes=28), start_time.shift(hours=3.5)),
        100: (start_time.shift(hours=2, minutes=56), start_time.shift(hours=6, minutes=40)),
        150: (start_time.shift(hours=4, minutes=25), start_time.shift(hours=10)),
        200: (start_time.shift(hours=5, minutes=53), start_time.shift(hours=13.5)), 
            }
    check_brevets(checkpoints, dist, start_time)

def test_brevet2():
    start_time = arrow.get("2023-02-22 00:00", "YYYY-MM-DD HH:mm")
    dist = 200
    checkpoints = {
        0: (start_time, start_time.shift(hours=1)),
        60: (start_time.shift(hours=1, minutes=46), start_time.shift(hours=4)),
        120: (start_time.shift(hours=3, minutes=32), start_time.shift(hours=8)),
        175: (start_time.shift(hours=5, minutes=9), start_time.shift(hours=11, minutes=40)),
        205: (start_time.shift(hours=5, minutes=53), start_time.shift(hours=13.5)), 
            }
    check_brevets(checkpoints, dist, start_time)

def test_brevet3():
    start_time = arrow.get("2023-02-22 00:00", "YYYY-MM-DD HH:mm")
    dist = 400
    checkpoints = {
        0: (start_time, start_time.shift(hours=1)),
        50: (start_time.shift(hours=1, minutes=28), start_time.shift(hours=3.5)),
        100: (start_time.shift(hours=2, minutes=56), start_time.shift(hours=6, minutes=40)),
        150: (start_time.shift(hours=4, minutes=25), start_time.shift(hours=10)),
        200: (start_time.shift(hours=5, minutes=53), start_time.shift(hours=13, minutes=20)),
        250: (start_time.shift(hours=7, minutes=27), start_time.shift(hours=16, minutes=40)),
        300: (start_time.shift(hours=9, minutes=1), start_time.shift(hours=20)),
        350: (start_time.shift(hours=10, minutes=34), start_time.shift(hours=23, minutes=20)),
        400: (start_time.shift(hours=12, minutes=8), start_time.shift(days=1, hours=3)),
            }
    check_brevets(checkpoints, dist, start_time)

def test_brevet4():
    start_time = arrow.get("2023-02-22 00:00", "YYYY-MM-DD HH:mm")
    dist = 1000
    checkpoints = {
        0: (start_time, start_time.shift(hours=1)),
        100: (start_time.shift(hours=2, minutes=56), start_time.shift(hours=6, minutes=40)),
        500: (start_time.shift(hours=15, minutes=28), start_time.shift(days=1, hours=9, minutes=20)),
        700: (start_time.shift(hours=22, minutes=22), start_time.shift(days=2, minutes=45)), 
        999: (start_time.shift(days=1, hours=9, minutes=3), start_time.shift(days=3, hours=2, minutes=55)), 
        1000: (start_time.shift(days=1, hours=9, minutes=5), start_time.shift(days=3, hours=3)), 
            }
    check_brevets(checkpoints, dist, start_time)

def test_brevet5():
    start_time = arrow.get("2023-02-22 00:00", "YYYY-MM-DD HH:mm")
    dist = 200
    checkpoints = {
        0: (start_time, start_time.shift(hours=1)),
        10: (start_time.shift(minutes=18), start_time.shift(hours=1, minutes=30)),
        20: (start_time.shift(minutes=35), start_time.shift(hours=2)),
        50: (start_time.shift(hours=1, minutes=28), start_time.shift(hours=3, minutes=30)),
        61: (start_time.shift(hours=1, minutes=48), start_time.shift(hours=4, minutes=4)),
        200: (start_time.shift(hours=5, minutes=53), start_time.shift(hours=13.5)), 
            }
    check_brevets(checkpoints, dist, start_time)


