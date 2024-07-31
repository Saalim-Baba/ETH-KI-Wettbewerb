from random import *
import math
import json 
import sys

Spacedrepetition = {"f1": 10, "f2": 8, "f3": 2, "f4": 4, "f5": 7, "f6": 5, "f7": 8, "f8": 1, "f9": 9, "f10": 6}
blurtingmethod = {"f1": 8, "f2": 10, "f3": 9, "f4": 7, "f5": 5, "f6": 8, "f7": 9, "f8": 6, "f9": 7, "f10": 5}
Pomodorotechnique = {"f1": 6, "f2": 7, "f3": 10, "f4": 6, "f5": 5, "f6": 9, "f7": 8, "f8": 7, "f9": 6, "f10": 9}
interleavedlearning = {"f1": 9, "f2": 8, "f3": 5, "f4": 10, "f5": 8, "f6": 4, "f7": 3, "f8": 8, "f9": 4, "f10": 10}
FeynmanTechnique = {"f1": 8, "f2": 9, "f3": 7, "f4": 6, "f5": 10, "f6": 8, "f7": 6, "f8": 5, "f9": 7, "f10": 8}
TimeBlocking = {"f1": 7, "f2": 6, "f3": 5, "f4": 4, "f5": 6, "f6": 10, "f7": 7, "f8": 6, "f9": 8, "f10": 9}
FiveMinuteRule = {"f1": 6, "f2": 7, "f3": 6, "f4": 5, "f5": 7, "f6": 8, "f7": 10, "f8": 9, "f9": 8, "f10": 6}
ThreeTwoOneMethod = {"f1": 5, "f2": 6, "f3": 7, "f4": 6, "f5": 5, "f6": 7, "f7": 10, "f8": 8, "f9": 7, "f10": 8}
LeitnerSystem = {"f1": 10, "f2": 8, "f3": 2, "f4": 4, "f5": 7, "f6": 5, "f7": 8, "f8": 1, "f9": 9, "f10": 6}

