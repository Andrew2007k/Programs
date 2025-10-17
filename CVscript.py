import pandas as panda
import numpy as np

def CVAnalyze(filepath):
    with open(filepath, 'r') as DTA1:
        Datalines = DTA1.readlines()
    start = next(i for i, line in enumerate(Datalines) if line.strip().startswith("CURVE1"))
    df = panda.read_csv(filepath, sep=r'\s+', skiprows=start + 3, comment='#', header=None)
    df.columns = ['A', 'Sec', 'Vf', 'Im', 'Col5', 'Col6', 'Col7', 'Col8', 'col9']
    df = df[['Sec', 'Vf', 'Im']].dropna()

    df['Vf'] = panda.to_numeric(df['Vf'], errors='coerce')
    df['Im'] = panda.to_numeric(df['Im'], errors='coerce')

    threshhold1 = 0
    dIdV = np.gradient(df['Im'], df['Vf'])
    rside = np.argmax(dIdV < threshhold1) * 0.2  #Fix this value to match scans
    rside = round(rside)

    
