from slacker_log_handler import SlackerLogHandler
import logging
import sys
import yaml

def change_slack_settings(slack_handler, option, settings):
    #option true means that it is a info message, false means that it is an error message
    if option:
        slack_handler.icon_emoji = ":white_check_mark:"
        slack_handler.channel = settings["slack_channel_info"]
    else:
        slack_handler.icon_emoji = ":bangbang:"
        slack_handler.channel = settings["slack_channel_error"]

yaml_file = open("settings.yaml", 'r')
settings = yaml.load(yaml_file)

slack_handler = SlackerLogHandler(str(settings["web_hook_url"]), channel=str(settings["slack_channel"]),
                                      username=str(settings["slack_username"]))

logger = logging.getLogger('debug_application')
logger.addHandler(slack_handler)

formatter = logging.Formatter('%(asctime)s|%(levelname)s|%(filename)s:%(lineno)s|%(funcName)20s()|%(message)s')

slack_handler.setFormatter(formatter)
slack_handler.setLevel(logging.DEBUG)

logging.basicConfig(stream=sys.stdout,
format='%(asctime)s|%(levelname)s|%(filename)s:%(lineno)s|%(funcName)20s()|%(message)s',
level=logging.DEBUG)

logger.error("this is an erorr message")
logger.info("this is an info message")
