#coding:utf-8
import configparser
config = configparser.ConfigParser()
config.read('code.ini')
config.sections()
error_code = config['ERROR_CODE']