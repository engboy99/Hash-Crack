import tensorflow as tf
import numpy as np

def load_model(model_path: str):
    """Load a pre-trained AI model for hash prediction."""
    return tf.keras.models.load_model(model_path)

def predict_hash(model, hash_value: str):
    """Predict original text from hash using AI model."""
    input_data = np.array([list(hash_value.encode())])
    prediction = model.predict(input_data)
    return prediction
