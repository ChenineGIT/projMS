salle = {
    "id1": {"name": "s1", "capacity": 45,"reserve": False},
    "id2": {"name": "s2", "capacity": 45,"reserve": False},
    "id3": {"name": "s3", "capacity": 45,"reserve": False},
    "id4": {"name": "s4", "capacity": 45,"reserve": False},

    "id5": {"name": "a1", "capacity": 200,"reserve": False},
    "id6": {"name": "a2", "capacity": 200,"reserve": False},
    "id7": {"name": "a3", "capacity": 200,"reserve": False},
    "id8": {"name": "a4", "capacity": 200,"reserve": False},

    "id9": {"name": "t1", "capacity": 35,"reserve": False},
    "id10": {"name": "t2", "capacity": 35,"reserve": False},
    "id11": {"name": "t3", "capacity": 40,"reserve": False},
    "id12": {"name": "t4", "capacity": 40,"reserve": False},
    "id13": {"name": "t5", "capacity": 45,"reserve": False}

}
profs = {
    "prof1": {"name": "prof1", "teach": ['RES', 'SemP'], "is_read": False},
    "prof2": {"name": "prof2", "teach": ['SEC', 'BDA'], "is_read": False},
    "prof3": {"name": "prof3", "teach": ['SIN'], "is_read": False},
    "prof4": {"name": "prof4", "teach": ['MS'], "is_read": False},
    "prof5": {"name": "prof5", "teach": ['SE'], "is_read": False},
    "prof6": {"name": "prof6", "teach": ['PL'], "is_read": False},
    "prof7": {"name": "prof7", "teach": ['GL'], "is_read": False},
    "prof8": {"name": "prof8", "teach": ['IHM'], "is_read": False},
    "prof9": {"name": "prof9", "teach": ['COMP'], "is_read": False},
    "prof10": {"name": "prof10", "teach": ['SI'], "is_read": False},
    "prof11": {"name": "prof11", "teach": ['PS'], "is_read": False}

}
modules = {
    "ASR1": {"name": "RES", "types": [{"session": "cour", "nbr_session": 2, "is_read": False}, {"session": "tp", "nbr_session": 1, "is_read": False}]},
    "ASR2": {"name": "SEC", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}, {"session": "td", "nbr_session": 1, "is_read": False}, {"session": "tp", "nbr_session": 1, "is_read": False}]},
    "ASR3": {"name": "SIN", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}, {"session": "td", "nbr_session": 1, "is_read": False}, {"session": "tp", "nbr_session": 1, "is_read": False}]},
    "ASR4": {"name": "BDA", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}, {"session": "td", "nbr_session": 1, "is_read": False}, {"session": "tp", "nbr_session": 1, "is_read": False}]},
    "ASR5": {"name": "SemP", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}]},
    "ASR6": {"name": "SE", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}, {"session": "tp", "nbr_session": 1, "is_read": False}]},
    "ASR7": {"name": "MS", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}]},

    "L3_1": {"name": "PL", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}]},
    "L3_2": {"name": "GL", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}, {"session": "td", "nbr_session": 1, "is_read": False}, {"session": "tp", "nbr_session": 1, "is_read": False}]},
    "L3_3": {"name": "IHM", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}, {"session": "tp", "nbr_session": 1, "is_read": False}]},
    "L3_4": {"name": "COMP", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}, {"session": "td", "nbr_session": 1, "is_read": False}, {"session": "tp", "nbr_session": 1, "is_read": False}]},
    "L3_5": {"name": "SI", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}, {"session": "td", "nbr_session": 1, "is_read": False}, {"session": "tp", "nbr_session": 1, "is_read": False}]},
    "L3_6": {"name": "PS", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}, {"session": "td", "nbr_session": 1, "is_read": False}]},

    "L2_1": {"name": "MN", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}]},
    "L2_2": {"name": "ASD", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}, {"session": "td", "nbr_session": 1, "is_read": False}, {"session": "tp", "nbr_session": 1, "is_read": False}]},
    "L2_3": {"name": "TG", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}, {"session": "td", "nbr_session": 1, "is_read": False}]},
    "L2_4": {"name": "AO", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}, {"session": "td", "nbr_session": 1, "is_read": False}]},
    "L2_5": {"name": "SE", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}, {"session": "td", "nbr_session": 1, "is_read": False}, {"session": "tp", "nbr_session": 1, "is_read": False}]},
    "L2_6": {"name": "LM", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}, {"session": "td", "nbr_session": 1, "is_read": False}]}

}
groups = {
    "group1": [{"name": "ASR", "modules": [{"name": "RES"}, {"name": "SIN"}, {"name": "SEC"}, {"name": "BDA"}, {"name": "MS"}, {"name": "SE"}] , "capacity": 35, "is_read": False}],
    "group2": [{"name": "FOND", "modules": [{"name": "M1"}, {"name": "M2"}, {"name": "M3"}, {"name": "M4"}], "capacity": 38, "is_read": False}],
    "group3": [{"name": "IND", "modules": [{"name": "MS"}, {"name": "m6"}], "capacity": 33, "is_read": False}],
    "group4": [{"name": "AI", "modules": [{"name": "IMG"}, {"name": "MATH"}, {"name": "PS"}], "capacity": 32, "is_read": False}],
    "group5": [{"name": "L3-a", "modules": [{"name": "PL"}, {"name": "GL"}, {"name": "IHM"}, {"name": "COMP"}, {"name": "SI"}, {"name": "PS"}], "capacity": 29, "is_read": False}],
    "group6": [{"name": "L3-b", "modules": [{"name": "PL"}, {"name": "GL"}, {"name": "IHM"}, {"name": "COMP"}, {"name": "SI"}, {"name": "PS"}], "capacity": 30, "is_read": False}],
    "group7": [{"name": "L2-a", "modules": [{"name": "ASD"}, {"name": "TG"}, {"name": "AO"}, {"name": "MN"}, {"name": "LM"}, {"name": "SE"}], "capacity": 30, "is_read": False}]
}

