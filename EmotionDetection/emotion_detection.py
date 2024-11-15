import requests  # Import the requests library to handle HTTP requests
import json
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }  
    response = requests.post(url, json = input_json, headers=header) 
    
    if response.status_code == 200:
        # Parsing the JSON response from the API
        formatted_response = json.loads(response.text)
        
        # Extracting sentiment label and score from the response
        emotions = formatted_response['emotionPredictions'][0]['emotion']

        # Find dominant emotion by sorting emotions dictionary in descending order and get key of first pair
        dominant_emotion = sorted(emotions.items(), key=lambda item: item[1], reverse=True)[0][0]

        # Add dominant emotion to output
        emotions['dominant_emotion'] = dominant_emotion
    elif response.status_code == 400:
        emotions = {
            "anger": None, 
            "disgust": None, 
            "fear": None, 
            "joy": None, 
            "sadness": None, 
            "dominant_emotion": None
        }

    # Returning a dictionary containing sentiment analysis results
    return emotions