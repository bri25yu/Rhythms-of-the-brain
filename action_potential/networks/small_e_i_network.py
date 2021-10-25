import numpy as np, matplotlib.pyplot as plt

from action_potential.gates import (
    OlufsenPyramidalSodiumActivation,
    OlufsenPyramidalSodiumInactivation,
    OlufsenPyramidalPotassiumActivation,
    WangBuzsakiFastSpikingSodiumActivation,
    WangBuzsakiFastSpikingSodiumInactivation,
    WangBuzsakiFastSpikingPotassiumActivation,
)
from action_potential.action_potentials import (
    OlufsenPyramidalCurrentModulatedActionPotential,
    WangBuzsakiFastSpikingCurrentModulatedActionPotential,
)
from action_potential.currents.adjustable_input_current import AdjustableInputCurrent
from action_potential.neurons import Neuron
from action_potential.synapses import AMPASynapse, GABABasketSynapse


class SmallEINetwork:
    NUM_E = 80
    NUM_I = 20

    def __init__(self, fast=False):
        self.fast = fast

        if self.fast:
            self._init_e_neurons_fast(self.NUM_E)
            self._init_i_neurons_fast(self.NUM_I)
            self._init_ei_ie_synapses_fast()
            self.neurons = (self.i_neurons, self.e_neurons)
        else:
            self._init_e_neurons(self.NUM_E)
            self._init_i_neurons(self.NUM_I)
            self._init_ei_ie_synapses()
            self.neurons = self.i_neurons + self.e_neurons

    def update(self):
        if self.fast:
            self._update_fast()
        else:
            self._update()

    def snapshot(self):
        if self.fast:
            return np.hstack((self.i_neurons.voltage, self.e_neurons.voltage))
        else:
            return np.array([neuron.voltage for neuron in self.neurons])

    def draw(self, T):
        updates_per_tick = 100
        ticks_per_ms = 1000 // updates_per_tick
        total_ticks = T * ticks_per_ms

        data = [self.snapshot()]
        for i in range(total_ticks):
            for _ in range(updates_per_tick):
                self.update()
            data.append(self.snapshot())
            if (i+1) % 10 == 0:
                print(f"Finished {i+1} / {total_ticks}\r", end="", flush=True)
        print()
        spikes = np.array(data).T >= 35.0
        spike_locations, spike_times = np.argwhere(spikes).T + 1
        spike_times = spike_times / ticks_per_ms

        fig, ax = plt.subplots(figsize=(15, 15))
        ax.scatter(spike_times, spike_locations)
        ax.set_xlim(0, T)

        ax.set_ylabel("Neurons")
        ax.set_xlabel("t (ms)")

        return fig

    def _init_e_neurons(self, num_e):
        self.e_neurons = []
        for _ in range(num_e):
            ap = OlufsenPyramidalCurrentModulatedActionPotential(
                OlufsenPyramidalSodiumActivation(),
                OlufsenPyramidalSodiumInactivation(),
                OlufsenPyramidalPotassiumActivation(),
                AdjustableInputCurrent(),
            )
            self.e_neurons.append(Neuron(ap))

    def _init_e_neurons_fast(self, num_e):
        self.e_neurons = Neuron(
            OlufsenPyramidalCurrentModulatedActionPotential(
                OlufsenPyramidalSodiumActivation(),
                OlufsenPyramidalSodiumInactivation(),
                OlufsenPyramidalPotassiumActivation(),
                AdjustableInputCurrent(),
            )
        )
        self.e_neurons.voltage = np.ones(num_e) * self.e_neurons.voltage

    def _init_i_neurons(self, num_i):
        self.i_neurons = []
        for _ in range(num_i):
            ap = WangBuzsakiFastSpikingCurrentModulatedActionPotential(
                WangBuzsakiFastSpikingSodiumActivation(),
                WangBuzsakiFastSpikingSodiumInactivation(),
                WangBuzsakiFastSpikingPotassiumActivation(),
                AdjustableInputCurrent(),
            )
            self.i_neurons.append(Neuron(ap))

    def _init_i_neurons_fast(self, num_i):
        self.i_neurons = Neuron(
            WangBuzsakiFastSpikingCurrentModulatedActionPotential(
                WangBuzsakiFastSpikingSodiumActivation(),
                WangBuzsakiFastSpikingSodiumInactivation(),
                WangBuzsakiFastSpikingPotassiumActivation(),
                AdjustableInputCurrent(),
            )
        )
        self.i_neurons.voltage = np.ones(num_i) * self.i_neurons.voltage

    def _init_ei_ie_synapses(self):
        for e_neuron in self.e_neurons:
            for i_neuron in self.i_neurons:
                e_synapse = AMPASynapse(0.5, e_neuron, i_neuron)
                i_synapse = GABABasketSynapse(1.5, i_neuron, e_neuron)

                e_neuron.add_synapses((e_synapse,))
                i_neuron.add_synapses((i_synapse,))

    def _init_ei_ie_synapses_fast(self):
        e_synapse = AMPASynapse(0.5, self.e_neurons, self.i_neurons)
        i_synapse = GABABasketSynapse(1.5, self.i_neurons, self.e_neurons)

        self.e_neurons.add_synapses((e_synapse,))
        self.i_neurons.add_synapses((i_synapse,))

    def _update(self):
        for i, e_neuron in enumerate(self.e_neurons):
            input_current = 2.5 + 2 * (i + 20) / len(self.e_neurons)
            e_neuron.integrate(input_current)

        for neuron in self.neurons:
            neuron.fire()

        for neuron in self.neurons:
            neuron.update()

    def _update_fast(self):
        input_current = 2.5 + 2 * (np.arange(self.NUM_E) + 20) / self.NUM_E
        self.e_neurons.integrate(input_current)

        self.e_neurons.fire()
        self.i_neurons.fire()

        self.e_neurons.update()
        self.i_neurons.update()
