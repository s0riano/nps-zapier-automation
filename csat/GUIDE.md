Hvordan sette opp zap-Automasjon for CSAT til Slack


1 - Lag en ny Zap

2 - Klikk på "Trigger" i Zap-en som ble laget og velg "Email By Zappier"

3 - Velg "Inbound Mail" som event 

4 - På feltet som heter "Trigger" må det tildeles et navn til email adressen

5 - Klikk på plusstegnet og velg Code By Zappier og velg "Run Python" som event

6 - Lim inn koden fra filen run.py. Det limes inn i feltet "code" som ligger under "Action"

7 - Legg deretter til et nytt step, det skal være "filter". 
        Lag en continue if på hver av konsulentene mot konsulent variablenen som er deklarert i Python

8 - Legg deretter til steppet å sende melding til Slack.
    Legg inn dette under i *Message Text. 
    Krøllparantesene må byttes ut med de faktiske variablene. De henter du ved å klikke på Run code under Insert Data...

    *Kundenavn: * {{236340754__Kundenavn}}
    *Score: * {{236340754__Score}}
    *Konsulent: * {{236340754__Konsulent}}
    *Hovedårsak til score: * {{236340754__Hovedårsak til score}}
    *Andre tilbakemeldinger: * {{236340754__Andre tilbakemeldinger}}
    *Annet: * {{236340754__Andre tilbakemeldinger}}


Lag gjerne en test-kanal for å skrive ut resultatene gjennom prossessen. 
Et tips er å justere hvor slack sender meldinger og så sende mails til adressen for å teste.