import numpy as np
import pickle
from scipy.stats import mode
from .forms import symptoms as original_symptoms

symptoms = [x for x,_ in original_symptoms]
pickled_encoder = pickle.load(open("symptom_checker/models_saved/encoder.pkl", "rb")) 
final_rf_model = pickle.load(open("symptom_checker/models_saved/rf_model.pkl", "rb")) 
final_nb_model = pickle.load(open("symptom_checker/models_saved/nb_model.pkl", "rb")) 
final_svm_model = pickle.load(open("symptom_checker/models_saved/svm_model.pkl", "rb")) 

symptom_index = {}
for index, value in enumerate(symptoms):
    symptom = value
    symptom_index[symptom] = index
 
data_dict = {
    "symptom_index":symptom_index,
    "predictions_classes":pickled_encoder
}

def predictDisease(symptoms):
    symptoms = [x for x in symptoms.split(", ") if x]
     
    data_input = [0] * len(data_dict["symptom_index"])
    for symptom in symptoms:
        index = data_dict["symptom_index"][symptom]
        data_input[index] = 1
         
    data_input = np.array(data_input).reshape(1,-1)

    rf_conf = final_rf_model.predict_proba(data_input)
    max_rf_confidence = max(rf_conf[0])

    nb_conf = final_nb_model.predict_proba(data_input)
    max_nb_confidence = max(nb_conf[0])
    
    rf_prediction = data_dict["predictions_classes"][final_rf_model.predict(data_input)[0]]
    nb_prediction = data_dict["predictions_classes"][final_nb_model.predict(data_input)[0]]
    svm_prediction = data_dict["predictions_classes"][final_svm_model.predict(data_input)[0]]
    
    final_prediction = mode([rf_prediction, nb_prediction, svm_prediction])[0][0]
    predictions = {
        "final_prediction":final_prediction,
        "final_score": (max_rf_confidence + max_nb_confidence)/2 * 100
    }
    return predictions