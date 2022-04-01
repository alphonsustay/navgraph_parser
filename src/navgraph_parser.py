#! /usr/bin/env python

######################### Iteration 2 - 1 APRIL 2022 #############################
## Assuming that the building map name is the location label for the beds ########
import sys
from textwrap import indent
from turtle import clear
import yaml
import json
# config = "../resource/0.yaml"
# output = "../resource/waypoint.yaml"


class NavgraphParser:
    def __init__(self):
        print("Initialising Parser....")
        self.input = "../resource/0.yaml"
        self.output = "../resource/waypoint.yaml"
        self.json_output = "../resource/bed.json"

    def backbone_conversion(self):
        all_waypoints = {}
        with open(self.input, "r") as stream:
            navgraph_data = yaml.load(stream, Loader=yaml.FullLoader)

    ################################ YAML OUTPUT #########################################  
            # for level in navgraph_data['levels']:
            #     level_waypoints = []
            #     for waypoint in navgraph_data['levels'][level]['vertices']:
            #         if (waypoint[2]["name"] != ""):
            #             level_waypoints.append({"name": waypoint[2]["name"], "x": waypoint[0], "y":waypoint[1]})
            
            #     all_waypoints.append({"level": level, "waypoints": level_waypoints})
        
        # with open(self.output, "w") as final:
        #     yaml.dump(all_waypoints, final)
        #     final.close()
    ######################################################################################
            location = navgraph_data['building_name']
            for level in navgraph_data['levels']:
                level_waypoints = {}
                for waypoint in navgraph_data['levels'][level]['vertices']:
                    if ('bed' in waypoint[2]['name']):
                        name = waypoint[2]['name']
                        key_index = name.index('bed') + 3
                        key = waypoint[2]['name'][key_index:]
                        level_waypoints[key] = name
                if level_waypoints:
                    all_waypoints[location] = level_waypoints

        with open(self.json_output, "w", newline='') as json_final:
            output = json.dumps(all_waypoints, indent = 4)
            json_final.write(output)
def main():
    parser = NavgraphParser()
    parser.backbone_conversion()

if __name__ == "__main__":
    main()