import os

from action_potential.networks.small_e_i_network import SmallEINetwork

from action_potential.experiments.experiment import Experiment, register


@register
class SmallEINetworkExperiment(Experiment):
    def run(self):
        T = 200  # in ms

        network = SmallEINetwork()
        fig = network.draw(T)
        fig.tight_layout()
        fig.savefig(os.path.join(self.output_dir, "SmallEINetworkExperiment.png"))
