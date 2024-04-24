import re

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

output = {
    }

input["body_html"] = re.sub("<[^<]+?>", "", input["body_html"])

def nps_pattern(pattern: str, group: int, dotall: bool=False):

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

def nps_pattern_subject(pattern: str):
    try:
        match = re.search(pattern, input["subject"], flags=re.DOTALL).group(0)
        return match
    except:
        return ""

def extract_onboarding_status(email_content):
    if 'onboarding completed' in email_content.lower():
        return 'completed'
    elif 'onboarding' in email_content.lower():
        return 'onboarding'
    else:
        return 'Unknown'

onboarding_status = extract_onboarding_status(input["body_html"])

output["Onboarding_Status"] = onboarding_status

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