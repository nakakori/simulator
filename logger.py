import yaml
import logging
import logging.config

def main():
    filepath = "config/logger.conf"
    with open(filepath, encoding='UTF-8') as f:
        confdata = yaml.load(f.read())
    
    logging.config.dictConfig(confdata)
    
    logger = logging.getLogger("loggers").getChild("console")

    logger.info('test')

if __name__ == '__main__':
    main()