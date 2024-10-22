import re


def clean_ads(recipes_dict):
    regex_base = re.compile("ADVERTISEMENT")
    for recipe, rec_attributes in recipes_dict.items():
        for i in range(len(rec_attributes["ingredients"])):
            # if rec_attributes["ingredients"][i] == 'INGRDIENTS':
            #     del rec_attributes["ingredients"][i]
            #     continue
            if regex_base.sub(" ", rec_attributes["ingredients"][i]):
                rec_attributes["ingredients"][i] = regex_base.sub(" ", rec_attributes["ingredients"][i])
        for i in range(len(rec_attributes["ingredients"])):
            if rec_attributes["ingredients"][i] == ' ':
                del rec_attributes["ingredients"][i]
                