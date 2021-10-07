import os
import numpy as np, matplotlib.pyplot as plt

from action_potential.approximations import (
    Approximation,
    RK2Approximation,
)
from action_potential.gates import (
    SodiumActivation,
    SodiumInactivation,
    PotassiumActivation,
)
from action_potential.action_potentials import CurrentModulatedActionPotential
from action_potential.currents import (
    BaseInputCurrent,
    BlipInputCurrent,
    SustainedInputCurrent,
)

from action_potential.experiments.experiment import Experiment, register


@register
class InputCurrentsExperiment(Experiment):
    def run(self):
        input_currents = [
            BaseInputCurrent,
            BlipInputCurrent,
            SustainedInputCurrent,
        ]

        t = np.arange(0, 100, Approximation.EPS)

        n_input_currents = len(input_currents)
        fig, axs = plt.subplots(n_input_currents, figsize=(8, 5 * n_input_currents))

        current_modulated_action_potential = CurrentModulatedActionPotential(
            SodiumActivation(),
            SodiumInactivation(),
            PotassiumActivation(),
            None,
        )

        for input_current, ax in zip(input_currents, axs):
            current_modulated_action_potential.set_input_current(input_current)
            current = np.array([input_current.F(v) for v in t])
            approximation = RK2Approximation.approximate(
                current_modulated_action_potential, t
            )

            ax.plot(t, current, label=input_current.name)
            ax.plot(t, approximation, label="Action potentials")

            ax.set_xlabel("t (ms)")
            ax.set_ylabel("Voltage (mV)")

            ax.set_ylim((-80, 40))

            ax.legend()

        fig.suptitle("Action potentials with various input currents")
        fig.tight_layout()

        plt.savefig(os.path.join(self.output_dir, "InputCurrentsExperiment.png"))
