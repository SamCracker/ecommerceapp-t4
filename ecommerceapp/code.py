import logging

class WriteLog:
    def __init__(self, log_message):
        self.write_log(log_message)

    def write_log(self, log_message):
        logging.basicConfig(level=logging.DEBUG, 
            format='%(asctime)s.%(msecs)03d %(levelname)s:\t%(message)s',
            datefmt='%Y-%m-%d %H:%M:%S')
        logging.debug(log_message)

val = "my messages"
WriteLog = WriteLog()
WriteLog.write_log(val)
