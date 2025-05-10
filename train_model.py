from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from sklearn import datasets
import joblib
import pandas as pd
import numpy as np
# Note: Jupyter is not typically imported in scripts