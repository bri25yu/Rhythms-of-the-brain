import os
import numpy as np, matplotlib.pyplot as plt

from action_potential.networks import (
    StrongPingEINetwork,
    WeakPingEINetwork,
    StrongOnWeakPingBackgroundEINetwork,
    AsyncISuppressesENetwork,
    StrongPingWithDistractorEINetwork,
    WeakPingWithDistractorEINetwork,
)

from action_potential.experiments.experiment import Experiment, register


@register
class PingPropertiesEINetworkExperiment(Experiment):
    def run(self):
        T = 200  # in ms

        networks = [
            StrongPingEINetwork(),
            WeakPingEINetwork(),
            StrongOnWeakPingBackgroundEINetwork(),
            AsyncISuppressesENetwork(),
            StrongPingWithDistractorEINetwork(),
            WeakPingWithDistractorEINetwork(),
        ]

        n_rows, n_cols = 3, 2
        fig, axs = plt.subplots(n_rows, n_cols, figsize=(10 * n_cols, 6 * n_rows))
        axs = np.hstack(axs)
        for network, ax in zip(networks, axs):
            print(f"Starting {network.name}...")
            network.draw(T, (fig, ax))
            ax.set_title(network.name)

        fig.tight_layout()
        fig.savefig(os.path.join(self.output_dir, "PingPropertiesEINetworkExperiment.png"))
