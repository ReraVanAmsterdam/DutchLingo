import pandas as pd
from fields import *
import re

def convert_google_sheet_url(url):
    # Regular expression to match and capture the necessary part of the URL
    pattern = r'https://docs\.google\.com/spreadsheets/d/([a-zA-Z0-9-_]+)(/edit#gid=(\d+)|/edit.*)?'

    # Replace function to construct the new URL for CSV export
    # If gid is present in the URL, it includes it in the export URL, otherwise, it's omitted
    replacement = lambda m: f'https://docs.google.com/spreadsheets/d/{m.group(1)}/export?' + (f'gid={m.group(3)}&' if m.group(3) else '') + 'format=csv'

    # Replace using regex
    new_url = re.sub(pattern, replacement, url)

    return new_url

def loadVerbConjugationsTable():
    print("START | Loading table...")
    url = "https://docs.google.com/spreadsheets/d/10GM8ZXs2PA5upT-kN7ScpWPMgLw1_y5w/edit#gid=1294425407"
    new_url = convert_google_sheet_url(url)

    verbsConjugationsDict={}

    #table = pd.read_excel(url, sheet_name='Normale Verb Conjugations')
    table = pd.read_csv(new_url)

    # Populate verbsConjugationsDict
    for i in range(len(table)):
        key = str(table.loc[i, VERB_CONJUGATIONS_FIELDS.INFINITIEF.value])
        values = {VERB_CONJUGATIONS_FIELDS.ENGELS.value        : str(table.loc[i, VERB_CONJUGATIONS_FIELDS.ENGELS.value]),
                  VERB_CONJUGATIONS_FIELDS.STAM_T.value        : str(table.loc[i, VERB_CONJUGATIONS_FIELDS.STAM_T.value]),
                  VERB_CONJUGATIONS_FIELDS.IMPERFECTUM_S.value : str(table.loc[i, VERB_CONJUGATIONS_FIELDS.IMPERFECTUM_S.value]),
                  VERB_CONJUGATIONS_FIELDS.IMPERFECTUM_P.value : str(table.loc[i, VERB_CONJUGATIONS_FIELDS.IMPERFECTUM_P.value]),
                  VERB_CONJUGATIONS_FIELDS.PARTICIPIUM.value   : str(table.loc[i, VERB_CONJUGATIONS_FIELDS.PARTICIPIUM.value]),
                  VERB_CONJUGATIONS_FIELDS.HEB_BEN.value       : str(table.loc[i, VERB_CONJUGATIONS_FIELDS.HEB_BEN.value])
                 }
        verbsConjugationsDict[key] = values

    # Print out verbsConjugationsDict
    for key in verbsConjugationsDict.keys():
        print(key + " : " + str(verbsConjugationsDict[key]))

    print("END | Loading table...")
    return verbsConjugationsDict

def verifyAnswer(table, infinitief, entered_engels, entered_stam_t, entered_imperfectum_s, entered_imperfectum_p, entered_participium, entered_heb_radio):

    entered_heb_ben = "heb" if entered_heb_radio else "ben"

    response={VERB_CONJUGATIONS_FIELDS.ENGELS.value        : "CORRECT(" + table[infinitief].get(VERB_CONJUGATIONS_FIELDS.ENGELS.value)        + ")",
              VERB_CONJUGATIONS_FIELDS.STAM_T.value        : "CORRECT(" + table[infinitief].get(VERB_CONJUGATIONS_FIELDS.STAM_T.value)        + ")",
              VERB_CONJUGATIONS_FIELDS.IMPERFECTUM_S.value : "CORRECT(" + table[infinitief].get(VERB_CONJUGATIONS_FIELDS.IMPERFECTUM_S.value) + ")",
              VERB_CONJUGATIONS_FIELDS.IMPERFECTUM_P.value : "CORRECT(" + table[infinitief].get(VERB_CONJUGATIONS_FIELDS.IMPERFECTUM_P.value) + ")",
              VERB_CONJUGATIONS_FIELDS.PARTICIPIUM.value   : "CORRECT(" + table[infinitief].get(VERB_CONJUGATIONS_FIELDS.PARTICIPIUM.value)   + ")",
              VERB_CONJUGATIONS_FIELDS.HEB_BEN.value       : "CORRECT(" + table[infinitief].get(VERB_CONJUGATIONS_FIELDS.HEB_BEN.value)       + ")",
              "FAIL"                     : 0
              }
    fail = 0

    if entered_engels        != table[infinitief].get(VERB_CONJUGATIONS_FIELDS.ENGELS.value):
        response[VERB_CONJUGATIONS_FIELDS.ENGELS.value]        = "INCORRECT(" + entered_engels         + ") => " + table[infinitief].get(VERB_CONJUGATIONS_FIELDS.ENGELS.value)
        fail += 1
    if entered_stam_t        != table[infinitief].get(VERB_CONJUGATIONS_FIELDS.STAM_T.value):
        response[VERB_CONJUGATIONS_FIELDS.STAM_T.value]        = "INCORRECT(" + entered_stam_t         + ") => " + table[infinitief].get(VERB_CONJUGATIONS_FIELDS.STAM_T.value)
        fail += 1
    if entered_imperfectum_s != table[infinitief].get(VERB_CONJUGATIONS_FIELDS.IMPERFECTUM_S.value):
        response[VERB_CONJUGATIONS_FIELDS.IMPERFECTUM_S.value] = "INCORRECT(" + entered_imperfectum_s  + ") => " + table[infinitief].get(VERB_CONJUGATIONS_FIELDS.IMPERFECTUM_S.value)
        fail += 1
    if entered_imperfectum_p != table[infinitief].get(VERB_CONJUGATIONS_FIELDS.IMPERFECTUM_P.value):
        response[VERB_CONJUGATIONS_FIELDS.IMPERFECTUM_P.value] = "INCORRECT(" + entered_imperfectum_p  + ") => " + table[infinitief].get(VERB_CONJUGATIONS_FIELDS.IMPERFECTUM_P.value)
        fail += 1
    if entered_participium   != table[infinitief].get(VERB_CONJUGATIONS_FIELDS.PARTICIPIUM.value):
        response[VERB_CONJUGATIONS_FIELDS.PARTICIPIUM.value]   = "INCORRECT(" + entered_participium    + ") => " + table[infinitief].get(VERB_CONJUGATIONS_FIELDS.PARTICIPIUM.value)
        fail += 1
    if entered_heb_ben       != table[infinitief].get(VERB_CONJUGATIONS_FIELDS.HEB_BEN.value):
        response[VERB_CONJUGATIONS_FIELDS.HEB_BEN.value]       = "INCORRECT(" + entered_heb_ben        + ") => " + table[infinitief].get(VERB_CONJUGATIONS_FIELDS.HEB_BEN.value)
        fail += 1 

    response["FAIL"] = fail

    return response