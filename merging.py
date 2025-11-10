# -*- coding: utf-8 -*-
# Author: Runsheng Xu <rxx3386@ucla.edu>
# License: TDG-Attribution-NonCommercial-NoDistrib

import os

import carla

import opencda.scenario_testing.utils.cosim_api as sim_api
import opencda.scenario_testing.utils.customized_map_api as map_api
from opencda.core.common.cav_world import CavWorld
from opencda.scenario_testing.evaluations.evaluate_manager import \
    EvaluationManager
from opencda.scenario_testing.utils.yaml_utils import add_current_time


def run_scenario(opt, scenario_params):
    try:
        scenario_params = add_current_time(scenario_params)

        # create CAV world
        cav_world = CavWorld(opt.apply_ml)

        # sumo config file path
        current_path = os.path.dirname(os.path.realpath(__file__))
        sumo_cfg = os.path.join(current_path, '../assets/Merging')

        # create co-simulation scenario manager
        scenario_manager = sim_api.CoScenarioManager(
            scenario_params,
            opt.apply_ml,
            opt.version,
            town='Town06',
            cav_world=cav_world,
            sumo_file_parent_path=sumo_cfg
        )

        # ❗️DON'T create vehicle managers from the YAML scenario
        # This is the line that was spawning the extra CARLA car:
        # single_cav_list = scenario_manager.create_vehicle_manager(
        #     application=['single'],
        #     map_helper=map_api.spawn_helper_2lanefree
        # )
        single_cav_list = []

        # create evaluation manager (still OK to create)
        eval_manager = EvaluationManager(
            scenario_manager.cav_world,
            script_name='single_2lanefree_cosim',
            current_time=scenario_params['current_time']
        )

        # You can still set the spectator, but now we don't have a CARLA vehicle
        # to attach to. So just place it at a fixed spot.
        spectator = scenario_manager.world.get_spectator()
        spectator.set_transform(
            carla.Transform(
                carla.Location(x=220, y=139.51, z=50.0),
                carla.Rotation(pitch=-90.0)
            )
        )

        while True:
            # tick CARLA + SUMO
            scenario_manager.tick()

            # no CAVs to update or control now
            # for single_cav in single_cav_list:
            #     single_cav.update_info()
            #     control = single_cav.run_step()
            #     single_cav.vehicle.apply_control(control)

    finally:
        # eval_manager.evaluate()
        scenario_manager.close()
        for v in single_cav_list:
            v.destroy()
