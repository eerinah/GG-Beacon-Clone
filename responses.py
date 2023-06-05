def handle_response(message) -> str:
    #so message here is what is SENT by the person,
    #can preprocess the message and then maybe run the model on it
    p_message = message.lower()

    #return this
    return p_message