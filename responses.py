def handle_response(message) -> str:
    #so message here is what is SENT by the person,
    #can preprocess the message and then maybe run the model on it
    p_message = message.lower()

    #based on what the model returns,
    #we prefix the message with 0 (no problem), 1 (hate), or 2 (depressive)
    p_message = '0' + p_message
    return p_message