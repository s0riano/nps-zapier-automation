_...The Archive folder is the folder i received when the project was handed down to me_
# oNPS in Zapier

## About this repo
This repository documents the Zapier integration for oNPS in the Payroll project.
It consists of documentation on how to set up the zap and code contained in the zap.

## About the process
The general process looks like this:
1. A new customer starts using Payroll (or any other product that uses oNPS)
2. The customer is added to the oNPS database
3. The customer is interviewed by the oNPS team(?)
4. The response is recorded in the external system for customer feedback (confirmit)
5. An email is sent to the zapier email address
6. The zap is triggered and spits out two messages in slack:
   - Always: A message in the #vsi-swno-onboarding-nps-referat-all channel
   - If the response is about Payroll: A message in the #vsi-vnet-payroll-onps channel
7. Anyone can read and discuss the oNPS response in the slack channels

## Contact persons
Customer success: Tone Kristiansen

## How to set up the zap
Precondition: You have to have a zapier.com account. To be able to send the amount of messages this zap takes (up to a few hundred per month), you need to have a subscription too.

1. Trigger: New inbound email in email by Zapier
   - App & event:
     - App: Email by Zapier
     - Event: New Inbound Email
   - Step details:
     - Email address: Whatever the email adress it gives you is.
2. Action: Run python in Code by Zapier
   - App & Event:
     - App: Code by Zapier
     - Event: Run Python
   - Input data:
     - body_html: 1.Body HTML (from step 1)
     - subject: 1. Subject (from step 1)
   - Code:
     - See code in this repo (script.py)
3. Action: Send channel message in Slack
   - App & Event:
     - App: Slack
     - Event: Send Channel Message
     - User: Choose the user you want to log into slack with
   - Step details:
     - Channel: C03F52CTV6J (find this by right clicking a channel, clicking "channel details" and scrolling to the bottom)
     - Message Text: see slack_messages.py
     - Send as bot?: true
     - Bot name: Visma oNPS
     - Bot icon: :vismalogo:
     - Include a link to this zap?: false
     - Auto-Expan links?: false
     - Link usernames and Channel names?: false
     - File: [no file]
     - Broadcast to channel: false
4. Action: Only continue if...
    - Continue if...: 2. Body plain (from step 2) contains "Visma.net Payroll"
5. Action: Send channel message in Slack
   - App & Event:
     - App: Slack
     - Event: Send Channel Message
     - User: Choose the user you want to log into slack with
   - Step details:
     - Channel: C02MUEBP9DG
     - Message Text: see slack_messages.py
     - Send as bot?: true
     - Bot name: Visma oNPS
     - Bot icon: :vismalogo:
     - Include a link to this zap?: false
     - Auto-Expan links?: false
     - Link usernames and Channel names?: false
     - File: [no file]
     - Broadcast to channel: false