final_table = {
    "Saturday": {
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": []
    },
    "Sunday": {
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": []
    },
    "Monday": {
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": []
    },
    "Tuesday": {
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": []
    },
    "Wednesday": {
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": []
    },
    "Thursday": {
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": []
    }
}

def compenent_sessions(groups: dict, profs: dict, modules: dict):
    list_of_session = list()
    for group in groups:
        for sub_group in groups[group]:
            name_group = sub_group["name"]
            for mod in sub_group["modules"]:
                name_module = mod["name"]
                for prof in profs:
                    for teach in profs[prof]["teach"]:
                        if teach == name_module:
                            name_prof = profs[prof]["name"]
                            # print(name_group, name_module, name_prof)

                            for module in modules:
                                if modules[module]["name"] == name_module:
                                    for types in modules[module]["types"]:
                                        for in_type in types:
                                            temp_nbrSession = types["nbr_session"]
                                            if types["nbr_session"] != 0:
                                                for i in range(1, types["nbr_session"]+1):

                                                    this_session = {
                                                        "name_group": name_group,
                                                        "name_prof": name_prof,
                                                        "name_module": name_module,
                                                        "type_session": types["session"],
                                                        "number_session": i
                                                    }
                                                    list_of_session.append(this_session)
                                            types["nbr_session"] = 0
                                        types["nbr_session"] = temp_nbrSession
    return list_of_session


def divise_typeModules(list_of_session: list):
    """ func divise all module to cour , td , tp"""
    list_cours = list()
    list_td = list()
    list_tp = list()
    for sessions in list_of_session:
        if sessions["type_session"] == "cour":
            list_cours.append(sessions)
        elif sessions["type_session"] == "td":
            list_td.append(sessions)
        else:
            list_tp.append(sessions)
    return list_cours, list_td, list_tp

def pose_table(list_cour: list, list_td: list, list_tp: list, final_table: dict):
    """ func pose all session in table """

    for cour in list_cour:
        print(cour)



















# =======================================================================================
""" main program """
if __name__ == '__main__':

    list_sessions = compenent_sessions(groups, profs, modules)

    for session in list_sessions:
        print(session)
        print("===================")
    # list_cour, list_td, list_tp = divise_typeModules(list_sessions)
    #
    # pose_table(list_cour, list_td, list_tp,final_table)


