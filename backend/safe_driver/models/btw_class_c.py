from django.db import models
from django.utils.translation import ugettext_lazy as _

from safe_driver.image_functions import signature_image_folder, map_image_folder
from safe_driver.utils import BTWClassManager, BTWClassMixin

NUMBER_CHOICES = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
    (0, "N/A"),
)


# student BTW Class C
class BTWClassC(models.Model):
    test = models.ForeignKey('safe_driver.StudentTest', on_delete=models.CASCADE, null=False,
                             related_name='btw_test_class_c')

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
        verbose_name = "Behind The Wheel Class C"
        verbose_name_plural = "Behind The Wheel Class C"


# 1. Cab safety Class C
class BTWCabSafetyClassC(BTWClassMixin, models.Model):
    btw = models.OneToOneField('safe_driver.BTWClassC', on_delete=models.CASCADE, null=False,
                               related_name='btw_cab_safety_class_c')

    seat_belt = models.IntegerField(_('Seat Belt'), choices=NUMBER_CHOICES, default=0, )
    cab_distractions = models.IntegerField(_('Cab distractions'), choices=NUMBER_CHOICES, default=0, )
    cab_obstructions = models.IntegerField(_('Cab Obstructions'), choices=NUMBER_CHOICES, default=0, )
    cab_chemicals = models.IntegerField(_('Cab Chemicals'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW Cab Safety Class C"


# 2. Start Engine ClassC
class BTWStartEngineClassC(BTWClassMixin, models.Model):
    btw = models.OneToOneField('safe_driver.BTWClassC', on_delete=models.CASCADE, null=False,
                               related_name='btw_start_engine_class_c')

    park_brake_applied = models.IntegerField(_('Park Brake Applied'), choices=NUMBER_CHOICES, default=0, )
    trans_in_neutral = models.IntegerField(_('Trans in Neutral'), choices=NUMBER_CHOICES, default=0, )
    clutch_depressed = models.IntegerField(_('Clutch depressed'), choices=NUMBER_CHOICES, default=0, )
    uses_starter_properly = models.IntegerField(_('Uses Starter Properly'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW Start Engine Class C"


# 3. Engine Operation ClassC
class BTWEngineOperationClassC(BTWClassMixin, models.Model):
    btw = models.OneToOneField('safe_driver.BTWClassC', on_delete=models.CASCADE, null=False,
                               related_name='btw_engine_operation_class_c')

    lugging = models.IntegerField(_('Lugging'), choices=NUMBER_CHOICES, default=0, )
    over_revving = models.IntegerField(_('Over Revving'), choices=NUMBER_CHOICES, default=0, )
    check_gauges = models.IntegerField(_('Check Gauges'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW Engine Operation Class C"


# 4. Clutch and Transmission ClassC
class BTWClutchAndTransmissionClassC(BTWClassMixin, models.Model):
    btw = models.OneToOneField('safe_driver.BTWClassC', on_delete=models.CASCADE, null=False,
                               related_name='btw_clutch_and_transmission_class_c')

    start_off_smoothly = models.IntegerField(_('Start off smoothly'), choices=NUMBER_CHOICES, default=0, )
    proper_gear_use = models.IntegerField(_('Proper gear use'), choices=NUMBER_CHOICES, default=0, )
    shifter_smoothly = models.IntegerField(_('Shifter smoothly'), choices=NUMBER_CHOICES, default=0, )
    proper_gear_sequence = models.IntegerField(_('Proper gear sequence'), choices=NUMBER_CHOICES, default=0, )
    does_not_ride = models.IntegerField(_('Does not Ride'), choices=NUMBER_CHOICES, default=0, )
    does_not_coast = models.IntegerField(_('Does not Coast'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW Clutch and Transmission Class C"


# 5. Coupling Class C (skipped)
# 6. Uncoupling Class C (skipped)
# 7. Use of Brakes and Stopping Class C
class BTWBrakesAndStoppingsClassC(BTWClassMixin, models.Model):
    btw = models.OneToOneField('safe_driver.BTWClassC', on_delete=models.CASCADE, null=False,
                               related_name='btw_brakes_and_stoppings_class_c')

    checks_rear_or_gives_warning = models.IntegerField(_('Checks rear/gives warning'), choices=NUMBER_CHOICES,
                                                       default=0, )
    full_stop_or_smooth = models.IntegerField(_('Full Stop/Smooth(no rebound)'), choices=NUMBER_CHOICES, default=0, )
    does_not_fan = models.IntegerField(_('Doesn’t fan'), choices=NUMBER_CHOICES, default=0, )
    down_shifts = models.IntegerField(_('Down Shifts'), choices=NUMBER_CHOICES, default=0, )
    uses_foot_brake_only = models.IntegerField(_('Uses foot brake only'), choices=NUMBER_CHOICES, default=0, )
    does_not_roll_back = models.IntegerField(_('Doesn’t roll back'), choices=NUMBER_CHOICES, default=0, )
    engine_assist = models.IntegerField(_('Engine Assist'), choices=NUMBER_CHOICES, default=0, )
    avoids_sudden_stops = models.IntegerField(_('Avoids sudden stops'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Use of Brakes and Stopping Class C"


# 8. Eye movement and mirror use Class C
class BTWEyeMovementAndMirrorClassC(BTWClassMixin, models.Model):
    btw = models.OneToOneField('safe_driver.BTWClassC', on_delete=models.CASCADE, null=False,
                               related_name='btw_eye_movement_and_mirror_class_c')

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

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Eye movement and mirror use Class C"


# 9. Recognizes Hazards Class C
class BTWRecognizesHazardsClassC(BTWClassMixin, models.Model):
    btw = models.OneToOneField('safe_driver.BTWClassC', on_delete=models.CASCADE, null=False,
                               related_name='btw_recognizes_hazards_class_c')

    uses_horn = models.IntegerField(_('Uses Horn to communicate'), choices=NUMBER_CHOICES, default=0, )
    makes_adjustments = models.IntegerField(_('Makes Adjustments'), choices=NUMBER_CHOICES, default=0, )
    path_of_least_resistance = models.IntegerField(_('Path of least resistance'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Recognizes Hazards Class C"


# 10. Lights and Signals Class C
class BTWLightsAndSignalsClassC(BTWClassMixin, models.Model):
    btw = models.OneToOneField('safe_driver.BTWClassC', on_delete=models.CASCADE, null=False,
                               related_name='btw_lights_and_signals_class_c')

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

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Lights and Signals Class C"


# 11. Steering Class C
class BTWSteeringClassC(BTWClassMixin, models.Model):
    btw = models.OneToOneField('safe_driver.BTWClassC', on_delete=models.CASCADE, null=False,
                               related_name='btw_steering_class_c')

    over_steers = models.IntegerField(_('Over Steers'), choices=NUMBER_CHOICES, default=0, )
    floats = models.IntegerField(_('Floats'), choices=NUMBER_CHOICES, default=0, )
    poisture_and_grip = models.IntegerField(_('Posture and Grip'), choices=NUMBER_CHOICES, default=0, )
    centered_in_lane = models.IntegerField(_('Centered in lane'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Steering Class C"


# 12. Backing Class C
class BTWBackingClassC(BTWClassMixin, models.Model):
    btw = models.OneToOneField('safe_driver.BTWClassC', on_delete=models.CASCADE, null=False,
                               related_name='btw_backing_class_c')

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

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Backing Class C"


# 13. Speed Class C
class BTWSpeedClassC(BTWClassMixin, models.Model):
    btw = models.OneToOneField('safe_driver.BTWClassC', on_delete=models.CASCADE, null=False,
                               related_name='btw_speed_class_c')

    adjust_to_conditions = models.IntegerField(_('Adjust to conditions'), choices=NUMBER_CHOICES, default=0, )
    speed = models.IntegerField(_('Speed'), choices=NUMBER_CHOICES, default=0, )
    proper_following_distance = models.IntegerField(_('Proper Following distance'), choices=NUMBER_CHOICES, default=0, )
    speed_on_curves = models.IntegerField(_('Speed on Curves'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Speed Class C"


# 14. Intersections Class C
class BTWIntersectionsClassC(BTWClassMixin, models.Model):
    btw = models.OneToOneField('safe_driver.BTWClassC', on_delete=models.CASCADE, null=False,
                               related_name='btw_intersections_class_c')

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

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Intersections Class C"


# 15. Turning Class C
class BTWTurningClassC(BTWClassMixin, models.Model):
    btw = models.OneToOneField('safe_driver.BTWClassC', on_delete=models.CASCADE, null=False,
                               related_name='btw_turning_class_c')

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

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Turning Class C"


# 16. Parking Class C
class BTWParkingClassC(BTWClassMixin, models.Model):
    btw = models.OneToOneField('safe_driver.BTWClassC', on_delete=models.CASCADE, null=False,
                               related_name='btw_parking_class_c')

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

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Parking Class C"


# 17. Multiple trailers Class C (skipped)
# 18. Hills Class C
class BTWHillsClassC(BTWClassMixin, models.Model):
    btw = models.OneToOneField('safe_driver.BTWClassC', on_delete=models.CASCADE, null=False,
                               related_name='btw_hills_class_c')

    proper_gear_up_down = models.IntegerField(_('Proper gear up or down'), choices=NUMBER_CHOICES, default=0, )
    avoids_rolling_back = models.IntegerField(_('Avoids rolling back H/V'), choices=NUMBER_CHOICES, default=0, )
    test_brakes_prior = models.IntegerField(_('Test brakes prior'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Hills Class C"


# 19. Passing Class C
class BTWPassingClassC(BTWClassMixin, models.Model):
    btw = models.OneToOneField('safe_driver.BTWClassC', on_delete=models.CASCADE, null=False,
                               related_name='btw_passing_class_c')

    sufficient_space_to_pass = models.IntegerField(_('Sufficient Space to Pass'), choices=NUMBER_CHOICES, default=0, )
    signals_property = models.IntegerField(_('Signals Property'), choices=NUMBER_CHOICES, default=0, )
    check_mirrors = models.IntegerField(_('Checks Mirrors'), choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - Passing Class C"


# 20. General Safety and DOT adherence Class C
class BTWGeneralSafetyAndDOTAdherenceClassC(BTWClassMixin, models.Model):
    btw = models.OneToOneField('safe_driver.BTWClassC', on_delete=models.CASCADE, null=False,
                               related_name='btw_general_safety_and_dot_adherence_class_c')

    avoids_crowding_effect = models.IntegerField(_('Avoids crowding effect'), choices=NUMBER_CHOICES, default=0, )
    stays_right_or_correct_lane = models.IntegerField(_('Stays to the right/correct lane'),
                                                      choices=NUMBER_CHOICES, default=0, )
    aware_hours_of_service = models.IntegerField(_('Aware of hours of service'), choices=NUMBER_CHOICES, default=0, )
    proper_use_off_mirrors = models.IntegerField(_('Proper use of mirrors'), choices=NUMBER_CHOICES, default=0, )
    self_confident_not_complacement = models.IntegerField(_('Self confident not complacent'),
                                                          choices=NUMBER_CHOICES, default=0, )
    check_instruments = models.IntegerField(_('Checks instruments'), choices=NUMBER_CHOICES, default=0, )
    uses_horn_properly = models.IntegerField(_('Uses horn properly'), choices=NUMBER_CHOICES, default=0, )
    maintains_dot_log = models.IntegerField(_('Maintains DOT log'), choices=NUMBER_CHOICES, default=0, )
    drives_defensively = models.IntegerField(_('Drives defensively'), choices=NUMBER_CHOICES, default=0, )
    company_haz_mat_protocol = models.IntegerField(_('Company Haz Mat protocol'), choices=NUMBER_CHOICES, default=0, )
    air_cans_or_line_moisture_free = models.IntegerField(_('Air cans/lines free of moisture'),
                                                         choices=NUMBER_CHOICES, default=0, )
    avoid_distractions_while_driving = models.IntegerField(_('Avoid distractions while driving'),
                                                           choices=NUMBER_CHOICES, default=0, )
    works_safely_to_avoid_injuries = models.IntegerField(_('Works safely to avoid injuries'),
                                                         choices=NUMBER_CHOICES, default=0, )

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    class Meta:
        ordering = ('-created',)
        verbose_name = "BTW - General Safety and DOT adherence - Class C"

