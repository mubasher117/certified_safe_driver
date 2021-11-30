import React, { useRef, useState } from 'react';
import ReactToPrint from 'react-to-print';
import { useDispatch, connect } from 'react-redux';
import Backdrop from '@material-ui/core/Backdrop';
import CircularProgress from '@material-ui/core/CircularProgress';
import PrintProvider, { Print } from 'react-easy-print';
import jsPDF from 'jspdf';
import * as html2canvas from 'html2canvas';
import { getStudentReport } from '../../actions/studentsActions';

import './styles.css';
import logo from '../../assets/images/csd-logo.png';

class StudentDetailedReports extends React.Component {
  state = {
    company: 'Coca Cola',
    department: 5346,
    routeNumber: 345,
    startTime: '',
    endTime: '',
    onTime: 'Yes',
    keysReady: 'Yes',
    timecardSystemReady: 'Yes',
    equipmentReady: 'Yes',
    equipmentClean: 'Yes',
    startOdometer: '6685',
    finishOdometer: 346,
    miles: 'miles',
  };

  handleChange = ({ target: { value, id } }) => {
    this.setState({ [id]: value });
  };

  render = () => {
    const {
      studentReport: {
        id,
        first_name,
        last_name,
        pas: {
          cab_safety: { cab_chemicals, cab_obstructions, can_distractions, seat_belt } = {},
          start_engine: { park_brake_applied, uses_starter_properly, trans_in_park_or_neutral } = {},
          engine_operation: { over_revving, check_gauges, start_off_smoothly } = {},
          brakes_and_stopping: {
            checks_rear_or_gives_warning,
            full_stop_or_smooth,
            down_shifts,
            uses_foot_brake_only,
            hand_valve_use,
            does_not_roll_back,
            does_not_fan,
            engine_assist,
            avoids_sudden_stops,
          } = {},
          eye_movement_and_mirror: {
            eyes_ahead,
            follow_up_in_mirror,
            checks_mirror,
            scans_does_not_stare,
            avoid_billboards,
          } = {},
          recognizes_hazards: { uses_horn, makes_adjustments, path_of_least_resistance } = {},
          lights_and_signals: {
            proper_use_of_lights,
            adjust_speed,
            signals_well_in_advance,
            cancels_signal,
            use_of_4_ways,
          } = {},
          steering: { over_steers, floats, poisture_and_grip, centered_in_lane } = {},
          backing: {
            size_of_situation,
            driver_side_back,
            check_rear,
            gets_attention,
            backs_slowly,
            rechecks_conditions,
            uses_other_aids,
            steers_correctly,
            does_not_hit_dock,
            use_spotter,
          } = {},
          speed: { adjust_to_conditions, speed, proper_following_distance, speed_on_curves } = {},
          intersections: {
            approach_decision_point,
            clear_intersection,
            check_mirrors,
            full_stop,
            times_light_or_starts,
            yields_right_of_way,
            steering_axel_staright,
            proper_speed_or_gear,
            leaves_space,
            stop_lines,
            railroad_crossings,
          } = {},
          turning: {
            signals_correctly,
            gets_in_proper_time,
            downshifts_to_pulling_gear,
            handles_light_correctly,
            setup_and_execution,
            turn_speed,
            mirror_follow_up,
            turns_lane_to_lane,
          } = {},
          parking: {
            does_not_hit_curb,
            curbs_wheels,
            chock_wheels,
            park_brake_applied: park_brake_applied_parking,
            trans_in_neutral,
            engine_off,
          } = {},
          hills: { proper_gear_up_down, avoids_rolling_back, test_brakes_prior } = {},
          passing: { sufficient_space_to_pass, signals_property, check_mirrors: check_mirrors_passing } = {},
          general_safety_and_dot_adherence: {
            avoids_crowding_effect,
            stays_right_or_correct_lane,
            aware_hours_of_service,
            proper_use_off_mirrors,
            self_confident_not_complacement,
            check_instruments,
            uses_horn_properly,
            maintains_dot_log,
            drives_defensively,
            company_haz_mat_protocol,
            air_cans_or_line_moisture_free,
            avoid_distractions_while_driving,
            works_safely_to_avoid_injuries,
          } = {},
          passenger_safety: {
            everyone_seated,
            holding_hand_rails_standing,
            no_one_past_standee_line,
            seatbelts_on,
            steps_clear,
          } = {},
          rail_road_crossing: {
            signal_and_activate_4_ways,
            open_window_and_door,
            look_listen_clear,
            signal_and_merge_into_traffic,
            stop_prior,
          } = {},
          start_time,
          end_time,
          driver_signature,
          evaluator_signature,
          company_rep_signature,
          company_rep_name,
        } = {},
        info: {
          driver_license_class,
          driver_license_expire_date,
          dot_expiration_date,
          endorsements,
          corrective_lense_required,
          location,
          company: { name: company_name } = {},
          ...company
        } = {},
        ...studentReport
      },
    } = this.props;

    console.log(
      'btw',
      company,
      studentReport,
      driver_signature,
      evaluator_signature,
      company_rep_signature,
      company_rep_name,
    );

    return (
      <>
        <div className="row">
          <div id="first-page">
            <div className="col-sm-12">
              <img src={logo} style={{ position: 'relative', top: 10 }} width="200" alt="" />
              <div className="row">
                <div className="col-sm-12 text-center">
                  <h3>Certified Safe Driver Inc.</h3>
                  <h4>Passenger Vehicle</h4>
                </div>
              </div>
              <div className="row">
                <div className="col-sm-12">
                  <div className="row">
                    <div className="col-sm-6"></div>
                    <div className="col-sm-6">
                      <span>Company Name</span>
                      <span className="value" id="company">
                        {company_name}
                      </span>
                    </div>
                  </div>
                </div>

                <div className="col-sm-4 text-center">
                  <div>
                    <span>Date:</span>
                    <span className="value" id="dateTime">
                      {new Date().toLocaleDateString()}
                    </span>
                  </div>
                  <div>
                    <span>Employee #:</span>
                    <span className="value" id="employeeId">
                      {id}
                    </span>
                  </div>
                  <div>
                    <span>Driver Name:</span>
                    <span className="value" id="driverName">
                      {first_name} {last_name}
                    </span>
                  </div>
                </div>
                <div className="col-sm-4 text-center">
                  <div className="row">
                    <div className="col-sm-6">
                      <div>
                        <span>License Exp. date:</span>
                        <span className="value" id="driverLicenseExpirationDate">
                          {driver_license_expire_date}
                        </span>
                      </div>
                    </div>
                    <div className="col-sm-6">
                      <div>
                        <span>Class:</span>
                        <span className="value" id="driverLicenseClass">
                          {driver_license_class}
                        </span>
                      </div>
                    </div>
                  </div>
                  <div>
                    <span>History reviewed:</span>
                    <span className="value" id="driverHistoryReviewed"></span>
                  </div>
                </div>
                <div className="col-sm-4 text-center">
                  <div>
                    <span>Endorsements:</span>
                    <span className="value" id="endorsements">
                      {endorsements ? 'Yes' : 'No'}
                    </span>
                  </div>
                  <div>
                    <span>Dot Exp. date:</span>
                    <span className="value" id="dotExpirationDate">
                      {dot_expiration_date}
                    </span>
                  </div>
                </div>
              </div>
            </div>
            <div className="col-sm-12 text-center" style={{ backgroundColor: 'rgb(166, 166, 236)' }}>
              <span>
                5 = performed correctly-4 = Reinforced - 3 = corrected &amp; reinforced - 2 = Multi corrections &amp;
                reinforced - 1 = unacceptable
              </span>
            </div>
            <div className="col-sm-12 text-center">
              <div className="row">
                <div className="col-sm-6">
                  <span>Start Time:</span>
                  <span className="value" id="startTime">
                    {start_time}
                  </span>
                </div>
                <div className="col-sm-6">
                  <span>End Time:</span>
                  <span className="value" id="endTime">
                    {end_time}
                  </span>
                </div>
              </div>
            </div>

            <div className="row" id="pdf_template_1" style={{ paddingLeft: 30 }}>
              <div className="col-sm-12 col-xs-12 pdf-sections">
                <div className="pdf-section-block">
                  <div className="pdf-section-block-number">
                    <span>1)</span>
                  </div>
                  <div className="pdf-section-block-title">
                    <span>Cab Safety</span>
                  </div>
                  <div className="pdf-section-block-content">
                    <div className="row">
                      <div className="col-sm-10">a) Seat belt</div>
                      <input defaultValue={seat_belt} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">b) Cab distractions</div>
                      <input defaultValue={can_distractions} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">c) Cab obstruction</div>
                      <input defaultValue={cab_obstructions} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">d) Cab Chemicals</div>
                      <input defaultValue={cab_chemicals} className="col-sm-2" />
                    </div>
                  </div>
                </div>

