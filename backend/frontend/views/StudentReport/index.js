import React, { useState, useRef } from 'react';
import ReactToPrint from 'react-to-print';

import './styles.css';
import logo from '../../assets/images/csd-logo.png';

class StudentReports extends React.Component {
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
    return (
      <div id="pdf_template" style={{ width: 1000, paddingLeft: 20 }}>
        <div className="row" id="pdf_template_1">
          <div className="pdf-sections">
            <div id="new_pdf" className="row">
              <div className="col-sm-2 col-xs-2 small-size">
                <p className="text-right">Date:</p>
                <p className="text-right">Employee #:</p>
                <p className="text-right">Driver Name:</p>
                <p className="text-right">Observer:</p>
              </div>
              <div className="col-sm-2 col-xs-2 bold small-size">
                <p className="text-left underLined" id="dateTime">
                  04/02/2020
                </p>
                <p className="text-left underLined" id="employeeId">
                  ll3456
                </p>
                <p className="text-left underLined" id="driverName">
                  Cola 11F Cola 11L
                </p>
                <p className="text-left" id="observer">
                  Instructor1 Instructor1
                </p>
              </div>
              <div className="col-sm-4 col-xs-4" id="header_logo">
                <div className="col-sm-12 text-center">
                  <img src={logo} width="200" alt="CSD" />
                </div>
                <h3 className="text-center">Certified Safe Driver, Inc.</h3>
              </div>
              <div className="col-sm-2 col-xs-2 small-size">
                <p className="text-right mb-0 p-10 mt-0">Company Name:</p>
                <p className="text-right mb-0 p-10 mt-0">Department:</p>
                <p className="text-right mb-0 p-10 mt-0">Route Number:</p>
              </div>
              <div className="col-sm-2 col-xs-2 bold small-size">
                <input
                  value={this.state.company}
                  onChange={this.handleChange}
                  className="text-center bordered mb-0"
                  id="company"
                />

                <input
                  value={this.state.department}
                  onChange={this.handleChange}
                  className="text-center bordered mb-0"
                  id="department"
                />
                <input
                  value={this.state.routeNumber}
                  onChange={this.handleChange}
                  className="text-center bordered mb-0"
                  id="routeNumber"
                />
                <p className="text-center bordered mb-0 mt-0" style={{ padding: 5 }}></p>
              </div>
              <div className="col-sm-12 col-xs-12">
                <div className="col-sm-12 col-xs-12 text-center bordered coloredBlue">
                  5 = performed correctly - 4 = Reinforced - 3 = corrected &amp; reinforced - 2 = Mult corrections &amp;
                  reinforced - 1 = unacceptable
                </div>
              </div>
              <div className="col-sm-12 col-xs-12" style={{ position: 'relative', zIndex: '14', background: '#fff' }}>
                <div className="col-sm-1 col-xs-1 p-0 small-size">
                  <p className="text-right mb-0 p-10">Start time:</p>
                  <p className="text-right mb-0 p-10">Finish time:</p>
                </div>
                <div className="col-sm-1 col-xs-1 bold" style={{ paddingLeft: 2 }}>
                  <input
                    style={{ marginTop: 15 }}
                    value={this.state.startTime}
                    onChange={this.handleChange}
                    className="text-center bordered mb-0"
                    id="startTime"
                  />
                  <input
                    style={{ marginTop: 15 }}
                    value={this.state.endTime}
                    onChange={this.handleChange}
                    className="text-center bordered mb-0"
                    id="endTime"
                  />
                </div>
                <div className="col-sm-2 col-xs-2 p-0 small-size">
                  <p className="text-right mb-0 p-10">On Time</p>
                  <p className="text-right mb-0 p-10">Keys Ready</p>
                  <p className="text-right mb-0 p-10">Timecard System Ready</p>
                </div>
                <div className="col-sm-1 col-xs-1 bold" style={{ paddingLeft: 2 }}>
                  <input
                    style={{ marginTop: 15 }}
                    value={this.state.keysReady}
                    onChange={this.handleChange}
                    className="text-center bordered mb-0"
                    id="keysReady"
                  />
                  <input
                    style={{ marginTop: 15 }}
                    value={this.state.timecardSystemReady}
                    onChange={this.handleChange}
                    className="text-center bordered mb-0"
                    id="timecardSystemReady"
                  />
                </div>
                <div className="col-sm-2 col-xs-1 p-0 small-size">
                  <p className="text-right mb-0 p-10">Equipment Ready</p>
                  <p className="text-right mb-0 p-10">Equipment Clean</p>
                </div>
                <div className="col-sm-1 col-xs-1 bold" style={{ paddingLeft: 2 }}>
                  <input
                    style={{ marginTop: 15 }}
                    value={this.state.equipmentReady}
                    onChange={this.handleChange}
                    className="text-center bordered mb-0"
                    id="equipmentReady"
                  />
                  <input
                    style={{ marginTop: 15 }}
                    value={this.state.equipmentClean}
                    onChange={this.handleChange}
                    className="text-center bordered mb-0"
                    id="equipmentClean"
                  />
                </div>
                <div className="col-sm-2 col-xs-2 p-0 small-size" style={{ paddingRight: 2 }}>
                  <p className="text-right mb-0 p-10">Start Odometer</p>
                  <p className="text-right mb-0 p-10">Finish Odometer</p>
                  <p className="text-right mb-0 p-10">Miles</p>
                </div>
                <div className="col-sm-2 col-xs-2 p-0" style={{ border: '1px solid #000' }}>
                  <div className="col-sm-12 col-xs-12 p-0">
                    <div className="col-sm-4 col-xs-4 bold p-0">
                      <input
                        style={{ marginTop: 15 }}
                        value={this.state.startOdometer}
                        onChange={this.handleChange}
                        className="text-center bordered mb-0"
                        id="startOdometer"
                      />
                    </div>
                    <div className="col-sm-4 col-xs-4 bold p-0">
                      <p className="text-center bordered mb-0" style={{ minHeight: 27, width: '100%' }}></p>
                    </div>
                  </div>
                  <div className="col-sm-12 col-xs-12 p-0">
                    <div className="col-sm-4 col-xs-4 bold p-0">
                      <input
                        style={{ marginTop: 15 }}
                        value={this.state.finishOdometer}
                        onChange={this.handleChange}
                        className="text-center bordered mb-0"
                        id="finishOdometer"
                      />
                    </div>
                    <div className="col-sm-4 col-xs-4 bold p-0">
                      <p className="text-center bordered mb-0" style={{ minHeight: 27, width: '100%' }}></p>
                    </div>
                  </div>
                  <div className="col-sm-12 col-xs-12 p-0">
                    <div className="col-sm-4 col-xs-4 bold p-0">
                      <input
                        style={{ marginTop: 15 }}
                        value={this.state.miles}
                        onChange={this.handleChange}
                        className="text-center bordered mb-0"
                        id="miles"
                      />
                    </div>
                    <div className="col-sm-4 col-xs-4 bold p-0">
                      <p className="text-center bordered mb-0" style={{ minHeight: 27, width: '100%' }}></p>
                    </div>
                    <div className="col-sm-4 col-xs-4 bold p-0">
                      <p className="text-center bordered mb-0" style={{ minHeight: 27, width: '100%' }}></p>
                    </div>
                  </div>
                </div>
              </div>

              <div className="col-sm-12 col-xs-12" style={{ top: '-3px' }}>
                <p id="table_note">If you change tractors, skip a line and start with new tractor miles</p>
                <table id="pdf_table" className="table table-striped table-bordered">
                  <thead>
                    <th style={{ width: '3%', verticalAlign: 'bottom' }}>
                      <p className="on_buttom">Time</p>
                    </th>
                    <th style={{ width: '3%', verticalAlign: 'bottom' }}>
                      <p className="on_buttom">Location</p>
                    </th>
                    <th style={{ width: '3%', verticalAlign: 'bottom' }}>
                      <p className="on_buttom">Trailer #</p>
                    </th>
                    <th style={{ width: '3%' }} className="pdf_tableHeader">
                      <p className="transformed">Start Work</p>
                    </th>
                    <th style={{ width: '3%' }} className="pdf_tableHeader">
                      <p className="transformed">Leave building</p>
                    </th>
                    <th style={{ width: '3%' }} className="pdf_tableHeader">
                      <p className="transformed">Travel Path</p>
                    </th>
                    <th style={{ width: '3%' }} className="pdf_tableHeader">
                      <p className="transformed">Speed</p>
                    </th>
                    <th style={{ width: '3%' }} className="pdf_tableHeader">
                      <p className="transformed">Idle Time</p>
                    </th>
                    <th style={{ width: '3%' }} className="pdf_tableHeader">
                      <p className="transformed">Plan Ahead</p>
                    </th>
                    <th style={{ width: '3%' }} className="pdf_tableHeader">
                      <p className="transformed">Turn Around</p>
                    </th>
                    <th style={{ width: '3%' }} className="pdf_tableHeader">
                      <p className="transformed">On Schedule</p>
                    </th>
                    <th style={{ width: '3%' }} className="pdf_tableHeader">
                      <p className="transformed">Customer Contact</p>
                    </th>
                    <th style={{ width: '3%' }} className="pdf_tableHeader">
                      <p className="transformed">Not Ready Situations</p>
                    </th>
                    <th style={{ width: '3%' }} className="pdf_tableHeader">
                      <p className="transformed">Brisk Pace</p>
                    </th>
                    <th style={{ width: '3%' }} className="pdf_tableHeader">
                      <p className="transformed">Finish Work</p>
                    </th>
                    <th style={{ width: '2%', verticalAlign: 'bottom' }} className="pdf_tableHeader">
                      <p className="on_buttom">Odometer</p>
                    </th>
                  </thead>
                  <tbody>
                    <tr id="insert_before_this_div">
                      <td style={{ border: 'none !important' }}></td>
                      <td style={{ border: 'none !important' }}></td>
                      <td style={{ border: 'none !important' }}></td>
                      <td id="total1">14</td>
                      <td id="total2">12</td>
                      <td id="total3">11</td>
                      <td id="total4">10</td>
                      <td id="total5">9</td>
                      <td id="total6">10</td>
                      <td id="total7">11</td>
                      <td id="total8">12</td>
                      <td id="total9">13</td>
                      <td id="total10">12</td>
                      <td id="total11">11</td>
                      <td id="total12">8</td>
                      <td>
                        <div className="odometer-divs"></div>
                        <div className="odometer-divs" style={{ borderRight: 'none' }} id="totalMiles">
                          133
                        </div>
                      </td>
                    </tr>
                    <tr>
                      <td style={{ border: 'none !important' }}></td>
                      <td style={{ border: 'none !important', textAlign: 'right' }}>Percent</td>
                      <td style={{ border: 'none !important' }}>Effective</td>
                      <td id="totalPercentage1">70%</td>
                      <td id="totalPercentage2">60%</td>
                      <td id="totalPercentage3">55%</td>
                      <td id="totalPercentage4">50%</td>
                      <td id="totalPercentage5">45%</td>
                      <td id="totalPercentage6">50%</td>
                      <td id="totalPercentage7">55%</td>
                      <td id="totalPercentage8">60%</td>
                      <td id="totalPercentage9">65%</td>
                      <td id="totalPercentage10">60%</td>
                      <td id="totalPercentage11">55%</td>
                      <td id="totalPercentage12">40%</td>
                      <td>
                        <div className="odometer-divs">
                          <b>Total</b>
                        </div>
                        <div className="odometer-divs" style={{ borderRight: 'none' }} id="totalPercentage">
                          56%
                        </div>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <div className="col-sm-12"></div>
            </div>
          </div>
          <br />
          <br />

          <div className="col-sm-12 col-xs-12 signatures">
            <br />

            <div className="row">
              <div className="col-sm-12 col-xs-12">
                <div className="row">
                  <div className="col-sm-2 col-xs-2">
                    <span style={{ position: 'relative', bottom: '-27px' }}>Employee Signature:</span>
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
                    <span style={{ position: 'relative', bottom: '-27px' }}>Trainer Signature:</span>
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
                    <span style={{ position: 'relative', bottom: '-27px' }}>Company rep.:</span>
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
          </div>
        </div>
      </div>
    );
  };
}

const Prienter = ({ history: { push } }) => {
  const componentRef = useRef();

  return (
    <div>
      <ReactToPrint trigger={() => <button>Print this out!</button>} content={() => componentRef.current} />
      <StudentReports ref={componentRef} />
    </div>
  );
};
export default Prienter;
