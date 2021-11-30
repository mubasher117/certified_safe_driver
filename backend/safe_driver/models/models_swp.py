from django.db import models
from django.utils.translation import ugettext_lazy as _

from safe_driver.image_functions import signature_image_folder
from safe_driver.utils import model_fields_received_points, model_fields_possible_points

NUMBER_CHOICES = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
    (0, "N/A"),
)


# SWP
class SafeDriveSWP(models.Model):
    # student = models.OneToOneField('users.User', on_delete=models.CASCADE, null=False, related_name='swp_student')
    test = models.ForeignKey('safe_driver.StudentTest', on_delete=models.CASCADE, null=False,
                             related_name='swp_student_test')
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

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s" % self.pk

    def __str__(self):
        return "%s" % self.test.student.username

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Safe Work Training(SWP)'
        verbose_name_plural = 'Safe Work Trainings(SWP)'


# 1. Employees Interview
class SWPEmployeesInterview(models.Model):
    swp = models.OneToOneField('safe_driver.SafeDriveSWP', on_delete=models.CASCADE, null=False)

    positive_attitude = models.BooleanField(_('Positive Attitude Towards Safety'), default=True)
    nearest_exit = models.BooleanField(_('Nearest Exit'), default=True)
    eye_wash = models.BooleanField(_('Eye Wash'), default=True)
    evacuation_plan = models.BooleanField(_('Evacuation Plan'), default=True)
    evacuation_assembly = models.BooleanField(_('Evacuation Assembly'), default=True)
    equipment_emergency_shut_offs = models.BooleanField(_('Equipment Emergency Shut Offs'), default=True)
    evacuation_notification = models.BooleanField(_('Evacuation Notification'), default=True)
    demonstrate_power_zone = models.BooleanField(_('Demonstrate Power Zone'), default=True)
    dehydration = models.BooleanField(_('Dehydration'), default=True)
    employee_understand_protocol = models.BooleanField(_(
        'Employee Understand Protocol for Reporting Incidents Immediately'),
        default=True)

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    @property
    def possible_points(self):
        fields = self._meta.get_fields()
        boolean_count = 0
        for field in fields:
            field_type = field.get_internal_type()
            if field_type == 'BooleanField':
                boolean_count += 5
        return boolean_count

    @property
    def points_received(self):
        fields = self._meta.get_fields()
        boolean_count = 0
        for field in fields:
            field_type = field.get_internal_type()
            if field_type == 'BooleanField':
                field_value = field.value_from_object(self)
                if field_value is True:
                    boolean_count += 5
        return boolean_count

    @property
    def percent_effective(self):
        percent = 0
        if self.possible_points > 0 and self.possible_points >= self.points_received:
            percent = (self.points_received / self.possible_points) * 100
        return '%s' % percent

    class Meta:
        ordering = ('-created',)
        verbose_name = "SWP - Employees Interview"


# 2. Power Equipment
class SWPPowerEquipment(models.Model):
    swp = models.OneToOneField('safe_driver.SafeDriveSWP', on_delete=models.CASCADE, null=False)

    eye_contact_with_operator = models.IntegerField(_('Eye Contact with Operator'), choices=NUMBER_CHOICES, default=0)
    lock_out_tag_out = models.IntegerField(_('Lock out-Tag Out'), choices=NUMBER_CHOICES, default=0)
    using_conveyor_equipment = models.IntegerField(_('Using Conveyor Equipment'), choices=NUMBER_CHOICES, default=0)
    system_security = models.IntegerField(_('System Security'), choices=NUMBER_CHOICES, default=0)
    equipement_pinch_points = models.IntegerField(_('Equipment Pinch Points'), choices=NUMBER_CHOICES, default=0)

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    @property
    def possible_points(self):
        # total = 0
        # for field in self._meta.get_fields():
        #     field_type = field.get_internal_type()
        #     if field_type == 'IntegerField':
        #         field_value = field.value_from_object(self)
        #         if field_value > 0:
        #             total += 5
        # # points = 5 * 5
        total = model_fields_possible_points(self, self._meta.get_fields())
        return total

    @property
    def points_received(self):
        # print(field)
        # points = self.eye_contact_with_operator + self.lock_out_tag_out + self.using_conveyor_equipment \
        #          + self.system_security + self.equipement_pinch_points
        # return points

        total = model_fields_received_points(self, self._meta.get_fields())
        return total

    @property
    def percent_effective(self):
        percent = 0
        if self.possible_points > 0 and self.possible_points >= self.points_received:
            percent = (self.points_received / self.possible_points) * 100
        return '%s' % percent

    class Meta:
        ordering = ('-created',)
        verbose_name = "SWP - Power Equipment"