def datenverarbeiten(trainingszahlen):
    for i in range(len(trainingszahlen)):
        trainingszahlen[i] = int(trainingszahlen[i])

    global Spacedrepetition
    global blurtingmethod
    global Pomodorotechnique
    global interleavedlearning
    global FeynmanTechnique
    global TimeBlocking
    global FiveMinuteRule
    global ThreeTwoOneMethod
    global LeitnerSystem

    differenz1 = 0
    differenz1 += math.fabs(trainingszahlen[0] - Spacedrepetition["f1"])
    differenz1 += math.fabs(trainingszahlen[1] - Spacedrepetition["f2"])
    differenz1 += math.fabs(trainingszahlen[2] - Spacedrepetition["f3"])
    differenz1 += math.fabs(trainingszahlen[3] - Spacedrepetition["f4"])
    differenz1 += math.fabs(trainingszahlen[4] - Spacedrepetition["f5"])
    differenz1 += math.fabs(trainingszahlen[5] - Spacedrepetition["f6"])
    differenz1 += math.fabs(trainingszahlen[6] - Spacedrepetition["f7"])
    differenz1 += math.fabs(trainingszahlen[7] - Spacedrepetition["f8"])
    differenz1 += math.fabs(trainingszahlen[8] - Spacedrepetition["f9"])
    differenz1 += math.fabs(trainingszahlen[9] - Spacedrepetition["f10"])

    differenz2 = 0
    differenz2 += math.fabs(trainingszahlen[0] - blurtingmethod["f1"])
    differenz2 += math.fabs(trainingszahlen[1] - blurtingmethod["f2"])
    differenz2 += math.fabs(trainingszahlen[2] - blurtingmethod["f3"])
    differenz2 += math.fabs(trainingszahlen[3] - blurtingmethod["f4"])
    differenz2 += math.fabs(trainingszahlen[4] - blurtingmethod["f5"])
    differenz2 += math.fabs(trainingszahlen[5] - blurtingmethod["f6"])
    differenz2 += math.fabs(trainingszahlen[6] - blurtingmethod["f7"])
    differenz2 += math.fabs(trainingszahlen[7] - blurtingmethod["f8"])
    differenz2 += math.fabs(trainingszahlen[8] - blurtingmethod["f9"])
    differenz2 += math.fabs(trainingszahlen[9] - blurtingmethod["f10"])

    differenz3 = 0
    differenz3 += math.fabs(trainingszahlen[0] - Pomodorotechnique["f1"])
    differenz3 += math.fabs(trainingszahlen[1] - Pomodorotechnique["f2"])
    differenz3 += math.fabs(trainingszahlen[2] - Pomodorotechnique["f3"])
    differenz3 += math.fabs(trainingszahlen[3] - Pomodorotechnique["f4"])
    differenz3 += math.fabs(trainingszahlen[4] - Pomodorotechnique["f5"])
    differenz3 += math.fabs(trainingszahlen[5] - Pomodorotechnique["f6"])
    differenz3 += math.fabs(trainingszahlen[6] - Pomodorotechnique["f7"])
    differenz3 += math.fabs(trainingszahlen[7] - Pomodorotechnique["f8"])
    differenz3 += math.fabs(trainingszahlen[8] - Pomodorotechnique["f9"])
    differenz3 += math.fabs(trainingszahlen[9] - Pomodorotechnique["f10"])

    differenz4 = 0
    differenz4 += math.fabs(trainingszahlen[0] - interleavedlearning["f1"])
    differenz4 += math.fabs(trainingszahlen[1] - interleavedlearning["f2"])
    differenz4 += math.fabs(trainingszahlen[2] - interleavedlearning["f3"])
    differenz4 += math.fabs(trainingszahlen[3] - interleavedlearning["f4"])
    differenz4 += math.fabs(trainingszahlen[4] - interleavedlearning["f5"])
    differenz4 += math.fabs(trainingszahlen[5] - interleavedlearning["f6"])
    differenz4 += math.fabs(trainingszahlen[6] - interleavedlearning["f7"])
    differenz4 += math.fabs(trainingszahlen[7] - interleavedlearning["f8"])
    differenz4 += math.fabs(trainingszahlen[8] - interleavedlearning["f9"])
    differenz4 += math.fabs(trainingszahlen[9] - interleavedlearning["f10"])

    differenz5 = 0
    differenz5 += math.fabs(trainingszahlen[0] - FeynmanTechnique["f1"])
    differenz5 += math.fabs(trainingszahlen[1] - FeynmanTechnique["f2"])
    differenz5 += math.fabs(trainingszahlen[2] - FeynmanTechnique["f3"])
    differenz5 += math.fabs(trainingszahlen[3] - FeynmanTechnique["f4"])
    differenz5 += math.fabs(trainingszahlen[4] - FeynmanTechnique["f5"])
    differenz5 += math.fabs(trainingszahlen[5] - FeynmanTechnique["f6"])
    differenz5 += math.fabs(trainingszahlen[6] - FeynmanTechnique["f7"])
    differenz5 += math.fabs(trainingszahlen[7] - FeynmanTechnique["f8"])
    differenz5 += math.fabs(trainingszahlen[8] - FeynmanTechnique["f9"])
    differenz5 += math.fabs(trainingszahlen[9] - FeynmanTechnique["f10"])

    differenz6 = 0
    differenz6 += math.fabs(trainingszahlen[0] - TimeBlocking["f1"])
    differenz6 += math.fabs(trainingszahlen[1] - TimeBlocking["f2"])
    differenz6 += math.fabs(trainingszahlen[2] - TimeBlocking["f3"])
    differenz6 += math.fabs(trainingszahlen[3] - TimeBlocking["f4"])
    differenz6 += math.fabs(trainingszahlen[4] - TimeBlocking["f5"])
    differenz6 += math.fabs(trainingszahlen[5] - TimeBlocking["f6"])
    differenz6 += math.fabs(trainingszahlen[6] - TimeBlocking["f7"])
    differenz6 += math.fabs(trainingszahlen[7] - TimeBlocking["f8"])
    differenz6 += math.fabs(trainingszahlen[8] - TimeBlocking["f9"])
    differenz6 += math.fabs(trainingszahlen[9] - TimeBlocking["f10"])

    differenz7 = 0
    differenz7 += math.fabs(trainingszahlen[0] - FiveMinuteRule["f1"])
    differenz7 += math.fabs(trainingszahlen[1] - FiveMinuteRule["f2"])
    differenz7 += math.fabs(trainingszahlen[2] - FiveMinuteRule["f3"])
    differenz7 += math.fabs(trainingszahlen[3] - FiveMinuteRule["f4"])
    differenz7 += math.fabs(trainingszahlen[4] - FiveMinuteRule["f5"])
    differenz7 += math.fabs(trainingszahlen[5] - FiveMinuteRule["f6"])
    differenz7 += math.fabs(trainingszahlen[6] - FiveMinuteRule["f7"])
    differenz7 += math.fabs(trainingszahlen[7] - FiveMinuteRule["f8"])
    differenz7 += math.fabs(trainingszahlen[8] - FiveMinuteRule["f9"])
    differenz7 += math.fabs(trainingszahlen[9] - FiveMinuteRule["f10"])

    differenz8 = 0
    differenz8 += math.fabs(trainingszahlen[0] - ThreeTwoOneMethod["f1"])
    differenz8 += math.fabs(trainingszahlen[1] - ThreeTwoOneMethod["f2"])
    differenz8 += math.fabs(trainingszahlen[2] - ThreeTwoOneMethod["f3"])
    differenz8 += math.fabs(trainingszahlen[3] - ThreeTwoOneMethod["f4"])
    differenz8 += math.fabs(trainingszahlen[4] - ThreeTwoOneMethod["f5"])
    differenz8 += math.fabs(trainingszahlen[5] - ThreeTwoOneMethod["f6"])
    differenz8 += math.fabs(trainingszahlen[6] - ThreeTwoOneMethod["f7"])
    differenz8 += math.fabs(trainingszahlen[7] - ThreeTwoOneMethod["f8"])
    differenz8 += math.fabs(trainingszahlen[8] - ThreeTwoOneMethod["f9"])
    differenz8 += math.fabs(trainingszahlen[9] - ThreeTwoOneMethod["f10"])

    differenz9 = 0
    differenz9 += math.fabs(trainingszahlen[0] - LeitnerSystem["f1"])
    differenz9 += math.fabs(trainingszahlen[1] - LeitnerSystem["f2"])
    differenz9 += math.fabs(trainingszahlen[2] - LeitnerSystem["f3"])
    differenz9 += math.fabs(trainingszahlen[3] - LeitnerSystem["f4"])
    differenz9 += math.fabs(trainingszahlen[4] - LeitnerSystem["f5"])
    differenz9 += math.fabs(trainingszahlen[5] - LeitnerSystem["f6"])
    differenz9 += math.fabs(trainingszahlen[6] - LeitnerSystem["f7"])
    differenz9 += math.fabs(trainingszahlen[7] - LeitnerSystem["f8"])
    differenz9 += math.fabs(trainingszahlen[8] - LeitnerSystem["f9"])
    differenz9 += math.fabs(trainingszahlen[9] - LeitnerSystem["f10"])
   

    dictionary = {
        "Spacedrepetition": differenz1, 
        "BlurtingMethod": differenz2, 
        "PomodoroTechnique": differenz3, 
        "InterleavedLearning": differenz4,
        "FeynmanTechnique": differenz5,
        "TimeBlocking": differenz6,
        "FiveMinuteRule": differenz7,
        "ThreeTwoOneMethod": differenz8,
        "LeitnerSystem": differenz9
    }

    beste_methode = min(dictionary, key=dictionary.get)
    print(f"{beste_methode}")

    return beste_methode

if __name__ == '__main__':
    argument_json = sys.argv[1]
    data = json.loads(argument_json)
    lernmethode = datenverarbeiten(data)

