
from pathlib import Path
import pandas as pd

from scoringmodel.config.core import DATASET_DIR, config


def load_dataset(file_name: str) -> pd.DataFrame:
    rawdata = pd.read_excel(Path(f"{DATASET_DIR}/{file_name}"), 
    	                    index_col=0, header=1)

    # rename variables with spaces, pay_0 to pay_1, and to lowercases
    transformed = rawdata.rename(columns=config.model_config.variables_to_rename)
    transformed.columns = [col.lower() for col in transformed.columns] 

    return transformed