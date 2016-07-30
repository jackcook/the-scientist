from aenum import Enum

"""
    pos.py
    ~~~~~~

    References:
    - https://cs.nyu.edu/grishman/jet/guide/PennPOS.html
    - http://nlp.stanford.edu/software/dependencies_manual.pdf
"""

class CoarsePOS(Enum):
    coordinating_conjunction = "CC"
    determiner = "DT"
    foreign_word = "FW"
    preposition_or_subordinating_conjunction = "IN"
    adjective = "JJ"
    adjective_comparative = "JJR"
    superfluous_punctuation = "NFP" # double check
    noun = "NN"
    noun_plural = "NNS"
    proper_noun_singular = "NNP"
    possessive_ending = "POS"
    personal_pronoun = "PRP"
    possessive_pronoun = "PRP$"
    adverb = "RB"
    particle = "RP"
    interjection = "UH"
    verb_base_form = "VB"
    verb_past_tense = "VBD"
    verb_gerund_pr_present_participle = "VBG"
    verb_past_participle = "VBN"
    verb_non_third_person_singular_present = "VBP"
    verb_third_person_singular_present = "VBZ"
    wh_pronoun = "WP"
    wh_adverb = "WRB"
    apostrophe = "''"
    comma = ","
    colon = ":"
    punctuation = "."

class FinePOS(Enum):
    adverbial_clause_modifier = "advcl"
    adverb_modifier = "advmod"
    adjectival_modifier = "amod"
    auxiliary = "aux"
    passive_auxiliary = "auxpass"
    coordination = "cc"
    clausal_complement = "ccomp"
    conjunct = "conj"
    copula = "cop"
    dependent = "dep"
    determiner = "det"
    discourse_element = "discourse"
    direct_object = "dobj"
    marker = "mark"
    negation_modifier = "neg"
    noun_compound_modifier = "nn"
    nominal_subject = "nsubj"
    passive_nominal_subject = "nsubjpass"
    parataxis = "parataxis"
    reduced_non_finite_verbal_modifier_participial = "partmod" # double check
    object_of_a_preposition = "pobj"
    possession_modifier = "poss"
    possessive_modifier = "possessive"
    prepositional_modifier = "prep"
    phrasal_verb_particle = "prt"
    punctuation = "punct"
    relative_clause_modifier = "rcmod"
    root = "ROOT"
