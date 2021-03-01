import json
import struct
import os
from rule import Rule
from pprint import pprint
import sys
import csv
from operator import itemgetter

from PyInquirer import style_from_dict, Token, prompt

from examples import custom_style_3

print('Dog diagnoser')

rules = []
with open("symptom_data.csv", "r") as f:
    reader = csv.reader(f, delimiter=",")
    header = []
    for i, line in enumerate(reader):
        if (i == 0):
            # Save header
            header = line
        else:
            # Compute
            disease = line[0]
            line = line[1:]
            achievedScore = 0
            bestScore = len(line)

            # print('Computing for disease: ' + disease)
            disease = ["{}".format(disease)]
            symptoms = []
            for index, column in enumerate(header[1:]):
                # print('Parsing {}: {} == {}'.format(
                #     column, line[index], answers[column]))
                symptoms.append("{}_{}".format(column, line[index]))
            rules.append(Rule(symptoms, disease))
            #     if answers[column] == line[index]:
            #         achievedScore += 1
            # results[disease] = round(100*float(achievedScore)/bestScore, 2)

mode_question = [{
    'type': 'list',
    'name': 'mode',
    'message': 'Seleccione el modo en que desea correr el programa',
    'choices': ['If', 'RETE'],
    'filter': lambda val: val.lower()
}]

mode_answers = prompt(mode_question, style=custom_style_3)

if (mode_answers['mode'] == 'if'):
    # If mode
    questions = [
        {
            'type': 'list',
            'name': 'picazon',
            'message': 'Presenta picazón?',
            'choices': ['No', 'Normal', 'Intensa'],
            'filter': lambda val: val.lower()
        },
        {
            'type': 'list',
            'name': 'comportamiento',
            'message': 'Cuál es su comportamiento?',
            'choices': ['Normal', 'Inquieto', 'Nervioso', 'Hiperactivo', 'Decaído', 'Apático'],
            'filter': lambda val: val.lower()
        },
        {
            'type': 'list',
            'name': 'heridas',
            'message': 'Presenta heridas?',
            'choices': ['No', 'Si'],
            'filter': lambda val: val.lower()
        },
        {
            'type': 'list',
            'name': 'pelaje',
            'message': 'Cuál es el estado del pelaje?',
            'choices': ['Normal', 'Con insectos', 'Con caídas leves', 'Con caídas severas'],
            'filter': lambda val: val.lower()
        },
        {
            'type': 'list',
            'name': 'heces',
            'message': 'Cuál es el estado de las heces?',
            'choices': ['Normal', 'Con parásitos'],
            'filter': lambda val: val.lower()
        },
        {
            'type': 'list',
            'name': 'sangrado',
            'message': 'Presenta sangrado?',
            'choices': ['No', 'Si'],
            'filter': lambda val: val.lower()
        },
        {
            'type': 'list',
            'name': 'paralisis',
            'message': 'Presenta parálisis?',
            'choices': ['No', 'Si'],
            'filter': lambda val: val.lower()
        },
        {
            'type': 'list',
            'name': 'ardor',
            'message': 'Presenta ardor?',
            'choices': ['No', 'Si'],
            'filter': lambda val: val.lower()
        },
        {
            'type': 'list',
            'name': 'apetito',
            'message': 'Cuál es su apetito?',
            'choices': ['Normal', 'Leve', 'Moderado', 'Severo'],
            'filter': lambda val: val.lower()
        },
        {
            'type': 'list',
            'name': 'fiebre',
            'message': 'Presenta fiebre?',
            'choices': ['No', 'Baja', 'Alta'],
            'filter': lambda val: val.lower()
        },
        {
            'type': 'list',
            'name': 'convulsiones',
            'message': 'Presenta convulsiones?',
            'choices': ['No', 'Si'],
            'filter': lambda val: val.lower()
        },
        {
            'type': 'list',
            'name': 'ojos',
            'message': 'Cuál es el estado de sus ojos?',
            'choices': ['Normal', 'Con lágrimas', 'Con pus'],
            'filter': lambda val: val.lower()
        },
        {
            'type': 'list',
            'name': 'tos',
            'message': 'Presenta tos?',
            'choices': ['No', 'Si'],
            'filter': lambda val: val.lower()
        },
        {
            'type': 'list',
            'name': 'estornudos',
            'message': 'Presenta estornudos?',
            'choices': ['No', 'Si'],
            'filter': lambda val: val.lower()
        },
        {
            'type': 'list',
            'name': 'vomito',
            'message': 'Presenta vómitos?',
            'choices': ['No', 'Si'],
            'filter': lambda val: val.lower()
        },
        {
            'type': 'list',
            'name': 'oidos',
            'message': 'Cuál es el estado de sus oídos?',
            'choices': ['Normal', 'Con temperatura', 'Con olor'],
            'filter': lambda val: val.lower()
        },
        {
            'type': 'list',
            'name': 'debilidad',
            'message': 'Se encuentra débil?',
            'choices': ['No', 'Si'],
            'filter': lambda val: val.lower()
        },
        {
            'type': 'list',
            'name': 'cojera',
            'message': 'Presenta cojera?',
            'choices': ['No', 'Si'],
            'filter': lambda val: val.lower()
        },
        {
            'type': 'list',
            'name': 'dolor',
            'message': 'Presenta dolor?',
            'choices': ['No', 'Abdominal', 'En las extremidades'],
            'filter': lambda val: val.lower()
        },
        {
            'type': 'list',
            'name': 'jadeo',
            'message': 'Jadea?',
            'choices': ['No', 'Si'],
            'filter': lambda val: val.lower()
        },
        {
            'type': 'list',
            'name': 'ladridos',
            'message': 'Ladra?',
            'choices': ['Normal', 'Más de lo normal'],
            'filter': lambda val: val.lower()
        }
    ]

    answers = prompt(questions, style=custom_style_3)

    results = {}
    with open("symptom_data.csv", "r") as f:
        reader = csv.reader(f, delimiter=",")
        header = []
        for i, line in enumerate(reader):
            if (i == 0):
                header = line
            else:
                disease = line[0]
                line = line[1:]
                achievedScore = 0
                bestScore = len(line)

                for index, column in enumerate(header[1:]):
                    if answers[column] == line[index]:
                        achievedScore += 1
                results[disease] = round(100*float(achievedScore)/bestScore, 2)

    results = sorted(results.items(), key=itemgetter(1), reverse=True)
    for i in results:
        print('\nChances de que tenga {}: {}%'.format(i[0], i[1]))
