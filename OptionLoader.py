import yaml

class OptionLoader:
  
    def __init__(self, option_file):
            self.load_options(option_file)

    def load_options(self, option_file):
        with open(option_file, 'r') as file:
            option_data = yaml.safe_load(file)

        for key, value in option_data.items():
            setattr(self, key, value)