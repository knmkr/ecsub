# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 10:41:12 2018

@author: Okada
"""

import ecsub.ansi
import datetime

def get_title_color (no):
    return ecsub.ansi.colors.roll_list[no % len(ecsub.ansi.colors.roll_list)]
        
def message (title, no, messages):
    text = "%s " % (str(datetime.datetime.now()))
    if no != None:     
        text += ecsub.ansi.colors.paint("[%s:%03d]" % (title, no), get_title_color(no))
    else:
        text += "[%s]" % (title)
        
    for m in messages:
        if "color" in m.keys():
            text += ecsub.ansi.colors.paint(m["text"], m["color"])
        else:
            text += m["text"]

    return text

def warning_message (title, no, text):
    return message (title, no, [{"text": " [WARNING] %s" % (text), "color": ecsub.ansi.colors.WARNING}])

def error_message (title, no, text):
    return message (title, no, [{"text": " [ERROR] %s" % (text), "color": ecsub.ansi.colors.FAIL}])

def info_message (title, no, text):
    return message (title, no, [{"text": " %s" % (text)}])

def base64_encode(text):
    import six
    
    if six.PY2:
        return text.encode('base64')
    
    import base64
    return base64.b64encode(text.encode('utf-8'))

def datetime_to_isoformat(dt):
    return dt.isoformat() + "Z"

def isoformat_to_datetime(text):
    return datetime.datetime.strptime(text, '%Y-%m-%dT%H:%M:%S.%fZ')
    
def main():
    pass

if __name__ == "__main__":
    main()