                <div className="pdf-section-block f-right">
                  <div className="pdf-section-block-number">
                    <span>2)</span>
                  </div>
                  <div className="pdf-section-block-title">
                    <span>Start Engine</span>
                  </div>
                  <div className="pdf-section-block-content">
                    <div className="row">
                      <div className="col-sm-10">a)Park brake applied</div>
                      <input defaultValue={park_brake_applied} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">b)Trans in Neutral</div>
                      <input defaultValue={trans_in_park_or_neutral} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">c)Uses Starter properly</div>
                      <input defaultValue={uses_starter_properly} className="col-sm-2" />
                    </div>
                  </div>
                </div>

                <div className="pdf-section-block">
                  <div className="pdf-section-block-number">
                    <span>3)</span>
                  </div>
                  <div className="pdf-section-block-title">
                    <span>Engine Operation</span>
                  </div>
                  <div className="pdf-section-block-content">
                    <div className="row">
                      <div className="col-sm-10">a)Over revving</div>
                      <input defaultValue={over_revving} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">b)Check Gauges</div>
                      <input defaultValue={check_gauges} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">c)Start off smoothly</div>
                      <input defaultValue={start_off_smoothly} className="col-sm-2" />
                    </div>
                  </div>
                </div>

                <div className="pdf-section-block f-right">
                  <div className="pdf-section-block-number">
                    <span>4)</span>
                  </div>
                  <div className="pdf-section-block-title">
                    <span>Use of brakes and stopping</span>
                  </div>
                  <div className="pdf-section-block-content">
                    <div className="row">
                      <div className="col-sm-10">a)Checks rear/gives warning</div>
                      <input defaultValue={checks_rear_or_gives_warning} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">b)Full stop/smooth (no rebound)</div>
                      <input defaultValue={full_stop_or_smooth} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">c)Doesn't fan</div>
                      <input defaultValue={does_not_fan} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">d)Down shifts</div>
                      <input defaultValue={down_shifts} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">e)Uses foot brake only</div>
                      <input defaultValue={uses_foot_brake_only} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">f)Hand valve use</div>
                      <input defaultValue={hand_valve_use} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">g)Doesn't roll back</div>
                      <input defaultValue={does_not_roll_back} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">h)Engine assist</div>
                      <input defaultValue={engine_assist} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">i)Avoids sudden stops</div>
                      <input defaultValue={avoids_sudden_stops} className="col-sm-2" />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div id="second-page">
            <div className="row" id="pdf_template_1" style={{ paddingLeft: 30 }}>
              <div className="col-sm-12 col-xs-12 pdf-sections">
                <div className="pdf-section-block">
                  <div className="pdf-section-block-number">
                    <span>5)</span>
                  </div>
                  <div className="pdf-section-block-title">
                    <span>Passenger Safety</span>
                  </div>
                  <div className="pdf-section-block-content">
                    <div className="row">
                      <div className="col-sm-10">a)No One Past Standee Line</div>
                      <input defaultValue={no_one_past_standee_line} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">b)Steps Clear</div>
                      <input defaultValue={steps_clear} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">c)Everyone Seated</div>
                      <input defaultValue={everyone_seated} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">d)Seatbelts On (if Required)</div>
                      <input defaultValue={seatbelts_on} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">e)Holding Hand Rails Standing</div>
                      <input defaultValue={holding_hand_rails_standing} className="col-sm-2" />
                    </div>
                  </div>
                </div>

                <div className="pdf-section-block f-right">
                  <div className="pdf-section-block-number">
                    <span>6)</span>
                  </div>
                  <div className="pdf-section-block-title">
                    <span>Eye Movement - Mirror Use</span>
                  </div>
                  <div className="pdf-section-block-content">
                    <div className="row">
                      <div className="col-sm-10">a)Eyes ahead </div>
                      <input defaultValue={eyes_ahead} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">b)Follow-up in mirror</div>
                      <input defaultValue={follow_up_in_mirror} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">c)Checks mirrors 5 to 8 sec's</div>
                      <input defaultValue={checks_mirror} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">d)Scans doesn't stare</div>
                      <input defaultValue={scans_does_not_stare} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">e)Avoid Billboards</div>
                      <input defaultValue={avoid_billboards} className="col-sm-2" />
                    </div>
                  </div>
                </div>

                <div className="pdf-section-block">
                  <div className="pdf-section-block-number">
                    <span>7)</span>
                  </div>
                  <div className="pdf-section-block-title">
                    <span>Recognizes Hazards</span>
                  </div>
                  <div className="pdf-section-block-content">
                    <div className="row">
                      <div className="col-sm-10">a)Uses Horn to communicate </div>
                      <input defaultValue={uses_horn} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">b)Makes adjustments</div>
                      <input defaultValue={makes_adjustments} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">c)Path of least resistance</div>
                      <input defaultValue={path_of_least_resistance} className="col-sm-2" />
                    </div>
                  </div>
                </div>

                <div className="pdf-section-block f-right">
                  <div className="pdf-section-block-number">
                    <span>8)</span>
                  </div>
                  <div className="pdf-section-block-title">
                    <span>Lights &amp; Signals</span>
                  </div>
                  <div className="pdf-section-block-content">
                    <div className="row">
                      <div className="col-sm-10">a)Proper use of lights </div>
                      <input defaultValue={proper_use_of_lights} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">b)Adjust speed</div>
                      <input defaultValue={adjust_speed} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">c)Signals well in advance</div>
                      <input defaultValue={signals_well_in_advance} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">d)Cancels signal</div>
                      <input defaultValue={cancels_signal} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">e)Use of 4 ways</div>
                      <input defaultValue={use_of_4_ways} className="col-sm-2" />
                    </div>
                  </div>
                </div>

                <div className="pdf-section-block">
                  <div className="pdf-section-block-number">
                    <span>9)</span>
                  </div>
                  <div className="pdf-section-block-title">
                    <span>Steering</span>
                  </div>
                  <div className="pdf-section-block-content">
                    <div className="row">
                      <div className="col-sm-10">a)Over Steers</div>
                      <input defaultValue={over_steers} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">b)Floats</div>
                      <input defaultValue={floats} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">c)Posture &amp; grip</div>
                      <input defaultValue={poisture_and_grip} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">d)Centered in lane</div>
                      <input defaultValue={centered_in_lane} className="col-sm-2" />
                    </div>
                  </div>
                </div>

                <div className="pdf-section-block f-right">
                  <div className="pdf-section-block-number">
                    <span>10)</span>
                  </div>
                  <div className="pdf-section-block-title">
                    <span>Backing</span>
                  </div>
                  <div className="pdf-section-block-content">
                    <div className="row">
                      <div className="col-sm-10">a)Size up situation</div>
                      <input defaultValue={size_of_situation} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">b)Driver side back</div>
                      <input defaultValue={driver_side_back} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">c)Check rear</div>
                      <input defaultValue={check_rear} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">d)Gets attention</div>
                      <input defaultValue={gets_attention} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">e)Backs slowly</div>
                      <input defaultValue={backs_slowly} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">f)Re-checks conditions</div>
                      <input defaultValue={rechecks_conditions} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">g)Uses other aids</div>
                      <input defaultValue={uses_other_aids} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">h)Steers correctly</div>
                      <input defaultValue={steers_correctly} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">i)Doesn't hit dock</div>
                      <input defaultValue={does_not_hit_dock} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">j)Use a Spotter (If Applicable)</div>
                      <input defaultValue={use_spotter} className="col-sm-2" />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div id="third-page">
            <div className="row" id="pdf_template_1" style={{ paddingLeft: 30 }}>
              <div className="col-sm-12 col-xs-12 pdf-sections">
                <div className="pdf-section-block">
                  <div className="pdf-section-block-number">
                    <span>11)</span>
                  </div>
                  <div className="pdf-section-block-title">
                    <span>Speed</span>
                  </div>
                  <div className="pdf-section-block-content">
                    <div className="row">
                      <div className="col-sm-10">a)Adjust to conditions</div>
                      <input defaultValue={adjust_to_conditions} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">b)Speed</div>
                      <input defaultValue={speed} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">c)Proper following distance</div>
                      <input defaultValue={proper_following_distance} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">d)Speed on curves</div>
                      <input defaultValue={speed_on_curves} className="col-sm-2" />
                    </div>
                  </div>
                </div>

                <div className="pdf-section-block f-right">
                  <div className="pdf-section-block-number">
                    <span>12)</span>
                  </div>
                  <div className="pdf-section-block-title">
                    <span>Intersections</span>
                  </div>
                  <div className="pdf-section-block-content">
                    <div className="row">
                      <div className="col-sm-10">a)Approach - decision point</div>
                      <input defaultValue={approach_decision_point} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">b)Clear Intersection L-R-L</div>
                      <input defaultValue={clear_intersection} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">c)Check mirrors</div>
                      <input defaultValue={check_mirrors} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">d)Full stop when needed</div>
                      <input defaultValue={full_stop} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">e)Times light or starts too fast</div>
                      <input defaultValue={times_light_or_starts} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">f)Steering axle straight</div>
                      <input defaultValue={steering_axel_staright} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">g)Yields right-of-way</div>
                      <input defaultValue={yields_right_of_way} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">h)Proper speed/gear</div>
                      <input defaultValue={proper_speed_or_gear} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">i)Leaves space for an out</div>
                      <input defaultValue={leaves_space} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">j)Stop lines - crosswalks</div>
                      <input defaultValue={stop_lines} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">k)Railroad crossings</div>
                      <input defaultValue={railroad_crossings} className="col-sm-2" />
                    </div>
                  </div>
                </div>

                <div className="pdf-section-block">
                  <div className="pdf-section-block-number">
                    <span>13)</span>
                  </div>
                  <div className="pdf-section-block-title">
                    <span>Turning</span>
                  </div>
                  <div className="pdf-section-block-content">
                    <div className="row">
                      <div className="col-sm-10">a)Signals correctly</div>
                      <input defaultValue={signals_correctly} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">b)Gets in proper lane</div>
                      <input defaultValue={gets_in_proper_time} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">c)Downshifts to pulling gear</div>
                      <input defaultValue={downshifts_to_pulling_gear} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">d)Handles light correctly</div>
                      <input defaultValue={handles_light_correctly} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">e)Set up &amp; execution</div>
                      <input defaultValue={setup_and_execution} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">f)Turn speed</div>
                      <input defaultValue={turn_speed} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">g)Mirror follow up</div>
                      <input defaultValue={mirror_follow_up} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">h)Turns lane to lane</div>
                      <input defaultValue={turns_lane_to_lane} className="col-sm-2" />
                    </div>
                  </div>
                </div>

                <div className="pdf-section-block f-right">
                  <div className="pdf-section-block-number">
                    <span>14)</span>
                  </div>
                  <div className="pdf-section-block-title">
                    <span>Parking</span>
                  </div>
                  <div className="pdf-section-block-content">
                    <div className="row">
                      <div className="col-sm-10">a)Doesn't hit curb</div>
                      <input defaultValue={does_not_hit_curb} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">b)Curbs wheels</div>
                      <input defaultValue={curbs_wheels} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">c)chock wheels (if required)</div>
                      <input defaultValue={chock_wheels} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">d)Park brake applied</div>
                      <input defaultValue={park_brake_applied_parking} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">e)Trans in neutral</div>
                      <input defaultValue={trans_in_neutral} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">f)Engine off - Takes keys</div>
                      <input defaultValue={engine_off} className="col-sm-2" />
                    </div>
                  </div>
                </div>

                <div className="pdf-section-block">
                  <div className="pdf-section-block-number">
                    <span>15)</span>
                  </div>
                  <div className="pdf-section-block-title">
                    <span>Hills</span>
                  </div>
                  <div className="pdf-section-block-content">
                    <div className="row">
                      <div className="col-sm-10">a)Proper gear up or down</div>
                      <input defaultValue={proper_gear_up_down} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">b)Avoids rolling back H/V</div>
                      <input defaultValue={avoids_rolling_back} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">c)Test brakes prior</div>
                      <input defaultValue={test_brakes_prior} className="col-sm-2" />
                    </div>
                  </div>
                </div>

                <div className="pdf-section-block">
                  <div className="pdf-section-block-number">
                    <span>16)</span>
                  </div>
                  <div className="pdf-section-block-title">
                    <span>Passing</span>
                  </div>
                  <div className="pdf-section-block-content">
                    <div className="row">
                      <div className="col-sm-10">a)Sufficient space to pass</div>
                      <input defaultValue={sufficient_space_to_pass} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">b)Signals properly</div>
                      <input defaultValue={signals_property} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">c)Checks mirrors</div>
                      <input defaultValue={check_mirrors_passing} className="col-sm-2" />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div id="fourth-page">
            <div className="row" id="pdf_template_1" style={{ paddingLeft: 30 }}>
              <div className="col-sm-12 col-xs-12 pdf-sections">
                <div className="pdf-section-block">
                  <div className="pdf-section-block-number">
                    <span>17)</span>
                  </div>
                  <div className="pdf-section-block-title">
                    <span>Railroad Crossing</span>
                  </div>
                  <div className="pdf-section-block-content">
                    <div className="row">
                      <div className="col-sm-10">a)Signal &amp; Activate 4-ways</div>
                      <input defaultValue={signal_and_activate_4_ways} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">b)Stop 10' to 50' prior</div>
                      <input defaultValue={stop_prior} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">c)Open window &amp; door</div>
                      <input defaultValue={open_window_and_door} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">d)Look, Listen &amp; Clear</div>
                      <input defaultValue={look_listen_clear} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">e)Signal &amp; merge into traffic</div>
                      <input defaultValue={signal_and_merge_into_traffic} className="col-sm-2" />
                    </div>
                  </div>
                </div>

                <div className="pdf-section-block f-right">
                  <div className="pdf-section-block-number">
                    <span>18)</span>
                  </div>
                  <div className="pdf-section-block-title">
                    <span>General safety and DOT adherence</span>
                  </div>
                  <div className="pdf-section-block-content">
                    <div className="row">
                      <div className="col-sm-10">a)Avoids crowding effect</div>
                      <input defaultValue={avoids_crowding_effect} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">b)Stays to the right / correct lane</div>
                      <input defaultValue={stays_right_or_correct_lane} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">c)Aware of Hours of Service</div>
                      <input defaultValue={aware_hours_of_service} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">d)Proper use of mirrors</div>
                      <input defaultValue={proper_use_off_mirrors} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">e)Self confident not complacent </div>
                      <input defaultValue={self_confident_not_complacement} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">f)Checks instruments</div>
                      <input defaultValue={check_instruments} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">g)Uses horn properly</div>
                      <input defaultValue={uses_horn_properly} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">h)Maintains DOT log</div>
                      <input defaultValue={maintains_dot_log} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">i)Drives defensively</div>
                      <input defaultValue={drives_defensively} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">j)Company Haz Mat protocol</div>
                      <input defaultValue={company_haz_mat_protocol} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">k)Air cans/lines free of Moisture</div>
                      <input defaultValue={air_cans_or_line_moisture_free} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">l)Avoid distractions while driving</div>
                      <input defaultValue={avoid_distractions_while_driving} className="col-sm-2" />
                    </div>
                    <div className="row">
                      <div className="col-sm-10">m)Works safely to avoid injuries</div>
                      <input defaultValue={works_safely_to_avoid_injuries} className="col-sm-2" />
                    </div>
                  </div>
                </div>
              </div>

              <div className="col-sm-12  col-xs-12 signatures" style={{ paddingLeft: 52 }}>
                <div className="row">
                  <div className="col-sm-3 col-xs-3">
                    <table border='3"' style={{ width: 360 }}>
                      <tbody>
                        <tr>
                          <td style={{ borderBottom: '3px solid grey' }}>Possible Points: </td>
                          <td id="pointsPossible" style={{ borderBottom: '3px solid grey' }}>
                            595
                          </td>
                          <td rowSpan="2" style={{ borderLeft: '3px solid grey', borderRight: '3px solid grey' }}>
                            % Eff
                          </td>
                          <td rowSpan="2" id="pointsPercentage">
                            0.00 %
                          </td>
                        </tr>
                        <tr style={{ borderBottom: '3px solid grey' }}>
                          <td style={{ borderBottom: '3px solid grey' }}>Points Received: </td>
                          <td style={{ borderBottom: '3px solid grey' }} id="pointsReceived">
                            0
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                  <div className="col-sm-9 text-center">
                    <span>See supplimental</span>
                  </div>
                </div>
                <br />
                <div className="row">
                  <div className="col-sm-12">
                    <div className="row" style={{ border: '1px solid grey' }}>
                      <div className="col-sm-6" style={{ borderRight: '1px solid grey' }}>
                        <span>Corrective lens required:</span>
                        <span id="correctiveLensRequired">{corrective_lense_required ? 'Yes' : 'No'}</span>
                      </div>
                      <div className="col-sm-6">
                        <span>Power Unit:</span>
                        <span id="powerUnit">HDT</span>
                      </div>
                    </div>

                    <div className="row" style={{ border: '1px solid grey' }}>
                      <div className="col-sm-6" style={{ borderRight: '1px solid grey' }}>
                        <span>Evaluation Location:</span>
                        <span id="pdf_evaluation_location">{corrective_lense_required}</span>
                      </div>
                      <div className="col-sm-6">
                        <span>Driver Name:</span>
                        <span id="pdf_driver_name">
                          {first_name} {last_name}
                        </span>
                      </div>
                    </div>

                    <div className="row" style={{ border: '1px solid grey' }}>
                      <div className="col-sm-6" style={{ borderRight: '1px solid grey' }}>
                        <span></span>
                        <span></span>
                      </div>
                      <div className="col-sm-6">
                        <span>Driver License Expiration Date:</span>
                        <span id="driverLicenseExpirationDateBottom">{driver_license_expire_date}</span>
                      </div>
                    </div>
                  </div>
                </div>
                <div className="row">
                  <div className="col-sm-12 col-xs-12">
                    <div className="row">
                      <div className="col-sm-2 col-xs-2">
                        <span style={{ position: 'relative', bottom: '-27px' }}>Drivers Sign.:</span>
                      </div>
                      <div className="col-sm-6 col-xs-6" style={{ borderBottom: '2px solid grey', height: 70 }}>
                        <span id="pdf_driver_signature_name"></span>
                      </div>
                      <div className="col-sm-4 col-xs-4">
                        <br />
                        <br />
                        <br />

                        <div className="row">
                          <div className="col-sm-4 col-xs-4">
                            <span>Date:</span>
                          </div>
                          <div className="col-sm-8 col-xs-8" style={{ borderBottom: '2px solid grey' }}>
                            <span id="pdf_driver_signature_date"></span>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <br />
                  <div className="col-sm-12 col-xs-12">
                    <div className="row">
                      <div className="col-sm-2 col-xs-2">
                        <span style={{ position: 'relative', bottom: '-27px' }}>Evaluators Sign.:</span>
                      </div>
                      <div className="col-sm-6 col-xs-6" style={{ borderBottom: '2px solid grey', height: 70 }}>
                        <span id="pdf_evaluators_signature_name"></span>
                      </div>
                      <div className="col-sm-4 col-xs-4">
                        <br />
                        <br />
                        <br />

                        <div className="row">
                          <div className="col-sm-4 col-xs-4">
                            <span>Date:</span>
                          </div>
                          <div className="col-sm-8 col-xs-8" style={{ borderBottom: '2px solid grey' }}>
                            <span id="pdf_evaluators_signature_date"></span>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <br />
                  <div className="col-sm-12 col-xs-12">
                    <div className="row">
                      <div className="col-sm-2 col-xs-2">
                        <span style={{ position: 'relative', bottom: '-27px' }}>Company Rep. Sign.:</span>
                      </div>
                      <div className="col-sm-6 col-xs-6" style={{ borderBottom: '2px solid grey', height: 70 }}>
                        <span id="pdf_evaluators_signature_name"></span>
                      </div>
                      <div className="col-sm-4 col-xs-4">
                        <br />
                        <br />
                        <br />

                        <div className="row">
                          <div className="col-sm-4 col-xs-4">
                            <span>Date:</span>
                          </div>
                          <div className="col-sm-8 col-xs-8" style={{ borderBottom: '2px solid grey' }}>
                            <span id="pdf_company_rep_signature_date"></span>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <br />
              </div>
              <br />
              <br />
            </div>
          </div>

          <div id="pdf_template_2" style={{ paddingLeft: 30, maxWidth: 850 }}>
            <div className="pdf-sections-results">
              <table className="table table-bordered" id="table">
                <tbody>
                  <tr></tr>
                  <tr id="01_tr" className="pdf-table-row">
                    <td>1</td>
                    <td>Cab Safety</td>
                    <td id="01_possible_p">Possible Points: 0</td>
                    <td id="01_received_p">Points Received: 0</td>
                    <td id="01_effective_p">Percent Effective: 0.00 %</td>
                    <td id="01_note">Note: N/A </td>
                  </tr>
                  <tr></tr>
                  <tr id="02_tr" className="pdf-table-row">
                    <td>2</td>
                    <td>Start Engine</td>
                    <td id="02_possible_p">Possible Points: 0</td>
                    <td id="02_received_p">Points Received: 0</td>
                    <td id="02_effective_p">Percent Effective: 0.00 %</td>
                    <td id="02_note">Note: N/A </td>
                  </tr>
                  <tr></tr>
                  <tr id="03_tr" className="pdf-table-row">
                    <td>3</td>
                    <td>Engine Operation</td>
                    <td id="03_possible_p">Possible Points: 0</td>
                    <td id="03_received_p">Points Received: 0</td>
                    <td id="03_effective_p">Percent Effective: 0.00 %</td>
                    <td id="03_note">Note: N/A </td>
                  </tr>
                  <tr></tr>
                  <tr id="04_tr" className="pdf-table-row">
                    <td>4</td>
                    <td>Use of Brakes and Stopping</td>
                    <td id="04_possible_p">Possible Points: 0</td>
                    <td id="04_received_p">Points Received: 0</td>
                    <td id="04_effective_p">Percent Effective: 0.00 %</td>
                    <td id="04_note">Note: N/A </td>
                  </tr>
                  <tr></tr>
                  <tr id="05_tr" className="pdf-table-row">
                    <td>5</td>
                    <td>Passenger Safety</td>
                    <td id="05_possible_p">Possible Points: 0</td>
                    <td id="05_received_p">Points Received: 0</td>
                    <td id="05_effective_p">Percent Effective: 0.00 %</td>
                    <td id="05_note">Note: N/A </td>
                  </tr>
                  <tr></tr>
                  <tr id="06_tr" className="pdf-table-row">
                    <td>6</td>
                    <td>Eye Movement and Mirror Use</td>
                    <td id="06_possible_p">Possible Points: 0</td>
                    <td id="06_received_p">Points Received: 0</td>
                    <td id="06_effective_p">Percent Effective: 0.00 %</td>
                    <td id="06_note">Note: N/A </td>
                  </tr>
                  <tr></tr>
                  <tr id="07_tr" className="pdf-table-row">
                    <td>7</td>
                    <td>Recognizes Hazards</td>
                    <td id="07_possible_p">Possible Points: 0</td>
                    <td id="07_received_p">Points Received: 0</td>
                    <td id="07_effective_p">Percent Effective: 0.00 %</td>
                    <td id="07_note">Note: N/A </td>
                  </tr>
                  <tr></tr>
                  <tr id="08_tr" className="pdf-table-row">
                    <td>8</td>
                    <td>Lights and Signals</td>
                    <td id="08_possible_p">Possible Points: 0</td>
                    <td id="08_received_p">Points Received: 0</td>
                    <td id="08_effective_p">Percent Effective: 0.00 %</td>
                    <td id="08_note">Note: N/A </td>
                  </tr>
                  <tr></tr>
                  <tr id="09_tr" className="pdf-table-row">
                    <td>9</td>
                    <td>Steering</td>
                    <td id="09_possible_p">Possible Points: 0</td>
                    <td id="09_received_p">Points Received: 0</td>
                    <td id="09_effective_p">Percent Effective: 0.00 %</td>
                    <td id="09_note">Note: N/A </td>
                  </tr>
                  <tr></tr>
                  <tr id="10_tr" className="pdf-table-row">
                    <td>10</td>
                    <td>Backing</td>
                    <td id="10_possible_p">Possible Points: 0</td>
                    <td id="10_received_p">Points Received: 0</td>
                    <td id="10_effective_p">Percent Effective: 0.00 %</td>
                    <td id="10_note">Note: N/A </td>
                  </tr>
                  <tr></tr>
                  <tr id="11_tr" className="pdf-table-row">
                    <td>11</td>
                    <td>Speed</td>
                    <td id="11_possible_p">Possible Points: 0</td>
                    <td id="11_received_p">Points Received: 0</td>
                    <td id="11_effective_p">Percent Effective: 0.00 %</td>
                    <td id="11_note">Note: N/A </td>
                  </tr>
                  <tr></tr>
                  <tr id="12_tr" className="pdf-table-row">
                    <td>12</td>
                    <td>Intersections</td>
                    <td id="12_possible_p">Possible Points: 0</td>
                    <td id="12_received_p">Points Received: 0</td>
                    <td id="12_effective_p">Percent Effective: 0.00 %</td>
                    <td id="12_note">Note: N/A </td>
                  </tr>
                  <tr></tr>
                  <tr id="13_tr" className="pdf-table-row">
                    <td>13</td>
                    <td>Turning</td>
                    <td id="13_possible_p">Possible Points: 0</td>
                    <td id="13_received_p">Points Received: 0</td>
                    <td id="13_effective_p">Percent Effective: 0.00 %</td>
                    <td id="13_note">Note: N/A </td>
                  </tr>
                  <tr></tr>
                  <tr id="14_tr" className="pdf-table-row">
                    <td>14</td>
                    <td>Parking</td>
                    <td id="14_possible_p">Possible Points: 0</td>
                    <td id="14_received_p">Points Received: 0</td>
                    <td id="14_effective_p">Percent Effective: 0.00 %</td>
                    <td id="14_note">Note: N/A </td>
                  </tr>
                  <tr></tr>
                  <tr id="15_tr" className="pdf-table-row">
                    <td>15</td>
                    <td>Hills</td>
                    <td id="15_possible_p">Possible Points: 0</td>
                    <td id="15_received_p">Points Received: 0</td>
                    <td id="15_effective_p">Percent Effective: 0.00 %</td>
                    <td id="15_note">Note: N/A </td>
                  </tr>
                  <tr></tr>
                  <tr id="16_tr" className="pdf-table-row">
                    <td>16</td>
                    <td>Passing</td>
                    <td id="16_possible_p">Possible Points: 0</td>
                    <td id="16_received_p">Points Received: 0</td>
                    <td id="16_effective_p">Percent Effective: 0.00 %</td>
                    <td id="16_note">Note: N/A </td>
                  </tr>
                  <tr></tr>
                  <tr id="17_tr" className="pdf-table-row">
                    <td>17</td>
                    <td>Railroad Crossing</td>
                    <td id="17_possible_p">Possible Points: 0</td>
                    <td id="17_received_p">Points Received: 0</td>
                    <td id="17_effective_p">Percent Effective: 0.00 %</td>
                    <td id="17_note">Note: N/A </td>
                  </tr>
                  <tr></tr>
                  <tr id="18_tr" className="pdf-table-row">
                    <td>18</td>
                    <td>General safety and DOT adherence</td>
                    <td id="18_possible_p">Possible Points: 0</td>
                    <td id="18_received_p">Points Received: 0</td>
                    <td id="18_effective_p">Percent Effective: 0.00 %</td>
                    <td id="18_note">Note: N/A </td>
                  </tr>
                  <tr></tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </>
    );
  };
}

