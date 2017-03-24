"""
    starting point of application
"""

# I have never used Jinja2 in my life I usually build apis In python
# but since it was a small task I didn't prefer to write angular2 app in frontend
# Due to this the Ui as well as the UX of the app won't be cool
# I hope this doesn't matter at this point of time

from flask import Flask, render_template, jsonify
from flask_reqparse import RequestParser
import six

from constants import ATTACK_PATTERN, LOG_PATTERN
from util import convert_log_to_dict, is_indian_ip

APP = Flask(__name__)
parser = RequestParser()

def contains(string, sub_string):
    """
        Index wrapper to handle notfound sliently
    """
    try:
        string.index(sub_string)
        return True
    except ValueError:
        return False

@APP.route('/')
def index_get():
    """
        Loads the page where you can upload the file
    """
    return render_template('index.html')

@APP.route('/process_log', methods=['POST'])
@parser.validate_arguments([
    {
        'name': "log_file",
        'required': True,
        'source': 'file',
        'help': 'log file not recieved'
    }
])
def process_log(args):
    """
        input: log file
        output: array of object containing keys like origin header, ip and isSuspicious
    """
    log_file = args['log_file']
    response = []
    for line in log_file:
        log_dict = convert_log_to_dict(LOG_PATTERN, line.decode())
        ip_address = log_dict['CLIENT_IP:port'].split(':')[0]
        is_suspicious = False
        for key, value in six.iteritems(ATTACK_PATTERN):
            if contains(log_dict[key], value):
                is_suspicious = True
                break
        if not is_suspicious:
            if is_indian_ip(ip_address):
                is_suspicious = True
        response.append({
            'ip_address': ip_address,
            'HTTP_METHOD': log_dict['HTTP_METHOD'],
            'ORIGIN_HEADER': log_dict['ORIGIN_HEADER'],
            'is_suspicious': is_suspicious
        })

    return render_template('index.html', data=response)




if __name__ == '__main__':
    APP.run(debug=True)
