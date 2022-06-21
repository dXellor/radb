from datetime import date

def remapYear(value, start_min_range, start_max_range, end_min_range, end_max_range):
    x = round(((value - start_min_range) * (end_max_range - end_min_range)/(start_max_range - start_min_range) + end_min_range), 4)
    if x < end_min_range: 
        x = end_min_range
    return x

def remap(value, min_value, max_value):
    if value < min_value:
        return 0
    return round(value/max_value, 4)


def return_score(espb, prosek, indeks):

    godina = int(indeks.split('/')[1])
    #Ako je student raxx/2021 u drugoj godini racunamo da se prebacio nas smer a da se upisao 2020
    if godina == 2021:                  
        godina = 2020

    #Za donje granice stavljamo donja_granica-1 zato sto necemo da student za dovoljnim minimalnim scoreom dobije score 0
    espb_score = remap(espb, 73, 120)
    prosek_score = remap(prosek, 6.00, 10.00)
    godina_score = remapYear(godina, 2020, 2016, 1, 0)

    return round((espb_score*prosek_score*godina_score), 4)

