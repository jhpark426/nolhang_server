# coding:UTF-8
from os import path
from xlrd import open_workbook
from .models import Space, Position, Mission, Item, Player
from app import db

#input_path setup
XL_PATH = '/import/question_all.xlsx'
cwd_xl = path.dirname(path.abspath(__file__)) + XL_PATH
dir_strings = cwd_xl.split("/")
dir_strings = [i for i in dir_strings]
import_xl_path = "/".join(dir_strings)

def load_wb(path):
    return open_workbook(path)

def load_worksheet(wb, sheet_name):
    return wb.sheet_by_name(sheet_name)

def load_keys(sheet):
    return [ sheet.cell_value(0,i) for i in range(sheet.ncols)]

sgd_wb = load_wb(import_xl_path)

db.create_all()

def _check_previous_populated():
        return Space.query.count() + Position.query.count() + Itemp.query.count()


def _create_region():
        region=load_worksheet(sgd_wb,"regions")
        for r in range(region.nrows-1):
                row={}
                for c,key in enumerate(load_keys(region)):
                        row[key]=space.cell_value(r+1,c)
                s=Region(region_code=int(row["region_code"]),region_name=row["region_name"])
                db.session.add(s)
        db.session.commit()

def _create_question():
        question=load_worksheet(sgd_wb,"questions")
        for r in range(question.nrow-1):
                row={}
                for c, key in enumerate(load_keys(question)):
                        row[key]=question.cell_value(r+1,c)
                q=Question(question_code=int(row["question_code"]),region_code=row["region_code"],question=row["question"],answer=row["answer"],content_type=row["content_type"])
                db.session.add(q)
        db.session.commit()

def create_all():
        if _check_previous_populated():
                return

        _create_region()
        _create_question()


create_all()
