from django.db import models
from django.utils.translation import ugettext_lazy as _

from safe_driver.image_functions import signature_image_folder, map_image_folder

NUMBER_CHOICES = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
    (0, "N/A"),
)


# student BTW Bus
class BTWBus(models.Model):
    test = models.ForeignKey('safe_driver.StudentTest', on_delete=models.CASCADE, null=False,
                             related_name='btw_test_bus')

    date = models.DateField(null=True, blank=True, default=None, verbose_name='Date')
    start_time = models.TimeField(null=True, blank=True, default=None, verbose_name='Start Time')
    end_time = models.TimeField(null=True, blank=True, default=None, verbose_name='End Time')
    driver_signature = models.ImageField(_('Driver Signature'), upload_to=signature_image_folder, default=None,
                                         null=True, blank=True)
    evaluator_signature = models.ImageField(_('Evaluator Signature'), upload_to=signature_image_folder,
                                            default=None, null=True,
                                            blank=True)
    company_rep_signature = models.ImageField(_('Company Rep Signature'), upload_to=signature_image_folder,
                                              default=None, null=True,
                                              blank=True)
    company_rep_name = models.CharField(max_length=150, null=True, blank=True, default=None,
                                        verbose_name='Company Rep. Name')

    map_data = models.TextField(_('Map Data'), null=True, blank=True)
    map_image = models.ImageField(_('Map Image'), upload_to=map_image_folder, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    def __str__(self):
        return '%s BTW - %s' % (self.test.student.full_name, self.pk)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Behind The Wheel Bus"
        verbose_name_plural = "Behind The Wheel Bus"


# 1. Cab safety Bus
class BTWCabSafetyBus(models.Model):
    btw = models.OneToOneField('safe_driver.BTWBus', on_delete=models.CASCADE, null=False,
                               related_name='btw_cab_safety_bus')

    seat_belt = models.IntegerField(_('Seat Belt'), choices=NUMBER_CHOICES, default=0, )
    cab_distractions = models.IntegerField(_('Cab distractions'), choices=NUMBER_CHOICES, default=0, )
    cab_obstructions = models.IntegerField(_('Cab Obstructions'), choices=NUMBER_CHOICES, default=0, )
    cab_chemicals = models.IntegerField(_('Cab Chemicals'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    @property
    def possible_points(self):
        points = 5 * 4
        return points

    @property
    def points_received(self):
        points = self.seat_belt + self.cab_distractions + self.cab_obstructions + self.cab_chemicals
        return points

    @property
    def percent_effective(self):
        percent = (self.points_received / self.possible_points) * 100
        return '%s' % percent

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW Cab Safety Bus"


# 2. Start Engine Bus
class BTWStartEngineBus(models.Model):
    btw = models.OneToOneField('safe_driver.BTWBus', on_delete=models.CASCADE, null=False,
                               related_name='btw_start_engine_bus')

    park_brake_applied = models.IntegerField(_('Park Brake Applied'), choices=NUMBER_CHOICES, default=0, )
    trans_in_neutral = models.IntegerField(_('Trans in Neutral'), choices=NUMBER_CHOICES, default=0, )
    uses_starter_properly = models.IntegerField(_('Uses Starter Properly'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    @property
    def possible_points(self):
        points = 5 * 4
        return points

    @property
    def points_received(self):
        points = self.park_brake_applied + self.trans_in_neutral + self.uses_starter_properly
        return points

    @property
    def percent_effective(self):
        percent = (self.points_received / self.possible_points) * 100
        return '%s' % percent

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW Start Engine Bus"


# 3. Engine Operation Bus
class BTWEngineOperationBus(models.Model):
    btw = models.OneToOneField('safe_driver.BTWBus', on_delete=models.CASCADE, null=False,
                               related_name='btw_engine_operation_bus')

    lugging = models.IntegerField(_('Lugging'), choices=NUMBER_CHOICES, default=0, )
    check_gauges = models.IntegerField(_('Check Gauges'), choices=NUMBER_CHOICES, default=0, )
    start_off_smoothly = models.IntegerField(_('Start Off Smoothly'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    @property
    def possible_points(self):
        points = 5 * 3
        return points

    @property
    def points_received(self):
        points = self.lugging + self.check_gauges + self.start_off_smoothly
        return points

    @property
    def percent_effective(self):
        percent = (self.points_received / self.possible_points) * 100
        return '%s' % percent

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW Engine Operation Bus"


# 4. Use of Brakes and Stopping Bus
class BTWBrakesAndStoppingsBus(models.Model):
    btw = models.OneToOneField('safe_driver.BTWBus', on_delete=models.CASCADE, null=False,
                               related_name='btw_brakes_and_stopping_bus')

    checks_rear_or_gives_warning = models.IntegerField(_('Checks rear/gives warning'), choices=NUMBER_CHOICES,
                                                       default=0, )
    full_stop_or_smooth = models.IntegerField(_('Full Stop/Smooth(no rebound)'), choices=NUMBER_CHOICES, default=0, )
    does_not_fan = models.IntegerField(_('Doesn’t fan'), choices=NUMBER_CHOICES, default=0, )
    down_shifts = models.IntegerField(_('Down Shifts'), choices=NUMBER_CHOICES, default=0, )
    uses_foot_brake_only = models.IntegerField(_('Uses foot brake only'), choices=NUMBER_CHOICES, default=0, )
    hand_valve_use = models.IntegerField(_('Hand valve use'), choices=NUMBER_CHOICES, default=0, )
    does_not_roll_back = models.IntegerField(_('Doesn’t roll back'), choices=NUMBER_CHOICES, default=0, )
    engine_assist = models.IntegerField(_('Engine Assist'), choices=NUMBER_CHOICES, default=0, )
    avoids_sudden_stops = models.IntegerField(_('Avoids sudden stops'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    @property
    def possible_points(self):
        points = 5 * 9
        return points

    @property
    def points_received(self):
        points = self.checks_rear_or_gives_warning + self.full_stop_or_smooth + self.does_not_fan + \
                 self.down_shifts + self.uses_foot_brake_only + self.hand_valve_use + \
                 self.does_not_roll_back + self.engine_assist + self.avoids_sudden_stops
        return points

    @property
    def percent_effective(self):
        percent = (self.points_received / self.possible_points) * 100
        return '%s' % percent

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Use of Brakes and Stopping Bus"


# 5. Passenger Safety
class BTWPassengerSafetyBus(models.Model):
    btw = models.OneToOneField('safe_driver.BTWBus', on_delete=models.CASCADE, null=False,
                               related_name='btw_passenger_safety_bus')

    no_one_past_standee_line = models.IntegerField(_('No One Past Standee Line'), choices=NUMBER_CHOICES, default=0, )
    steps_clear = models.IntegerField(_('Steps Clear'), choices=NUMBER_CHOICES, default=0, )
    everyone_seated = models.IntegerField(_('Everyone Seated'), choices=NUMBER_CHOICES, default=0, )
    seatbelts_on = models.IntegerField(_('Seatbelts On (if required)'), choices=NUMBER_CHOICES, default=0, )
    holding_hand_rails_standing = models.IntegerField(_('Holding Hand Rails Standing'), choices=NUMBER_CHOICES,
                                                      default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    @property
    def possible_points(self):
        points = 5 * 5
        return points

    @property
    def points_received(self):
        points = self.no_one_past_standee_line + self.steps_clear + self.everyone_seated + self.seatbelts_on + \
                 self.holding_hand_rails_standing
        return points

    @property
    def percent_effective(self):
        percent = (self.points_received / self.possible_points) * 100
        return '%s' % percent

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW PAS - Passenger Safety"


# 6. Eye movement and mirror use Bus
class BTWEyeMovementAndMirrorBus(models.Model):
    btw = models.OneToOneField('safe_driver.BTWBus', on_delete=models.CASCADE, null=False,
                               related_name='btw_eye_movement_and_mirror_bus')

    eyes_ahead = models.IntegerField(_('Eyes ahead'), choices=NUMBER_CHOICES, default=0, )
    follow_up_in_mirror = models.IntegerField(_('Follow-up in mirror'), choices=NUMBER_CHOICES, default=0, )
    checks_mirror = models.IntegerField(_('Checks mirrors 5 to 8 sec’s'), choices=NUMBER_CHOICES, default=0, )
    scans_does_not_stare = models.IntegerField(_('Scans doesn’t stare'), choices=NUMBER_CHOICES, default=0, )
    avoid_billboards = models.IntegerField(_('Avoid Billboards'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    @property
    def possible_points(self):
        points = 5 * 5
        return points

    @property
    def points_received(self):
        points = self.eyes_ahead + self.follow_up_in_mirror + self.checks_mirror + \
                 self.scans_does_not_stare + self.avoid_billboards
        return points

    @property
    def percent_effective(self):
        percent = (self.points_received / self.possible_points) * 100
        return '%s' % percent

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Eye movement and mirror use Bus"


# 7. Recognizes Hazards Bus
class BTWRecognizesHazardsBus(models.Model):
    btw = models.OneToOneField('safe_driver.BTWBus', on_delete=models.CASCADE, null=False,
                               related_name='btw_recognizes_hazards_bus')

    uses_horn = models.IntegerField(_('Uses Horn to communicate'), choices=NUMBER_CHOICES, default=0, )
    makes_adjustments = models.IntegerField(_('Makes Adjustments'), choices=NUMBER_CHOICES, default=0, )
    path_of_least_resistance = models.IntegerField(_('Path of least resistance'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    @property
    def possible_points(self):
        points = 5 * 3
        return points

    @property
    def points_received(self):
        points = self.uses_horn + self.makes_adjustments + self.path_of_least_resistance
        return points

    @property
    def percent_effective(self):
        percent = (self.points_received / self.possible_points) * 100
        return '%s' % percent

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Recognizes Hazards Bus"


# 8. Lights and Signals Bus
class BTWLightsAndSignalsBus(models.Model):
    btw = models.OneToOneField('safe_driver.BTWBus', on_delete=models.CASCADE, null=False,
                               related_name='btw_lights_and_signals_bus')

    proper_use_of_lights = models.IntegerField(_('Proper use of lights'), choices=NUMBER_CHOICES, default=0, )
    adjust_speed = models.IntegerField(_('Adjust Speed'), choices=NUMBER_CHOICES, default=0, )
    signals_well_in_advance = models.IntegerField(_('Signals well in advance'), choices=NUMBER_CHOICES, default=0, )
    cancels_signal = models.IntegerField(_('Cancels signal'), choices=NUMBER_CHOICES, default=0, )
    use_of_4_ways = models.IntegerField(_('Use of 4 Ways'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    @property
    def possible_points(self):
        points = 5 * 5
        return points

    @property
    def points_received(self):
        points = self.proper_use_of_lights + self.adjust_speed + self.signals_well_in_advance + \
                 self.cancels_signal + self.use_of_4_ways
        return points

    @property
    def percent_effective(self):
        percent = (self.points_received / self.possible_points) * 100
        return '%s' % percent

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Lights and Signals Bus"


# 9. Steering Bus
class BTWSteeringBus(models.Model):
    btw = models.OneToOneField('safe_driver.BTWBus', on_delete=models.CASCADE, null=False,
                               related_name='btw_steering_bus')

    over_steers = models.IntegerField(_('Over Steers'), choices=NUMBER_CHOICES, default=0, )
    floats = models.IntegerField(_('Floats'), choices=NUMBER_CHOICES, default=0, )
    poisture_and_grip = models.IntegerField(_('Posture and Grip'), choices=NUMBER_CHOICES, default=0, )
    centered_in_lane = models.IntegerField(_('Centered in lane'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    @property
    def possible_points(self):
        points = 5 * 4
        return points

    @property
    def points_received(self):
        points = self.over_steers + self.floats + self.poisture_and_grip + self.centered_in_lane
        return points

    @property
    def percent_effective(self):
        percent = (self.points_received / self.possible_points) * 100
        return '%s' % percent

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Steering Bus"


# 10. Backing Bus
class BTWBackingBus(models.Model):
    btw = models.OneToOneField('safe_driver.BTWBus', on_delete=models.CASCADE, null=False,
                               related_name='btw_backing_bus')

    size_up_situation = models.IntegerField(_('Size up situation'), choices=NUMBER_CHOICES, default=0, )
    driver_side_back = models.IntegerField(_('Driver side back'), choices=NUMBER_CHOICES, default=0, )
    check_rear = models.IntegerField(_('Check rear'), choices=NUMBER_CHOICES, default=0, )
    gets_attention = models.IntegerField(_('Gets Attention'), choices=NUMBER_CHOICES, default=0, )
    backs_slowly = models.IntegerField(_('Backs slowly'), choices=NUMBER_CHOICES, default=0, )
    rechecks_conditions = models.IntegerField(_('Re-checks conditions'), choices=NUMBER_CHOICES, default=0, )
    uses_other_aids = models.IntegerField(_('Uses other aids'), choices=NUMBER_CHOICES, default=0, )
    steers_correctly = models.IntegerField(_('Steers correctly'), choices=NUMBER_CHOICES, default=0, )
    does_not_hit_dock = models.IntegerField(_('Doesn’t hit dock'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    @property
    def possible_points(self):
        points = 5 * 9
        return points

    @property
    def points_received(self):
        points = self.size_up_situation + self.driver_side_back + self.check_rear + self.gets_attention + \
                 self.backs_slowly + self.rechecks_conditions + self.uses_other_aids + \
                 self.steers_correctly + self.does_not_hit_dock
        return points

    @property
    def percent_effective(self):
        percent = (self.points_received / self.possible_points) * 100
        return '%s' % percent

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Backing Bus"


# 11. Speed Bus
class BTWSpeedBus(models.Model):
    btw = models.OneToOneField('safe_driver.BTWBus', on_delete=models.CASCADE, null=False,
                               related_name='btw_speed_bus')

    adjust_to_conditions = models.IntegerField(_('Adjust to conditions'), choices=NUMBER_CHOICES, default=0, )
    speed = models.IntegerField(_('Speed'), choices=NUMBER_CHOICES, default=0, )
    proper_following_distance = models.IntegerField(_('Proper Following distance'), choices=NUMBER_CHOICES, default=0, )
    speed_on_curves = models.IntegerField(_('Speed on Curves'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    @property
    def possible_points(self):
        points = 5 * 4
        return points

    @property
    def points_received(self):
        points = self.adjust_to_conditions + self.speed + self.proper_following_distance + self.speed_on_curves
        return points

    @property
    def percent_effective(self):
        percent = (self.points_received / self.possible_points) * 100
        return '%s' % percent

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Speed Bus"


# 12. Intersections BTW Bus
class BTWIntersectionsBus(models.Model):
    btw = models.OneToOneField('safe_driver.BTWBus', on_delete=models.CASCADE, null=False,
                               related_name='btw_intersections_bus')

    approach_decision_point = models.IntegerField(_('Approach -decision point'), choices=NUMBER_CHOICES, default=0, )
    clear_intersection = models.IntegerField(_('Clear Intersection L-R-L'), choices=NUMBER_CHOICES, default=0, )
    check_mirrors = models.IntegerField(_('Check Mirrors'), choices=NUMBER_CHOICES, default=0, )
    full_stop = models.IntegerField(_('Full stop when needed'), choices=NUMBER_CHOICES, default=0, )
    times_light_or_starts = models.IntegerField(_('Times light or starts too fast'), choices=NUMBER_CHOICES,
                                                default=0, )
    steering_axel_staright = models.IntegerField(_('Steering axel straight'), choices=NUMBER_CHOICES, default=0, )
    yields_right_of_way = models.IntegerField(_('Yields right-of-way'), choices=NUMBER_CHOICES, default=0, )
    proper_speed_or_gear = models.IntegerField(_('Proper speed/gear'), choices=NUMBER_CHOICES, default=0, )
    leaves_space = models.IntegerField(_('Leaves space for an out'), choices=NUMBER_CHOICES, default=0, )
    stop_lines = models.IntegerField(_('Stop Lines - crosswalks'), choices=NUMBER_CHOICES, default=0, )
    railroad_crossings = models.IntegerField(_('Railroad crossings'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    @property
    def possible_points(self):
        points = 5 * 11
        return points

    @property
    def points_received(self):
        points = self.approach_decision_point + self.clear_intersection + self.check_mirrors + \
                 self.full_stop + self.times_light_or_starts + self.steering_axel_staright + \
                 self.yields_right_of_way + self.proper_speed_or_gear + self.leaves_space + \
                 self.stop_lines + self.railroad_crossings
        return points

    @property
    def percent_effective(self):
        percent = (self.points_received / self.possible_points) * 100
        return '%s' % percent

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Intersections BUS"


# 13. Turning BTW Bus
class BTWTurningBus(models.Model):
    btw = models.OneToOneField('safe_driver.BTWBus', on_delete=models.CASCADE, null=False,
                               related_name='btw_turning_bus')

    signals_correctly = models.IntegerField(_('Signals correctly'), choices=NUMBER_CHOICES, default=0, )
    gets_in_proper_time = models.IntegerField(_('Gets in proper lane'), choices=NUMBER_CHOICES, default=0, )
    downshifts_to_pulling_gear = models.IntegerField(_('Downshifts to pulling gear'), choices=NUMBER_CHOICES,
                                                     default=0, )
    handles_light_correctly = models.IntegerField(_('Handles light correctly'), choices=NUMBER_CHOICES, default=0, )
    setup_and_execution = models.IntegerField(_('Set up and execution'), choices=NUMBER_CHOICES, default=0, )
    turn_speed = models.IntegerField(_('Turn Speed'), choices=NUMBER_CHOICES, default=0, )
    mirror_follow_up = models.IntegerField(_('Mirror follow up'), choices=NUMBER_CHOICES, default=0, )
    turns_lane_to_lane = models.IntegerField(_('Turns lane to lane'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    @property
    def possible_points(self):
        points = 5 * 8
        return points

    @property
    def points_received(self):
        points = self.signals_correctly + self.gets_in_proper_time + self.downshifts_to_pulling_gear + \
                 self.handles_light_correctly + self.setup_and_execution + self.turn_speed + \
                 self.mirror_follow_up + self.turns_lane_to_lane
        return points

    @property
    def percent_effective(self):
        percent = (self.points_received / self.possible_points) * 100
        return '%s' % percent

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Turning Bus"


# 14. Parking BTW Bus
class BTWParkingBus(models.Model):
    btw = models.OneToOneField('safe_driver.BTWBus', on_delete=models.CASCADE, null=False,
                               related_name='btw_parking_bus')

    does_not_hit_curb = models.IntegerField(_('Doesn’t hit curb'), choices=NUMBER_CHOICES, default=0, )
    curbs_wheels = models.IntegerField(_('Curbs wheels'), choices=NUMBER_CHOICES, default=0, )
    chock_wheels = models.IntegerField(_('Chock wheels (if required)'), choices=NUMBER_CHOICES, default=0, )
    park_brake_applied = models.IntegerField(_('Park Brake applied'), choices=NUMBER_CHOICES, default=0, )
    trans_in_neutral = models.IntegerField(_('Trans in neutral'), choices=NUMBER_CHOICES, default=0, )
    engine_off = models.IntegerField(_('Engine off - Take keys'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    @property
    def possible_points(self):
        points = 5 * 6
        return points

    @property
    def points_received(self):
        points = self.does_not_hit_curb + self.curbs_wheels + self.chock_wheels + self.park_brake_applied + \
                 self.trans_in_neutral + self.engine_off
        return points

    @property
    def percent_effective(self):
        percent = (self.points_received / self.possible_points) * 100
        return '%s' % percent

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Parking Bus"


# 15. Hills Bus
class BTWHillsBus(models.Model):
    btw = models.OneToOneField('safe_driver.BTWBus', on_delete=models.CASCADE, null=False,
                               related_name='btw_hills_bus')

    proper_gear_up_down = models.IntegerField(_('Proper gear up or down'), choices=NUMBER_CHOICES, default=0, )
    avoids_rolling_back = models.IntegerField(_('Avoids rolling back H/V'), choices=NUMBER_CHOICES, default=0, )
    test_brakes_prior = models.IntegerField(_('Test brakes prior'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    @property
    def possible_points(self):
        points = 5 * 3
        return points

    @property
    def points_received(self):
        points = self.proper_gear_up_down + self.avoids_rolling_back + self.test_brakes_prior
        return points

    @property
    def percent_effective(self):
        percent = (self.points_received / self.possible_points) * 100
        return '%s' % percent

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Hills Bus"


# 16. Passing Bus
class BTWPassingBus(models.Model):
    btw = models.OneToOneField('safe_driver.BTWBus', on_delete=models.CASCADE, null=False,
                               related_name='btw_passing_bus')

    sufficient_space_to_pass = models.IntegerField(_('Sufficient Space to Pass'), choices=NUMBER_CHOICES, default=0, )
    signals_property = models.IntegerField(_('Signals Property'), choices=NUMBER_CHOICES, default=0, )
    check_mirrors = models.IntegerField(_('Checks Mirrors'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    @property
    def possible_points(self):
        points = 5 * 3
        return points

    @property
    def points_received(self):
        points = self.sufficient_space_to_pass + self.signals_property + self.check_mirrors
        return points

    @property
    def percent_effective(self):
        percent = (self.points_received / self.possible_points) * 100
        return '%s' % percent

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Passing Bus"


# 17. Railroad Crossing BTW Bus
class BTWRailroadCrossingBus(models.Model):
    btw = models.OneToOneField('safe_driver.BTWBus', on_delete=models.CASCADE, null=False,
                               related_name='btw_railroad_crossing_bus')

    signal_and_activate_4_ways = models.IntegerField(_('Signal & Activate 4-ways'), choices=NUMBER_CHOICES, default=0, )
    stop_prior = models.IntegerField(_('Stop 10’ to 50’ prior'), choices=NUMBER_CHOICES, default=0, )
    open_window_and_door = models.IntegerField(_('Open window & door'), choices=NUMBER_CHOICES, default=0, )
    look_listen_clear = models.IntegerField(_('Look, Listen & Clear'), choices=NUMBER_CHOICES, default=0, )
    signal_and_merge_into_traffic = models.IntegerField(_('Signal & merge into traffic'), choices=NUMBER_CHOICES,
                                                        default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    @property
    def possible_points(self):
        points = 5 * 5
        return points

    @property
    def points_received(self):
        points = self.signal_and_activate_4_ways + self.stop_prior + self.open_window_and_door + \
                 self.look_listen_clear + self.signal_and_merge_into_traffic
        return points

    @property
    def percent_effective(self):
        percent = (self.points_received / self.possible_points) * 100
        return '%s' % percent

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Railroad Crossing Bus"


# 18. General Safety and DOT adherence
class BTWGeneralSafetyAndDOTAdherenceBus(models.Model):
    btw = models.OneToOneField('safe_driver.BTWBus', on_delete=models.CASCADE, null=False,
                               related_name='btw_general_safety_bus')

    avoids_crowding_effect = models.IntegerField(_('Avoids crowding effect'), choices=NUMBER_CHOICES, default=0, )
    stays_right_or_correct_lane = models.IntegerField(_('Stays to the right/correct lane'), choices=NUMBER_CHOICES,
                                                      default=0, )
    aware_hours_of_service = models.IntegerField(_('Aware of hours of service'), choices=NUMBER_CHOICES, default=0, )
    proper_use_off_mirrors = models.IntegerField(_('Proper use of mirrors'), choices=NUMBER_CHOICES, default=0, )
    self_confident_not_complacement = models.IntegerField(_('Self confident not complacent'), choices=NUMBER_CHOICES,
                                                          default=0, )
    check_instruments = models.IntegerField(_('Checks instruments'), choices=NUMBER_CHOICES, default=0, )
    uses_horn_properly = models.IntegerField(_('Uses horn properly'), choices=NUMBER_CHOICES, default=0, )
    maintains_dot_log = models.IntegerField(_('Maintains DOT log'), choices=NUMBER_CHOICES, default=0, )
    drives_defensively = models.IntegerField(_('Drives defensively'), choices=NUMBER_CHOICES, default=0, )
    company_haz_mat_protocol = models.IntegerField(_('Company Haz Mat protocol'), choices=NUMBER_CHOICES, default=0, )
    air_cans_or_line_moisture_free = models.IntegerField(_('Air cans/lines free of moisture'), choices=NUMBER_CHOICES,
                                                         default=0, )
    avoid_distractions_while_driving = models.IntegerField(_('Avoid distractions while driving'),
                                                           choices=NUMBER_CHOICES,
                                                           default=0, )
    works_safely_to_avoid_injuries = models.IntegerField(_('Works safely to avoid injuries'), choices=NUMBER_CHOICES,
                                                         default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    @property
    def possible_points(self):
        points = 5 * 13
        return points

    @property
    def points_received(self):
        points = self.avoids_crowding_effect + self.stays_right_or_correct_lane + self.aware_hours_of_service + \
                 self.proper_use_off_mirrors + self.self_confident_not_complacement + self.check_instruments + \
                 self.uses_horn_properly + self.maintains_dot_log + self.drives_defensively + \
                 self.company_haz_mat_protocol + self.air_cans_or_line_moisture_free + \
                 self.avoid_distractions_while_driving + self.works_safely_to_avoid_injuries
        return points

    @property
    def percent_effective(self):
        percent = (self.points_received / self.possible_points) * 100
        return '%s' % percent

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - General Safety and DOT adherence - Bus"


# 19. Internal Environtment -  BTW Bus
class BTWInternalEnvironmentBus(models.Model):
    btw = models.OneToOneField('safe_driver.BTWBus', on_delete=models.CASCADE, null=False,
                               related_name='btw_internal_environment_bus')

    driver_aid = models.IntegerField(_('Driver Aid'), choices=NUMBER_CHOICES, default=0, )
    interior_passenger_mirror_check = models.IntegerField(_('Interior Passenger Mirror Check'),
                                                          choices=NUMBER_CHOICES, default=0, )
    safe_path = models.IntegerField(_('Safe Path'), choices=NUMBER_CHOICES, default=0, )
    maintain_proper_grip = models.IntegerField(_('Maintain Proper Grip'), choices=NUMBER_CHOICES, default=0, )
    smooth_driving_movements = models.IntegerField(_('Smooth Driving Movements'), choices=NUMBER_CHOICES, default=0, )
    maintain_comfortable_environment = models.IntegerField(_('Maintain a Comfortable Environment'),
                                                           choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    @property
    def possible_points(self):
        points = 5 * 6
        return points

    @property
    def points_received(self):
        points = self.driver_aid + self.interior_passenger_mirror_check + self.safe_path + \
                 self.maintain_proper_grip + self.smooth_driving_movements + self.maintain_comfortable_environment
        return points

    @property
    def percent_effective(self):
        percent = (self.points_received / self.possible_points) * 100
        return '%s' % percent

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Internal Environtment - Bus"
