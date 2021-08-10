#!/bin/env python3

# Copyright (c) 2021 Seagate Technology LLC and/or its Affiliates
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
# For any questions about this software or licensing,
# please email opensource@seagate.com or cortx-questions@seagate.com.

import traceback
from cortx.utils.log import Log
from cortx.utils.conf_store import Conf


class CSMWebSetupError(Exception):
    """
    Generic Exception with error code and output
    """
    def __init__(self, rc, message, *args):
        """
        Initializing CSMWebSetupError
        """
        self._rc = rc
        self._desc = message

    def __str__(self):
        """
        Return error in String
        """
        if self._rc == 0: return self._desc
        return f"error({self._rc}): {self._desc}\n\n {traceback.format_exc()}"

    @property
    def rc(self):
        return self._rc


class CSMWeb:
    """
    Represents CSMWeb and Performs setup related actions
    """
    CONSUMER_INDEX = "consumer"
    ENV_INDEX = "env_index"
    CSM_WEB_DIST_ENV_FILE_PATH  = "/opt/seagate/cortx/csm/web/web-dist/.env"

    def __init__(self, conf_url, **kwargs):
        """
        Initializing CSMWeb
        """
        Conf.init()
        Conf.load(CSMWeb.CONSUMER_INDEX, conf_url)
        Conf.load(self.ENV_INDEX, f"properties://{self.CSM_WEB_DIST_ENV_FILE_PATH }")
        Log.init(service_name = "csm_web_setup", log_path = "/tmp/csm/setup_logs",
                level="INFO")
        self.conf_url = conf_url
        self.pre_factory = kwargs.get("pre_factory")

    def post_install(self):
        """
        Performs post install operations for CSM Web as well as cortxcli.
        Raises exception on error.
        """
        Log.info("Executing post install")
        return 0

    def prepare(self):
        """
        Performs post install operations.
        Raises exception on error
        """
        Log.info("Executing prepare")
        return 0

    def config(self):
        """
        Performs configurations.
        Raises exception on error
        """
        Log.info("Executing config")
        return 0

    def init(self):
        """
        Perform initialization.
        Raises exception on error
        """
        Log.info("Executing init")
        return 0

    def reset(self):
        """
        Performs Configuraiton reset.
        Raises exception on error
        """
        Log.info("Executing reset")
        return 0

    def pre_upgrade(self):
        """
        Performs Pre upgrade functionalitied.
        Raises exception on error
        """
        Log.info("Executing pre upgrade")
        return 0

    def post_upgrade(self):
        """
        Performs Post upgrade functionalitied.
        Raises exception on error
        """
        Log.info("Executing post upgrade")
        return 0

    def test(self, plan):
        """
        Perform configuration testing.
        Raises exception on error
        """
        Log.info("Executing test")
        return 0

    def cleanup(self):
        """
        Performs Configuraiton cleanup.
        Raises exception on error
        """
        Log.info("Executing cleanup")
        return 0