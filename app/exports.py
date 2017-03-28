from app.models import *
from json import dump
from app.common import convert_as_camel_case, JSONEncoder
from app import db, export
from os import getcwd
import json

def export_database_to_json ():
    models = [Region,Question]
    table_names = ["regions","questions"]
    out = getcwd() + "/app/export/"
    for index, table in enumerate(table_names):
        data_list = [ convert_as_camel_case(row) for row in db.session.query(models[index]).all() ]
        with open(out + table +'.json', mode='w', encoding="utf-8") as outfile:
            # dump(JSONEncoder().encode(data_list),outfile,ensure_ascii=False)
            # dump(data_list,outfile,ensure_ascii=False)
            try:
                dump(data_list,outfile,ensure_ascii=False)
            except TypeError as e:
                dump(JSONEncoder().encode(data_list),outfile,ensure_ascii=False)

export_database_to_json()
