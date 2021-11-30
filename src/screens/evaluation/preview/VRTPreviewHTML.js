import React from 'react';
import _ from 'lodash';
import {counterToAlpha} from '../../../utils/function';
import moment from 'moment';

export default VRT = (
  dataModal,
  state,
  studentInfo,
  companyInfo,
  testInfo,
  instructorInfo,
  pdf,
) => {
  let htmlString = '';
  let level1Counter = 0;
  let level2Counter = 0;
  let level2HTML = '';
  let htmlsignature = '';
  let htmltableRow = '';
  let isQualified = null;
  let notQualifiedRemarks = '';

  var totalPossiblePoints = 0;
  var totalPointsReceived = 0;
  var totalPercentage = 0;
  console.log(testInfo)
  // console.log('studentInfo: ', studentInfo?.info.driver_license_number, studentInfo?.info, state.medical_card_expire_date );
  console.log(
    '********************************************************************',
  );
  console.log(
    '********************************************************************',
  );
  console.log(
    '********************************************************************',
  );
  console.log('GRAPH DATA');
  // console.log(state);
  console.log(
    '********************************************************************',
  );
  console.log(
    '********************************************************************',
  );
  console.log(
    '********************************************************************',
  );

  _.forEach(dataModal, (level1) => {
    // console.log('level1', level1)
    ++level1Counter;
    level2Counter = 0;
    level2HTML = '';
    if (level1.title == 'Qualified') {
      isQualified = state[level1.key];
    } else if (level1.title === 'Remarks') {
      console.log('IS QUALIFIED: ', state.qualified);
      console.log('remarks: ', state[level1.key]);
      if (state.qualified === false) {
        notQualifiedRemarks = state[level1.key];
      }
      // else  (
      //   level1.title === 'Remarks' &&
      //   state.qualified &&
      //   state.qualified === true
      // ) {
      //   notQualifiedRemarks = ''
      // }
    } else if (level1.value === undefined) {
      htmltableRow += `<tr style="border:3px solid #c4c4c4 !important;" class="section-results-pdf">
                                    <td>${level1Counter}</td>
                                    <td colspan="5">${level1.title}</td>
                                </tr>`;

      _.forEach(level1, (level2, key) => {
        if (
          key == 'key' ||
          key == 'title' ||
          level2.key == 'possible_points' ||
          level2.key == 'points_received' ||
          level2.key == 'percent_effective'
        ) {
          return null;
        }
        if (level2.key == 'notes') {
          ++level2Counter;
          level2HTML += `
                <div class="row">
                <div class="col-xs-12 col-sm-12 col-md-12"  ${
                  level2.title == 'Notes' && 'style="font-weight:bold"'
                }> ${
            level2.title == 'Notes' ? '' : `${counterToAlpha(level2Counter)})`
          }  ${
            level2.title == 'Notes' ? 'Note' : level2.title
          }<br /><div style="font-weight:normal">${
            state[level1.key][level2.key] == null
              ? ''
              : state[level1.key][level2.key]
          }</div></div>
              </div>
                `;
        } else {
          ++level2Counter;
          level2HTML += `
                    <div class="row">
                    <div class="col-sm-10 col-xs-10" ${
                      level2.title == 'Score' && 'style="font-weight:bold"'
                    }> ${
            level2.title == 'Score' ? '' : `${counterToAlpha(level2Counter)})`
          }  ${level2.title}</div>
                    <div class="col-sm-2 col-xs-2" id="01a">${
                      state[level1.key][level2.key] == null
                        ? 'N/A'
                        : level2.options == 4
                        ? state[level1.key][level2.key] == 0
                          ? 'N/A'
                          : state[level1.key][level2.key]
                        : state[level1.key][level2.key] == 0
                        ? 'N/A'
                        : state[level1.key][level2.key] == 1
                        ? 'Ok'
                        : state[level1.key][level2.key] == 2
                        ? 'Imp'
                        : state[level1.key][level2.key]
                    } </div>
                  </div>
                    `;
          if (key === 'score' && state[level1.key][level2.key] != 0) {
            totalPossiblePoints = totalPossiblePoints + 4;
            totalPointsReceived =
              totalPointsReceived + state[level1.key][level2.key];
          }
        }
       
        state?.instructions?.map((instruction, idx) => {
          // console.log("Inst: ", instruction.field_name.toLowerCase())
          // console.log(state[level1.key][level2])
          if (
            instruction.field_name.toLowerCase() === key &&
            instruction.db_table === state[level1.key]?.db_table &&
            state[level1.key][level2.key] == 2 
          ) {
            // console.log('key', key, 'instruction', state.instructions)
            let additionalText = '';
            switch (state[level1.key][level2.key]) {
              case 1:
                additionalText = `Driver ${studentInfo?.first_name} failed to ensure that the`;
                break;
              case 2:
                additionalText = `I instructed ${studentInfo?.first_name} to`;
                break;
              case 3:
                additionalText = `I instructed ${studentInfo?.first_name} to`;
                break;
              case 4:
                additionalText = `I reinforced with ${studentInfo?.first_name} to`;
                break;
              default:
                break;
            }
            htmltableRow += `
              <tr class="pdf-table-row-white">
                 <td colspan="6">${level1Counter}${counterToAlpha(
              level2Counter,
            )}). ${additionalText} ${instruction.instruction}</td>
                 </tr>`;
          }
        });
        // }
      });

      htmlString += `
                <div class="col-sm-12  col-xs-12">
                <div class="pdf-section-block">
                <div class="pdf-section-block-number"><span>${level1Counter})</span></div>
                <div class="pdf-section-block-title"><span>${
                  level1.title
                }</span></div>
                <div class="pdf-section-block-content">
          ${level2HTML}
          </div>
        </div>
      </div>`;
    } else if (level1.title.includes('signature')) {
      htmlsignature += `<div class="col-sm-12 col-xs-12">
            <div class="row">
                <div class="col-sm-2 col-xs-2">
                    <span style="line-height: 75px;">${level1.title}:</span>
                </div>
                <div class="col-sm-6 col-xs-6" style="border-bottom:2px solid grey;">
                    <img src=${
                      state[level1.key]
                    } id="pdf_driver_signature" width="100" height="50">
                    <span id="pdf_driver_signature_name">${
                      level1.key == 'driver_signature'
                        ? studentInfo?.first_name + ' ' + studentInfo?.last_name
                        : level1.key == 'evaluator_signature'
                        ? instructorInfo &&
                          `${instructorInfo.first_name} ${instructorInfo.last_name}`
                        : level1.key == 'company_rep_signature'
                        ? state.company_rep_name
                          ? state.company_rep_name
                          : ''
                        : ''
                    }</span>
                </div>
                <div class="col-sm-4 col-xs-4">
                    <br>
                    <br>
                    <div class="row">
                        <div class="col-sm-4 col-xs-4">
                            <span>Date:</span>
                        </div>
                        <div class="col-sm-8 col-xs-8" style="border-bottom:2px solid grey">
                            <span id="pdf_driver_signature_date">${
                              state.date ? state?.date : ''
                            }</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>`;
    }
  });

  totalPercentage = (totalPointsReceived / totalPossiblePoints) * 100;
  totalPercentage = totalPercentage.toFixed(2);

  return `<!DOCTYPE html>
    <html>
    
    <head>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
            integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
        <style>
            #pdf_template {
                background: white;
                width: 1000px;
                font-size: 12px;
                /* display: none; */
            }
    
            .pdf-section-block {
                ${!pdf && 'width: 100%;'}
                margin: 5px;
                overflow: hidden;
                ${!pdf && 'display: inline-block;'}
                vertical-align: top;
            }
    
            .pdf-section-block-title {
                text-align: center;
                text-decoration: underline;
            }
    
            .pdf-section-block-content {
                border: 2px solid grey !important;
            }
    
            .pdf-section-block-content .row {
                margin-left: 0px !important;
                margin-right: 0px !important;
            }
    
            .pdf-section-block .col-sm-10 {
                border-right: 2px solid grey;
            }
    
            .pdf-section-block .col-sm-2 {
                /*background-color: orange;*/
                background: orange !important;
            }
    
            .pdf-table-row,
            .pdf-table-row td {
                background: #D3D3D3 !important;
            }
    
            .pdf-section-block .row {
                border-bottom: 2px solid grey !important;
            }
    
            .pdf-section-block-content>div:last-child .col-sm-2:last-child {
                background-color: palegreen !important;
            }
    
            .section-results-pdf {
                background-color: #c6c6c6 !important;
            }
    
            #remark table td {
                padding: 11px;
            }
    
            .dmv-bordered {
                border: 1px solid;
            }
    
            .border-bottom {
                min-height: 30px;
                border-bottom: 1px solid;
                padding-top: 3px;
            }
    
            .p-0 {
                padding: 0;
            }
    
            .no-bottom {
                border-bottom: none;
            }
    
            .m-0 {
                margin: 0;
            }
    
            @media print {
                body {
                    -webkit-print-color-adjust: exact !important;
                    float: none !important;
                }
    
                .pdf-section-block .col-sm-2,
                .pdf-section-block .col-xs-2 {
                    background: rgb(255, 165, 0) !important;
                }
    
                .pdf-section-block-content,
                .pdf-section-block,
                .signatures,
                .signatures>div {
                    page-break-inside: avoid !important;
                }
    
                #pdf_template_2,
                .pdf-sections-results,
                #pdf_template_3 {
                    float: none !important;
                }
    
                #container1,
                #pdf_template_2 .pdf-sections-results,
                #pdf_template_3 {
                    page-break-before: always !important;
                }
    
                .section-results-pdf td {
                    background-color: #c6c6c6 !important;
                }
    
                .header-text {
                    background-color: #a6a6ec !important;
                }
            }
        </style>
    </head>
    
    <body>
        <script src="https://code.highcharts.com/highcharts.js"></script>
        <div id="pdf_template" style="padding-left:15px">
            <div class="row">
                <div class="col-sm-12 col-xs-12">
                    <img src="CSDlogo.png" style="position:relative; top:10px;" width="200" alt="">
                    <div class="row">
                        <div class="col-sm-12 col-xs-12 text-center">
                            <h3>Certified Safe Driver Inc.</h3>
                            <h4>Commercial Motor Vehicle Road Test</h4>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-sm-12 col-xs-12">
                            <div class="row">
                                <div class="col-sm-6 col-xs-6"></div>
                                <div class="col-sm-6 col-xs-6">
                                    <span>Company Name</span>
                                    <span class="value" id="company">${
                                      companyInfo?.name == null
                                        ? 'N/A'
                                        : companyInfo?.name
                                    }</span>
                                </div>
                            </div>
                        </div>
    
                        <div class="col-sm-4 col-xs-4 text-center">
                            <div>
                                <span>Date:</span>
                                <span class="value" id="dateTime">${
                                  testInfo?.test?.created
                            ? testInfo?.test?.created.split('T')[0]
                            : 'N/A'
                                }</span>
                            </div>
                            <div>
                                <span>Employee #:</span>
                                <span class="value" id="employeeId">${
                                  studentInfo?.id ? studentInfo?.id : 'N/A'
                                }</span>
                            </div>
                            <div>
                                <span>Driver Name:</span>
                                <span class="value" id="driverName">${
                                  studentInfo?.first_name +
                                  ' ' +
                                  studentInfo?.last_name
                                }</span>
                            </div>
                        </div>
                        <div class="col-sm-4 col-xs-4 text-center">
                            <div class="row">
                                <div class="col-sm-6 col-xs-6">
                                    <div>
                                        <span>License Exp. date:</span>
                                        <span class="value" id="driverLicenseExpirationDate">${
                                          testInfo?.info
                                            .driver_license_expire_date == null
                                            ? 'N/A'
                                            : testInfo?.info
                                                .driver_license_expire_date
                                        }</span>
                                    </div>
                                </div>
                                <div class="col-sm-6 col-xs-6">
                                    <div>
                                        <span>Class:</span>
                                        <span class="value" id="driverLicenseClass">${
                                          testInfo?.info.driver_license_class ==
                                          null
                                            ? 'N/A'
                                            : testInfo?.info.driver_license_class
                                        }</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-sm-4 col-xs-4 text-center">
                            <div>
                                <span>Endorsements:</span>
                                <span class="value" id="endorsements">${
                                  testInfo?.info.endorsements === false
                                    ? 'no'
                                    : 'yes'
                                }</span>
                            </div>
                            <div>
                                <span>Dot Exp. date:</span>
                                <span class="value" id="dotExpirationDate">${
                                  testInfo?.info.dot_expiration_date == null
                                    ? 'N/A'
                                    : testInfo?.info.dot_expiration_date
                                }</span>
                            </div>
                        </div>
                    </div>
                </div>
                <br>
                <div class="col-sm-12 text-center" style="background-color:#a6a6ec;">
                    <p class="header-text" style="display: inline-block !important; width: 100% !important;">Circle the
                        applicable rating for each element - Rating Legend: 4 = Exellent 3 = Good 2 = Fair 1 = Poor</p>
                </div>
                <div class="col-sm-12 text-center">
                    <div class="row">
                        <div class="col-sm-6 col-xs-6">
                            <span>Start Time:</span>
                            <span class="value" id="startTime">${
                              testInfo?.start_time == null
                                ? 'N/A'
                                : testInfo?.start_time
                            }</span>
                        </div>
                        <div class="col-sm-6 col-xs-6">
                            <span>End Time:</span>
                            <span class="value" id="endTime">${
                              testInfo?.end_time == null
                                ? 'N/A'
                                : testInfo?.end_time
                            }</span>
                        </div>
                    </div>
                </div>
                <div class="row" id="pdf_template_1">
    
    
                <div class="col-sm-12 pdf-sections">
               ${htmlString}
            </div>
    
    
                    <div class="col-sm-12  col-xs-12 signatures" style="padding-left: 52px;">
                        <div class="row">
                            <div class="col-sm-3 col-xs-3">
                                <table border="3&quot;" style="width: 360px;">
                                    <tbody>
                                        <tr>
                                            <td style="border-bottom:3px solid grey">Possible Points: </td>
                                            <td id="pointsPossible" style="border-bottom:3px solid grey; text-align: center;">${totalPossiblePoints}</td>
                                            <td rowspan="2" style="border-left:3px solid grey; border-right:3px solid grey; text-align: center;">
                                                % Eff
                                            </td>
                                            <td style="text-align: center;" rowspan="2" id="pointsPercentage">${totalPercentage} %</td>
                                        </tr>
                                        <tr style="border-bottom:3px solid grey">
                                            <td style="border-bottom:3px solid grey">Points Received: </td>
                                            <td style="border-bottom:3px solid grey; text-align: center;" id="pointsReceived">${totalPointsReceived}</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                            <div class="col-sm-9 col-xs-9 text-center">
                                <span></span>
                            </div>
                        </div>
                        <br>
                        <div class="row">
                            <div class="col-sm-12 col-xs-12">
                                <div class="row" style="border:1px solid grey">
                                    <div class="col-sm-6 col-xs-6" style="border-right:1px solid grey">
                                        <span>Corrective lens required:</span>
                                        <span id="correctiveLensRequired">${
                                          testInfo?.corrective_lense_required
                                            ? 'Yes'
                                            : 'No'
                                        }</span>
                                    </div>
                                    <div class="col-sm-6 col-xs-6">
                                        <span>Evaluation Location:</span>
                                        <span id="pdf_evaluation_location">${
                                          testInfo?.location
                                            ? testInfo?.location
                                            : 'N/A'
                                        }</span>
                                    </div>
                                </div>
    
                                <div class="row" style="border:1px solid grey">
                                    <div class="col-sm-6 col-xs-6" style="border-right:1px solid grey">
                                        <span>Driver Name:</span>
                                        <span id="pdf_driver_name">${
                                          studentInfo?.first_name +
                                          ' ' +
                                          studentInfo?.last_name
                                        }</span>
                                    </div>
                                    <div class="col-sm-6 col-xs-6">
                                        <span>Driver License Expiration Date:</span>
                                        <span id="driverLicenseExpirationDateBottom">${
                                          testInfo?.driver_license_expire_date
                                            ? testInfo?.driver_license_expire_date
                                            : 'N/A'
                                        }</span>
                                        </span>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                        ${htmlsignature}
                        </div>
                    </div>
                    <br>
                    <br>
                </div>
    
                <div class="col-sm-12 col-xs-12" id="pdf_template_2" style="width: 100%;padding-top: 20px !important;">
                    <div class="pdf-sections-results">
                        <table class="table table-bordered">
                            <tbody>
                                <tr style="border-bottom:3px solid grey">
                                    <td style="border-bottom:3px solid grey; background-color: #c6c6c6 !important;">Score:
                                    </td>
                                    <td style="border-bottom:3px solid grey;" id="form_scored1">${totalPercentage} %</td>
                                    <td style="border-bottom:3px solid grey; background-color: #c6c6c6 !important;">
                                        Qualified</td>
                                    <td style="border-bottom:3px solid grey;" id="qualified1">${
                                      isQualified === true ? 'X' : ''
                                    }</td>
                                    <td style="border-bottom:3px solid grey; background-color: #c6c6c6 !important;">No
                                        Qualified</td>
                                    <td style="border-bottom:3px solid grey;" id="notQualified1">${
                                      isQualified === false ? 'X' : ''
                                    }</td>
                                </tr>
                                <tr>
                                    <td colspan="6" style="padding: 7px; border: 3px solid #c4c4c4;">If NOT
                                        Qualified(EXPLAIN)</td>
                                </tr>
                                <tr>
                                    <td colspan="6" style="padding: 14px; border: 3px solid #c4c4c4;"
                                        id="disqualifiedRemarks">${notQualifiedRemarks}</td>
                                </tr>
                                <tr>
                                    <td colspan="6" style="padding: 14px; border: 3px solid #c4c4c4;"></td>
                                </tr>

                                ${htmltableRow}
    
                            </tbody>
                        </table>
                    </div>
    
                    <div class="col-sm-12 col-xs-12">
                        <p>This is to certified that the above named driver was given a road test under my superviosion on
                            <span style="padding:20px;" id="month2">${
                              state.date
                                ? moment(state?.date).format('MM / DD / YYYY')
                                : ''
                            } consisting of <span
                                style="padding:0 20px; border-bottom:1px dashed #000;" id="miles1">${
                                  state.miles
                                }</span>miles of
                            driving. It is my considered option that this driver possesses sufficient skill to operate
                            safely the type of commercial motor vehicle listed above.</p>
                    </div>
                    <br>
                    <br>
                    <div class="col-sm-12 col-xs-12" style="border:1px solid;">
                        <h6 class="text-center">Company District Office Address</h6>
                        <h6 class="text-center">Certified Safe Driver Inc. 20803 E.Valley Suite 109 Walnut CA 91789</h6>
                    </div>
                </div>
                <div class="col-sm-12 col-xs-12" id="pdf_template_3">
                    <div class="col-sm-12 p-0">
                        <img src="CSDlogo.png" style="position:relative; top:10px;" width="200" alt="">
                        <div class="row">
                            <div class="col-sm-12 text-center">
                                <h2>Commercial Motor Vehicle Road Test</h2>
                            </div>
                        </div>
                        <div class="">
                            <div class="col-sm-4 col-xs-4 text-center p-0">
                                <div class="dmv-bordered">
                                    <p>Employee #</p>
                                    <p class="" id="dmv_employeeId">${
                                      studentInfo?.id ? studentInfo?.id : 'N/A'
                                    }</p>
                                </div>
                                <div class="dmv-bordered">
                                    <p>Driver Name:</p>
                                    <p class="" id="dmv_driverName">${
                                      studentInfo?.first_name +
                                      ' ' +
                                      studentInfo?.last_name
                                    }</p>
                                </div>
                                <div class="dmv-bordered">
                                    <p>Driver License Number:</p>
                                    <p class="" id="dmv_driverLicenseNumber">${
                                      studentInfo?.info
                                        ? studentInfo?.info
                                            .driver_license_number
                                        : ''
                                    }</p>
                                </div>
                            </div>
                            <div class="col-sm-4 col-xs-4 text-center">
                                <div class="dmv-bordered">
                                    <p>License Expiration Date:</p>
                                    <p class="" id="dmv_driverLicenseExpirationDate">${
                                      studentInfo?.info
                                        ? studentInfo?.info
                                            .driver_license_expire_date
                                        : ''
                                    }</p>
                                </div>
                                <div class="dmv-bordered">
                                    <p>Medical Card Exp. Date:</p>
                                    <p class="" id="medicalCardExpirationDate">${
                                      studentInfo?.info.dot_expiration_date
                                        ? studentInfo?.info.dot_expiration_date
                                        : ''
                                    }</p>
                                </div>
                                <div class="dmv-bordered">
                                    <p>State:</p>
                                    <p class="" id="testState">${
                                      companyInfo?.state ? companyInfo.state : ''
                                    }</p>
                                </div>
                            </div>
                            <div class="col-sm-4 col-xs-4 text-center dmv-bordered p-0">
                                <p class="txt-center">Type of Equipment</p>
                                <div class="col-sm-6 col-xs-6 p-0" style="border-right: 1px solid; border-top: 1px solid">
                                    <p class="border-bottom m-0">Type of Powr Unit:</p>
                                    <p class="border-bottom m-0">Trailer Length:</p>
                                    <p class="border-bottom no-bottom m-0">Number Of Trailers:</p>
                                </div>
                                <div class="col-sm-6 col-xs-6 p-0" style="border-top: 1px solid;">
                                    <p class="border-bottom m-0" id="powerUnit">${
                                      state.type_of_power_unit
                                        ? state.type_of_power_unit
                                        : ''
                                    }</p>
                                    <p class="border-bottom m-0" id="trailerLength">${
                                      state.trailer_length
                                        ? state.trailer_length
                                        : ''
                                    }</p>
                                    <p class="border-bottom no-bottom m-0" id="numberofTrailers">${
                                      state.number_of_trailers
                                        ? state.number_of_trailers
                                        : ''
                                    }</p>
                                </div>
    
                            </div>
                        </div>
                    </div>
                    <div class="col-sm-12 copy-part pdf-sections-results p-0">
                        <br>
                        <br>
                        <br>
                        <table class="table table-bordered">
                            <tbody>
                                <tr style="border-bottom:3px solid grey">
                                    <td style="border-bottom:3px solid grey; background-color: #c6c6c6 !important;">Score:
                                    </td>
                                    <td style="border-bottom:3px solid grey;" id="form_scored2">${totalPercentage} %</td>
                                    <td style="border-bottom:3px solid grey; background-color: #c6c6c6 !important;">
                                        Qualified</td>
                                    <td style="border-bottom:3px solid grey;" id="qualified2">${
                                      isQualified === true ? 'X' : ''
                                    }</td>
                                    <td style="border-bottom:3px solid grey; background-color: #c6c6c6 !important;">No
                                        Qualified</td>
                                    <td style="border-bottom:3px solid grey;" id="notQualified2">${
                                      isQualified === false ? 'X' : ''
                                    }</td>
                                </tr>
    
                            </tbody>
                        </table>
    
                        <div class="col-sm-12 col-xs-12">
                            <p>This is to certified that the above named driver was given a road test under my superviosion
                                on <span style="padding:20px;" id="month1">${
                                  state.date
                                    ? moment(state?.date).format(
                                        'MM / DD / YYYY',
                                      )
                                    : ''
                                }</span> consisting of 
                                <span style="padding:0 20px; border-bottom:1px dashed #000;" id="miles2">${
                                  state.miles
                                }</span>miles of
                                driving. It is my considered option that this driver possesses sufficient skill to operate
                                safely the type of commercial motor vehicle listed above.</p>
                        </div>
                        <br>
                        <br>
    
                    </div>
                    <div class="row">
                        
                        ${htmlsignature}
                     
                        <br>
                       
                        <div class="col-sm-12">
                            <div class="col-sm-12 col-xs-12">
                                <div class="col-sm-2 col-xs-2">
                                    <span style="line-height: 75px;">Print:</span>
                                </div>
                                <div class="col-sm-6 col-xs-6" style="border-bottom:2px solid grey; height:70px;">
                                    <img src="#" id="dmv_pdf_print" width="100" height="70" alt="" hidden="">
                                    <p style="position: absolute; bottom: -5px;" id="evaluatorName">${
                                      state.print ? state.print : ''
                                    }</p>
                                    <span id="evaluatorNameOld"></span>
                                </div>
                            </div>
                        </div>
                        <div class="col-sm-12">
                            <div class="col-sm-12 col-xs-12">
                                <div class="col-sm-2 col-xs-2">
                                    <span style="line-height: 75px;">Title:</span>
                                </div>
                                <div class="col-sm-6 col-xs-6" style="border-bottom:2px solid grey; height:70px;">
                                    <img src="#" id="dmv_pdf_title" width="100" height="70" alt="" hidden="">
                                    <p style="position: absolute; bottom: -5px;" id="evaluatorTitle">${
                                      state.title ? state.title : ''
                                    }</p>
    
                                    <span id="evaluatorTitleOld"></span>
                                </div>
                            </div>
                        </div>
                        <br>
    
                    </div>
                    <div class="col-sm-12 p-0 dmv_footer">
    
                        <div class="col-sm-12 col-xs-12" style="border:1px solid;">
                            <h6 class="text-center" id="companyAddress">Company District Office Address</h6>
                            <h6 class="text-center">Certified Safe Driver INC. 20803 E.Valley Suite 109 Walnut CA 91789</h6>
                        </div>
                    </div>
                </div>
            </div>
    </body>
    </html>
    `;
};
