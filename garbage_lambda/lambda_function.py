# Main function

import text_builders
import dates_parser

def lambda_handler(event, context):
    if event['session']['new']:
        on_start()
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event)
    elif event['request']['type'] == "IntentRequest":
        return intent_scheme(event)
    elif event['request']['type'] == "SessionEndedRequest":
        return on_end()

def on_start():
    print("Session Started.")

def on_launch(event):
    onlunch_MSG = "Inizializzazione spazzatura!"
    reprompt_MSG = "Dimmi cosa vuoi sapere sulla spazzatura"
    card_TEXT = ""
    card_TITLE = ""
    return text_builders.output_json_builder_with_reprompt_and_card(onlunch_MSG, card_TEXT, card_TITLE, reprompt_MSG, False)

def on_end():
    print("Session Ended.")

def intent_scheme(event):
    intent_name = event['request']['intent']['name']
    if intent_name == "CheckNextDayIntent":
        date = event['request']['intent']['slots']['date']['value']
        return check_day(date)        
    elif intent_name in ["AMAZON.NoIntent", "AMAZON.StopIntent", "AMAZON.CancelIntent"]:
        return stop_the_skill(event)
    elif intent_name == "AMAZON.HelpIntent":
        return assistance(event)
    elif intent_name == "AMAZON.FallbackIntent":
        return fallback_call(event)

def check_day(date):
    # in format of '2015-11-24'
    garbage = dates_parser.get_garbage_at_date(date)
    card_TEXT = ""
    card_TITLE = ""
    reprompt_MSG = ""
    return text_builders.output_json_builder_with_reprompt_and_card(garbage, card_TEXT, card_TITLE, reprompt_MSG, False)
    
def stop_the_skill(event):
    stop_MSG = "Grazie, ciao!"
    reprompt_MSG = ""
    card_TEXT = ""
    card_TITLE = ""
    return text_builders.output_json_builder_with_reprompt_and_card(stop_MSG, card_TEXT, card_TITLE, reprompt_MSG, True)
    
def assistance(event):
    assistance_MSG = "Puoi dirmi: che spazzatura c'é domani? O qualsiasi altra data"
    reprompt_MSG = "Vuoi sapere che spazzatura viene ritirata in un dato giorno?"
    card_TEXT = ""
    card_TITLE = ""
    return text_builders.output_json_builder_with_reprompt_and_card(assistance_MSG, card_TEXT, card_TITLE, reprompt_MSG, False)

def fallback_call(event):
    fallback_MSG = "Mi spiace ma non posso aiutarti."
    reprompt_MSG = "Vuoi sapere che spazzatura viene ritirata in un dato giorno?"
    card_TEXT = ""
    card_TITLE = ""
    return text_builders.output_json_builder_with_reprompt_and_card(fallback_MSG, card_TEXT, card_TITLE, reprompt_MSG, False)