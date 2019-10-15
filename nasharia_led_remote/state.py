"""LICENSE
Copyright 2019 Hermann Krumrey <hermann@krumreyh.com>

This file is part of nasharia-led-remote.

nasharia-led-remote is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

nasharia-led-remote is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with nasharia-led-remote.  If not, see <http://www.gnu.org/licenses/>.
LICENSE"""

import os
import json
from typing import Dict, Any

config_dir = os.path.join(os.path.expanduser("~"), ".config/led-remote")
"""
The directory containing configuration data for this application
"""

state_file = os.path.join(config_dir, "state.json")
"""
The file in which state variables are stored
"""


def get_state() -> Dict[str, Any]:
    """
    Retrieves the current state variables from the state file
    :return: A dictionary containing the current state
    """
    with open(state_file, "r") as f:
        return json.load(f)


def set_state(state: Dict[str, Any]):
    """
    Sets the state file tot the values of a dictionary
    :param state: The new state data
    :return: None
    """
    with open(state_file, "w") as f:
        json.dump(state, f)


def is_on() -> bool:
    """
    Checks whether or not the LEDs are currently on
    :return: True if on, False if off
    """
    return bool(get_state()["power"])


def set_power_state(state: bool):
    """
    Sets the power state
    :param state: The power state
    :return: None
    """
    old = get_state()
    old["power"] = state
    set_state(old)
