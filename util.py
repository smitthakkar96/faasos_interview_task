"""
    All the utility modules are present here
"""
import shlex

from geolite2 import geolite2

def convert_log_to_dict(log_pattern, line):
    """
        Takes log_pattern and line as input and returns a dict
    """
    keys = shlex.split(log_pattern)
    values = shlex.split(line)
    return dict(zip(keys, values))


def is_indian_ip(ip_address):
    """
        Checks if the ip address that sent the request is a non-indian ip
    """
    reader = geolite2.reader()
    match = reader.get(ip_address)
    return match['country']['iso_code'] == 'IN'
