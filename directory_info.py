# coding=utf-8
import os

# Project Root Directory
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# Project Name
PROJECT_DIR_NAME = "VideoDecoder"


def get_project_dir():
    """
    Returns the project root directory
    :return:
        Project path
    """
    global ROOT_DIR

    paths = ROOT_DIR.split("/")
    paths = list(filter(lambda a: a != '', paths))

    if PROJECT_DIR_NAME not in paths[-1]:
        ROOT_DIR = ROOT_DIR + PROJECT_DIR_NAME

    if ROOT_DIR[-1] != "/":
        ROOT_DIR = ROOT_DIR + "/"

return ROOT_DIR