const Prienter = ({
  match: {
    params: { id },
  },
  studentReport,
  isLoading,
}) => {
  const dispatch = useDispatch();
  const componentRef = useRef();
  const [loader, setLoader] = useState(false);

  React.useEffect(() => {
    console.log('id', id);
    if (id) dispatch(getStudentReport(id));
  }, [id]);
  return (
    <div>
      {isLoading ? (
        <Backdrop open={isLoading}>
          <CircularProgress color="inherit" />
        </Backdrop>
      ) : (
        <>
          {/* <ReactToPrint
            copyStyles={true}
            trigger={() => <button>Print this out!</button>}
            content={() => componentRef.current}
          /> */}
          <button
            disabled={loader}
            style={{ cursor: 'pointer' }}
            onClick={async () => {
              setLoader(true);
              const pdf = new jsPDF();

              var doc = new jsPDF('p', 'mm', 'a4');
              var width = doc.internal.pageSize.getWidth();
              var height = doc.internal.pageSize.getHeight();

              const input = document.getElementById('first-page');
              await html2canvas(input).then(canvas => {
                const imgData = canvas.toDataURL('image/png');
                pdf.addImage(imgData, 'PNG', 0, 0, width - 10, height - 10);
                pdf.addPage();
              });
              const input2 = document.getElementById('second-page');
              await html2canvas(input2).then(canvas => {
                const imgData = canvas.toDataURL('image/png');
                pdf.addImage(imgData, 'PNG', 0, 0, width - 10, height - 10);
                pdf.addPage();
              });
              const input3 = document.getElementById('third-page');
              await html2canvas(input3).then(canvas => {
                const imgData = canvas.toDataURL('image/png');
                pdf.addImage(imgData, 'PNG', 0, 0, width - 10, height - 10);
                pdf.addPage();
              });
              const input4 = document.getElementById('fourth-page');
              await html2canvas(input4).then(canvas => {
                const imgData = canvas.toDataURL('image/png');
                pdf.addImage(imgData, 'PNG', 0, 0, width - 10, height - 10);
                pdf.addPage();
              });
              const input5 = document.getElementById('pdf_template_2');
              await html2canvas(input5).then(canvas => {
                const imgData = canvas.toDataURL('image/png');
                pdf.addImage(imgData, 'PNG', 0, 0, width - 10, height - 10);
                pdf.save('download.pdf');
                setLoader(false);
              });
            }}
          >
            {!loader ? 'Click me for print' : 'File Printing ...'}
          </button>
          <StudentDetailedReports ref={componentRef} studentReport={studentReport} />
        </>
      )}
    </div>
  );
};

const mapStateToProps = state => {
  const { studentReport, isLoading } = state.students;

  return {
    studentReport,
    isLoading,
  };
};

export default connect(mapStateToProps)(Prienter);
