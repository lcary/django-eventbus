from django.conf import settings

SETTINGS_KEY = 'EVENTBUS'


class SettingConfigurationError(Exception):
    pass


class DefaultSettings(object):
    CONSUMER_TIMEOUT = 5.0
    PRODUCER_TIMEOUT = 1.0


class SettingsCache(object):

    def __getattr__(self, name):
        try:
            return self.__dict__[name]
        except KeyError:
            val = self.get_required(name)
            self.__dict__[name] = val
            return val

    @classmethod
    def get_or_default(cls, setting, default=None):
        if default is None:
            default = getattr(DefaultSettings, setting)
        return cls.settings.get(setting, default)

    @classmethod
    def get_required(cls, setting):
        try:
            return cls.settings[setting]
        except KeyError:
            raise SettingConfigurationError((
                'Unable to find required setting "{}" '
                'in the "{}" section of the Django settings file.'
            ).format(setting, SETTINGS_KEY))

    @property
    def settings(self):
        try:
            return settings.EVENTBUS
        except AttributeError:
            raise SettingConfigurationError((
                'Unable to find required setting dict "{}" '
                'in the Django settings file.').format(SETTINGS_KEY))


eventbus_settings = SettingsCache()
