from urls import *
import logging

logging.basicConfig(filename="log", filemode="w", level=logging.INFO, format="%(levelname)s:%(message)s")


for i in range(100):
    try:
        x = 1  # code
    except Exception as e:
        logging.exception(e)
