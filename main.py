import sys

import numpy as np
np.random.seed(0)

from action_potential.experiments import registered_experiments


def main():
    experiment_name = ""

    if len(sys.argv) <= 1:
        experiment_names = list(registered_experiments.keys())
        lines = [
            "Registered experiments:",
            *map(lambda p: f"{p[0]+1}) {p[1]}", enumerate(experiment_names)),
        ]
        print("\n\t".join(lines))

        selection = input()
        try:
            experiment_name = experiment_names[int(selection)-1]
        except:
            pass
    else:
        experiment_name = sys.argv[1]

    if experiment_name in registered_experiments:
        experiment = registered_experiments[experiment_name]()
        experiment.run()
    else:
        print(f"Experiment not found: {experiment_name}")


if __name__ == "__main__":
    main()
