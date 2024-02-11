from enum import Enum

class VERB_CONJUGATIONS_FIELDS(Enum):
    ENGELS        = "Engels"
    INFINITIEF    = "Infinitief"
    STAM_T        = "Stam(t)"
    IMPERFECTUM_S = "Imperfectum(S)"
    IMPERFECTUM_P = "Imperfectum(P)"
    PARTICIPIUM   = "Participium"
    HEB_BEN       = "Heb/Ben"

class MAIN_GUI_KEYS(Enum):
    VERB_CONJUGATIONS = 'VerbConjugations'
    ADJECTIVES        = 'Adjectives'
    WORDS             = 'Words' #Could be divided per chapters
    FREQUENCY         = 'Frequency' 
