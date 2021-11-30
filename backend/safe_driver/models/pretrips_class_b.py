from django.db import models
from django.utils.translation import ugettext_lazy as _

from safe_driver.image_functions import signature_image_folder
from safe_driver.utils import PreTripClassMixin

NUMBER_CHOICES = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
    (0, "N/A"),
)


# Pre Trip Class B
class PreTripClassB(models.Model):
    test = models.OneToOneField('safe_driver.StudentTest', on_delete=models.CASCADE, null=False,
                                related_name='pretrip_student_test_class_b')
    date = models.DateField(null=True, blank=True, default=None, verbose_name='Date')
    start_time = models.TimeField(null=True, blank=True, default=None, verbose_name='Start Time')
    end_time = models.TimeField(null=True, blank=True, default=None, verbose_name='End Time')
    driver_signature = models.ImageField(upload_to=signature_image_folder, default=None, null=True, blank=True)
    evaluator_signature = models.ImageField(upload_to=signature_image_folder, default=None, null=True,
                                            blank=True)
    company_rep_signature = models.ImageField(upload_to=signature_image_folder, default=None, null=True,
                                              blank=True)
    company_rep_name = models.CharField(max_length=150, null=True, blank=True, default=None,
                                        verbose_name='Company Rep. Name')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Pre Trip Class B"
        verbose_name_plural = "Pre Trips Class B"


