import os
import numpy as np, matplotlib.pyplot as plt

from action_potential.approximations import (
    Approximation,
    EulerApproximation,
)
from action_potential.gates import (
    SodiumActivation,
    SodiumInactivation,
    PotassiumActivation,
)
from action_potential.action_potentials import ActionPotential

from action_potential.experiments.experiment import Experiment, register


@register
class ActionPotentialExperiment(Experiment):
    def run(self):
        t = np.arange(0, 25, Approximation.EPS)

        action_potential = ActionPotential(
            SodiumActivation(), SodiumInactivation(), PotassiumActivation()
        )
        V_0s = [-65.0, -70.0, -55.0]

        for V_0 in V_0s:
            action_potential.set_V_0(V_0)
            action_potential_approximation = EulerApproximation.approximate(
                action_potential, t
            )
            plt.plot(t, action_potential_approximation, label=r"$V_0=$" + str(V_0))

        plt.legend()
        plt.title("Action potentials by starting voltage")
        plt.xlabel("Time (ms)")
        plt.ylabel("Voltage (mV)")
        plt.savefig(os.path.join(self.output_dir, "ActionPotentialExperiment.png"))
        print(f"Steady state voltage: {action_potential_approximation[-1]}mV")
