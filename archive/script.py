"""
This script is used to extract data from an email provided through Zapier.
It needs to be run in a zap, it will not run locally without the correct input.
"""

import re

# This code is for debugging locally. This replaces the "input["body_html"]" and "input["subject"]" with values from a local file you need to give the path to.
# To debug, comment out the following lines:
# with open("path/to/zapier_html2.txt", "r") as file:
#    zapier_html = file.read()

#input = {
#    "body_html": zapier_html,
#    "subject":  "Visma har gjennomført en Onboarding på vår felles kunde LÅshuset Sikkerhetssenter AS"
#}

# These patterns are used to extract data from the email body
PATTERN_KUNDENAVN = "(Kundenavn: )(.{5,100}\n)"
PATTERN_KUNDEGRUPPE = "(Kundegruppe: )(.{0,2}\n)"
PATTERN_KJERNEPRODUKT = "(Kjerneprodukt:)(.{5,100}\n)"
PATTERN_PARTNER = "(Partner:)(.{5,40}\n)"
PATTERN_NPS_SCORE = "(NPS Score: )(\d{1,2})"
PATTERN_BRA = "(Hva har vært bra\?)(.+\n)"
PATTERN_BEDRE = "(Hva kunne vært bedre\?)(.+\n)"
PATTERN_ERDETNOEN = "(Er det noen hos .+ du mener har utmerket seg og som du vil trekke fram positivt så langt i oppstartsfasen\?)(.+)"
PATTERN_REFERAT = "(Referat: )(.+)(Ta gjerne kontakt med oss på Customer Success om du har spørsmål)"
PATTERN_TYPE = "(Onboarding completed)|(Onboarding)"
PATTERN_PRODUKT = "(Valgte produkter og hvor sannsynlig det er å anbefale dem)(.+)"
PATTERN_BRANSJEKODE = "(Bransjekode: )(.+)"

# Create a dictionary to put output in
# Zapier will only handle output if it is in a dictionary
output = {
    }

# Remove html tags from email body
# This works better than just using the plain email body from zapier
input["body_html"] = re.sub("<[^<]+?>", "", input["body_html"])

# Function to extract data from email body using the patterns above
def nps_pattern(pattern: str, group: int, dotall: bool=False):
    """
    This function extracts data from the email body using a pattern and a group number.
    :param pattern: A regex pattern to search for
    :param group: regex group number to extract
    :param dotall: regex flag to use dotall or not. Default is False. Dotall enables multiline search.
    :return:
    """

    # A dotall check is used because some of the patterns are multiline and some are not
    if dotall:
        try:
            match = re.search(pattern, input["body_html"], flags=re.DOTALL).group(group)
            match = re.sub("\\n","", match)
            match = re.sub("Ta gjerne kontakt med oss på Customer Success om du har spørsmål", "", match)
            return match
        except:
            return ""
    if not dotall:
        try:
            match = re.search(pattern, input["body_html"]).group(group)
            match = re.sub("\\n","", match)
            return match
        except:
            return ""

# Function to extract data from email subject using the patterns above
def nps_pattern_subject(pattern: str):
    try:
        match = re.search(pattern, input["subject"], flags=re.DOTALL).group(0)
        return match
    except:
        return ""

# Extract data from email body and put it in the output dictionary
output["Kundenavn_a"] = nps_pattern(PATTERN_KUNDENAVN,1)
output["Kundenavn_b"] = nps_pattern(PATTERN_KUNDENAVN,2)
output["Kundegruppe_a"] = nps_pattern(PATTERN_KUNDEGRUPPE,1)
output["Kundegruppe_b"] = nps_pattern(PATTERN_KUNDEGRUPPE,2)
output["Kjerneprodukt_a"] = nps_pattern(PATTERN_KJERNEPRODUKT,1)
output["Kjerneprodukt_b"] = nps_pattern(PATTERN_KJERNEPRODUKT,2)
output["Partner_a"] = nps_pattern(PATTERN_PARTNER,1)
output["Partner_b"] = nps_pattern(PATTERN_PARTNER,2)
output["NPS_Score_a"] = nps_pattern(PATTERN_NPS_SCORE,1)
output["NPS_Score_b"] = nps_pattern(PATTERN_NPS_SCORE,2)
output["Bra_a"] = nps_pattern(PATTERN_BRA,1)
output["Bra_b"] = nps_pattern(PATTERN_BRA,2)
output["Bedre_a"] = nps_pattern(PATTERN_BEDRE,1)
output["Bedre_b"] = nps_pattern(PATTERN_BEDRE,2)
output["Erdetnoen_a"] = nps_pattern(PATTERN_ERDETNOEN,1)
output["Erdetnoen_b"] = nps_pattern(PATTERN_ERDETNOEN,2)
output["Referat_a"] = nps_pattern(PATTERN_REFERAT,1, dotall=True)
output["Referat_b"] = nps_pattern(PATTERN_REFERAT,2, dotall=True)
output["Type"] = nps_pattern_subject(PATTERN_TYPE)
output["Produkt_a"] = nps_pattern(PATTERN_PRODUKT, 1)
output["Produkt_b"] = nps_pattern(PATTERN_PRODUKT, 2)
output["Bransjekode_a"] = nps_pattern(PATTERN_BRANSJEKODE, 1)
output["Bransjekode_b"] = nps_pattern(PATTERN_BRANSJEKODE, 2)