# 3. Job Setup
class SWPJobSetup(models.Model):
    swp = models.OneToOneField('safe_driver.SafeDriveSWP', on_delete=models.CASCADE, null=False)

    shoes_slip_resistant = models.IntegerField(_('Shoes Slip Resistant'), choices=NUMBER_CHOICES, default=0)
    shoes_good_repair = models.IntegerField(_('Shoes Good Repair'), choices=NUMBER_CHOICES, default=0)
    arrives_on_time = models.IntegerField(_('Arrives on Time'), choices=NUMBER_CHOICES, default=0)
    organizes_tools = models.IntegerField(_('Organizes Tools'), choices=NUMBER_CHOICES, default=0)
    avoids_distractions = models.IntegerField(_('Avoids Distractions'), choices=NUMBER_CHOICES, default=0)
    focus_on_assignment = models.IntegerField(_('Focus on Assignment'), choices=NUMBER_CHOICES, default=0)
    start_with_stretching = models.IntegerField(_('Start with Stretching'), choices=NUMBER_CHOICES, default=0)
    stretch_after_long_delays = models.IntegerField(_('Stretch after Long Delays'), choices=NUMBER_CHOICES, default=0)
    stay_hydrated = models.IntegerField(_('Stay Hydrated'), choices=NUMBER_CHOICES, default=0)
    breaks_and_lunches_adhered_to = models.IntegerField(_('Breaks and Lunches Adhered to'), choices=NUMBER_CHOICES,
                                                        default=0)
    dress_appropriately = models.IntegerField(_('Dress Appropriately'), choices=NUMBER_CHOICES, default=0)
    clean_work_area = models.IntegerField(_('Clean Work Area'), choices=NUMBER_CHOICES, default=0)
    no_tripping_hazards = models.IntegerField(_('No Tripping Hazards'), choices=NUMBER_CHOICES, default=0)
    secure_power_equipment = models.IntegerField(_('Secure Power Equipment'), choices=NUMBER_CHOICES, default=0)
    maintain_daily_routine = models.IntegerField(_('Maintain Daily Routine'), choices=NUMBER_CHOICES, default=0)
    proper_tool_storage = models.IntegerField(_('Proper Tool Storage'), choices=NUMBER_CHOICES, default=0)
    report_safety_hazards = models.IntegerField(_('Report Safety Hazards'), choices=NUMBER_CHOICES, default=0)

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    @property
    def possible_points(self):
        # points = 5 * 17
        total = model_fields_possible_points(self, self._meta.get_fields())
        return total

    @property
    def points_received(self):
        # points = self.shoes_slip_resistant + self.shoes_good_repair + self.arrives_on_time + self.organizes_tools + \
        #          self.avoids_distractions + self.focus_on_assignment + self.start_with_stretching + \
        #          self.stretch_after_long_delays + self.stay_hydrated + self.breaks_and_lunches_adhered_to + \
        #          self.dress_appropriately + self.clean_work_area + self.no_tripping_hazards + \
        #          self.secure_power_equipment + self.maintain_daily_routine + self.proper_tool_storage + \
        #          self.report_safety_hazards

        total = model_fields_received_points(self, self._meta.get_fields())
        return total

    @property
    def percent_effective(self):
        percent = 0
        if self.possible_points > 0 and self.possible_points >= self.points_received:
            percent = (self.points_received / self.possible_points) * 100
        return '%s' % percent

    class Meta:
        ordering = ('-created',)
        verbose_name = "SWP - Job Setup"