# def compenent_sessions(groups: dict, profs: dict, modules: dict):
#     list_of_session = list()
#     for group in groups:
#         for sub_group in groups[group]:
#             """ print all groups"""
#             # print(sub_group["name"])
#             """ take name group"""
#             name_group = sub_group["name"]
#             """ take names module she read this group"""
#             for modulee in sub_group["modules"]:
#                 name_module = modulee["name"]
#                 """ take name prof he is read this module"""
#                 for prof in profs:
#                     for teacher in profs[prof]["teach"]:
#                         """ check from modules are read prof == name module or no"""
#                         if teacher == name_module:
#                             name_prof = profs[prof]["name"]
#                             """ take type session the module (cour or td or tp)"""
#                             for module in modules:
#                                 if modules[module]["name"] == name_module:
#                                     for typ in modules[module]["types"]:
#                                         for on_type in typ:
#                                             """ check from number session"""
#                                             temp_nbrSession = typ["nbr_session"]
#                                             if typ["nbr_session"] != 0:
#                                                 for i in range(1, typ["nbr_session"]+1):
#                                                     this_Session = {
#                                                         "name_group": name_group,
#                                                         "name_prof": name_prof,
#                                                         "name_module": name_module,
#                                                         "type_session": typ["session"],
#                                                         "number_session": i
#                                                     }
#                                                     """ append session to list session"""
#                                                     list_of_session.append(this_Session)
#                                                 typ["nbr_session"] = 0
#                                         typ["nbr_session"] = temp_nbrSession
#     return list_of_session

salle = {
    "id1": {"name": "s1", "capacity": 45,"reserve": False},
    "id2": {"name": "s2", "capacity": 45,"reserve": False},
    "id3": {"name": "s3", "capacity": 45,"reserve": False},
    "id4": {"name": "s4", "capacity": 45,"reserve": False},

    "id5": {"name": "a1", "capacity": 200,"reserve": False},
    "id6": {"name": "a2", "capacity": 200,"reserve": False},
    "id7": {"name": "a3", "capacity": 200,"reserve": False},
    "id8": {"name": "a4", "capacity": 200,"reserve": False},

    "id9": {"name": "t1", "capacity": 35,"reserve": False},
    "id10": {"name": "t2", "capacity": 35,"reserve": False},
    "id11": {"name": "t3", "capacity": 40,"reserve": False},
    "id12": {"name": "t4", "capacity": 40,"reserve": False},
    "id13": {"name": "t5", "capacity": 45,"reserve": False}

}
profs = {
    "prof1": {"name": "prof1", "teach": ['m1', 'm2'], "is_read": False},
    "prof2": {"name": "prof2", "teach": ['m3', 'm4'], "is_read": False},
    "prof3": {"name": "prof3", "teach": ['m6', 'm5'], "is_read": False},
    "prof4": {"name": "prof4", "teach": ['m7'], "is_read": False},
    "prof5": {"name": "prof5", "teach": ['m8'], "is_read": False},
    "prof6": {"name": "prof6", "teach": ['m9'], "is_read": False}

}
modules = {
    "module1": {"name": "m1", "types": [{"session": "cour", "nbr_session": 2, "is_read": False}, {"session": "tp", "nbr_session": 1, "is_read": False}]},
    "module2": {"name": "m2", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}, {"session": "td", "nbr_session": 1, "is_read": False}]},
    "module3": {"name": "m3", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}, {"session": "td", "nbr_session": 1, "is_read": False}, {"session": "tp", "nbr_session": 1, "is_read": False}]},
    "module4": {"name": "m4", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}]},
    "module5": {"name": "m5", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}, {"session": "td", "nbr_session": 1, "is_read": False}]},
    "module6": {"name": "m6", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}, {"session": "tp", "nbr_session": 1, "is_read": False}]},
    "module7": {"name": "m7", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}]},
    "module8": {"name": "m8", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}, {"session": "td", "nbr_session": 1, "is_read": False}]},
    "module9": {"name": "m9", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}, {"session": "tp", "nbr_session": 1, "is_read": False}]},
    "module10": {"name": "m10", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}]},
    "module11": {"name": "m11", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}, {"session": "td", "nbr_session": 1, "is_read": False}]}

}
groups = {
    "group1": [{"name": "ASR", "modules": [{"name": "m1"}, {"name": "m4"}] , "capacity": 35, "is_read": False}],
    "group2": [{"name": "FOND", "modules": [{"name": "m2"}, {"name": "m5"}], "capacity": 38, "is_read": False}],
    "group3": [{"name": "IND", "modules": [{"name": "m3"}, {"name": "m6"}], "capacity": 33, "is_read": False}],
    "group4": [{"name": "AI", "modules": [{"name": "m7"}, {"name": "m8"}], "capacity": 32, "is_read": False}],
    "group5": [{"name": "L3-a", "modules": [{"name": "m9"}, {"name": "m10"}], "capacity":29, "is_read": False}],
    "group6": [{"name": "L3-b", "modules":[{"name": "m9"}, {"name": "m10"}], "capacity": 30, "is_read": False}]

}

