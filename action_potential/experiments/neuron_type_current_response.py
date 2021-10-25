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
    TortOLMInterneuronSodiumActivation,
    TortOLMInterneuronSodiumInactivation,
    TortOLMInterneuronPotassiumActivation,
    TortOLMInterneuronAActivation,
    TortOLMInterneuronBActivation,
    TortOLMInterneuronRActivation,
)
from action_potential.action_potentials import (
    CurrentModulatedActionPotential,
    OlufsenPyramidalCurrentModulatedActionPotential,
    WangBuzsakiFastSpikingCurrentModulatedActionPotential,
    TortOLMInterneuronCurrentModulatedActionPotential,
)
from action_potential.currents import (
    BaseInputCurrent,
    SustainedInputCurrent,
)

from action_potential.experiments.experiment import Experiment, register


@register
class NeuronTypeCurrentResponseExperiment(Experiment):
    def run(self):
        neuron_types = [
            self._init_hodgkin_huxley(),
            self._init_olufsen_pyramidal(),
            self._init_wang_buzsaki_fast_spiking(),
            self._init_tort_o_lm_interneuron(),
        ]
        t = np.arange(0, 100, Approximation.EPS)

        n_neuron_types = len(neuron_types)
        fig, axs = plt.subplots(n_neuron_types, figsize=(10, 6 * n_neuron_types))

        for neuron_type, ax in zip(neuron_types, axs):
            name, ap = neuron_type
            print(f"Starting {name}...")
            current = np.array([ap.input_current.F(v) for v in t])
            approximation = RK2Approximation.approximate(ap, t)

            ax.plot(t, current, label=ap.input_current.name)
            ax.plot(t, approximation, label=name)

            ax.set_xlabel("t (ms)")
            ax.set_ylabel("Voltage (mV)")

            ax.set_title(f"Action potential for {name} neurons")

            ax.set_ylim((-100, 60))

            ax.legend()

        fig.tight_layout()

        plt.savefig(os.path.join(self.output_dir, "NeuronTypeCurrentResponseExperiment.png"))

    @staticmethod
    def _init_hodgkin_huxley():
        name = "Hodgkin Huxley"
        ap = CurrentModulatedActionPotential(
            HodgkinHuxleySodiumActivation(),
            HodgkinHuxleySodiumInactivation(),
            HodgkinHuxleyPotassiumActivation(),
            SustainedInputCurrent,
        )
        return name, ap

    @staticmethod
    def _init_olufsen_pyramidal():
        name = "Olufsen Pyramidal"
        ap = OlufsenPyramidalCurrentModulatedActionPotential(
            OlufsenPyramidalSodiumActivation(),
            OlufsenPyramidalSodiumInactivation(),
            OlufsenPyramidalPotassiumActivation(),
            SustainedInputCurrent,
        )
        return name, ap

    @staticmethod
    def _init_wang_buzsaki_fast_spiking():
        name = "Wang-Buzsaki Fast Spiking"
        ap = WangBuzsakiFastSpikingCurrentModulatedActionPotential(
            WangBuzsakiFastSpikingSodiumActivation(),
            WangBuzsakiFastSpikingSodiumInactivation(),
            WangBuzsakiFastSpikingPotassiumActivation(),
            SustainedInputCurrent,
        )
        return name, ap

    @staticmethod
    def _init_tort_o_lm_interneuron():
        name = "Tort O-LM Interneuron"
        ap = TortOLMInterneuronCurrentModulatedActionPotential(
            TortOLMInterneuronSodiumActivation(),
            TortOLMInterneuronSodiumInactivation(),
            TortOLMInterneuronPotassiumActivation(),
            TortOLMInterneuronAActivation(),
            TortOLMInterneuronBActivation(),
            TortOLMInterneuronRActivation(),
            BaseInputCurrent,
        )
        return name, ap
