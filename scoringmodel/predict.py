
from typing import Union
import pandas as pd

from scoringmodel.processing.data_manager import load_model, _version
from scoringmodel.pipeline import feature_pipeline
from scoringmodel.config.core import config


model_file_name = f"{config.app_config.model_save_file}{_version}.pkl"
_model = load_model(file_name=model_file_name)

def make_prediction(*, input_data: Union[pd.DataFrame, dict]) -> dict:
    """Make a prediction using a saved model pipeline."""

    data = pd.DataFrame(input_data)

    errors = None #    validated_data, errors = validate_inputs(input_data=data)
    
    results = {"predictions": None, "version": _version, "errors": errors}

    if not errors:
        data = feature_pipeline(data)

        predictions = _model.predict(data[config.model_config.features])

        results = {"predictions": [pred for pred in predictions],
                   "version": _version,
                   "errors": errors,
                   }

    return results