final_table = {
    "Saturday": {
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": []
    },
    "Sunday": {
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": []
    },
    "Monday": {
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": []
    },
    "Tuesday": {
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": []
    },
    "Wednesday": {
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": []
    },
    "Thursday": {
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": []
    }
}

def compenent_sessions(groups: dict, profs: dict, modules: dict):
    list_of_session = list()
    for group in groups:
        for sub_group in groups[group]:
            """ print all groups"""
            print(sub_group["name"], end='')
            """ take name group"""
            name_group = sub_group["name"]
            """ take names module she read this group"""
            for modulee in sub_group["modules"]:
                name_module = modulee["name"]
                """ take name prof he is read this module"""
                for prof in profs:
                    for teacher in profs[prof]["teach"]:
                        """ check from modules are read prof == name module or no"""
                        if teacher == name_module:
                            name_prof = profs[prof]["name"]
                            """ take type session the module (cour or td or tp)"""
                            for module in modules:
                                if modules[module]["name"] == name_module:
                                    for typ in modules[module]["types"]:
                                        for on_type in typ:
                                            """ check from number session"""
                                            temp_nbrSession = typ["nbr_session"]
                                            if typ["nbr_session"] != 0:
                                                for i in range(1, typ["nbr_session"]+1):
                                                    this_Session = {
                                                        "name_group": name_group,
                                                        "name_prof": name_prof,
                                                        "name_module": name_module,
                                                        "type_session": typ["session"],
                                                        "number_session": i
                                                    }
                                                    """ append session to list session"""
                                                    list_of_session.append(this_Session)
                                                typ["nbr_session"] = 0
                                        typ["nbr_session"] = temp_nbrSession
    return list_of_session


def divise_typeModules(list_of_session: list):
    """ func divise all module to cour , td , tp"""
    list_cours = list()
    list_td = list()
    list_tp = list()
    for sessions in list_of_session:
        if sessions["type_session"] == "cour":
            list_cours.append(sessions)
        elif sessions["type_session"] == "td":
            list_td.append(sessions)
        else:
            list_tp.append(sessions)
    return list_cours, list_td, list_tp

def pose_table(list_cour: list, list_td: list, list_tp: list, final_table: dict):
    """ func pose all session in table """

    for cour in list_cour:
        print(cour)



















# =======================================================================================
""" main program """
if __name__ == '__main__':

    list_sessions = compenent_sessions(groups, profs, modules)

    for session in list_sessions:
        print(session)
        print("===================")
    # list_cour, list_td, list_tp = divise_typeModules(list_sessions)
    #
    # pose_table(list_cour, list_td, list_tp,final_table)


