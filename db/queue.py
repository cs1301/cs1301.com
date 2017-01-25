#!/usr/bin/python

import sqlite3
import cgi
import json
import re
import sys

def do_action(action, data):
    result = {}
    conn = sqlite3.connect("queue.sqlt")
    c = conn.cursor()
    if action == "get":
        last_id = str(re.sub(r'[^\-0-9]', r'', data["last_id"].value))
        c.execute("SELECT * FROM queue WHERE id > (?);", [last_id])
        result["success"] = True
        result["data"] = c.fetchall()
    elif action == "insert":
        name = str(re.sub(r'[^A-Za-z]', r'', data["name"].value))
        c.execute("INSERT INTO queue (name) VALUES (?);", [name])
        result["success"] = True
    elif action == "remove":
        item_id = str(re.sub(r'[^0-9]', r'', data["id"].value))
        c.execute("DELETE FROM queue where id=?;", [item_id])
        result["success"] = True

    c.execute("DELETE FROM queue WHERE date < datetime('now', '-1 days');")

    conn.commit()
    conn.close()
    return result

def main():
    print("Content-type: text/html\n\n")

    data = cgi.FieldStorage()
    result = {"success": False}
    try:
        action = data["action"].value
        result.update(do_action(action, data))
    except Exception as e:
        result["error"] = e

    print(json.dumps(result))

main()
