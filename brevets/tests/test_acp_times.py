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
        150: (start_time.shift(hours=4, minutes=25), start_time.shift(hours=10)),
        200: (start_time.shift(hours=5, minutes=53), start_time.shift(hours=13.5)), 
            }
    check_brevets(checkpoints, dist, start_time)


