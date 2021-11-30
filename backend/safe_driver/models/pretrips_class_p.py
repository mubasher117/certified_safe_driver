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


# Pre Trip Class P
class PreTripClassP(models.Model):
    test = models.OneToOneField('safe_driver.StudentTest', on_delete=models.CASCADE, null=False,
                                related_name='pretrip_student_test_class_p')
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
        verbose_name = "Pre Trip Class P"
        verbose_name_plural = "Pre Trips Class P"


# 1. Pre Trip Inside Cab Class P
class PreTripInsideCabClassP(PreTripClassMixin, models.Model):
    # relation
    pre_trip_class_p = models.OneToOneField('safe_driver.PreTripClassP', on_delete=models.CASCADE, null=False,
                                            related_name='pretrip_insidecab_class_p')
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
    cab_or_berth = models.IntegerField(_('Cab/Berth'), choices=NUMBER_CHOICES, default=0, )
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
    stadee_line_clear = models.IntegerField(_('Stadee Line Clear'), choices=NUMBER_CHOICES, default=0, )
    # splitter = models.IntegerField(_('Splitter'), choices=NUMBER_CHOICES, default=0, )
    clear_floor_board = models.IntegerField(_('Clear floor Board'), choices=NUMBER_CHOICES, default=0, )
    pedals = models.IntegerField(_('Pedals'), choices=NUMBER_CHOICES, default=0, )
    park_brake_test = models.IntegerField(_('Park Brake Test'), choices=NUMBER_CHOICES, default=0, )
    service_brake_test = models.IntegerField(_('Service Brake Test'), choices=NUMBER_CHOICES, default=0, )
    trailer_brake_test = models.IntegerField(_('Trailer Brake Test'), choices=NUMBER_CHOICES, default=0, )
    pull_key = models.IntegerField(_('Pull Key'), choices=NUMBER_CHOICES, default=0, )
    exit_safely = models.IntegerField(_('Exit Safely'), choices=NUMBER_CHOICES, default=0, )
    steps = models.IntegerField(_('Steps'), choices=NUMBER_CHOICES, default=0, )
    door_entry_clear = models.IntegerField(_('Door Entry Clear'), choices=NUMBER_CHOICES, default=0, )
    step_lights = models.IntegerField(_('Step Lights'), choices=NUMBER_CHOICES, default=0, )
    emergency_exits_marked_acc = models.IntegerField(_('Emergency Exits Marked Acc'), choices=NUMBER_CHOICES,
                                                     default=0, )

    notes = models.TextField(default="", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Pre Trip Inside Cab Class P"
        verbose_name_plural = "Pre Trip Inside Cab Class P List"


# 2. Pre Trip COALS Class P
class PreTripCOALSClassP(PreTripClassMixin, models.Model):
    # relation
    pre_trip_class_p = models.OneToOneField('safe_driver.PreTripClassP', on_delete=models.CASCADE, null=False,
                                            related_name='pretrip_coals_class_p')

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
        verbose_name = "Pre Trip COALS Class P"
        verbose_name_plural = "Pre Trip COALS Class P List"


# 3. Pre Trip Engine Compartment Class P
class PreTripEngineCompartmentClassP(PreTripClassMixin, models.Model):
    # relation
    pre_trip_class_p = models.OneToOneField('safe_driver.PreTripClassP', on_delete=models.CASCADE, null=False,
                                            related_name='pretrip_engine_compartment_class_p')

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
        verbose_name = "Pre Trip Engine Compartment Class P"
        verbose_name_plural = "Pre Trip Engine Compartment Class P List"


# 4. Pre Trip Vehicle Front Class P
class PreTripVehicleFrontClassP(PreTripClassMixin, models.Model):
    # relation
    pre_trip_class_p = models.OneToOneField('safe_driver.PreTripClassP', on_delete=models.CASCADE, null=False,
                                            related_name='pretrip_vehicle_front_class_p')

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
        verbose_name = "Pre Trip Vehicle Front Class P"
        verbose_name_plural = "Pre Trip Vehicle Front Class P List"


# 5. Pre Trip Both Sides Vehicles Class P
class PreTripBothSidesVehiclesClassP(PreTripClassMixin, models.Model):
    # relation
    pre_trip_class_p = models.OneToOneField('safe_driver.PreTripClassP', on_delete=models.CASCADE, null=False,
                                            related_name='pretrip_both_sides_vehicle_class_p')

    mirrors = models.IntegerField(_('Mirrors'), choices=NUMBER_CHOICES, default=0, )
    vehicle_markings_or_decals = models.IntegerField(_('Vehicle Markings/Decals'), choices=NUMBER_CHOICES, default=0, )
    dots = models.IntegerField(_('DOT’s, CA, MC #’s'), choices=NUMBER_CHOICES, default=0, )
    ifta_permit = models.IntegerField(_('IFTA Permit'), choices=NUMBER_CHOICES, default=0, )
    air_tanks = models.IntegerField(_('Air Tanks'), choices=NUMBER_CHOICES, default=0, )
    fuel_tank_alternative = models.IntegerField(_('Fuel Tank - Alternative Fuel'), choices=NUMBER_CHOICES, default=0, )
    _def = models.IntegerField(_('DEF'), choices=NUMBER_CHOICES, default=0, )
    battery_box = models.IntegerField(_('Battery Box'), choices=NUMBER_CHOICES, default=0, )
    cargo_compartment_door = models.IntegerField(_('Cargo Compartment Door'), choices=NUMBER_CHOICES, default=0, )
    engine_doors = models.IntegerField(_('Engine Doors'), choices=NUMBER_CHOICES, default=0, )
    frame = models.IntegerField(_('Frame'), choices=NUMBER_CHOICES, default=0, )
    side_flectors = models.IntegerField(_('Side Flectors'), choices=NUMBER_CHOICES, default=0, )
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
    windows = models.IntegerField(_('Windows'), choices=NUMBER_CHOICES, default=0, )
    stop_arm = models.IntegerField(_('Stop Arm'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(default="", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Pre Trip Both Sides Vehicles Class P"
        verbose_name_plural = "Pre Trip Both Sides Vehicles Class P List"


# 6. Pre Trip Rear Of Vehicle Class P
class PreTripRearOfVehicleClassP(PreTripClassMixin, models.Model):
    # relation
    pre_trip_class_p = models.OneToOneField('safe_driver.PreTripClassP', on_delete=models.CASCADE, null=False,
                                            related_name='pretrip_rear_of_vehicle_class_p')

    brake_and_others = models.IntegerField(_('Brake, Tail, 4way, Signal Lights'), choices=NUMBER_CHOICES, default=0, )
    body_condition = models.IntegerField(_('Body Condition'), choices=NUMBER_CHOICES, default=0, )
    reflectors = models.IntegerField(_('Reflectors'), choices=NUMBER_CHOICES, default=0, )
    mud_flaps = models.IntegerField(_('Mud Flaps'), choices=NUMBER_CHOICES, default=0, )
    license_plate_and_light = models.IntegerField(_('Licenses Plate & Light'), choices=NUMBER_CHOICES, default=0, )
    bumper = models.IntegerField(_('Bumper'), choices=NUMBER_CHOICES, default=0, )
    engine_door = models.IntegerField(_('Engine Door'), choices=NUMBER_CHOICES, default=0, )
    tail_pipe = models.IntegerField(_('Tail Pipe'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(default="", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Pre Trip Rear or Vehicle Class P"
        verbose_name_plural = "Pre Trip Rear or Vehicle Class P List"


# 7. Cargo Area Class P
class PreTripCargoAreaClassP(PreTripClassMixin, models.Model):
    # relation
    pre_trip_class_p = models.OneToOneField('safe_driver.PreTripClassP', on_delete=models.CASCADE, null=False,
                                            related_name='pretrip_cargo_area_class_p')
    all_cargo_door = models.IntegerField(_('All Cargo Door'), choices=NUMBER_CHOICES, default=0, )
    cargo_load_area = models.IntegerField(_('Cargo, Load, Area'), choices=NUMBER_CHOICES, default=0, )
    all_securing_devices = models.IntegerField(_('All Securing Devices'), choices=NUMBER_CHOICES, default=0, )
    cargo_doors_hinges = models.IntegerField(_('Card Doors Hinges'), choices=NUMBER_CHOICES, default=0, )
    door_locking_devices = models.IntegerField(_('Door Locking Devices'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(default="", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Pre Trip Cargo Area Class P"
        verbose_name_plural = "Pre Trip Cargo Area Class P List"


# 8. Ramp Class P
class PreTripRampClassP(PreTripClassMixin, models.Model):
    # relation
    pre_trip_class_p = models.OneToOneField('safe_driver.PreTripClassP', on_delete=models.CASCADE, null=False,
                                            related_name='pretrip_ramp_class_p')

    power_lift = models.IntegerField(_('Power Lift'), choices=NUMBER_CHOICES, default=0, )
    lift_door = models.IntegerField(_('Lift Door'), choices=NUMBER_CHOICES, default=0, )
    buzzer = models.IntegerField(_('Buzzer'), choices=NUMBER_CHOICES, default=0, )
    interlock = models.IntegerField(_('Interlock'), choices=NUMBER_CHOICES, default=0, )
    identification = models.IntegerField(_('Identification'), choices=NUMBER_CHOICES, default=0, )
    lights = models.IntegerField(_('Lights'), choices=NUMBER_CHOICES, default=0, )
    fluid_and_air_leaks = models.IntegerField(_('Fluid & Air Leaks'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(default="", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Pre Trip Ramp Class P"
        verbose_name_plural = "Pre Trip Ramp Class P List"


# 9. Interior Operations Class P
class PreTripInteriorOperationClassP(PreTripClassMixin, models.Model):
    # relation
    pre_trip_class_p = models.OneToOneField('safe_driver.PreTripClassP', on_delete=models.CASCADE, null=False,
                                            related_name='pretrip_interior_operation_class_p')

    interior_damage = models.IntegerField(_('Interior Damage'), choices=NUMBER_CHOICES, default=0, )
    interior_cleanlines = models.IntegerField(_('Interior Cleanliness'), choices=NUMBER_CHOICES, default=0, )
    first_aid_kit = models.IntegerField(_('First Aid Kit (If Applicable)'), choices=NUMBER_CHOICES, default=0, )
    emergency_door_buzzer = models.IntegerField(_('Emergency Door Buzzer'), choices=NUMBER_CHOICES, default=0, )
    seat_belt_cutter = models.IntegerField(_('Seat Belt Cutter'), choices=NUMBER_CHOICES, default=0, )
    seats = models.IntegerField(_('Seats'), choices=NUMBER_CHOICES, default=0, )
    hand_rails = models.IntegerField(_('Hand Rails'), choices=NUMBER_CHOICES, default=0, )
    stop_arm_control = models.IntegerField(_('Stop Arm Control (if applicable)'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(default="", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Pre Trip Interior Operations Class P"
        verbose_name_plural = "Pre Trip Interior Operations Class P List"


# 10. Pre Trip Handy Cap Class P
class PreTripHandyCapClassP(PreTripClassMixin, models.Model):
    # relation
    pre_trip_class_p = models.OneToOneField('safe_driver.PreTripClassP', on_delete=models.CASCADE, null=False,
                                            related_name='pretrip_handycap_class_p')

    power_lift = models.IntegerField(_('Power Lift'), choices=NUMBER_CHOICES, default=0, )
    lift_door = models.IntegerField(_('Lift Door'), choices=NUMBER_CHOICES, default=0, )
    buzzer = models.IntegerField(_('Buzzer'), choices=NUMBER_CHOICES, default=0, )
    interlock = models.IntegerField(_('Interlock'), choices=NUMBER_CHOICES, default=0, )
    indentification = models.IntegerField(_('Identification'), choices=NUMBER_CHOICES, default=0, )
    federal_inspection_or_bit = models.IntegerField(_('Federal Inspection or BIT'), choices=NUMBER_CHOICES, default=0, )
    lights = models.IntegerField(_('Lights'), choices=NUMBER_CHOICES, default=0, )
    fluid_and_air_leaks = models.IntegerField(_('Fluid & Air Leaks'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(default="", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Pre Trip Front or Trailer - Header Board Class P"
        verbose_name_plural = "Pre Trip Front or Trailer - Header Board Class P List"


# 11. Pre Trip PostTrip Class P
class PreTripPostTripClassP(PreTripClassMixin, models.Model):
    # relation
    pre_trip_class_p = models.OneToOneField('safe_driver.PreTripClassP', on_delete=models.CASCADE, null=False,
                                            related_name='pretrip_posttrip_class_p')

    condition = models.IntegerField(_('Vehicle Condition'), choices=NUMBER_CHOICES, default=0, )
    all_lights = models.IntegerField(_('All Lights'), choices=NUMBER_CHOICES, default=0, )
    tire_condition = models.IntegerField(_('Tire Condition'), choices=NUMBER_CHOICES, default=0, )
    tire_inflation = models.IntegerField(_('Tire Inflation'), choices=NUMBER_CHOICES, default=0, )
    hub_heat = models.IntegerField(_('Hub Heat'), choices=NUMBER_CHOICES, default=0, )
    reflective_devices = models.IntegerField(_('Reflective Devices'), choices=NUMBER_CHOICES, default=0, )
    fluid_air_leaks = models.IntegerField(_('Fluid & Air Leaks'), choices=NUMBER_CHOICES, default=0, )
    equipment_parked_secure = models.IntegerField(_('Equipement Parked - Secure'), choices=NUMBER_CHOICES, default=0, )
    inerior_clear_and_clean = models.IntegerField(_('Interior Clear & Clean'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(default="", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Pre Trip PostTrip Class P"
        verbose_name_plural = "Pre Trip PostTrip Class P"