# 4. Expect The Unexpected
class SWPExpectTheUnexpected(models.Model):
    swp = models.OneToOneField('safe_driver.SafeDriveSWP', on_delete=models.CASCADE, null=False)

    use_designated_walkways = models.IntegerField(_('Use Designated Walkways'), choices=NUMBER_CHOICES, default=0)
    place_and_secure_objects = models.IntegerField(_('Place and Secure Objects'), choices=NUMBER_CHOICES, default=0)
    face_work_flow = models.IntegerField(_('Face Work Flow'), choices=NUMBER_CHOICES, default=0)
    use_caution_when_opening_doors = models.IntegerField(_('Use Caution When Opening Doors'), choices=NUMBER_CHOICES,
                                                         default=0)
    know_location_of_emergency_equipment = models.IntegerField(_('Know Location of Emergency Equipment'),
                                                               choices=NUMBER_CHOICES, default=0)
    verify_proper_egress = models.IntegerField(_('Verify Proper Egress'), choices=NUMBER_CHOICES, default=0)
    look_for_Sharp_splintery_cutting_hazards = models.IntegerField(_('Look for Sharp Splintery Cutting Hazards'),

                                                                   choices=NUMBER_CHOICES, default=0)

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    @property
    def possible_points(self):
        points = 5 * 7
        total = model_fields_possible_points(self, self._meta.get_fields())
        return total

    @property
    def points_received(self):
        # points = self.use_designated_walkways + self.place_and_secure_objects + self.face_work_flow + \
        #          self.use_caution_when_opening_doors + self.know_location_of_emergency_equipment + \
        #          self.verify_proper_egress + self.look_for_Sharp_splintery_cutting_hazards
        total = model_fields_received_points(self, self._meta.get_fields())
        return total

    @property
    def percent_effective(self):
        percent = 0
        if self.possible_points > 0 and self.possible_points >= self.points_received:
            percent = (self.points_received / self.possible_points) * 100
        return '%s' % percent

    class Meta:
        ordering = ('-created',)
        verbose_name = "SWP - Expect The Unexpected"


# 5. Pushing and Pulling
class SWPPushingAndPulling(models.Model):
    swp = models.OneToOneField('safe_driver.SafeDriveSWP', on_delete=models.CASCADE, null=False)

    keeps_work_in_front = models.IntegerField(_('Keeps Work in Front'), choices=NUMBER_CHOICES, default=0)
    seek_assistant = models.IntegerField(_('Seeks Assistant when moving heavy or awkward objects'),
                                         choices=NUMBER_CHOICES, default=0)
    keep_arms_slightly_bent = models.IntegerField(_('Keep arms slightly bent when working repetitive motions'),
                                                  choices=NUMBER_CHOICES, default=0)
    heavy_off_shaped_objects = models.IntegerField(_('Heavy odd shaped objects'), choices=NUMBER_CHOICES, default=0)

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    @property
    def possible_points(self):
        points = 5 * 4
        total = model_fields_possible_points(self, self._meta.get_fields())
        return total

    @property
    def points_received(self):
        # points = self.keeps_work_in_front + self.seek_assistant + self.keep_arms_slightly_bent + \
        #          self.heavy_off_shaped_objects
        total = model_fields_received_points(self, self._meta.get_fields())
        return total

    @property
    def percent_effective(self):
        percent = 0
        if self.possible_points > 0 and self.possible_points >= self.points_received:
            percent = (self.points_received / self.possible_points) * 100
        return '%s' % percent

    class Meta:
        ordering = ('-created',)
        verbose_name = "SWP - Pushing and Pulling"


# 6. End Range Motion
class SWPEndRangeMotion(models.Model):
    swp = models.OneToOneField('safe_driver.SafeDriveSWP', on_delete=models.CASCADE, null=False)

    position_shoulder_parallel = models.IntegerField(_('Position shoulder parallel to the object'),
                                                     choices=NUMBER_CHOICES, default=0)
    use_equipment = models.IntegerField(_('Use equipment to minimize end range motions'), choices=NUMBER_CHOICES,
                                        default=0)

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    @property
    def possible_points(self):
        points = 5 * 2
        total = model_fields_possible_points(self, self._meta.get_fields())
        return total

    @property
    def points_received(self):
        # points = self.position_shoulder_parallel + self.use_equipment
        total = model_fields_received_points(self, self._meta.get_fields())
        return total

    @property
    def percent_effective(self):
        percent = 0
        if self.possible_points > 0 and self.possible_points >= self.points_received:
            percent = (self.points_received / self.possible_points) * 100
        return '%s' % percent

    class Meta:
        ordering = ('-created',)
        verbose_name = "SWP - End Range Motion"


