import speech_recognition as sr
from google.cloud import dialogflow

# Dialogflow API settings
PROJECT_ID = 'YOUR_PROJECT_ID'
LANGUAGE_CODE = 'en-IN'

# Create a Dialogflow agent client
dialogflow_client = dialogflow.AgentsClient()

# Create a speech recognition object
r = sr.Recognizer()

# Define a function to detect intent using Dialogflow
def detect_intent(text):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(PROJECT_ID, '123456789')  # Replace with a unique session ID
    text_input = dialogflow.TextInput(text=text, language_code=LANGUAGE_CODE)
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result.intent.display_name, response.query_result.fulfillment_text

# Define a function to handle voice commands
def handle_voice_command():
    with sr.Microphone() as source:
        print('Say something:')
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language=LANGUAGE_CODE)
            print(f'You said: {text}')
            intent, response = detect_intent(text)
            print(f'Intent: {intent}')
            print(f'Response: {response}')
        except sr.UnknownValueError:
            print('Sorry, I did not understand what you said')
        except sr.RequestError as e:
            print(f'Error: {e}')

# Main loop
while True:
    handle_voice_command()