# def compenent_sessions(groups: dict, profs: dict, modules: dict):
#     list_of_session = list()
#     for group in groups:
#         for sub_group in groups[group]:
#             """ print all groups"""
#             # print(sub_group["name"])
#             """ take name group"""
#             name_group = sub_group["name"]
#             """ take names module she read this group"""
#             for modulee in sub_group["modules"]:
#                 name_module = modulee["name"]
#                 """ take name prof he is read this module"""
#                 for prof in profs:
#                     for teacher in profs[prof]["teach"]:
#                         """ check from modules are read prof == name module or no"""
#                         if teacher == name_module:
#                             name_prof = profs[prof]["name"]
#                             """ take type session the module (cour or td or tp)"""
#                             for module in modules:
#                                 if modules[module]["name"] == name_module:
#                                     for typ in modules[module]["types"]:
#                                         for on_type in typ:
#                                             """ check from number session"""
#                                             temp_nbrSession = typ["nbr_session"]
#                                             if typ["nbr_session"] != 0:
#                                                 for i in range(1, typ["nbr_session"]+1):
#                                                     this_Session = {
#                                                         "name_group": name_group,
#                                                         "name_prof": name_prof,
#                                                         "name_module": name_module,
#                                                         "type_session": typ["session"],
#                                                         "number_session": i
#                                                     }
#                                                     """ append session to list session"""
#                                                     list_of_session.append(this_Session)
#                                                 typ["nbr_session"] = 0
#                                         typ["nbr_session"] = temp_nbrSession
#     return list_of_session
salle = {
    "id1": {"name": "s1", "capacity": 45,"reserve": False},
    "id2": {"name": "s2", "capacity": 45,"reserve": False},
    "id3": {"name": "s3", "capacity": 45,"reserve": False},
    "id4": {"name": "s4", "capacity": 45,"reserve": False},

    "id5": {"name": "a1", "capacity": 200,"reserve": False},
    "id6": {"name": "a2", "capacity": 200,"reserve": False},
    "id7": {"name": "a3", "capacity": 200,"reserve": False},
    "id8": {"name": "a4", "capacity": 200,"reserve": False},

    "id9": {"name": "t1", "capacity": 35,"reserve": False},
    "id10": {"name": "t2", "capacity": 35,"reserve": False},
    "id11": {"name": "t3", "capacity": 40,"reserve": False},
    "id12": {"name": "t4", "capacity": 40,"reserve": False},
    "id13": {"name": "t5", "capacity": 45,"reserve": False}

}
profs = {
    "prof1": {"name": "prof1", "teach": ['m1', 'm2'], "is_read": False},
    "prof2": {"name": "prof2", "teach": ['m3', 'm4'], "is_read": False},
    "prof3": {"name": "prof3", "teach": ['m6', 'm5'], "is_read": False},
    "prof4": {"name": "prof4", "teach": ['m7'], "is_read": False},
    "prof5": {"name": "prof5", "teach": ['m8'], "is_read": False},
    "prof6": {"name": "prof6", "teach": ['m9'], "is_read": False}

}
modules = {
    "module1": {"name": "m1", "types": [{"session": "cour", "nbr_session": 2, "is_read": False}, {"session": "tp", "nbr_session": 1, "is_read": False}]},
    "module2": {"name": "m2", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}, {"session": "td", "nbr_session": 1, "is_read": False}]},
    "module3": {"name": "m3", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}, {"session": "td", "nbr_session": 1, "is_read": False}, {"session": "tp", "nbr_session": 1, "is_read": False}]},
    "module4": {"name": "m4", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}]},
    "module5": {"name": "m5", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}, {"session": "td", "nbr_session": 1, "is_read": False}]},
    "module6": {"name": "m6", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}, {"session": "tp", "nbr_session": 1, "is_read": False}]},
    "module7": {"name": "m7", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}]},
    "module8": {"name": "m8", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}, {"session": "td", "nbr_session": 1, "is_read": False}]},
    "module9": {"name": "m9", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}, {"session": "tp", "nbr_session": 1, "is_read": False}]},
    "module10": {"name": "m10", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}]},
    "module11": {"name": "m11", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}, {"session": "td", "nbr_session": 1, "is_read": False}]}

}
groups = {
    "group1": [{"name": "ASR", "modules": [{"name": "m1"}, {"name": "m4"}] , "capacity": 35, "is_read": False}],
    "group2": [{"name": "FOND", "modules": [{"name": "m2"}, {"name": "m5"}], "capacity": 38, "is_read": False}],
    "group3": [{"name": "IND", "modules": [{"name": "m3"}, {"name": "m6"}], "capacity": 33, "is_read": False}],
    "group4": [{"name": "AI", "modules": [{"name": "m7"}, {"name": "m8"}], "capacity": 32, "is_read": False}],
    "group5": [{"name": "L3-a", "modules": [{"name": "m9"}, {"name": "m10"}], "capacity":29, "is_read": False}],
    "group6": [{"name": "L3-b", "modules":[{"name": "m9"}, {"name": "m10"}], "capacity": 30, "is_read": False}]

}

