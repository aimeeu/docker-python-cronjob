#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ===============LICENSE_START================================================
# Armory Apache-2.0
# ============================================================================
# Copyright (C) 2021 Armory. All rights reserved.
# ============================================================================
# This software file is distributed
# under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# This file is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============LICENSE_END==================================================

from datetime import datetime
import logging
from logging.handlers import RotatingFileHandler
from pprint import pprint

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
fh = RotatingFileHandler('cron-test.log', maxBytes=102400, backupCount=10)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

pprint ("hello world!" + str(datetime.now()))
logger.info("hello world" + str(datetime.now()))
pprint ("Welcome to python cron job" + str(datetime.now()))
logger.info("Welcome to python cron job" + str(datetime.now()))

logger.info("creating/opening cron-test.txt file" + str(datetime.now()))
pprint("creating/opening cron-test.txt file" + str(datetime.now()))
myFile = open('cron-test.txt', 'a')
logger.info("writing to cron-test.txt file" + str(datetime.now()))
pprint("writing to cron-test.txt file" + str(datetime.now()))
myFile.write('\nAccessed on ' + str(datetime.now()))
logger.info("closing cron-test.txt file" + str(datetime.now()))
pprint("closing cron-test.txt file" + str(datetime.now()))
myFile.close()
