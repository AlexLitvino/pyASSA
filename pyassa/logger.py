# -----------------------------------------------------------------------------
# Copyright 2017 Aleksey Litvinov litvinov.aleks@gmail.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Result logger and error logger defined in this file
# -----------------------------------------------------------------------------

import logging
import datetime
import os

logging.basicConfig(
    level=logging.DEBUG,
    format='%(message)s'
)


class DirMakeFileHandler(logging.FileHandler):
    """
    Custom file handler class to create required directory before start logging.
    """
    def __init__(self, filename, mode='a', encoding=None, delay=0):
        if not os.path.exists(os.path.dirname(filename)):
            os.mkdir(os.path.dirname(filename))
        logging.FileHandler.__init__(self, filename, mode, encoding, delay)

RESULT_LOGGER_NAME = "result_logger"
ERROR_LOGGER_NAME = "error_logger"
timestamp = datetime.datetime.now().strftime("%m%d%Y_%H%M%S")
RESULT_LOGGER_FILE = '..\\reports\\assa_' + timestamp + '.log'  # TODO: take from config
ERROR_LOGGER_FILE = '..\\reports\\error_' + timestamp + '.log'  # TODO: take from config

result_handler = DirMakeFileHandler(RESULT_LOGGER_FILE)
error_handler = DirMakeFileHandler(ERROR_LOGGER_FILE)

result_logger = logging.getLogger(RESULT_LOGGER_NAME)
result_logger.addHandler(result_handler)
result_logger.setLevel(logging.INFO)

error_logger = logging.getLogger(ERROR_LOGGER_NAME)
error_logger.addHandler(error_handler)
error_logger.setLevel(logging.INFO)
