import os
import numpy as np, matplotlib.pyplot as plt

from action_potential.functions import F1, F2
from action_potential.approximations import (
    Approximation,
    EulerApproximation,
    RK2Approximation,
    Taylor2Approximation,
)

from action_potential.experiments.experiment import Experiment, register


@register
class ApproximationsExperiment(Experiment):
    def run(self):
        t = np.arange(0, 5, Approximation.EPS)

        functions = [F1, F2]
        approximation_methods = [
            EulerApproximation,
            RK2Approximation,
            Taylor2Approximation,
        ]

        fig, axs = plt.subplots(len(functions), 2, figsize=(10 * len(functions), 15))

        for fn_axs, f in zip(axs, functions):
            actual_values = f.F(t)
            fn_axs[0].plot(t, actual_values, label=f.name)
            fn_axs[1].plot(
                t, actual_values - actual_values, label=r"Error of actual function"
            )

            for approximation_method in approximation_methods:
                approximation = approximation_method.approximate(f, t)
                label = f"Approximation of {f.name} using {approximation_method.name} method"
                fn_axs[0].plot(t, approximation, label=label)

                label = f"Error of {approximation_method.name} method"
                fn_axs[1].plot(t, approximation - actual_values, label=label)

            fn_axs[0].set_title(f"Approximations of {f.name}")
            fn_axs[1].set_title(f"Errors of approximations of {f.name}")

            fn_axs[0].legend()
            fn_axs[1].legend()

        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, "ApproximationsExperiment.png"))
