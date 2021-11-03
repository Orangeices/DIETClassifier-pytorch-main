from os import path, listdir
from typing import Union, List, Dict, Any, Tuple

import torch
import yaml
from transformers import BertTokenizer

import os
import sys

sys.path.append(os.getcwd())

from src.models.classifier import DIETClassifier, DIETClassifierConfig
from src.models.trainer import DIETTrainer
from src.data_reader.dataset import DIETClassifierDataset
from src.data_reader.data_reader import make_dataframe


class DIETCkassifierWrapper(object):
    def __init__(self, config: Union[Dict[str, Dict[str, Any]], str]):
        if isinstance(config, str):
            try:
                f = open(config, 'r')
            except Exception as ex:
                raise RuntimeError(f'Cannont read config file from {config} : {ex}')
            self.config_file_path = config
            config = yaml.load(f)
        self.config = config
        self.util_config = config.get("util", None)

        model_config_dict = config.get("model", None)
        if not model_config_dict:
            raise ValueError(f"config file should have 'model' attribute")

        self.dataset_config = model_config_dict

        if model_config_dict["device"] is not None:
            self.device = torch.device(model_config_dict["device"]) \
                if torch.cuda.is_available() else torch.device("cpu")
            model_config_attributes = ["model", "intents", "entities"]
            self.intents = model_config_dict["intents"]
            self.entities = model_config_dict["entities"]
