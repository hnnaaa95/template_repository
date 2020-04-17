#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import os
import json

EXE_PATH = os.getcwd() # 실행 경로
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__)) # 스크립트 경로
CONFIG_PATH = EXE_PATH + "/config.json"


def main():
    print("Execution Path : {}".format(EXE_PATH))
    print("Script Path : {}".format(SCRIPT_PATH))
    print("Config Path : {}".format(CONFIG_PATH))

    with open(CONFIG_PATH) as json_file:
        json_data = json.load(json_file)

    print("Config Data : {}".format(json_data))

	
    print("Hello Worlds!")

if __name__ == "__main__":
	main()
