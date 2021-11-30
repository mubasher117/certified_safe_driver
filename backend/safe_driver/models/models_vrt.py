from django.db import models
from django.utils.translation import ugettext_lazy as _

from safe_driver.image_functions import signature_image_folder
from safe_driver.utils import VRTPointMixin

VRT_NUMBER_CHOICES = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (0, "N/A"),
)

VRT_CHOICES = (
    (0, 'N/A'),
    (1, 'Imp'),
    (2, 'Ok'),
)


# VRT
class VehicleRoadTest(models.Model):
    # student = models.OneToOneField('users.User', on_delete=models.CASCADE, related_name='vrt_student',
    #                                null=False)
    test = models.OneToOneField('safe_driver.StudentTest', on_delete=models.CASCADE, null=False,
                                related_name='vrt_student_test')
    qualified = models.BooleanField(_('Qualified'), default=False)
    date = models.DateField(_('Date'), default=None, null=True, blank=True)
    start_time = models.TimeField(_('Start Time'), null=True, blank=True, default=None, )
    end_time = models.TimeField(_('End Time'), null=True, blank=True, default=None)
    equiment_used = models.CharField(_('Equipment'), default=None, max_length=120, null=True, blank=True)

    remarks = models.TextField(_('Remarks'), default=None, null=True, blank=True)

    medical_card_expire_date = models.DateField(_('Medical Card Expiration Date'), default=None, null=True, blank=True)
    state = models.CharField(_('State'), default=None, max_length=120, null=True, blank=True)

    type_of_power_unit = models.CharField(_('Type of Power Unit'), default=None, max_length=120, null=True, blank=True)
    trailer_length = models.CharField(_('Trailer Unit'), max_length=120, null=True, blank=True)
    number_of_trailers = models.IntegerField(_('Number of Trailers'), default=None, null=True, blank=True)
    miles = models.DecimalField(_('Miles'), max_digits=6, decimal_places=2, default=None, null=True, blank=True)

    driver_signature = models.ImageField(_('Driver Signature'), upload_to=signature_image_folder, default=None,
                                         null=True, blank=True)
    evaluator_signature = models.ImageField(_('Evaluator Signature'), upload_to=signature_image_folder,
                                            default=None, null=True,
                                            blank=True)

    company_rep_signature = models.ImageField(_('Company Rep Signature'), upload_to=signature_image_folder,
                                              default=None, null=True,
                                              blank=True)

    print = models.CharField(_('Print'), default=None, max_length=120, null=True, blank=True)
    title = models.CharField(_('Title'), default=None, max_length=250, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "Vehicle Road Test"


# 1. VRT Pre Trip
class VRTPreTrip(models.Model):
    vrt = models.OneToOneField('safe_driver.VehicleRoadTest', on_delete=models.CASCADE, null=False)

    emergency_device = models.IntegerField(_('Emergency Device'), choices=VRT_CHOICES, default=1, )
    documents = models.IntegerField(_('Documents'), choices=VRT_CHOICES, default=1, )
    htr_air_dfr = models.IntegerField(_('Htr/Air/Dfr'), choices=VRT_CHOICES, default=1, )
    wipers = models.IntegerField(_('Wipers'), choices=VRT_CHOICES, default=1, )
    pedals = models.IntegerField(_('Pedals'), choices=VRT_CHOICES, default=1, )
    gauges = models.IntegerField(_('Gauges'), choices=VRT_CHOICES, default=1, )
    switches = models.IntegerField(_('Switches'), choices=VRT_CHOICES, default=1, )
    steering = models.IntegerField(_('Steering'), choices=VRT_CHOICES, default=1, )
    mirrors = models.IntegerField(_('Mirrors'), choices=VRT_CHOICES, default=1, )
    horn = models.IntegerField(_('Horn'), choices=VRT_CHOICES, default=1, )
    engine = models.IntegerField(_('Engine'), choices=VRT_CHOICES, default=1, )
    fluids = models.IntegerField(_('Fluids'), choices=VRT_CHOICES, default=1, )
    lights = models.IntegerField(_('Lights'), choices=VRT_CHOICES, default=1, )
    reflectors = models.IntegerField(_('Reflectors'), choices=VRT_CHOICES, default=1, )
    air_lines = models.IntegerField(_('Air Lines'), choices=VRT_CHOICES, default=1, )
    coupling_devices = models.IntegerField(_('Coupling Devices'), choices=VRT_CHOICES, default=1, )
    tires = models.IntegerField(_('Tires'), choices=VRT_CHOICES, default=1, )
    wheels = models.IntegerField(_('Wheels'), choices=VRT_CHOICES, default=1, )
    chassis_undercarriage = models.IntegerField(_('Chassis Undercarriage'), choices=VRT_CHOICES, default=1, )
    leaks_air_fluid = models.IntegerField(_('Leaks/Air/Fluid'), choices=VRT_CHOICES, default=1, )
    drain_air_tanks = models.IntegerField(_('Drain Air Tanks'), choices=VRT_CHOICES, default=1, )
    park_or_emer_brake = models.IntegerField(_('Park/Emer Brake'), choices=VRT_CHOICES, default=1, )
    serv_brake_test = models.IntegerField(_('Serv Brake Test'), choices=VRT_NUMBER_CHOICES, default=1, )
    score = models.IntegerField(_('Score'), choices=VRT_NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), default=None, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    @property
    def possible_points(self):
        if self.score > 0:
            return 4 * 2
        return 0

    @property
    def points_received(self):
        if self.score:
            return self.score * 2
        return 0

    class Meta:
        ordering = ('-created',)
        verbose_name = "VRT - Pre Trip"


# 2. VRT Coupling
class VRTCoupling(VRTPointMixin, models.Model):
    vrt = models.OneToOneField('safe_driver.VehicleRoadTest', on_delete=models.CASCADE, null=False)

    equipment_alignment = models.IntegerField(_('Equipment Alignment'), choices=VRT_CHOICES, default=1, )
    air_lines_or_light_cord = models.IntegerField(_('Air Lines/Light Cord'), choices=VRT_CHOICES, default=1, )
    check_for_hazards = models.IntegerField(_('Check for Hazards'), choices=VRT_CHOICES, default=1, )
    back_under_slowly = models.IntegerField(_('Back Under Slowly'), choices=VRT_CHOICES, default=1, )
    test_tug = models.IntegerField(_('Test Tug'), choices=VRT_CHOICES, default=1, )
    secures_equip_properly = models.IntegerField(_('Secures Equip Properly'), choices=VRT_CHOICES, default=1, )
    verfiy_couple_secure = models.IntegerField(_('Verify Couple Secure'), choices=VRT_CHOICES, default=1, )

    raise_landing_gear = models.IntegerField(_('Raise Landing Gear'), choices=VRT_NUMBER_CHOICES, default=1, )

    score = models.IntegerField(_('Score'), choices=VRT_NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), default=None, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "VRT - Coupling"


# 3. VRT Uncoupling
class VRTUncoupling(VRTPointMixin, models.Model):
    vrt = models.OneToOneField('safe_driver.VehicleRoadTest', on_delete=models.CASCADE, null=False)

    secure_equip_properly = models.IntegerField(_('Secure Equip Properly'), choices=VRT_CHOICES, default=1, )
    chock_wheels = models.IntegerField(_('Chock Wheels'), choices=VRT_CHOICES, default=1, )
    lower_landing_gear = models.IntegerField(_('Lower Landing Gear'), choices=VRT_CHOICES, default=1, )
    air_lanes_or_light_cord = models.IntegerField(_('Air Lines/Light Cord'), choices=VRT_CHOICES, default=1, )
    unlock_fifth_gear = models.IntegerField(_('Unlock 5th Wheel'), choices=VRT_CHOICES, default=1, )
    lower_trailer_gently = models.IntegerField(_('Lower trailer Gently'), choices=VRT_CHOICES, default=1, )
    verify_firm_to_ground = models.IntegerField(_('Verify Firm to Ground'), choices=VRT_CHOICES, default=1, )

    score = models.IntegerField(_('Score'), choices=VRT_NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), default=None, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "VRT - Uncoupling"


# 4. VRT Engine Operations
class VRTEngineOperations(VRTPointMixin, models.Model):
    vrt = models.OneToOneField('safe_driver.VehicleRoadTest', on_delete=models.CASCADE, null=False)

    lugging = models.IntegerField(_('Lugging'), choices=VRT_CHOICES, default=1, )
    over_revving = models.IntegerField(_('Over Revving'), choices=VRT_CHOICES, default=1, )
    check_gauges = models.IntegerField(_('Checks Gauges'), choices=VRT_NUMBER_CHOICES, default=1, )

    score = models.IntegerField(_('Score'), choices=VRT_NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), default=None, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "VRT - Engine Operations"


# 5. VRT Start Engine
class VRTStartEngine(VRTPointMixin, models.Model):
    vrt = models.OneToOneField('safe_driver.VehicleRoadTest', on_delete=models.CASCADE, null=False)

    park_brake_applied = models.IntegerField(_('Park Brake Applied'), choices=VRT_CHOICES, default=1, )
    transmission_in_neutral = models.IntegerField(_('Transmission in Neutral'), choices=VRT_CHOICES, default=1, )
    clutch_depressed = models.IntegerField(_('Clutch Depressed'), choices=VRT_CHOICES, default=1, )
    starter_used_properly = models.IntegerField(_('Starter Used Properly'), choices=VRT_CHOICES, default=1, )
    reads_gauges = models.IntegerField(_('Reads Gauges'), choices=VRT_CHOICES, default=1, )
    seat_belt = models.IntegerField(_('Seat Belt'), choices=VRT_NUMBER_CHOICES, default=1, )

    score = models.IntegerField(_('Score'), choices=VRT_NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), default=None, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "VRT - Start Engine"


# 6. VRT Use Clutch
class VRTUseClutch(VRTPointMixin, models.Model):
    vrt = models.OneToOneField('safe_driver.VehicleRoadTest', on_delete=models.CASCADE, null=False)
    disengages_completely = models.IntegerField(_('Disengages Completely'), choices=VRT_CHOICES, default=1, )
    engages_smoothly = models.IntegerField(_('Engages Smoothly'), choices=VRT_CHOICES, default=1, )
    double_clutches_properly = models.IntegerField(_('Double Clutches Properly'), choices=VRT_CHOICES, default=1, )
    rides_clutch = models.IntegerField(_('Rides Clutch'), choices=VRT_CHOICES, default=1, )

    coast = models.IntegerField(_('Coast'), choices=VRT_NUMBER_CHOICES, default=1, )

    score = models.IntegerField(_('Score'), choices=VRT_NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), default=None, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "VRT - Use Clutch"


# 7. VRT Use of Transmission
class VRTUseOfTransmission(VRTPointMixin, models.Model):
    vrt = models.OneToOneField('safe_driver.VehicleRoadTest', on_delete=models.CASCADE, null=False)

    starts_in_low_gear = models.IntegerField(_('Starts in Low Gear'), choices=VRT_CHOICES, default=1, )
    proper_sequence = models.IntegerField(_('Proper Sequence'), choices=VRT_CHOICES, default=1, )
    shifts_without_classing = models.IntegerField(_('Shifts without classing'), default=1, )
    timing_up = models.IntegerField(_('Timing Up'), choices=VRT_CHOICES, default=1, )
    timing_down = models.IntegerField(_('Timing Down'), choices=VRT_NUMBER_CHOICES, default=1, )

    score = models.IntegerField(_('Score'), choices=VRT_NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), default=None, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "VRT - Use of Transmission"


# 8. VRT Use of Brakes
class VRTUseOfBrakes(VRTPointMixin, models.Model):
    vrt = models.OneToOneField('safe_driver.VehicleRoadTest', on_delete=models.CASCADE, null=False)

    smoothly_applies = models.IntegerField(_('Smoothly Applies'), choices=VRT_CHOICES, default=1, )
    stops_smoothly = models.IntegerField(_('Stops Smoothly'), choices=VRT_CHOICES, default=1, )

    fans_brakes = models.IntegerField(_('Fans Brakes'), choices=VRT_CHOICES, default=1, )
    engine_assist_brake = models.IntegerField(_('Engine Assist Brake'), choices=VRT_CHOICES, default=1, )
    foot_brake_only = models.IntegerField(_('Foot Brake Only'), choices=VRT_CHOICES, default=1, )

    hv_when_stopped_traffic = models.IntegerField(_('H/V when Stopped Traffic'),
                                                  choices=VRT_NUMBER_CHOICES, default=1, )

    score = models.IntegerField(_('Score'), choices=VRT_NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), default=None, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "VRT - Use of Brakes"


# 9. VRT Backing
class VRTBacking(VRTPointMixin, models.Model):
    vrt = models.OneToOneField('safe_driver.VehicleRoadTest', on_delete=models.CASCADE, null=False)

    checks_rear = models.IntegerField(_('Checks Rear'), choices=VRT_CHOICES, default=1, )
    communicates = models.IntegerField(_('Communicates'), choices=VRT_CHOICES, default=1, )
    backs_slowly = models.IntegerField(_('Backs Slowly'), choices=VRT_CHOICES, default=1, )
    checks_mirror = models.IntegerField(_('Checks Mirror'), choices=VRT_CHOICES, default=1, )
    uses_other_aids = models.IntegerField(_('Uses Other Aids'), choices=VRT_CHOICES, default=1, )
    looks_out_window = models.IntegerField(_('Looks Out Window'), choices=VRT_CHOICES, default=1, )
    steers_correctly = models.IntegerField(_('Steers Correctly'), choices=VRT_CHOICES, default=1, )

    does_not_hit_dock = models.IntegerField(_('Doesn’t Hit Dock'), choices=VRT_NUMBER_CHOICES, default=1, )

    score = models.IntegerField(_('Score'), choices=VRT_NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), default=None, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "VRT - Backing"
        verbose_name_plural = "VRT - Backings"


# 10. VRT Parking
class VRTParking(VRTPointMixin, models.Model):
    vrt = models.OneToOneField('safe_driver.VehicleRoadTest', on_delete=models.CASCADE, null=False)

    # does_not_hit_dock = models.IntegerField(_('Doesn’t Hit Dock'), choices=VRT_CHOICES, default=1, )
    does_not_hit_curb = models.IntegerField(_('Doesn’t Hit Curb'), choices=VRT_CHOICES, default=1, )
    curbs_wheel = models.IntegerField(_('Curbs Wheel'), choices=VRT_CHOICES, default=1, )
    chocks_wheel = models.IntegerField(_('Chocks Wheel'), choices=VRT_CHOICES, default=1, )
    parking_brake_applied = models.IntegerField(_('Parking Brake Applied'), choices=VRT_CHOICES, default=1, )
    transmission_neutral = models.IntegerField(_('Transmission Neutral'), choices=VRT_CHOICES, default=1, )

    engine_off_pull_key = models.IntegerField(_('Engine Off - Pull Key'), choices=VRT_NUMBER_CHOICES, default=1, )

    score = models.IntegerField(_('Score'), choices=VRT_NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), default=None, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "VRT - Parking"


# 11. VRT Driving Habits
class VRTDrivingHabits(models.Model):
    vrt = models.OneToOneField('safe_driver.VehicleRoadTest', on_delete=models.CASCADE, null=False)

    trafic_signals = models.IntegerField(_('Traffic Signals'), choices=VRT_CHOICES, default=1, )
    warning_signals = models.IntegerField(_('Warning Signals'), choices=VRT_CHOICES, default=1, )
    use_of_horn = models.IntegerField(_('Use of Horn'), choices=VRT_CHOICES, default=1, )
    steering = models.IntegerField(_('Steering'), choices=VRT_CHOICES, default=1, )
    intersections = models.IntegerField(_('Intersections'), choices=VRT_CHOICES, default=1, )
    use_of_lanes = models.IntegerField(_('Use of Lanes'), choices=VRT_CHOICES, default=1, )
    right_of_way = models.IntegerField(_('Right of Way'), choices=VRT_CHOICES, default=1, )
    following = models.IntegerField(_('Following'), choices=VRT_CHOICES, default=1, )
    right_of_turns = models.IntegerField(_('Right Turns'), choices=VRT_CHOICES, default=1, )
    left_turns = models.IntegerField(_('Left Turns'), choices=VRT_CHOICES, default=1, )
    speed_control = models.IntegerField(_('Speed Control'), choices=VRT_CHOICES, default=1, )
    use_of_mirrors = models.IntegerField(_('Use of Mirrors'), choices=VRT_CHOICES, default=1, )
    passing = models.IntegerField(_('Passing'), choices=VRT_CHOICES, default=1, )
    alertness = models.IntegerField(_('Alertness'), choices=VRT_CHOICES, default=1, )
    area_knowledge = models.IntegerField(_('Area Knowledge'), choices=VRT_CHOICES, default=1, )

    defensive_driving = models.IntegerField(_('Defensive Driving'), choices=VRT_NUMBER_CHOICES, default=1, )

    score = models.IntegerField(_('Score'), choices=VRT_NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), default=None, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    @property
    def possible_points(self):
        if self.score > 0:
            return 4 * 2
        return 0

    @property
    def points_received(self):
        if self.score:
            return self.score * 2
        return 0

    class Meta:
        ordering = ('-created',)
        verbose_name = "VRT - Driving Habits"


# 12. VRT Post Trip
class VRTPostTrip(VRTPointMixin, models.Model):
    vrt = models.OneToOneField('safe_driver.VehicleRoadTest', on_delete=models.CASCADE, null=False)

    lights = models.IntegerField(_('Lights'), choices=VRT_CHOICES, default=1, )
    reflectors = models.IntegerField(_('Reflectors'), choices=VRT_CHOICES, default=1, )
    body_damage = models.IntegerField(_('Body Damage'), choices=VRT_CHOICES, default=1, )
    tires = models.IntegerField(_('Tires'), choices=VRT_CHOICES, default=1, )
    hub_heat = models.IntegerField(_('Hub Heat'), choices=VRT_CHOICES, default=1, )

    leaks = models.IntegerField(_('Leaks'), choices=VRT_NUMBER_CHOICES, default=1, )

    score = models.IntegerField(_('Score'), choices=VRT_NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), default=None, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "VRT - Post Trip"
