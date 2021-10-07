import os


class Experiment:
    output_dir = os.path.join("action_potential", "output")

    def run(self):
        raise NotImplementedError()


registered_experiments = dict()


def register(cls):
    registered_experiments[cls.__name__] = cls
    return cls
