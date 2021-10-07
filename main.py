import sys

from action_potential.experiments import registered_experiments


def main():
    experiment_name = sys.argv[1]
    if experiment_name in registered_experiments:
        experiment = registered_experiments[experiment_name]()
        experiment.run()


if __name__ == "__main__":
    main()
