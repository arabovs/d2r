from random import random, randint
import json

rune_drop = [
    {"Zod": 870298},
    {"Cham": 333474},
    {"Jah": 222316},
    {"Ber": 248272},
    {"Sur": 165515},
    {"Lo": 183608},
    {"Ohm": 122406},
    {"Vex": 128526},
    {"Gul": 85684},
    {"Ist": 90494},
    {"Mal": 60330},
    {"Um": 61836},
    {"Pul": 41224},
    {"Lo": 49998},
    {"Ohm": 33332},
    {"Vex": 35137},
    {"Gul": 23425},
    {"Ist": 519},
    {"Mal": 346},
    {"Um": 353},
    {"Pul": 235},
    {"Lem": 179},
    {"Fal": 119},
    {"Ko": 92},
    {"Lum": 61},
]


def getRune():
    for x in range(0, len(rune_drop)):
        for k, v in rune_drop[x].items():
            roll = randint(1, v)
            if roll == 1:
                if k == "Ber":
                    print(k)
                    break
    return 1


for x in range(0, 1000000):
    getRune()
