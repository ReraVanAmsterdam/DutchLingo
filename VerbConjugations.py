import PySimpleGUI as sg
import random as Random
from utils import *
from fields import *

class VerbConjugations:

    url = "https://docs.google.com/spreadsheets/d/10GM8ZXs2PA5upT-kN7ScpWPMgLw1_y5w/edit#gid=1294425407"

    def __init__(self):
        self.table = self.loadTable(self.url)

    def loadTable(self, url):
        print("START | Loading Verb Conjugations Table...")
        new_url = convert_google_sheet_url(url)

        verbsConjugationsDict={}

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

        print("END | Loading Verb Conjugations Table...")
        return verbsConjugationsDict
    
    def verifyAnswer(self, infinitief, entered_engels, entered_stam_t, entered_imperfectum_s, entered_imperfectum_p, entered_participium, entered_heb_radio):

        entered_heb_ben = "heb" if entered_heb_radio else "ben"

        response={VERB_CONJUGATIONS_FIELDS.ENGELS.value        : "CORRECT(" + self.table[infinitief].get(VERB_CONJUGATIONS_FIELDS.ENGELS.value)        + ")",
                  VERB_CONJUGATIONS_FIELDS.STAM_T.value        : "CORRECT(" + self.table[infinitief].get(VERB_CONJUGATIONS_FIELDS.STAM_T.value)        + ")",
                  VERB_CONJUGATIONS_FIELDS.IMPERFECTUM_S.value : "CORRECT(" + self.table[infinitief].get(VERB_CONJUGATIONS_FIELDS.IMPERFECTUM_S.value) + ")",
                  VERB_CONJUGATIONS_FIELDS.IMPERFECTUM_P.value : "CORRECT(" + self.table[infinitief].get(VERB_CONJUGATIONS_FIELDS.IMPERFECTUM_P.value) + ")",
                  VERB_CONJUGATIONS_FIELDS.PARTICIPIUM.value   : "CORRECT(" + self.table[infinitief].get(VERB_CONJUGATIONS_FIELDS.PARTICIPIUM.value)   + ")",
                  VERB_CONJUGATIONS_FIELDS.HEB_BEN.value       : "CORRECT(" + self.table[infinitief].get(VERB_CONJUGATIONS_FIELDS.HEB_BEN.value)       + ")",
                  "FAIL"                                       : 0
                }
        fail = 0

        if entered_engels        != self.table[infinitief].get(VERB_CONJUGATIONS_FIELDS.ENGELS.value):
            response[VERB_CONJUGATIONS_FIELDS.ENGELS.value]        = "INCORRECT(" + entered_engels         + ") => " + self.table[infinitief].get(VERB_CONJUGATIONS_FIELDS.ENGELS.value)
            fail += 1
        if entered_stam_t        != self.table[infinitief].get(VERB_CONJUGATIONS_FIELDS.STAM_T.value):
            response[VERB_CONJUGATIONS_FIELDS.STAM_T.value]        = "INCORRECT(" + entered_stam_t         + ") => " + self.table[infinitief].get(VERB_CONJUGATIONS_FIELDS.STAM_T.value)
            fail += 1
        if entered_imperfectum_s != self.table[infinitief].get(VERB_CONJUGATIONS_FIELDS.IMPERFECTUM_S.value):
            response[VERB_CONJUGATIONS_FIELDS.IMPERFECTUM_S.value] = "INCORRECT(" + entered_imperfectum_s  + ") => " + self.table[infinitief].get(VERB_CONJUGATIONS_FIELDS.IMPERFECTUM_S.value)
            fail += 1
        if entered_imperfectum_p != self.table[infinitief].get(VERB_CONJUGATIONS_FIELDS.IMPERFECTUM_P.value):
            response[VERB_CONJUGATIONS_FIELDS.IMPERFECTUM_P.value] = "INCORRECT(" + entered_imperfectum_p  + ") => " + self.table[infinitief].get(VERB_CONJUGATIONS_FIELDS.IMPERFECTUM_P.value)
            fail += 1
        if entered_participium   != self.table[infinitief].get(VERB_CONJUGATIONS_FIELDS.PARTICIPIUM.value):
            response[VERB_CONJUGATIONS_FIELDS.PARTICIPIUM.value]   = "INCORRECT(" + entered_participium    + ") => " + self.table[infinitief].get(VERB_CONJUGATIONS_FIELDS.PARTICIPIUM.value)
            fail += 1
        if entered_heb_ben       != self.table[infinitief].get(VERB_CONJUGATIONS_FIELDS.HEB_BEN.value):
            response[VERB_CONJUGATIONS_FIELDS.HEB_BEN.value]       = "INCORRECT(" + entered_heb_ben        + ") => " + self.table[infinitief].get(VERB_CONJUGATIONS_FIELDS.HEB_BEN.value)
            fail += 1 

        response["FAIL"] = fail

        return response
    
    def startGui(self):
        infinitiefs = list(self.table.keys())
        infinitiefIndex = 0
        score = 0
        life = 3
        Random.shuffle(infinitiefs)

        sg.theme('BluePurple')
        sg.set_options(font=('Arial Bold', 16))

        layout = [
            [sg.Text(VERB_CONJUGATIONS_FIELDS.INFINITIEF.value + " : " + infinitiefs[infinitiefIndex], size=(15,1), enable_events=True, key=VERB_CONJUGATIONS_FIELDS.INFINITIEF.value)],
            [sg.Text(VERB_CONJUGATIONS_FIELDS.ENGELS.value,        size=(15,1)), sg.InputText(key=VERB_CONJUGATIONS_FIELDS.ENGELS.value)],
            [sg.Text(VERB_CONJUGATIONS_FIELDS.STAM_T.value,        size=(15,1)), sg.InputText(key=VERB_CONJUGATIONS_FIELDS.STAM_T.value)],
            [sg.Text(VERB_CONJUGATIONS_FIELDS.IMPERFECTUM_S.value, size=(15,1)), sg.InputText(key=VERB_CONJUGATIONS_FIELDS.IMPERFECTUM_S.value)],
            [sg.Text(VERB_CONJUGATIONS_FIELDS.IMPERFECTUM_P.value, size=(15,1)), sg.InputText(key=VERB_CONJUGATIONS_FIELDS.IMPERFECTUM_P.value)],
            [sg.Text(VERB_CONJUGATIONS_FIELDS.PARTICIPIUM.value,   size=(15,1)), sg.InputText(key=VERB_CONJUGATIONS_FIELDS.PARTICIPIUM.value)],
            [sg.Text(VERB_CONJUGATIONS_FIELDS.HEB_BEN.value,       size=(15,1)), sg.Radio('heb', VERB_CONJUGATIONS_FIELDS.HEB_BEN.value, key='HEB', default=True),
                                                                                 sg.Radio('ben', VERB_CONJUGATIONS_FIELDS.HEB_BEN.value, key='BEN')],
            [sg.Text("Life : " + str(life), size=(15,1), enable_events=True, key="Life")],
            [sg.Text("Score : " + str(score), size=(15,1), enable_events=True, key="Score")],
            [sg.Submit(), sg.Button('Clear'), sg.Exit()]
        ]
        

        window = sg.Window('Verb Conjugations', layout, modal=True)

        def clear_input():
            for key in values:
                window[key]('')
            return None
        
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            if event == 'Clear':
                clear_input()
            if event == 'Submit':
                verifiedAnswer = self.verifyAnswer( infinitiefs[infinitiefIndex]
                                                  , window[VERB_CONJUGATIONS_FIELDS.ENGELS.value].get()
                                                  , window[VERB_CONJUGATIONS_FIELDS.STAM_T.value].get()
                                                  , window[VERB_CONJUGATIONS_FIELDS.IMPERFECTUM_S.value].get()
                                                  , window[VERB_CONJUGATIONS_FIELDS.IMPERFECTUM_P.value].get()
                                                  , window[VERB_CONJUGATIONS_FIELDS.PARTICIPIUM.value].get()
                                                  , window['HEB'].get()
                                                  )
                
                if verifiedAnswer["FAIL"] != 0:
                    sg.popup( str(verifiedAnswer["FAIL"]) + ' ANSWERS WERE INCORRECT'
                            , VERB_CONJUGATIONS_FIELDS.ENGELS.value        + " : " + verifiedAnswer[VERB_CONJUGATIONS_FIELDS.ENGELS.value]
                            , VERB_CONJUGATIONS_FIELDS.STAM_T.value        + " : " + verifiedAnswer[VERB_CONJUGATIONS_FIELDS.STAM_T.value]
                            , VERB_CONJUGATIONS_FIELDS.IMPERFECTUM_S.value + " : " + verifiedAnswer[VERB_CONJUGATIONS_FIELDS.IMPERFECTUM_S.value]
                            , VERB_CONJUGATIONS_FIELDS.IMPERFECTUM_P.value + " : " + verifiedAnswer[VERB_CONJUGATIONS_FIELDS.IMPERFECTUM_P.value]
                            , VERB_CONJUGATIONS_FIELDS.PARTICIPIUM.value   + " : " + verifiedAnswer[VERB_CONJUGATIONS_FIELDS.PARTICIPIUM.value]
                            , VERB_CONJUGATIONS_FIELDS.HEB_BEN.value       + " : " + verifiedAnswer[VERB_CONJUGATIONS_FIELDS.HEB_BEN.value]
                            )
                    if life == 0:
                        break
                    else:
                        life -=1
                        window["Life"].update("Life : " + str(life))
                else:    
                    sg.popup("ALL ANSWERS WERE CORRECT")
                    score +=1
                    window["Score"].update("Score : " + str(score))

                clear_input()
                infinitiefIndex += 1
                window[VERB_CONJUGATIONS_FIELDS.INFINITIEF.value].update(VERB_CONJUGATIONS_FIELDS.INFINITIEF.value + " : " + infinitiefs[infinitiefIndex])

        window.close()