import argparse

def get_arg():
    parse = argparse.ArgumentParser()
    parse.add_argument('--c')
    parse.add_argument('--v')

    args = parse.parse_args()
    
    return args.c.capitalize(), args.v