final_table = {
    "Saturday": {
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": []
    },
    "Sunday": {
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": []
    },
    "Monday": {
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": []
    },
    "Tuesday": {
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": []
    },
    "Wednesday": {
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": []
    },
    "Thursday": {
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": []
    }
}

def compenent_sessions(groups: dict, profs: dict, modules: dict):
    list_of_session = list()
    for group in groups:
        for sub_group in groups[group]:
            """ print all groups"""
            print(sub_group["name"], end='')
            """ take name group"""
            name_group = sub_group["name"]
            """ take names module she read this group"""
            for modulee in sub_group["modules"]:
                name_module = modulee["name"]
                """ take name prof he is read this module"""
                for prof in profs:
                    for teacher in profs[prof]["teach"]:
                        """ check from modules are read prof == name module or no"""
                        if teacher == name_module:
                            name_prof = profs[prof]["name"]
                            """ take type session the module (cour or td or tp)"""
                            for module in modules:
                                if modules[module]["name"] == name_module:
                                    for typ in modules[module]["types"]:
                                        for on_type in typ:
                                            """ check from number session"""
                                            temp_nbrSession = typ["nbr_session"]
                                            if typ["nbr_session"] != 0:
                                                for i in range(1, typ["nbr_session"]+1):
                                                    this_Session = {
                                                        "name_group": name_group,
                                                        "name_prof": name_prof,
                                                        "name_module": name_module,
                                                        "type_session": typ["session"],
                                                        "number_session": i
                                                    }
                                                    """ append session to list session"""
                                                    list_of_session.append(this_Session)
                                                typ["nbr_session"] = 0
                                        typ["nbr_session"] = temp_nbrSession
    return list_of_session


def divise_typeModules(list_of_session: list):
    """ func divise all module to cour , td , tp"""
    list_cours = list()
    list_td = list()
    list_tp = list()
    for sessions in list_of_session:
        if sessions["type_session"] == "cour":
            list_cours.append(sessions)
        elif sessions["type_session"] == "td":
            list_td.append(sessions)
        else:
            list_tp.append(sessions)
    return list_cours, list_td, list_tp

def pose_table(list_cour: list, list_td: list, list_tp: list, final_table: dict):
    """ func pose all session in table """

    for cour in list_cour:
        print(cour)



















# =======================================================================================
""" main program """
if __name__ == '__main__':

    list_sessions = compenent_sessions(groups, profs, modules)

    for session in list_sessions:
        print(session)
        print("===================")
    # list_cour, list_td, list_tp = divise_typeModules(list_sessions)
    #
    # pose_table(list_cour, list_td, list_tp,final_table)