else:
    # Rete mode
    questions = [
        {
            'type': 'list',
            'name': 'picazon',
            'message': 'Presenta picazón?',
            'choices': ['No', 'Normal', 'Intensa'],
            'filter': lambda val: 'picazon_' + val.lower(),
            'default': 0
        },
        {
            'type': 'list',
            'name': 'comportamiento',
            'message': 'Cuál es su comportamiento?',
            'choices': ['Normal', 'Inquieto', 'Nervioso', 'Hiperactivo', 'Decaído', 'Apático'],
            'filter': lambda val: 'comportamiento_' + val.lower(),
            'default': 0
        },
        {
            'type': 'list',
            'name': 'heridas',
            'message': 'Presenta heridas?',
            'choices': ['No', 'Si'],
            'default': 0,
            'filter': lambda val: 'heridas_' + val.lower(),
            'when': lambda answers: answers['comportamiento'] == 'comportamiento_inquieto' or answers['comportamiento'] == 'comportamiento_decaído'
        },
        {
            'type': 'list',
            'name': 'pelaje',
            'message': 'Cuál es el estado del pelaje?',
            'choices': ['Normal', 'Con insectos', 'Con caídas leves', 'Con caídas severas'],
            'default': 0,
            'filter': lambda val: 'pelaje_' + val.lower(),
            'when': lambda answers: answers['comportamiento'] == 'comportamiento_decaído' or answers['comportamiento'] == 'comportamiento_inquieto'
        },
        {
            'type': 'list',
            'name': 'heces',
            'message': 'Cuál es el estado de las heces?',
            'choices': ['Normal', 'Con parásitos'],
            'default': 0,
            'filter': lambda val: 'heces_' + val.lower()
        },
        {
            'type': 'list',
            'name': 'sangrado',
            'message': 'Presenta sangrado?',
            'choices': ['No', 'Si'],
            'default': 0,
            'filter': lambda val: 'sangrado_' + val.lower(),
            'when': lambda answers: answers['heces'] == 'heces_normal' and answers['comportamiento'] != 'comportamiento_normal' and answers['comportamiento'] != 'comportamiento_nervioso'

        },
        {
            'type': 'list',
            'name': 'paralisis',
            'message': 'Presenta parálisis?',
            'choices': ['No', 'Si'],
            'default': 0,
            'filter': lambda val: 'paralisis_' + val.lower(),
            'when': lambda answers: answers['heces'] == 'heces_normal' and ( answers['comportamiento'] == 'comportamiento_nervioso' or answers['comportamiento'] == 'comportamiento_inquieto' )

        },
        {
            'type': 'list',
            'name': 'ardor',
            'message': 'Presenta ardor?',
            'choices': ['No', 'Si'],
            'default': 1,
            'filter': lambda val: 'ardor_' + val.lower(),
            'when': lambda answers: answers['heces'] == 'heces_normal' and ( answers['comportamiento'] == 'comportamiento_nervioso' or answers['comportamiento'] == 'comportamiento_normal' or answers['comportamiento'] == 'comportamiento_apático' )

        },
        {
            'type': 'list',
            'name': 'apetito',
            'message': 'Cuál es su apetito?',
            'choices': ['Normal', 'Leve', 'Moderado', 'Severo'],
            'default': 0,
            'filter': lambda val: 'apetito_' + val.lower(),
            'when': lambda answers: answers['heces'] == 'heces_normal' and (answers['comportamiento'] == 'comportamiento_decaído' or answers['comportamiento'] == 'comportamiento_apático' )
        },
        {
            'type': 'list',
            'name': 'fiebre',
            'message': 'Presenta fiebre?',
            'choices': ['No', 'Baja', 'Alta'],
            'default': 0,
            'filter': lambda val: 'fiebre_' + val.lower(),
            'when': lambda answers: answers['heces'] == 'heces_normal'
            #'when': lambda answers: answers['heces'] == 'heces_normal' and (answers['comportamiento'] == 'comportamiento_inquieto' or answers['comportamiento'] == 'comportamiento_nervioso' ) and answers['pelaje'] == 'pelaje_normal'

        },
        {
            'type': 'list',
            'name': 'convulsiones',
            'message': 'Presenta convulsiones?',
            'choices': ['No', 'Si'],
            'default': 0,
            'filter': lambda val: 'convulsiones_' + val.lower(),
            'when': lambda answers: answers['heces'] == 'heces_normal' and answers['comportamiento'] == 'comportamiento_nervioso'

        },
        {
            'type': 'list',
            'name': 'ojos',
            'message': 'Cuál es el estado de sus ojos?',
            'choices': ['Normal', 'Con lagrimas', 'Con pus'],
            'filter': lambda val: 'ojos_' + val.lower(), #val.replace(" ","").lower(),
            'default': 0,
            'when': lambda answers: answers['heces'] == 'heces_normal'
            #'when': lambda answers: answers['picazon'] == 'picazon_normal' and answers['comportamiento'] == 'comportamiento_nervioso' and answers['heridas'] == 'heridas_no' and answers['pelaje'] == 'pelaje_normal' and answers['heces'] == 'heces_normal' and answers['sangrado'] == 'sangrado_no' and answers['paralisis'] == 'paralisis_si' and answers['ardor'] == 'ardor_si' and answers['apetito'] == 'apetito_normal' and answers['fiebre'] == 'fiebre_alta' and answers['convulsiones'] == 'convulsiones_si'
        },
        {
            'type': 'list',
            'name': 'tos',
            'message': 'Presenta tos?',
            'choices': ['No', 'Si'],
            'default': 0,
            'filter': lambda val: 'tos_' + val.lower(),
            'when': lambda answers: answers['heces'] == 'heces_normal' and answers['ojos'] == 'ojos_conpus'
        },
        {
            'type': 'list',
            'name': 'estornudos',
            'message': 'Presenta estornudos?',
            'choices': ['No', 'Si'],
            'filter': lambda val: 'estornudos_' + val.lower(),
            'default': 0,
            'when': lambda answers: answers['heces'] == 'heces_normal' and answers['ojos'] == 'ojos_conpus' and answers['tos'] == 'tos_si'
        },
        {
            'type': 'list',
            'name': 'vomito',
            'message': 'Presenta vómitos?',
            'choices': ['No', 'Si'],
            'default': 0,
            'filter': lambda val: 'vomito_' + val.lower(),
            'when': lambda answers: answers['heces'] == 'heces_normal' and answers['ojos'] == 'ojos_conpus' and answers['tos'] == 'tos_si' and answers['estornudos'] == 'estornudos_si'
        },
        {
            'type': 'list',
            'name': 'oidos',
            'message': 'Cuál es el estado de sus oídos?',
            'choices': ['Normal', 'Con temperatura', 'Con olor'],
            'default': 0,
            'filter': lambda val: 'oidos_' + val.lower(), #val.replace(" ","").lower(),
            'when': lambda answers: answers['heces'] == 'heces_normal' and ( answers['ojos'] == 'ojos_conpus' or answers['fiebre'] == 'fiebre_baja')
        },
        {
            'type': 'list',
            'name': 'debilidad',
            'message': 'Se encuentra débil?',
            'choices': ['No', 'Si'],
            'default': 0,
            'filter': lambda val: 'debilidad_' + val.lower(),
            'when': lambda answers: answers['heces'] == 'heces_normal' and answers['comportamiento'] != 'comportamiento_normal'

        },
        {
            'type': 'list',
            'name': 'cojera',
            'message': 'Presenta cojera?',
            'choices': ['No', 'Si'],
            'default': 0,
            'filter': lambda val: 'cojera_' + val.lower(),
            'when': lambda answers: answers['heces'] == 'heces_normal' and (answers['comportamiento'] == 'comportamiento_normal' or answers['comportamiento'] == 'comportamiento_apático')

        },
        {
            'type': 'list',
            'name': 'dolor',
            'message': 'Presenta dolor?',
            'choices': ['No', 'Abdominal', 'En las extremidades'],
            'filter': lambda val: 'dolor_' + val.lower(),
            'default': 0,
            'when': lambda answers: answers['heces'] == 'comportamiento_normal' and (answers['cojera'] == 'cojera_si' or answers['convulsiones'] == 'convulsiones_si')
        },
        {
            'type': 'list',
            'name': 'jadeo',
            'message': 'Jadea?',
            'choices': ['No', 'Si'],
            'default': 0,
            'filter': lambda val: 'jadeo_' + val.lower(),
            'when': lambda answers: answers['heces'] == 'heces_normal' and (answers.get('oidos','oidos_normal') == 'oidos_normal' or (answers.get('cojera','cojera_no') == 'cojera_si' and answers['comportamiento'] == 'comportamiento_normal'))
            #'when': lambda answers: answers['heces'] == 'heces_normal' and (answers.get('cojera','cojera_no') == 'cojera_si' and answers['comportamiento'] == 'comportamiento_normal')
        },
        {
            'type': 'list',
            'name': 'ladridos',
            'message': 'Ladra?',
            'choices': ['Normal', 'Más de lo normal'],
            'default': 0,
            'filter': lambda val: 'ladridos_' + val.lower(),
            'when': lambda answers: answers['heces'] == 'heces_normal' and answers.get('cojera', 'cojera_no') == 'cojera_si' and answers['comportamiento'] == 'comportamiento_normal'
        }
    ]

    answers = prompt(questions, style=custom_style_3)
    for question in questions:
        if question['name'] not in answers:
            answers[question['name']] = question['filter'](question['choices'][question['default']])
    
    #print(answers)

    initialKnowledge = answers.values()

    knowledge = list(initialKnowledge)

    someRuleApplies = True
    while ((len(rules) > 0) and (someRuleApplies == True)):
        someRuleApplies = False
        for rule in rules:
            if rule.applies(knowledge):
                rules.remove(rule)
                rule.apply(knowledge)
                knowledge = list(set(knowledge))
                someRuleApplies = True
                break


    print("\nDado el siguiente conocimiento inicial: " + ', '.join(initialKnowledge))
    newKnowledge = list(set(knowledge) - set(initialKnowledge))
    if (len(newKnowledge) > 0):
        print("\nDeducimos el conocimiento: " + ', '.join(newKnowledge))
    else:
        print("\nNo se puede deducir ningún conocimiento")
