class Settings:
    def __init__(self):
        self.settings_map = {'alpha': 1.0, 'beta': 0.75, 'gamma': 0.15}

    def get_settings_value(self, key):
        if key in self.settings_map:
            return self.settings_map[key]
        else:
            raise Exception("Wrong settings key")

    def set_settings_value(self, key, value):
        if key in self.settings_map:
            self.settings_map[key] = value
        else:
            raise Exception("Wrong settings key")

    def set_settings_values(self, request):
        tokens = request.split()
        for token in tokens[1:]:
            key_value = token.split(":")
            if len(key_value) == 2:
                self.set_settings_value(key_value[0], key_value[1])
        return self.get_settings_list()

    def get_settings_list(self):
        settings_list = []
        for key, value in self.settings_map.items():
            settings_list.append(key + " : " + str(value))
        return settings_list
