"""
json handelr
"""

from model import input_data

def input_json_data(json_data):
    try:
        if json_data["type"] == "report":
            input_data.input_report_data(json_data)
            
        elif json_data["type"] == "walk":
            input_data.input_walk_data(json_data)
        
    except:
        return "error"