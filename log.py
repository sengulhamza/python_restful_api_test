from datetime import datetime

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def log_to_term(log_type,type_tag, tag, log):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S.%f")[:-3]
    print(log_type + type_tag + " " + current_time + " " + tag + ": "+ log + bcolors.ENDC)

def LOG_I(tag, log):
    log_to_term(bcolors.OKGREEN, "I", tag, log)

def LOG_W(tag, log):
    log_to_term(bcolors.WARNING, "W", tag, log)

def LOG_E(tag, log):
    log_to_term(bcolors.FAIL, "E", tag, log)

def LOG_H(tag, log):
    log_to_term(bcolors.HEADER, "H", tag, log)

def LOG_B(tag, log):
    log_to_term(bcolors.BOLD, "B", tag, log)

def LOG_U(tag, log):
    log_to_term(bcolors.UNDERLINE, "U", tag, log)

def LOG_T(tag, log):
    log_to_term(bcolors.OKBLUE, "T", tag, log)
