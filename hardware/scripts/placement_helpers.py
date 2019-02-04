#!/usr/bin/env python

from math import sin, cos, radians, pi, degrees
from pcbnew import *

def place_circle(references, center, radius, angle_offset=0, rotation_angle=0):
    """
    Places components in a circle
    references: List of component references
    center: Tuple of (x, y) mils of circle center
    radius: Radius of the circle in mils
    """
    pcb = GetBoard()
    step = 2 * pi / len(references)

    for idx, rd in enumerate(references):
        part = pcb.FindModuleByReference(rd)

        angle = step * idx + angle_offset
        x0, y0 = center

        xmils = float(x0 + radius * cos(angle))
        ymils = float(y0 + radius * sin(angle))

        part.SetPosition(wxPointMM(xmils,ymils))
        part.SetOrientation((degrees(angle) + 90 + rotation_angle) * -10)
        part.Reference().SetVisible(False)

    print("Placement finished. Press F11 to refresh.")


def place_leds():
    return place_circle(
        references=["D{i}".format(i=i) for i in range(1, 24)],
        center=(0, 0),
        radius=(60-10/2),
    )

def place_caps():
    return place_circle(
        references=["C{i}".format(i=i) for i in range(1, 24)],
        center=(0, 0),
        angle_offset=10,
        rotation_angle=95,
        radius=(60-10/2)+0.25,
    )

