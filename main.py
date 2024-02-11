import PySimpleGUI as sg
import random as Random
from utils import *
from fields import *

def startVerbConjugationsGui():
    table = loadVerbConjugationsTable()
    infinitiefs = list(table.keys())
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
            verifiedAnswer = verifyAnswer( table 
                                         , infinitiefs[infinitiefIndex]
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

def main():

    sg.theme('BluePurple')
    sg.set_options(font=('Roboto Condensed', 16))

    layout = [
        [sg.Text("Which game do you want to play?", size=(35), justification='center')],
        [sg.Button('Verb Conjugations', size=15, key=MAIN_GUI_KEYS.VERB_CONJUGATIONS.value)],
        [sg.Button('Words'            , size=15, key=MAIN_GUI_KEYS.WORDS.value)],
        [sg.Button('Adjectives'       , size=15, key=MAIN_GUI_KEYS.ADJECTIVES.value)],
        [sg.Button('Frequency'        , size=15, key=MAIN_GUI_KEYS.FREQUENCY.value)]
    ]

    window = sg.Window('Menu', layout, element_justification='center')

    while True:
        event, values = window.read()
        match event:
            case sg.WIN_CLOSED:
                break
            case MAIN_GUI_KEYS.VERB_CONJUGATIONS.value:
                startVerbConjugationsGui()
            case MAIN_GUI_KEYS.WORDS.value:
                sg.popup('Not yet implemented')
            case MAIN_GUI_KEYS.ADJECTIVES.value:
                sg.popup('Not yet implemented')
            case MAIN_GUI_KEYS.FREQUENCY.value:
                sg.popup('Not yet implemented')
    
    window.close()


if __name__ == '__main__':
    main()