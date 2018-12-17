def error(whi,collect=['None']):
    error_dic={'pro':"No program or op called : %s"%collect[0],\
               'para':"Input parameter invalid"}
    if whi in error_dic:
        string = error_dic[whi]
    else:
        string = " debug !"
    return '[!] ERROR- '+string
