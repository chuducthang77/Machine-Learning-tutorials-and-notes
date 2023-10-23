from deepface import DeepFace
import pandas as pd
df = DeepFace.find(img_path = "Đức1.jpg", db_path = ".\data")
