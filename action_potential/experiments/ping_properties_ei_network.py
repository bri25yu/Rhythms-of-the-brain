import os
import matplotlib.pyplot as plt

from action_potential.networks import (
    StrongPingEINetwork,
    WeakPingEINetwork,
)

from action_potential.experiments.experiment import Experiment, register


@register
class PingPropertiesEINetworkExperiment(Experiment):
    def run(self):
        T = 200  # in ms

        networks = [
            StrongPingEINetwork(),
            WeakPingEINetwork(),
        ]

        fig, axs = plt.subplots(len(networks), figsize=(15, 10 * len(networks)))
        for network, ax in zip(networks, axs):
            print(f"Starting {network.name}...")
            network.draw(T, (fig, ax))
            ax.set_title(network.name)

        fig.tight_layout()
        fig.savefig(os.path.join(self.output_dir, "PingPropertiesEINetworkExperiment.png"))
