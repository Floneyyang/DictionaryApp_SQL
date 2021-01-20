import mysql.connector
import json
from difflib import get_close_matches

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

data = json.load(open("data.json"))
cursor = con.cursor()

def find_def(w):
    query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' "% w)
    results = cursor.fetchall()
    return results

def translate(w):
    w = w.lower()
    result = find_def(w)
    if len(result) != 0:
        return result
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        yn = yn.upper()
        if yn == "Y":
            return find_def(get_close_matches(w, data.keys())[0])
        elif yn == "N":
            return "This word doesn't exist. Please double check it."
        else:
            return "We didnt understand your entry."
    else:
        return "This word doesn't exist. Please double check it."


word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    print("Definition: ")
    for item in output:
        print(item[1])
else:
    print(output)
