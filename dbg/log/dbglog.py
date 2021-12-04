import logging, sys, os

def _get_logger(name, truncated=True):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s %(pathname)s[%(lineno)d] %(levelname)s pid=%(process)d(" + sys.argv[0] + "): %(message)s")
    
    h_stdout = logging.StreamHandler(stream=sys.stdout)
    h_stdout.setFormatter(formatter)
    logger.addHandler(h_stdout)
    
    if not os.path.exists("_log_"):
        os.mkdir("_log_")
 
    mode = "w" if truncated else "a"
    h_file = logging.FileHandler(os.path.join("_log_", "ovd.log"), mode=mode)
    h_file.setFormatter(formatter)
    logger.addHandler(h_file)
    
    logger.info("-----------------------Logger initialized.-----------------------")
    return logger

LOG = _get_logger("OVD", truncated=False)

if __name__ == "__main__":
    LOG.debug("debug")
    LOG.info("info")
    LOG.warning("warning")
    LOG.error("error")
    LOG.critical("critical")