# 1. Pre Trip Inside Cab Class B
class PreTripInsideCabClassB(PreTripClassMixin, models.Model):
    # relation
    pre_trip_class_b = models.OneToOneField('safe_driver.PreTripClassB', on_delete=models.CASCADE, null=False,
                                            related_name='pretrip_insidecab_class_b')
    hand_rails = models.IntegerField(_('Hand Rails'), choices=NUMBER_CHOICES, default=0, )
    fire_extinguisher = models.IntegerField(_('Fire Extinguisher'), choices=NUMBER_CHOICES, default=0, )
    fhwa = models.IntegerField(_('FHWA'), choices=NUMBER_CHOICES, default=0, )
    emergency_response_book = models.IntegerField(_('Emergency Response Book'), choices=NUMBER_CHOICES, default=0, )
    dvir = models.IntegerField(_('DVIR'), choices=NUMBER_CHOICES, default=0, )
    parking_brake_applied = models.IntegerField(_('Parking Brake Applied'), choices=NUMBER_CHOICES, default=0, )
    transmission_neutral_or_park = models.IntegerField(_('Transmission Neutral/Park'), choices=NUMBER_CHOICES,
                                                       default=0, )
    seat_adjustment = models.IntegerField(_('Seat Adjustment'), choices=NUMBER_CHOICES, default=0, )
    seat_belt = models.IntegerField(_('Seat Belt'), choices=NUMBER_CHOICES, default=0, )
    # cab_or_berth = models.IntegerField(_('Cab/Berth'), choices=NUMBER_CHOICES, default=0, )
    dome_and_map_lights = models.IntegerField(_('Dome and Map Lights'), choices=NUMBER_CHOICES, default=0, )
    windows = models.IntegerField(_('Windows'), choices=NUMBER_CHOICES, default=0, )
    mirros = models.IntegerField(_('Mirrors'), choices=NUMBER_CHOICES, default=0, )
    steering_wheel_play = models.IntegerField(_('Steering Wheel Play'), choices=NUMBER_CHOICES, default=0, )
    horn = models.IntegerField(_('Horn'), choices=NUMBER_CHOICES, default=0, )
    indicators = models.IntegerField(_('Indicators'), choices=NUMBER_CHOICES, default=0, )
    wipers = models.IntegerField(_('Wipers'), choices=NUMBER_CHOICES, default=0, )
    gauges = models.IntegerField(_('Gauges'), choices=NUMBER_CHOICES, default=0, )
    air_heater_defrost = models.IntegerField(_('Air, Heater, Defrost'), choices=NUMBER_CHOICES, default=0, )
    bi_directional_triangles = models.IntegerField(_('Bi-directional Triangles'), choices=NUMBER_CHOICES, default=0, )
    shifter_straight_and_secure = models.IntegerField(_('Shifter Straight and Secure'), choices=NUMBER_CHOICES,
                                                      default=0, )
    splitter = models.IntegerField(_('Splitter'), choices=NUMBER_CHOICES, default=0, )
    clear_floor_board = models.IntegerField(_('Clear floor Board'), choices=NUMBER_CHOICES, default=0, )
    pedals = models.IntegerField(_('Pedals'), choices=NUMBER_CHOICES, default=0, )
    park_brake_test = models.IntegerField(_('Park Brake Test'), choices=NUMBER_CHOICES, default=0, )
    service_brake_test = models.IntegerField(_('Service Brake Test'), choices=NUMBER_CHOICES, default=0, )
    # trailer_brake_test = models.IntegerField(_('Trailer Brake Test'), choices=NUMBER_CHOICES, default=0, )
    pull_key = models.IntegerField(_('Pull Key'), choices=NUMBER_CHOICES, default=0, )
    exit_safely = models.IntegerField(_('Exit Safely'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(default="", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Pre Trip Inside Cab Class B"
        verbose_name_plural = "Pre Trip Inside Cab Class B List"


# 2. Pre Trip COALS Class B
class PreTripCOALSClassB(PreTripClassMixin, models.Model):
    # relation
    pre_trip_class_b = models.OneToOneField('safe_driver.PreTripClassB', on_delete=models.CASCADE, null=False,
                                            related_name='pretrip_coals_class_b')

    chock_wheels = models.IntegerField(_('Chock Wheels'), choices=NUMBER_CHOICES, default=0, )
    cut_in = models.IntegerField(_('Cut in'), choices=NUMBER_CHOICES, default=0, )
    cut_out = models.IntegerField(_('Cut out'), choices=NUMBER_CHOICES, default=0, )
    applied_air_leak_test = models.IntegerField(_('Applied Air Leak Test'), choices=NUMBER_CHOICES, default=0, )
    low_air_warning = models.IntegerField(_('Low Air Warning'), choices=NUMBER_CHOICES, default=0, )
    spring_test = models.IntegerField(_('Spring Test'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(default="", null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Pre Trip COALS Class B"
        verbose_name_plural = "Pre Trip COALS Class B List"


# 3. Pre Trip Engine Compartment Class B
class PreTripEngineCompartmentClassB(PreTripClassMixin, models.Model):
    # relation
    pre_trip_class_b = models.OneToOneField('safe_driver.PreTripClassB', on_delete=models.CASCADE, null=False,
                                            related_name='pretrip_engine_compartment_class_b')

    fuses = models.IntegerField(_('Fuses'), choices=NUMBER_CHOICES, default=0, )
    hood_latches = models.IntegerField(_('Hood Latches'), choices=NUMBER_CHOICES, default=0, )
    hood_locking_device = models.IntegerField(_('Hood Locking Device'), choices=NUMBER_CHOICES, default=0, )
    engine_oil = models.IntegerField(_('Engine Oil'), choices=NUMBER_CHOICES, default=0, )
    transmission_oil = models.IntegerField(_('Transmission Oil'), choices=NUMBER_CHOICES, default=0, )
    power_steering_fluid = models.IntegerField(_('Power Steering Fluid'), choices=NUMBER_CHOICES, default=0, )
    washer_fluid = models.IntegerField(_('Washer Fluid'), choices=NUMBER_CHOICES, default=0, )
    coolant = models.IntegerField(_('Coolant'), choices=NUMBER_CHOICES, default=0, )
    belts_and_hoses = models.IntegerField(_('Belts and Hoses'), choices=NUMBER_CHOICES, default=0, )
    filters = models.IntegerField(_('Filters'), choices=NUMBER_CHOICES, default=0, )
    components = models.IntegerField(_('Components'), choices=NUMBER_CHOICES, default=0, )
    leaks_air_and_fluid = models.IntegerField(_('Leaks(Air & Fluid)'), choices=NUMBER_CHOICES, default=0, )
    frame = models.IntegerField(_('Frame'), choices=NUMBER_CHOICES, default=0, )
    suspension = models.IntegerField(_('Suspension'), choices=NUMBER_CHOICES, default=0, )
    steering_components = models.IntegerField(_('Steering Components'), choices=NUMBER_CHOICES, default=0, )
    brake_chambers_or_slack_adj = models.IntegerField(_('Brake Chambers/Slack Adjustors'),
                                                      choices=NUMBER_CHOICES, default=0, )
    brake_drums_and_pads = models.IntegerField(_('Brake Drums & Pads'), choices=NUMBER_CHOICES, default=0, )
    wheel_bearings = models.IntegerField(_('Wheel Bearings'), choices=NUMBER_CHOICES, default=0, )
    tire_inflation = models.IntegerField(_('Tire Inflation'), choices=NUMBER_CHOICES, default=0, )
    tire_and_rim_condition = models.IntegerField(_('Tire & Rim Condition'), choices=NUMBER_CHOICES, default=0, )
    valve_stems_and_hub_oil = models.IntegerField(_('Valve Stems & Hub Oil'), choices=NUMBER_CHOICES, default=0, )
    mud_flaps = models.IntegerField(_('Mud Flaps'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(default="", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Pre Trip Engine Compartment Class B"
        verbose_name_plural = "Pre Trip Engine Compartment Class B List"


# 4. Pre Trip Vehicle Front Class B
class PreTripVehicleFrontClassB(PreTripClassMixin, models.Model):
    # relation
    pre_trip_class_b = models.OneToOneField('safe_driver.PreTripClassB', on_delete=models.CASCADE, null=False,
                                            related_name='pretrip_vehicle_front_class_b')

    body_damage = models.IntegerField(_('Body Damage'), choices=NUMBER_CHOICES, default=0, )
    lights_id_and_others = models.IntegerField(_('Lights-I.D. mkr, head, 4way, road'), choices=NUMBER_CHOICES,
                                               default=0, )
    bumper_and_tow_hooks = models.IntegerField(_('Bumper and Tow Hooks'), choices=NUMBER_CHOICES, default=0, )
    license_plate = models.IntegerField(_('License Plate'), choices=NUMBER_CHOICES, default=0, )
    sensors = models.IntegerField(_('Sensors'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(default="", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Pre Trip Vehicle Front Class B"
        verbose_name_plural = "Pre Trip Vehicle Front Class B List"


# 5. Pre Trip Both Sides Vehicles Class B
class PreTripBothSidesVehiclesClassB(PreTripClassMixin, models.Model):
    # relation
    pre_trip_class_b = models.OneToOneField('safe_driver.PreTripClassB', on_delete=models.CASCADE, null=False,
                                            related_name='pretrip_both_sides_vehicle_class_b')

    mirrors = models.IntegerField(_('Mirrors'), choices=NUMBER_CHOICES, default=0, )
    vehicle_markings_or_decals = models.IntegerField(_('Vehicle Markings/Decals'), choices=NUMBER_CHOICES, default=0, )
    dots = models.IntegerField(_('DOT’s, CA, MC #’s'), choices=NUMBER_CHOICES, default=0, )
    ifta_permit = models.IntegerField(_('IFTA Permit'), choices=NUMBER_CHOICES, default=0, )
    air_tanks = models.IntegerField(_('Air Tanks'), choices=NUMBER_CHOICES, default=0, )
    fuel_tank_alternative = models.IntegerField(_('Fuel Tank - Alternative Fuel'), choices=NUMBER_CHOICES, default=0, )
    _def = models.IntegerField(_('DEF'), choices=NUMBER_CHOICES, default=0, )
    battery_box = models.IntegerField(_('Battery Box'), choices=NUMBER_CHOICES, default=0, )
    # deck_plate = models.IntegerField(_('Deck Plate'), choices=NUMBER_CHOICES, default=0, )
    # air_lines_lights_cord_spring = models.IntegerField(_('Air Lines, Light Cord, Spring'),
    #                                                    choices=NUMBER_CHOICES, default=0, )
    frame = models.IntegerField(_('Frame'), choices=NUMBER_CHOICES, default=0, )
    # fifth_wheel = models.IntegerField(_('5th Wheel'), choices=NUMBER_CHOICES, default=0, )
    mud_flaps = models.IntegerField(_('Mud Flaps'), choices=NUMBER_CHOICES, default=0, )
    drive_line = models.IntegerField(_('Drive Line'), choices=NUMBER_CHOICES, default=0, )
    air_cans_or_lines = models.IntegerField(_('Air Cans/Lines'), choices=NUMBER_CHOICES, default=0, )
    brake_chambers_or_slack_adj = models.IntegerField(_('Brake Chambers/Slack Adj'), choices=NUMBER_CHOICES,
                                                      default=0, )
    suspension = models.IntegerField(_('Suspension'), choices=NUMBER_CHOICES, default=0, )
    brake_drums_and_lining = models.IntegerField(_('Brake Drums & Lining'), choices=NUMBER_CHOICES, default=0, )
    tire_inflation = models.IntegerField(_('Tire Inflation'), choices=NUMBER_CHOICES, default=0, )
    tire_and_rim_condition = models.IntegerField(_('Tire & Rim Condition - Space'), choices=NUMBER_CHOICES, default=0, )
    valve_stem_and_hub_oil = models.IntegerField(_('Valve Stem & Hub Oil'), choices=NUMBER_CHOICES, default=0, )
    body_condition = models.IntegerField(_('Body Condition'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(default="", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Pre Trip Both Sides Vehicles Class B"
        verbose_name_plural = "Pre Trip Both Sides Vehicles Class B List"


# 6. Pre Trip Vehicle/TractorRear Class B
class PreTripVehicleOrTractorRearClassB(PreTripClassMixin, models.Model):
    # relation
    pre_trip_class_b = models.OneToOneField('safe_driver.PreTripClassB', on_delete=models.CASCADE, null=False,
                                            related_name='pretrip_vehicle_or_tractor_rear_class_b')

    brake_and_others = models.IntegerField(_('Brake, Tail, 4way, Signal Lights'), choices=NUMBER_CHOICES, default=0, )
    body_condition = models.IntegerField(_('Body Condition'), choices=NUMBER_CHOICES, default=0, )
    reflectors_and_work_light = models.IntegerField(_('Reflectors & Work Light'), choices=NUMBER_CHOICES, default=0, )
    mud_flaps = models.IntegerField(_('Mud Flaps'), choices=NUMBER_CHOICES, default=0, )
    couple_devices = models.IntegerField(_('Couple Devices'), choices=NUMBER_CHOICES, default=0, )
    license_plate_and_light = models.IntegerField(_('Licenses Plate & Light'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(default="", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Pre Trip Vehicle/TractorRear Class B"
        verbose_name_plural = "Pre Trip Vehicle/TractorRear Class B List"


# 7. Pre Trip Box - Header Board Class B
class PreTripBoxHeaderBoardClassB(PreTripClassMixin, models.Model):
    # relation
    pre_trip_class_b = models.OneToOneField('safe_driver.PreTripClassB', on_delete=models.CASCADE, null=False,
                                            related_name='pretrip_box_header_board_class_b')

    verfiy_header_board_condition = models.IntegerField(_('Verify Header Board Condition'),
                                                        choices=NUMBER_CHOICES, default=0, )
    verify_vehicle_height = models.IntegerField(_('Verify Vehicle Height'), choices=NUMBER_CHOICES, default=0, )
    clearance_lights = models.IntegerField(_('Clearance Lights'), choices=NUMBER_CHOICES, default=0, )
    reflectors = models.IntegerField(_('Reflectors'), choices=NUMBER_CHOICES, default=0, )
    refrigeration_system = models.IntegerField(_('Refrigeration System'), choices=NUMBER_CHOICES, default=0, )
    utility_box = models.IntegerField(_('Utility Box'), choices=NUMBER_CHOICES, default=0, )
    equipement_number_and_markings = models.IntegerField(_('Equipment Number and Markings'),
                                                         choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(default="", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Pre Trip Box Header Board Class B"
        verbose_name_plural = "Pre Trip Box Header Board Class B List"


# 8. Pre Trip Driver Side Trailer Box Class B
class PreTripDriverSideBoxClassB(PreTripClassMixin, models.Model):
    # relation
    pre_trip_class_b = models.OneToOneField('safe_driver.PreTripClassB', on_delete=models.CASCADE, null=False,
                                            related_name='pretrip_driver_side_box_class_b')

    condition = models.IntegerField(_('Condition'), choices=NUMBER_CHOICES, default=0, )
    reflectors = models.IntegerField(_('Reflectors'), choices=NUMBER_CHOICES, default=0, )
    marker_lights = models.IntegerField(_('Marker Lights'), choices=NUMBER_CHOICES, default=0, )
    frame_and_chassis = models.IntegerField(_('Frame & Chassis'), choices=NUMBER_CHOICES, default=0, )
    air_cans = models.IntegerField(_('Air Cans'), choices=NUMBER_CHOICES, default=0, )
    brake_chambers_or_slack_adj = models.IntegerField(_('Brake Chambers/Slack Adj'), choices=NUMBER_CHOICES,
                                                      default=0, )
    axel = models.IntegerField(_('Axel'), choices=NUMBER_CHOICES, default=0, )
    suspension = models.IntegerField(_('Suspension'), choices=NUMBER_CHOICES, default=0, )
    brake_drums_and_lining = models.IntegerField(_('Brake Drums & Lining'), choices=NUMBER_CHOICES, default=0, )
    tire_inflation = models.IntegerField(_('Tire Inflation'), choices=NUMBER_CHOICES, default=0, )
    tire_and_rim_condition = models.IntegerField(_('Tire & Rim Condition - Spacer'), choices=NUMBER_CHOICES,
                                                 default=0, )
    valve_stem_and_hub_oil = models.IntegerField(_('Valve Stem & Hub Oil'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(default="", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Driver Side Trailer Box Class B"
        verbose_name_plural = "Driver Side Trailer Box Class B List"


# 9. Pre Trip Cargo Area Class B
class PreTripCargoAreaClassB(PreTripClassMixin, models.Model):
    # relation
    pre_trip_class_b = models.OneToOneField('safe_driver.PreTripClassB', on_delete=models.CASCADE, null=False,
                                            related_name='pretrip_cargo_area_class_b')

    all_cargo_door = models.IntegerField(_('All Cargo Door'), choices=NUMBER_CHOICES, default=0, )
    cargo_load_area = models.IntegerField(_('Cargo, Load, Area'), choices=NUMBER_CHOICES, default=0, )
    all_securing_devices = models.IntegerField(_('All Securing Devices'), choices=NUMBER_CHOICES, default=0, )
    barn_doors_or_rollup = models.IntegerField(_('Barn Doors or Roll Up Door'), choices=NUMBER_CHOICES,
                                               default=0, )
    door_locking_devices = models.IntegerField(_('Door Locking Devices'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(default="", null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Pre TripCargo Area Class B"
        verbose_name_plural = "Pre Trip Cargo Area Class B"


# 10. Pre Trip Passenger Side Box Class B
class PreTripPassengerSideBoxClassB(PreTripClassMixin, models.Model):
    # relation
    pre_trip_class_b = models.OneToOneField('safe_driver.PreTripClassB', on_delete=models.CASCADE, null=False,
                                            related_name='pretrip_passenger_side_box_class_b')

    condition = models.IntegerField(_('Condition'), choices=NUMBER_CHOICES, default=0, )
    reflectors = models.IntegerField(_('Reflectors'), choices=NUMBER_CHOICES, default=0, )
    marker_lights = models.IntegerField(_('Marker Lights'), choices=NUMBER_CHOICES, default=0, )
    coupling = models.IntegerField(_('Coupling'), choices=NUMBER_CHOICES, default=0, )
    frame_and_chassis = models.IntegerField(_('Frame & Chassis'), choices=NUMBER_CHOICES, default=0, )
    landing_gear = models.IntegerField(_('Landing Gear'), choices=NUMBER_CHOICES, default=0, )
    air_cans = models.IntegerField(_('Air Cans'), choices=NUMBER_CHOICES, default=0, )
    brake_chambers_or_slack_adj = models.IntegerField(_('Brake Chambers/Slack Adj'), choices=NUMBER_CHOICES,
                                                      default=0, )
    axel = models.IntegerField(_('Axel'), choices=NUMBER_CHOICES, default=0, )
    suspension = models.IntegerField(_('Suspension'), choices=NUMBER_CHOICES, default=0, )
    brake_drums_and_lining = models.IntegerField(_('Brake Drums & Lining'), choices=NUMBER_CHOICES, default=0, )
    tire_inflation = models.IntegerField(_('Tire Inflation'), choices=NUMBER_CHOICES, default=0, )
    tire_and_rim_condition = models.IntegerField(_('Tire & Rim Condition - Space'), choices=NUMBER_CHOICES, default=0, )
    valve_stem_and_hub_oil = models.IntegerField(_('Valve Stem & Hub Oil'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(default="", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Pre Trip Passenger Side Box Class B"
        verbose_name_plural = "Pre Trip Passenger Side Box Class B"


# 11. Pre Trip Dolly Class B (skipped and not required in Class B)
# 12. Pre Trip PostTrip Class B
class PreTripPostTripClassB(PreTripClassMixin, models.Model):
    # relation
    pre_trip_class_b = models.OneToOneField('safe_driver.PreTripClassB', on_delete=models.CASCADE, null=False,
                                            related_name='pretrip_posttrip_class_b')

    condition = models.IntegerField(_('Condition'), choices=NUMBER_CHOICES, default=0, )
    all_lights = models.IntegerField(_('All Lights'), choices=NUMBER_CHOICES, default=0, )
    tire_condition = models.IntegerField(_('Tire Condition'), choices=NUMBER_CHOICES, default=0, )
    tire_inflation = models.IntegerField(_('Tire Inflation'), choices=NUMBER_CHOICES, default=0, )
    hub_heat = models.IntegerField(_('Hub Heat'), choices=NUMBER_CHOICES, default=0, )
    reflective_devices = models.IntegerField(_('Reflective Devices'), choices=NUMBER_CHOICES, default=0, )
    fluid_air_leaks = models.IntegerField(_('Fluid & Air Leaks'), choices=NUMBER_CHOICES, default=0, )
    equipment_parked_secure = models.IntegerField(_('Equipement Parked - Secure'), choices=NUMBER_CHOICES, default=0, )
    avoid_shifting_lead = models.IntegerField(_('Avoid Shifting Lead'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(default="", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Pre Trip PostTrip Class B"
        verbose_name_plural = "Pre Trip PostTrip Class B"
