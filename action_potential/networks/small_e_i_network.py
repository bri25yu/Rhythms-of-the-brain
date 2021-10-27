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
from action_potential.approximations.approximation import Approximation
from action_potential.neurons import Neuron
from action_potential.synapses import AMPASynapse, GABABasketSynapse


class SmallEINetwork:
    name = "Small E-I network"

    NUM_E = 80
    NUM_I = 20

    P_EE = 1.0
    P_EI = 1.0
    P_IE = 1.0
    P_II = 1.0

    g_EI = 0.5
    g_IE = 1.5
    g_EE = 0.0
    g_II = 0.0

    g_stoch_E = 0.0
    tau_D_stoch_E = 0.0
    f_stoch_E = 0.0

    g_stoch_I = 0.0
    tau_D_stoch_I = 0.0
    f_stoch_I = 0.0

    def __init__(self, fast=False):
        self.fast = fast

        self.s_stoch_E = np.zeros((self.NUM_E,))
        self.s_stoch_I = np.zeros((self.NUM_I,))

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

    def draw(self, T, fig_ax=None):
        updates_per_tick = 100
        ticks_per_ms = int(1 / Approximation.EPS) // updates_per_tick
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

        if fig_ax is None:
            fig, ax = plt.subplots(figsize=(15, 15))
        else:
            fig, ax = fig_ax

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
                ei_g = np.random.binomial(1, self.P_EI) * self.g_EI / (self.P_EI * self.NUM_E)
                ie_g = np.random.binomial(1, self.P_IE) * self.g_IE / (self.P_IE * self.NUM_I)

                e_synapse = AMPASynapse(ei_g, e_neuron, i_neuron)
                i_synapse = GABABasketSynapse(ie_g, i_neuron, e_neuron)

                e_neuron.add_synapses((e_synapse,))
                i_neuron.add_synapses((i_synapse,))

    def _init_ei_ie_synapses_fast(self):
        ei_g = np.random.binomial(1, self.P_EI, size=(self.NUM_E, self.NUM_I))
        ei_g = ei_g * self.g_EI / (self.P_EI * self.NUM_E)
        ie_g = np.random.binomial(1, self.P_IE, size=(self.NUM_I, self.NUM_E))
        ie_g = ie_g * self.g_IE / (self.P_IE * self.NUM_I)

        e_synapse = AMPASynapse(ei_g, self.e_neurons, self.i_neurons)
        i_synapse = GABABasketSynapse(ie_g, self.i_neurons, self.e_neurons)

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
        e_input_current = self._deterministic_E_input_current() + self._stochastic_E_input_current()
        self.e_neurons.integrate(e_input_current)

        i_input_current = self._deterministic_I_input_current() + self._stochastic_I_input_current()
        self.i_neurons.integrate(i_input_current)

        self.e_neurons.fire()
        self.i_neurons.fire()

        self.e_neurons.update()
        self.i_neurons.update()

    def _deterministic_E_input_current(self):
        return 2.5 + (2 * (np.arange(1, self.NUM_E + 1) + 20) / self.NUM_E)

    def _deterministic_I_input_current(self):
        return 0.0

    def _stochastic_E_input_current(self):
        self.s_stoch_E, input_current =\
            self._kopell_stochastic_input_current(
                self.s_stoch_E,
                self.tau_D_stoch_E,
                self.g_stoch_E,
                self.e_neurons.voltage,
                self.f_stoch_E,
            )
        return input_current
    
    def _stochastic_I_input_current(self):
        self.s_stoch_I, input_current =\
            self._kopell_stochastic_input_current(
                self.s_stoch_I,
                self.tau_D_stoch_I,
                self.g_stoch_I,
                self.i_neurons.voltage,
                self.f_stoch_I,
            )
        return input_current

    def _kopell_stochastic_input_current(self, s, tau, g, V, f):
        s = s - Approximation.EPS * tau * s
        input_current = -s * g * V

        reset = np.random.binomial(
            1,
            Approximation.EPS * f / 1000,
            size=s.shape,
        )
        s = reset + (1 - reset) * s

        return s, input_current
