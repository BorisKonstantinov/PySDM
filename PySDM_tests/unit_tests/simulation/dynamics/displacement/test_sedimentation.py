"""
Created at 12.03.2020

@author: Piotr Bartman
@author: Sylwester Arabas
"""

import numpy as np

from .displacement_setup import Setup


class ConstantTerminalVelocity:
    def __init__(self, particles):
        self.values = np.full(particles.n_sd, 1000)


class TestSedimentation:
    def test_boundary_condition(self):
        # Arrange
        setup = Setup()
        setup.dt = 1
        setup.sedimentation = True
        sut, particles = setup.get_displacement()

        particles.set_terminal_velocity(ConstantTerminalVelocity)

        # Act
        sut()

        # Assert
        assert particles.state.SD_num == 0
