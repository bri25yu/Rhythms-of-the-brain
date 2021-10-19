import os
import numpy as np, matplotlib.pyplot as plt

from action_potential.approximations import (
    Approximation,
    EulerApproximation,
)
from action_potential.gates import (
    HodgkinHuxleySodiumActivation,
    HodgkinHuxleySodiumInactivation,
    HodgkinHuxleyPotassiumActivation,
)
from action_potential.functions import GateFunction

from action_potential.experiments.experiment import Experiment, register


@register
class GatesExperiment(Experiment):
    def run(self):
        activations = [HodgkinHuxleySodiumActivation(), HodgkinHuxleySodiumInactivation(), HodgkinHuxleyPotassiumActivation()]

        t = np.arange(0, 5, Approximation.EPS)
        V = np.arange(-100, 50, 0.1)
        Vs = [(-70, -40), (0, 30)]

        n_rows = 1 + len(Vs)
        fig, axs = plt.subplots(n_rows, 2, figsize=(15, 5 * n_rows))

        for a in activations:
            axs[0][0].plot(V, a.steady_state(V), label=a.name)
            axs[0][1].plot(V, a.time_constant(V), label=a.name)

        axs[0][0].legend()
        axs[0][1].legend()

        axs[0][0].set_title("Steady state")
        axs[0][1].set_title("Time constant")

        axs[0][0].set_xlabel("V (mV)")
        axs[0][1].set_xlabel("V (mV)")

        for (V_i, V_f), (ax1, ax2) in zip(Vs, axs[1:]):
            for a in activations:
                gate = GateFunction(V_i, V_f, a)

                actual = gate.F(t)

                ax1.plot(t, EulerApproximation.approximate(gate, t), label=a.name)
                ax2.plot(
                    t, EulerApproximation.approximate(gate, t) - actual, label=a.name
                )

            ax1.set_title(
                r"Activation Euler approximations for $V_i = {V_i}, V_f = {V_f}$".format(
                    V_i=V_i, V_f=V_f
                )
            )
            ax2.set_title(
                r"Euler approximation error for $V_i = {V_i}, V_f = {V_f}$".format(
                    V_i=V_i, V_f=V_f
                )
            )

            ax1.legend()
            ax2.legend()

            ax1.set_xlabel("t (ms)")
            ax2.set_xlabel("t (ms)")

        fig.tight_layout()

        plt.savefig(os.path.join(self.output_dir, "GatesExperiment.png"))
