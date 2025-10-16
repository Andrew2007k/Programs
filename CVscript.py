import pandas as panda
import numpy as np

def CVAnalyze(filepath):
    with open(filepath, 'r') as DTA1:
        Datalines = DTA1.readlines()
    start = next(i for i, line in enumerate(Datalines) if line.strip().startswith("CURVE1"))
    df = panda.read_csv(filepath, sep='\t', skiprows=start + 2, comment='#')
    df.columns = ['Vf', 'Im']
    df = df[['Vf', 'Im']].dropna()


