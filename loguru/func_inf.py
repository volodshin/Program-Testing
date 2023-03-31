from loguru import logger
import time


def suma():
    a = 1
    b = 5

    start_time = time.time()

    func_time = time.time() - start_time

    suma = a + b
    logger.info(f'\na = {a} and b = {b}.\nResult: {suma}. \nExecution time:{func_time} seconds')

    return suma

suma()