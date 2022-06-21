from itertools import chain

def skrati_modul(modul):
    if modul == "Računarski upravljački sistemi": return 'auto'
    if modul == "Računarska tehnika i računarske komunikacije": return 'rtrk'
    return 'prni'

def produzi_modul(modul):
    if modul == "auto": return 'Računarski upravljački sistemi'
    if modul == "rtrk": return 'Računarska tehnika i računarske komunikacije'
    return 'Primenjene računarske nauke i informatika'

def broj_mesta(modul):
    if modul == "Računarski upravljački sistemi": 
        return 10 #128
    if modul == "Računarska tehnika i računarske komunikacije": 
        return 10 #128
    return 10

def vrati_filter(request):
    if request.GET and request.GET.get('filter'):
        return request.GET.get('filter')
    else:
        return skrati_modul(request.user.modul_prva_zelja)
        
def syncFirstWishes(request, user_list):
    for user in user_list:
        if user.pk != request.user.pk:
            user.upao_na_prvu_zelju = True
            user.save()

def syncSecondWishes(request, user_list):
    for user in user_list:
        if user.pk != request.user.pk:
            user.upao_na_drugu_zelju = True
            user.save()

def syncNotAccepted(request, user_list):
    for user in user_list:
        if user.pk != request.user.pk:
            user.upao_na_prvu_zelju = False
            user.save()

def returnList(request, all_users, modul, returnornot):
    tabela = []
    rest = []
    filtered_not_accepted = []
    syncNA = False
    sync2 = False
    zamodul = produzi_modul(modul)
    bm = broj_mesta(zamodul)
    pz = request.user.modul_prva_zelja
    dz = request.user.modul_druga_zelja

    filtered_users = all_users.filter(modul_prva_zelja=zamodul).order_by('-modul_score')[:bm]
    count = filtered_users.count()
    if count < bm:
        if pz == zamodul:
            request.user.upao_na_prvu_zelju = True
        elif dz == zamodul:
            request.user.upao_na_drugu_zelju = True
        rest = all_users.filter(modul_druga_zelja=zamodul, upao_na_prvu_zelju = False).order_by('-modul_score')[:(bm - count)]
        tabela = list(chain(filtered_users, rest))
        sync2 = True

    elif (filtered_users[count-1].modul_score < request.user.modul_score) or (filtered_users[count-1].pk == request.user.pk):
        if pz == zamodul:
            request.user.upao_na_prvu_zelju = True
        elif dz == zamodul:
            request.user.upao_na_drugu_zelju = True
        tabela = filtered_users
        filtered_not_accepted = filtered_users = all_users.filter(modul_prva_zelja=zamodul).order_by('-modul_score')[bm:]
        syncNA = True

    else:
        if pz == zamodul:
            request.user.upao_na_prvu_zelju = False
        elif dz == zamodul:
            request.user.upao_na_drugu_zelju = False
        tabela = filtered_users
        filtered_not_accepted = filtered_users = all_users.filter(modul_prva_zelja=zamodul).order_by('-modul_score')[bm:]
        syncNA = True

    request.user.save()

    if sync2:
        syncFirstWishes(request, filtered_users)
        syncSecondWishes(request, rest)
    else:
        syncFirstWishes(request, filtered_users)

    if syncNA:
        syncNotAccepted(request, filtered_not_accepted)

    if returnornot:
        return tabela