# def compenent_sessions(groups: dict, profs: dict, modules: dict):
#     list_of_session = list()
#     for group in groups:
#         for sub_group in groups[group]:
#             """ print all groups"""
#             # print(sub_group["name"])
#             """ take name group"""
#             name_group = sub_group["name"]
#             """ take names module she read this group"""
#             for modulee in sub_group["modules"]:
#                 name_module = modulee["name"]
#                 """ take name prof he is read this module"""
#                 for prof in profs:
#                     for teacher in profs[prof]["teach"]:
#                         """ check from modules are read prof == name module or no"""
#                         if teacher == name_module:
#                             name_prof = profs[prof]["name"]
#                             """ take type session the module (cour or td or tp)"""
#                             for module in modules:
#                                 if modules[module]["name"] == name_module:
#                                     for typ in modules[module]["types"]:
#                                         for on_type in typ:
#                                             """ check from number session"""
#                                             temp_nbrSession = typ["nbr_session"]
#                                             if typ["nbr_session"] != 0:
#                                                 for i in range(1, typ["nbr_session"]+1):
#                                                     this_Session = {
#                                                         "name_group": name_group,
#                                                         "name_prof": name_prof,
#                                                         "name_module": name_module,
#                                                         "type_session": typ["session"],
#                                                         "number_session": i
#                                                     }
#                                                     """ append session to list session"""
#                                                     list_of_session.append(this_Session)
#                                                 typ["nbr_session"] = 0
#                                         typ["nbr_session"] = temp_nbrSession
#     return list_of_session
"""
salle = {
    "id1": {"name": "s1", "capacity": 45,"reserve": False},
    "id2": {"name": "s2", "capacity": 45,"reserve": False},
    "id3": {"name": "s3", "capacity": 45,"reserve": False},
    "id4": {"name": "s4", "capacity": 45,"reserve": False},

    "id5": {"name": "a1", "capacity": 200,"reserve": False},
    "id6": {"name": "a2", "capacity": 200,"reserve": False},
    "id7": {"name": "a3", "capacity": 200,"reserve": False},
    "id8": {"name": "a4", "capacity": 200,"reserve": False},

    "id9": {"name": "t1", "capacity": 35,"reserve": False},
    "id10": {"name": "t2", "capacity": 35,"reserve": False},
    "id11": {"name": "t3", "capacity": 40,"reserve": False},
    "id12": {"name": "t4", "capacity": 40,"reserve": False},
    "id13": {"name": "t5", "capacity": 45,"reserve": False}

}
profs = {
    "prof1": {"name": "prof1", "teach": ['m1', 'm2'], "is_read": False},
    "prof2": {"name": "prof2", "teach": ['m3', 'm4'], "is_read": False},
    "prof3": {"name": "prof3", "teach": ['m6', 'm5'], "is_read": False},
    "prof4": {"name": "prof4", "teach": ['m7'], "is_read": False},
    "prof5": {"name": "prof5", "teach": ['m8'], "is_read": False},
    "prof6": {"name": "prof6", "teach": ['m9'], "is_read": False}

}
modules = {
    "module1": {"name": "m1", "types": [{"session": "cour", "nbr_session": 2, "is_read": False}, {"session": "tp", "nbr_session": 1, "is_read": False}]},
    "module2": {"name": "m2", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}, {"session": "td", "nbr_session": 1, "is_read": False}]},
    "module3": {"name": "m3", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}, {"session": "td", "nbr_session": 1, "is_read": False}, {"session": "tp", "nbr_session": 1, "is_read": False}]},
    "module4": {"name": "m4", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}]},
    "module5": {"name": "m5", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}, {"session": "td", "nbr_session": 1, "is_read": False}]},
    "module6": {"name": "m6", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}, {"session": "tp", "nbr_session": 1, "is_read": False}]},
    "module7": {"name": "m7", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}]},
    "module8": {"name": "m8", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}, {"session": "td", "nbr_session": 1, "is_read": False}]},
    "module9": {"name": "m9", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}, {"session": "tp", "nbr_session": 1, "is_read": False}]},
    "module10": {"name": "m10", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}]},
    "module11": {"name": "m11", "types": [{"session": "cour", "nbr_session": 1, "is_read": False}, {"session": "td", "nbr_session": 1, "is_read": False}]}

}
groups = {
    "group1": [{"name": "ASR", "modules": [{"name": "m1"}, {"name": "m4"}] , "capacity": 35, "is_read": False}],
    "group2": [{"name": "FOND", "modules": [{"name": "m2"}, {"name": "m5"}], "capacity": 38, "is_read": False}],
    "group3": [{"name": "IND", "modules": [{"name": "m3"}, {"name": "m6"}], "capacity": 33, "is_read": False}],
    "group4": [{"name": "AI", "modules": [{"name": "m7"}, {"name": "m8"}], "capacity": 32, "is_read": False}],
    "group5": [{"name": "L3-a", "modules": [{"name": "m9"}, {"name": "m10"}], "capacity":29, "is_read": False}],
    "group6": [{"name": "L3-b", "modules":[{"name": "m9"}, {"name": "m10"}], "capacity": 30, "is_read": False}]

}

final_table = {
    "Saturday": {
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": []
    },
    "Sunday": {
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": []
    },
    "Monday": {
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": []
    },
    "Tuesday": {
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": []
    },
    "Wednesday": {
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": []
    },
    "Thursday": {
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": []
    }
}

def compenent_sessions(groups: dict, profs: dict, modules: dict):
    list_of_session = list()
    for group in groups:
        for sub_group in groups[group]:
            """ print all groups"""
            print(sub_group["name"], end='')
            """ take name group"""
            name_group = sub_group["name"]
            """ take names module she read this group"""
            for modulee in sub_group["modules"]:
                name_module = modulee["name"]
                """ take name prof he is read this module"""
                for prof in profs:
                    for teacher in profs[prof]["teach"]:
                        """ check from modules are read prof == name module or no"""
                        if teacher == name_module:
                            name_prof = profs[prof]["name"]
                            """ take type session the module (cour or td or tp)"""
                            for module in modules:
                                if modules[module]["name"] == name_module:
                                    for typ in modules[module]["types"]:
                                        for on_type in typ:
                                            """ check from number session"""
                                            temp_nbrSession = typ["nbr_session"]
                                            if typ["nbr_session"] != 0:
                                                for i in range(1, typ["nbr_session"]+1):
                                                    this_Session = {
                                                        "name_group": name_group,
                                                        "name_prof": name_prof,
                                                        "name_module": name_module,
                                                        "type_session": typ["session"],
                                                        "number_session": i
                                                    }
                                                    """ append session to list session"""
                                                    list_of_session.append(this_Session)
                                                typ["nbr_session"] = 0
                                        typ["nbr_session"] = temp_nbrSession
    return list_of_session


def divise_typeModules(list_of_session: list):
    """ func divise all module to cour , td , tp"""
    list_cours = list()
    list_td = list()
    list_tp = list()
    for sessions in list_of_session:
        if sessions["type_session"] == "cour":
            list_cours.append(sessions)
        elif sessions["type_session"] == "td":
            list_td.append(sessions)
        else:
            list_tp.append(sessions)
    return list_cours, list_td, list_tp

def pose_table(list_cour: list, list_td: list, list_tp: list, final_table: dict):
    """ func pose all session in table """

    for cour in list_cour:
        print(cour)



















# =======================================================================================
""" main program """
if __name__ == '__main__':

    list_sessions = compenent_sessions(groups, profs, modules)

    for session in list_sessions:
        print(session)
        print("===================")
    # list_cour, list_td, list_tp = divise_typeModules(list_sessions)
    #
    # pose_table(list_cour, list_td, list_tp,final_table)


# def compenent_sessions(groups: dict, profs: dict, modules: dict):
#     list_of_session = list()
#     for group in groups:
#         for sub_group in groups[group]:
#             """ print all groups"""
#             # print(sub_group["name"])
#             """ take name group"""
#             name_group = sub_group["name"]
#             """ take names module she read this group"""
#             for modulee in sub_group["modules"]:
#                 name_module = modulee["name"]
#                 """ take name prof he is read this module"""
#                 for prof in profs:
#                     for teacher in profs[prof]["teach"]:
#                         """ check from modules are read prof == name module or no"""
#                         if teacher == name_module:
#                             name_prof = profs[prof]["name"]
#                             """ take type session the module (cour or td or tp)"""
#                             for module in modules:
#                                 if modules[module]["name"] == name_module:
#                                     for typ in modules[module]["types"]:
#                                         for on_type in typ:
#                                             """ check from number session"""
#                                             temp_nbrSession = typ["nbr_session"]
#                                             if typ["nbr_session"] != 0:
#                                                 for i in range(1, typ["nbr_session"]+1):
#                                                     this_Session = {
#                                                         "name_group": name_group,
#                                                         "name_prof": name_prof,
#                                                         "name_module": name_module,
#                                                         "type_session": typ["session"],
#                                                         "number_session": i
#                                                     }
#                                                     """ append session to list session"""
#                                                     list_of_session.append(this_Session)
#                                                 typ["nbr_session"] = 0
#                                         typ["nbr_session"] = temp_nbrSession
#     return list_of_session

"""