import requests
import os
from dotenv import load_dotenv

load_dotenv()

#Here are all the constants we use in the program. They are loaded from a .env file.

APP_ID = os.getenv('APP_ID')
PREDICTION_KEY = os.getenv("PREDICTION_KEY")
PREDICTION_ENDPOINT = os.getenv("PREDICTION_ENDPOINT")

class LUISRetriever():
    """
    A class used to communicate with LUIS

    ...

    Attributes
    ----------
    sentence : str
        the sentence which we need to analyze through LUIS

    Methods
    -------
    call()
        Call LUIS with the stored sentence
    """

    def __init__(self, sentence):
        self.sentence = sentence

    
    def call(self):
        """
        Used to call LUIS with the stored sentence.

        Returns:
            data: the json response of the LUIS API (returns None if an error occured)
        """

        data = None

        try:
            params = {
                'query': self.sentence,
                'timezoneOffset': '0',
                'verbose': 'true',
                'show-all-intents': 'true',
                'spellCheck': 'false',
                'staging': 'false',
                'subscription-key': PREDICTION_KEY
            }

            response = requests.get(f'{PREDICTION_ENDPOINT}luis/prediction/v3.0/apps/{APP_ID}/slots/production/predict', headers={}, params=params)

            if response.status_code != 200:
                raise Exception('Bad status code received: {}'.format(response.status_code))

            data = response.json()
        except Exception as e:
            print("Something gone wrong while calling LUISRetriever#call():")
            print(e)
        
        return data

