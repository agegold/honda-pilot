from collections import namedtuple
from typing import Dict, List, Union

from cereal import car
from selfdrive.car import dbc_dict
from selfdrive.car.docs_definitions import CarInfo

Ecu = car.CarParams.Ecu
TransmissionType = car.CarParams.TransmissionType

AngleRateLimit = namedtuple('AngleRateLimit', ['speed_points', 'max_angle_diff_points'])


class CarControllerParams:
  LKAS_STEP = 5       # 20Hz Lane_Assist_Data1, LateralMotionControl
  ACC_STEP = 2        # 50Hz ACCDATA
  LKAS_UI_STEP = 100  # 1Hz  IPMA_Data
  ACC_UI_STEP = 5     # 20Hz ACCDATA_3

  ACCEL_MAX = 2.0     # 2.0 m/s^2 max acceleration
  ACCEL_MIN = -3.5    # 3.5 m/s^2 max deceleration


class CANBUS:
  main = 0
  radar = 1
  camera = 2


class CAR:
  ESCAPE_MK4 = "FORD ESCAPE 4TH GEN"
  FOCUS_MK4 = "FORD FOCUS 4TH GEN"
  MAVERICK_MK1 = "FORD MAVERICK 1ST GEN"
  TRANSIT_MK4 = "FORD TRANSIT 4TH GEN"


CAR_INFO: Dict[str, Union[CarInfo, List[CarInfo]]] = {
}


FW_VERSIONS = {
  CAR.ESCAPE_MK4: {
    (Ecu.eps, 0x730, None): [
      b'LX6C-14D003-AH\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.esp, 0x760, None): [
      b'LX6C-2D053-NS\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.fwdRadar, 0x764, None): [
      b'LB5T-14D049-AB\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.fwdCamera, 0x706, None): [
      b'LJ6T-14F397-AD\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.engine, 0x7E0, None): [
      b'LX6A-14C204-ESG\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
  },
  CAR.FOCUS_MK4: {
    (Ecu.eps, 0x730, None): [
      b'JX6C-14D003-AH\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.esp, 0x760, None): [
      b'JX61-2D053-CJ\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.fwdRadar, 0x764, None): [
      b'JX7T-14D049-AC\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.fwdCamera, 0x706, None): [
      b'JX7T-14F397-AH\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.engine, 0x7E0, None): [
      b'JX6A-14C204-BPL\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
  },
  CAR.FOCUS_MK4: {
    (Ecu.eps, 0x730, None): [
      b'KK21-14D003-AJ\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.esp, 0x760, None): [
      b'NK41-2D053-AF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.fwdRadar, 0x764, None): [
      b'LB5T-14D049-AB\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.fwdCamera, 0x706, None): [
      b'NK3T-14F397-AA\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
  },
}


DBC = {
  CAR.ESCAPE_MK4: dbc_dict('ford_lincoln_base_pt', None),
  CAR.FOCUS_MK4: dbc_dict('ford_lincoln_base_pt', None),
  CAR.MAVERICK_MK1: dbc_dict('ford_lincoln_base_pt', None),
}
