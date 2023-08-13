import configparser


class LocalConfig:
    def __init__(self):
        self.path = '/home/pi/Terraria/conf.ini'
        self.config = configparser.ConfigParser()
        self.config.read(self.path)
        self.settings = dict()
        self.get_config_data()

    def get_config_data(self):
        try:
            self.config.read(self.path)
            for key, value in self.config.items("SETTINGS"):
                value = self.is_bool(value)
                self.settings[key] = value
        except IOError:
            return False

    @staticmethod
    def is_bool(value):
        if value == "1":
            return True
        elif value == "0":
            return False
        else:
            return value

    def set_error(self, sensor, value):
        self.set_config_data("ERROR", sensor, value)

    def set_config_data(self, section, key, value):
        self.config.set(section, key, str(value))
        self.write_config()

    def write_config(self):
        try:
            with open(self.path, 'w') as configfile:
                self.config.write(configfile)
            configfile.close()
        except Exception as e:
            print(e)
