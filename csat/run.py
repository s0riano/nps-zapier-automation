import re

PATTERN_KUNDENAVN = "(Kundenavn: )(.+)"
PATTERN_ORGNUMMER = "(Org\.nummer: )(\d+)"
PATTERN_TICKET = "(Ticket: )(\d+)"
PATTERN_KONSULENT = "(Konsulent: )(.+)"
PATTERN_PRODUKTTEAM = "(Produktteam: )(.+)"
PATTERN_SCORE = "(Score: )(\d+)"
PATTERN_HOVEDARSAK = "(Hovedårsak til score: )(.+)"
PATTERN_ANDRE_TILBAKEMELDINGER = "(Andre tilbakemeldinger: )(.+)"
PATTERN_OTHER = "(Other: )(.+)"

output = {}

def csat_pattern(pattern: str, group: int):
    try:
        match = re.search(pattern, input["body_html"]).group(group)
        match = re.sub("\\n", "", match)
        return match.strip()
    except:
        return ""

input["body_html"] = re.sub("<[^<]+?>", "", input["body_html"])

output["Kundenavn"] = csat_pattern(PATTERN_KUNDENAVN, 2)
output["Org.nummer"] = csat_pattern(PATTERN_ORGNUMMER, 2)
output["Ticket"] = csat_pattern(PATTERN_TICKET, 2)
output["Konsulent"] = csat_pattern(PATTERN_KONSULENT, 2)
output["Produktteam"] = csat_pattern(PATTERN_PRODUKTTEAM, 2)
output["Score"] = csat_pattern(PATTERN_SCORE, 2)
output["Hovedårsak til score"] = csat_pattern(PATTERN_HOVEDARSAK, 2)
output["Andre tilbakemeldinger"] = csat_pattern(PATTERN_ANDRE_TILBAKEMELDINGER, 2)
output["Other"] = csat_pattern(PATTERN_OTHER, 2)