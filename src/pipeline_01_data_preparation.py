import os
import argparse
import yaml # here we define our configurations
import logging # to log all the info

def parse_args():
    parser = argparse.ArgumentParser()
    default_config_path = os.path.join('config','params.yaml')
    parser.add_argument('--config', default=default_config_path, help='configuration file with all the default paths and parameters')
    parser.add_argument('--datasource', default=None, help='path to source training data, if default None, it chooses the datasouce from config file')
    parsed_args =  parser.parse_args()
    return parsed_args

def read_config(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def main():
    opts = parse_args()
    print(opts.config)
    print(opts.datasource)
    config = read_config(opts.config)
    print(config)



if __name__ == "__main__":
    main()