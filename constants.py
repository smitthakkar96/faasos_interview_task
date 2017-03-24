"""
    Constants are some hardcoded varaibles that are used throught application
"""

SAMPLE_LOG = 'GET https://kpi.xyz.com:443 HTTP/1.1 "MATLAB R2013a" AES128-SHA TLSv1 2016-09-29T23:45:37.43243Z Prod-API 183.87.18.119:12766 1 0.000046 0.00216 0.000033 200 200 0 17'

LOG_PATTERN = 'HTTP_METHOD URL HTTP_VERSION ORIGIN_HEADER SSL_CIPHER SSL_PROTOCOL DATETIME LB_NAME CLIENT_IP:port BACKEND_IP:port request_processing_time backend_processing_time response_processing_time elb_status_code backend_status_code received_bytes sent_bytes'

ATTACK_PATTERN = {
    'ORIGIN_HEADER': "MATLAB R2013"
}
