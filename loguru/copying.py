from loguru import logger
import time

def copy_txt():
    file_1 = 'firstfile.txt'
    file_2 = 'secondfile.txt'

    with open(f'{file_1}', 'r') as f1, open(f'{file_2}', 'w') as f2:
        for line in f1:
            f2.write(line)

    start_time = time.time()
    func_time = time.time() - start_time

    logger.info(f'From {file_1} copied text and written to {file_2}\nExecution time:{func_time} seconds')

copy_txt()