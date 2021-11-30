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


# Pre Trip Class C
class PreTripClassC(models.Model):
    # student = models.OneToOneField('users.User', on_delete=models.CASCADE,
    #                                related_name='pretrip_student_class_c', null=False)
    test = models.OneToOneField('safe_driver.StudentTest', on_delete=models.CASCADE, null=False,
                                related_name='pretrip_student_test_class_c')
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
        verbose_name = "Pre Trip Class C"
        verbose_name_plural = "Pre Trips Class C"


# 1. Pre Trip Inside Cab Class C
class PreTripInsideCabClassC(PreTripClassMixin, models.Model):
    # relation
    pre_trip_class_c = models.OneToOneField('safe_driver.PreTripClassC', on_delete=models.CASCADE, null=False,
                                            related_name='pretrip_insidecab_class_c')
    hand_rails = models.IntegerField(_('Hand Rails'), choices=NUMBER_CHOICES, default=0, )
    fire_extinguisher = models.IntegerField(_('Fire Extinguisher'), choices=NUMBER_CHOICES, default=0, )
    emergency_response_book = models.IntegerField(_('Emergency Response Book'), choices=NUMBER_CHOICES, default=0, )
    dvir = models.IntegerField(_('DVIR'), choices=NUMBER_CHOICES, default=0, )
    parking_brake_applied = models.IntegerField(_('Parking Brake Applied'), choices=NUMBER_CHOICES, default=0, )
    transmission_neutral_or_park = models.IntegerField(_('Transmission Neutral/Park'), choices=NUMBER_CHOICES,
                                                       default=0, )
    seat_adjustment = models.IntegerField(_('Seat Adjustment'), choices=NUMBER_CHOICES, default=0, )
    seat_belt = models.IntegerField(_('Seat Belt'), choices=NUMBER_CHOICES, default=0, )
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
    clear_floor_board = models.IntegerField(_('Clear floor Board'), choices=NUMBER_CHOICES, default=0, )
    pedals = models.IntegerField(_('Pedals'), choices=NUMBER_CHOICES, default=0, )
    park_brake_test = models.IntegerField(_('Park Brake Test'), choices=NUMBER_CHOICES, default=0, )
    service_brake_test = models.IntegerField(_('Service Brake Test'), choices=NUMBER_CHOICES, default=0, )
    pull_key = models.IntegerField(_('Pull Key'), choices=NUMBER_CHOICES, default=0, )
    exit_safely = models.IntegerField(_('Exit Safely'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(default="", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Pre Trip Inside Cab Class C"
        verbose_name_plural = "Pre Trip Inside Cab Class C List"


# Pre Trip COALS Class C (No COALS for Class C)
# 2. Pre Trip Engine Compartment Class C
class PreTripEngineCompartmentClassC(PreTripClassMixin, models.Model):
    # relation
    pre_trip_class_c = models.OneToOneField('safe_driver.PreTripClassC', on_delete=models.CASCADE, null=False,
                                            related_name='pretrip_engine_compartment_class_c')

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
        verbose_name = "Pre Trip Engine Compartment Class C"
        verbose_name_plural = "Pre Trip Engine Compartment Class C List"


# 3. Pre Trip Vehicle Front Class C
class PreTripVehicleFrontClassC(PreTripClassMixin, models.Model):
    # relation
    pre_trip_class_c = models.OneToOneField('safe_driver.PreTripClassC', on_delete=models.CASCADE, null=False,
                                            related_name='pretrip_vehicle_front_class_c')

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
        verbose_name = "Pre Trip Vehicle Front Class C"
        verbose_name_plural = "Pre Trip Vehicle Front Class C List"


# 4. Pre Trip Both Sides Vehicles Class C
class PreTripBothSidesVehiclesClassC(PreTripClassMixin, models.Model):
    # relation
    pre_trip_class_c = models.OneToOneField('safe_driver.PreTripClassC', on_delete=models.CASCADE, null=False,
                                            related_name='pretrip_both_sides_vehicle_class_c')

    verify_vehicle_height = models.IntegerField(_('Verify Vehicle Height'), choices=NUMBER_CHOICES, default=0, )
    clearance_lights = models.IntegerField(_('Clearance Lights'), choices=NUMBER_CHOICES, default=0, )
    equipment_number_and_markings = models.IntegerField(_('Equipment Number & Markings'),
                                                        choices=NUMBER_CHOICES, default=0, )
    mirrors = models.IntegerField(_('Mirrors'), choices=NUMBER_CHOICES, default=0, )
    fuel_tank_alternative = models.IntegerField(_('Fuel Tank - Alternative Fuel'), choices=NUMBER_CHOICES, default=0, )
    frame = models.IntegerField(_('Frame'), choices=NUMBER_CHOICES, default=0, )
    mud_flaps = models.IntegerField(_('Mud Flaps'), choices=NUMBER_CHOICES, default=0, )
    drive_line = models.IntegerField(_('Drive Line'), choices=NUMBER_CHOICES, default=0, )
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
        verbose_name = "Pre Trip Both Sides Vehicles Class C"
        verbose_name_plural = "Pre Trip Both Sides Vehicles Class C List"


# 5. Pre Trip Vehicle Rear Class C
class PreTripVehicleRearClassC(PreTripClassMixin, models.Model):
    # relation
    pre_trip_class_c = models.OneToOneField('safe_driver.PreTripClassC', on_delete=models.CASCADE, null=False,
                                            related_name='pretrip_vehicle_rear_class_c')

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
        verbose_name = "Pre Trip Vehicle Rear Class C"
        verbose_name_plural = "Pre Trip Vehicle Rear Class C List"


# 6. Pre Trip Cargo Area Class C
class PreTripCargoAreaClassC(PreTripClassMixin, models.Model):
    # relation
    pre_trip_class_c = models.OneToOneField('safe_driver.PreTripClassC', on_delete=models.CASCADE, null=False,
                                            related_name='pretrip_cargo_area_class_c')

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


# 7. Pre Trip PostTrip Class C
class PreTripPostTripClassC(PreTripClassMixin, models.Model):
    # relation
    pre_trip_class_c = models.OneToOneField('safe_driver.PreTripClassC', on_delete=models.CASCADE, null=False,
                                            related_name='pretrip_posttrip_class_c')

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
        verbose_name = "Pre Trip PostTrip Class C"
        verbose_name_plural = "Pre Trip PostTrip Class C"
