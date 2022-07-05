#!/bin/bash

pip3 install -r requirements.txt
python3 project/init/init_db.py
python3 runserver.py