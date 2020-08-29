import json
from datetime import datetime

from dizqueTV.exceptions import MissingSettingsError


def combine_settings(new_settings_dict: json, old_settings_dict: json) -> json:
    """
    Build a complete dictionary for new settings, using old settings as a base
    :param new_settings_dict: Dictionary of new settings kwargs
    :param old_settings_dict: Current settings
    :return: Dictionary of new settings
    """
    for k, v in new_settings_dict.items():
        if k in old_settings_dict.keys():
            old_settings_dict[k] = v
    return old_settings_dict


def settings_are_complete(new_settings_dict: json, template_settings_dict: json, ignore_id: bool = False) -> bool:
    """
    Check that all elements from the settings template are present in the new settings
    :param new_settings_dict: Dictionary of new settings kwargs
    :param template_settings_dict: Template of settings
    :param ignore_id: Ignore if "_id" is not included in new_settings_dict
    :return: True if valid, raise dizqueTV.exceptions.IncompleteSettingsError if not valid
    """
    for k in template_settings_dict.keys():
        if k not in new_settings_dict.keys():
            # or not isinstance(new_settings_dict[k], type(template_settings_dict[k]))
            if k == '_id' and ignore_id:
                pass
            else:
                print(k)
                raise MissingSettingsError
    return True


def remove_time_from_date(date_string: datetime) -> str:
    return date_string.strftime("%Y-%m-%d")


def get_year_from_date(date_string: datetime) -> int:
    return int(date_string.strftime("%Y"))
