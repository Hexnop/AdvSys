import argparse
import os


def check_super_user():
    if os.getuid() != 0:
        return False
    return True


def build_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", help="checking all system", action="store_true")
    parser.add_argument("--autofrw", help="setting auto ban connection", action="store_true")
    parser.add_argument("-guardian", help="Guard to system event folder, temp, cache, net", action="store_true")
    parser.add_argument("-only", help="Set you wanna be controlled")
    parser.add_argument("-p", help="checking package", action="store_true")
    parser.add_argument("-sub", help="check update system and auto upgrade", action="store_true")
    return parser
