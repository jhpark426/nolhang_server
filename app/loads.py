# coding:UTF-8
from os import path
from xlrd import open_workbook
from .models import Space, Position, Mission, Item, Player
from app import db

XL_PATH = '/import/SGD-config.xlsx'
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
    return Space.query.count() + Position.query.count() + Item.query.count()

def _create_space_table():
    space = load_worksheet(sgd_wb, "space")
    for r in range(space.nrows-1):
        row = {}
        for c, key in enumerate(load_keys(space)):
            row[key] = space.cell_value(r+1, c)
        s = Space(id=int(row["id"]), en=row["en"], ko=row["ko"], cn=row["cn"])
        db.session.add(s)
    db.session.commit()

def _create_position_table():
    position = load_worksheet(sgd_wb, "position")
    for r in range(position.nrows-1):
        row = {}
        for c, key in enumerate(load_keys(position)):
            row[key] = position.cell_value(r+1, c)
        p = Position(id=int(row["id"]), en=row["en"], ko=row["ko"], cn=row["cn"],
                group_level=int(row["group_level"]), grade=int(row["grade"]),
                min_require_mission=int(row["min_require_mission"]))
        db.session.add(p)
    db.session.commit()

def _create_mission_table():
    mission = load_worksheet(sgd_wb, "mission")
    for r in range(mission.nrows-1):
        row = {}
        for c, key in enumerate(load_keys(mission)):
            row[key] = mission.cell_value(r+1, c)
        try:
            m = Mission(id=int(row["id"]),
                        codes=str(row["codes"]),
                        access_group_level=int(row["access_group_level"]),
                        quest_type_ko=str(row["quest_type_ko"]),
                        quest_type_no=int(row["quest_type_no"]),
                        king_ko=str(row["king_ko"]),
                        king_en=str(row["king_en"]),
                        year=int(row["year"]),
                        era=int(row["era"]),
                        field_ko=str(row["field_ko"]),
                        field_en=str(row["field_en"]),
                        keyword_ko=str(row["keyword_ko"]),
                        keyword_en=str(row["keyword_en"]),
                        question_ko=str(row["question_ko"]),
                        question_en=str(row["question_en"]),
                        description_ko=str(row["description_ko"]),
                        description_en=str(row["description_en"]))
            db.session.add(m)
        except ValueError:
            pass
    db.session.commit()

def _create_item_table():
    item = load_worksheet(sgd_wb, "item")
    for r in range(item.nrows-1):
        row = {}
        for c, key in enumerate(load_keys(item)):
            row[key] = item.cell_value(r+1, c)
        i = Item(mission_id=int(row["mission_id"]), space_id=int(row["space_id"]), code=int(row["code"]), content_type=str(row["content_type"]),
                content_ko=str(row["content_ko"]), content_en=str(row["content_en"]), access_group_level=int(row["access_group_level"]))
        db.session.add(i)
    db.session.commit()

def create_all():
    if _check_previous_populated():
        return
    _create_space_table()
    _create_position_table()
    _create_mission_table()
    _create_item_table()

create_all()
