import os
import numpy as np, matplotlib.pyplot as plt

from action_potential.approximations import (
    Approximation,
    RK2Approximation,
)
from action_potential.gates import (
    HodgkinHuxleySodiumActivation,
    HodgkinHuxleySodiumInactivation,
    HodgkinHuxleyPotassiumActivation,
    OlufsenPyramidalSodiumActivation,
    OlufsenPyramidalSodiumInactivation,
    OlufsenPyramidalPotassiumActivation,
    WangBuzsakiFastSpikingSodiumActivation,
    WangBuzsakiFastSpikingSodiumInactivation,
    WangBuzsakiFastSpikingPotassiumActivation,
)
from action_potential.action_potentials import (
    CurrentModulatedActionPotential,
    OlufsenPyramidalCurrentModulatedActionPotential,
    WangBuzsakiFastSpikingCurrentModulatedActionPotential
)
from action_potential.currents import SustainedInputCurrent

from action_potential.experiments.experiment import Experiment, register


@register
class NeuronTypeCurrentResponseExperiment(Experiment):
    def run(self):
        neuron_types = [
            (
                "Hodgkin Huxley",
                HodgkinHuxleySodiumActivation,
                HodgkinHuxleySodiumInactivation,
                HodgkinHuxleyPotassiumActivation,
                CurrentModulatedActionPotential,
            ),
            (
                "Olufsen Pyramidal",
                OlufsenPyramidalSodiumActivation,
                OlufsenPyramidalSodiumInactivation,
                OlufsenPyramidalPotassiumActivation,
                OlufsenPyramidalCurrentModulatedActionPotential,
            ),
            (
                "Wang-Buzsaki Fast Spiking",
                WangBuzsakiFastSpikingSodiumActivation,
                WangBuzsakiFastSpikingSodiumInactivation,
                WangBuzsakiFastSpikingPotassiumActivation,
                WangBuzsakiFastSpikingCurrentModulatedActionPotential,
            ),
        ]
        t = np.arange(0, 100, Approximation.EPS)

        n_neuron_types = len(neuron_types)
        fig, axs = plt.subplots(n_neuron_types, figsize=(10, 6 * n_neuron_types))

        input_current = SustainedInputCurrent
        current = np.array([input_current.F(v) for v in t])

        for neuron_type, ax in zip(neuron_types, axs):
            name, m, h, n, ap = neuron_type
            print(f"Starting {name}...")
            current_modulated_action_potential = ap(m(), h(), n(), None)

            current_modulated_action_potential.set_input_current(input_current)
            approximation = RK2Approximation.approximate(
                current_modulated_action_potential, t
            )

            ax.plot(t, current, label=input_current.name)
            ax.plot(t, approximation, label=name)

            ax.set_xlabel("t (ms)")
            ax.set_ylabel("Voltage (mV)")

            ax.set_title(f"Action potential for {name} neurons")

            ax.set_ylim((-100, 50))

            ax.legend()

        fig.tight_layout()

        plt.savefig(os.path.join(self.output_dir, "NeuronTypeCurrentResponseExperiment.png"))