# 7. Keys Lifting and Lowering
class SWPKeysLiftingAndLowering(models.Model):
    swp = models.OneToOneField('safe_driver.SafeDriveSWP', on_delete=models.CASCADE, null=False)

    close_to_object_shoulders = models.IntegerField(_('Get close to the object-Shoulders Parallel to the ground'),
                                                    choices=NUMBER_CHOICES, default=0)
    position_feet = models.IntegerField(_('Position Feet'), choices=NUMBER_CHOICES, default=0)
    bend_your_knees = models.IntegerField(_('Bend your knees'), choices=NUMBER_CHOICES, default=0)
    test_weight = models.IntegerField(_('Test weight'), choices=NUMBER_CHOICES, default=0)
    firm_grip = models.IntegerField(_('Firm Grip'), choices=NUMBER_CHOICES, default=0)
    smooth_steady_lift = models.IntegerField(_('Smooth Steady Lift'), choices=NUMBER_CHOICES, default=0)
    pivot_feet_never_twist = models.IntegerField(_('Pivot feet, never twist'), choices=NUMBER_CHOICES, default=0)
    use_equipment_designed = models.IntegerField(_('Use equipment designed for heavy lifts'), choices=NUMBER_CHOICES,
                                                 default=0)

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    @property
    def possible_points(self):
        points = 5 * 8
        total = model_fields_possible_points(self, self._meta.get_fields())
        return total

    @property
    def points_received(self):
        # points = self.close_to_object_shoulders + self.bend_your_knees + self.test_weight + self.firm_grip + \
        #          self.smooth_steady_lift + self.pivot_feet_never_twist + self.use_equipment_designed
        total = model_fields_received_points(self, self._meta.get_fields())
        return total

    @property
    def percent_effective(self):
        percent = 0
        if self.possible_points > 0 and self.possible_points >= self.points_received:
            percent = (self.points_received / self.possible_points) * 100
        return '%s' % percent

    class Meta:
        ordering = ('-created',)
        verbose_name = "SWP - Keys Lifting and Lowering"


# 8. Be aware of cutting Hazards and Sharp Objects
class SWPCuttingHazardsAndSharpObjects(models.Model):
    swp = models.OneToOneField('safe_driver.SafeDriveSWP', on_delete=models.CASCADE, null=False)

    designate_storage_area = models.IntegerField(_('Designate storage area for sharp objects'), choices=NUMBER_CHOICES,
                                                 default=0)
    use_tabe_guns_properly = models.IntegerField(_('Use tape guns properly'), choices=NUMBER_CHOICES, default=0)
    aware_of_sharp_edges = models.IntegerField(_('Aware of Sharp Edges (cardboard etc.)'), choices=NUMBER_CHOICES,
                                               default=0)
    wares_gloves_when_possible = models.IntegerField(_('Wares gloves when possible'), choices=NUMBER_CHOICES, default=0)
    keep_blade_short = models.IntegerField(_('Keep the blade as short as possible'), choices=NUMBER_CHOICES, default=0)
    retract_blade = models.IntegerField(_('Retract blade as soon as possible'), choices=NUMBER_CHOICES, default=0)
    angle_cutting_surface = models.IntegerField(_('Angle cutting surface away from your body'), choices=NUMBER_CHOICES,
                                                default=0)
    apply_consisten_firm_pressure = models.IntegerField(_('Apply consistent firm pressure'), choices=NUMBER_CHOICES,
                                                        default=0)
    keep_thumbs_away = models.IntegerField(_('Keep thumbs away from cutting surface'), choices=NUMBER_CHOICES,
                                           default=0)
    dispose_of_used_blades = models.IntegerField(_('Dispose of used blades in puncture resistant container'),
                                                 choices=NUMBER_CHOICES, default=0)

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    @property
    def possible_points(self):
        points = 5 * 10
        total = model_fields_possible_points(self, self._meta.get_fields())
        return total

    @property
    def points_received(self):
        # points = self.designate_storage_area + self.use_tabe_guns_properly + self.aware_of_sharp_edges + \
        #          self.wares_gloves_when_possible + self.keep_blade_short + self.retract_blade + \
        #          self.angle_cutting_surface + self.apply_consisten_firm_pressure + self.keep_thumbs_away \
        #          + self.dispose_of_used_blades
        total = model_fields_received_points(self, self._meta.get_fields())
        return total

    @property
    def percent_effective(self):
        percent = 0
        if self.possible_points > 0 and self.possible_points >= self.points_received:
            percent = (self.points_received / self.possible_points) * 100
        return '%s' % percent

    class Meta:
        ordering = ('-created',)
        verbose_name = "SWP - Be aware of cutting Hazards and Sharp Objects"


