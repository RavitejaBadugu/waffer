import os
import yaml
import pandas as pd
import argparse

def get_params(config_path):
    with open(config_path) as f:
        file=yaml.safe_load(f)
    return file
def get_data(config_path):
    config=get_params(config_path)
    data=config['projectDetails']['data_store']['final_data']
    df=pd.read_csv(data)
    return df




if __name__=='__main__':
    args=argparse.ArgumentParser()
    args.add_argument('--config_file',default='config.yaml')
    parsed_args=args.parse_args()
    get_data(parsed_args.config_file)
