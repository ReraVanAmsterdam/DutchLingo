import PySimpleGUI as sg
from VerbConjugations import VerbConjugations
from utils import *
from fields import *

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
            verbConjugations = VerbConjugations()
            verbConjugations.startGui()
        case MAIN_GUI_KEYS.WORDS.value:
            sg.popup('Not yet implemented')
        case MAIN_GUI_KEYS.ADJECTIVES.value:
            sg.popup('Not yet implemented')
        case MAIN_GUI_KEYS.FREQUENCY.value:
            sg.popup('Not yet implemented')

window.close()