# 9. Keys to avoiding slips and falls
class SWPKeysToAvoidingSlipsAndFalls(models.Model):
    swp = models.OneToOneField('safe_driver.SafeDriveSWP', on_delete=models.CASCADE, null=False)

    walks_with_intent = models.IntegerField(_('Walks with intent (Never run)'), choices=NUMBER_CHOICES, default=0)
    maintain_balance = models.IntegerField(_('Maintain balance with firm footing'), choices=NUMBER_CHOICES, default=0)
    stays_off = models.IntegerField(_('Stays off moving belts, rollers and chutes'), choices=NUMBER_CHOICES, default=0)
    scan_work_area = models.IntegerField(_('Scan work area, Looks where you step-step where you look'),
                                         choices=NUMBER_CHOICES, default=0)
    aware_of_changing_conditions = models.IntegerField(
        _('Be aware of changing conditions, (make adjustments as needed)'),
        choices=NUMBER_CHOICES, default=0)
    keep_walk_paths_clear_and_clean = models.IntegerField(_('Keep walk paths clear and clean'),
                                                          choices=NUMBER_CHOICES, default=0)
    face_ladders_and_equipment = models.IntegerField(_('Face ladders and equipment ascending-descending'),
                                                     choices=NUMBER_CHOICES, default=0)
    use_three_points_of_contact = models.IntegerField(
        _('Use three points of contact with ladders and equipment at all times'),
        choices=NUMBER_CHOICES, default=0)
    uses_hand_rails = models.IntegerField(_('Uses hand rails when available'), choices=NUMBER_CHOICES, default=0)
    uses_designated_routes = models.IntegerField(_('Uses designated routes when entering and exiting the building'),
                                                 choices=NUMBER_CHOICES, default=0)
    safety_chains_and_gates_used_properly = models.IntegerField(_('Are safety chains and gates being used properly'),
                                                                choices=NUMBER_CHOICES, default=0)
    four_feet_rule = models.IntegerField(_('4 foot rule near unsecured ledges'), choices=NUMBER_CHOICES, default=0)

    notes = models.TextField(_('Notes'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.pk

    @property
    def possible_points(self):
        points = 5 * 12
        total = model_fields_possible_points(self, self._meta.get_fields())
        return total

    @property
    def points_received(self):
        # points = self.walks_with_intent + self.maintain_balance + self.stays_off + self.scan_work_area \
        #          + self.aware_of_changing_conditions + self.keep_walk_paths_clear_and_clean + \
        #          self.face_ladders_and_equipment + self.use_three_points_of_contact + self.uses_hand_rails + \
        #          self.uses_designated_routes + self.safety_chains_and_gates_used_properly + self.four_feet_rule

        total = model_fields_received_points(self, self._meta.get_fields())
        return total

    @property
    def percent_effective(self):
        percent = 0
        if self.possible_points > 0 and self.possible_points >= self.points_received:
            percent = (self.points_received / self.possible_points) * 100
        return '%s' % percent

    class Meta:
        ordering = ('-created',)
        verbose_name = "SWP - Keys to avoiding slips and falls"
        verbose_name_plural = "SWP - Keys to avoiding slips and falls"
