import React from 'react';
import _, {isNumber} from 'lodash';
import {counterToAlpha} from '../../../utils/function';

export default SWP = (
  dataModal,
  state,
  studentInfo,
  companyInfo,
  testInfo,
  instructorInfo,
  charData,
) => {
  let htmlString = '';
  let level1Counter = 0;
  let level2Counter = 0;
  let level2HTML = '';
  let htmlsignature = '';
  let htmltableRow = '';
  let effectiveBarChartData = [];
  _.forEach(dataModal, (level1) => {
    // console.log('level1', level1)
    if (state[level1.key]) {
      ++level1Counter;
      level2Counter = 0;
      level2HTML = '';

      var categoryPointsReceived = 0;
      var categoryPossiblePoints = 0;
      var categoryPercentage = 0;
      _.forEach(level1, (level2, key) => {
        if (level2 && level2.key) {
          // console.log('level2: ', state[level1.key][level2.key], level2);
          if (
            key == 'key' ||
            key == 'title' ||
            level2.key == 'possible_points' ||
            level2.key == 'points_received' ||
            level2.key == 'percent_effective'
          ) {
            //   return null;
          } else if (level2.key != 'notes') {
            if (
              state[level1.key][level2.key] &&
              isNumber(state[level1.key][level2.key]) &&
              state[level1.key][level2.key] !== 0
            ) {
              categoryPointsReceived =
                categoryPointsReceived + state[level1.key][level2.key];
              categoryPossiblePoints = categoryPossiblePoints + 5;
            }
          }
        }
      });
      categoryPercentage =
        (categoryPointsReceived / categoryPossiblePoints) * 100;
      categoryPercentage = categoryPercentage.toFixed(2);
      if (level1.value === undefined) {
        htmltableRow += `
            <tr id="01_tr" class="pdf-table-row">
                <td>${level1Counter}</td>
                <td>${level1.title}</td>
                <td id="01_possible_p">Possible Points: ${state[level1.key].possible_points}</td>
                <td id="01_received_p">Points Received: ${state[level1.key].points_received}</td>
                <td id="01_effective_p">Percent Effective: ${state[level1.key].percent_effective} %</td>
                <td id="01_note">Note: ${
                  state[level1.key].notes ? state[level1.key].notes : 'N/A'
                } </td>
            </tr>`;

        _.forEach(level1, (level2, key) => {
          // console.log('level2: ', state[level1.key][level2.key], level2);
          if (
            key == 'key' ||
            key == 'title' ||
            level2.key == 'possible_points' ||
            level2.key == 'points_received' ||
            level2.key == 'percent_effective'
          ) {
            return null;
          }
          if (level2.key != 'notes') {
            ++level2Counter;
            if (typeof level2.value === 'boolean') {
              level2HTML += `
                        <div class="row">
                        <div class="col-sm-10 col-xs-10"> ${counterToAlpha(
                          level2Counter,
                        )}) ${level2.title}</div>
                        <div class="col-sm-2 col-xs-2" id="01a">${
                          state[level1.key][level2.key] == true ? 'yes' : 'no'
                        }</div>
                      </div>
                        `;
            } else {
              level2HTML += `
                        <div class="row">
                        <div class="col-sm-10 col-xs-10"> ${counterToAlpha(
                          level2Counter,
                        )}) ${level2.title}</div>
                        <div class="col-sm-2 col-xs-2" id="01a">  ${
                          state[level1.key][level2.key] == 0 ||
                          state[level1.key][level2.key] == null
                            ? 'N/A'
                            : state[level1.key][level2.key]
                        }</div>
                      </div>
                        `;
            }

            state?.instructions?.map((instruction, idx) => {
              // console.log("Inst: ", instruction.field_name.toLowerCase())
              // console.log(state[level1.key][level2])
              if (typeof level2.value === 'boolean') {
                if (
                  instruction.field_name.toLowerCase() === key &&
                  state[level1.key][level2.key] === false
                ) {
                  let additionalText = '';
                  htmltableRow += `
                <tr class="pdf-table-row-white">
                   <td colspan="6">${level1Counter}${counterToAlpha(
                    level2Counter,
                  )}). ${additionalText} ${instruction.instruction}</td>
                   </tr>`;
                }
              } else if (
                instruction.field_name.toLowerCase() === key &&
                instruction.db_table === state[level1.key]?.db_table &&
                state[level1.key][level2.key] != 0 &&
                state[level1.key][level2.key] != 5
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
          }
        });

        htmlString += `
                    <div class="col-sm-12">
                    <div class="pdf-section-block">
                    <div class="pdf-section-block-number"><span>${level1Counter})</span></div>
                    <div class="pdf-section-block-title"><span>${level1.title}</span></div>
                    <div class="pdf-section-block-content">
                    ${level2HTML}
                    </div>
                    </div>
                </div>`;

        console.log(state[level1.key]);

        if (state[level1.key].percent_effective != undefined) {
          effectiveBarChartData.push(
            `["${level1.title}", ${state[level1.key].percent_effective}]`,
          );
        }
      } else if (level1.title.includes('signature')) {
        htmlsignature += `<div class="col-sm-12 col-xs-12">
            <div class="row">
                <div class="col-sm-2 col-xs-2">
                    <span style="line-height: 75px;">${level1.title}:</span>
                </div>
                <div class="col-sm-6 col-xs-6" style="border-bottom:2px solid grey;">
                    <img  src=${
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
    }
  });
  // console.log('ChartData: arrayswp: ', charData);

  return `
    <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">

    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
    integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

      <style>
          
        #pdf_template {
        background: white;
        width: 950px;
        font-size: 12px;
       }

          .pdf-section-block {
            margin: 5px;
            overflow: hidden;
            vertical-align: top;
          }
          .pdf-section-block-title {
            text-align: center;
            text-decoration: underline;
          }
          .pdf-section-block .col-sm-10 {
            border-right: 2px solid grey !important;
            padding-left: 0px;
            padding-right: 0px;
          }

          .pdf-section-block .col-sm-2 {
            background-color: orange !important;
          }

          .pdf-section-block .col-sm-10 {
            border-right: 2px solid grey !important;
         }

         .pdf-section-block .row {
          border-bottom: 2px solid grey !important;
        }

        .pdf-section-block-content .row {
          margin-left: 0px !important;
          margin-right: 0px !important;
        }
                
        .pdf-section-block-content {
          border: 2px solid grey !important;
        }
		
		.critical-item{
		  background-color: #ff7a83 !important;
		}

		.reason-txt span, .reason-date span, .history-txt span {
		  display: inline-block;
		  width: 28%;
		  text-align: center;
		  border: 1px solid black;
		  background-color: #e8e8e8 !important;
		  padding: 2px;
		  min-width: 40px;
		  margin-bottom:3px;
		}

		.reason-txt label, .reason-date label, .history-txt label {
		  display: inline-block;
		  width: 70%;
		  text-align: right;
		  margin-bottom:3px;
        }

        .section-results-pdf {
            background-color:#c6c6c6 !important;
         }
         
        .pdf-table-row,
    	.pdf-table-row td {
        	background: #D3D3D3 !important;
        }

        .pdf-table-row-white,
        .pdf-table-row-white td {
            background: #ffffff !important;
        }

    
    @media print {
        body {
            -webkit-print-color-adjust: exact !important;
            float:none !important;
        }

        .pdf-section-block .col-sm-2, .pdf-section-block .col-xs-2 {
            background: rgb(255,165,0) !important;
        }

        .pdf-section-block-content, .pdf-section-block, .signatures, #table, .signatures > div{
            page-break-inside: avoid !important;
        }

         #pdf_template_2, .pdf-sections-results{
             float: none !important;
         }

        #container1, #pdf_template_2 .pdf-sections-results{
            page-break-before: always !important;
        }
    }

      </style>

</head>

<body>
    <script src="https://code.highcharts.com/highcharts.js"></script>    
        <div id="pdf_template" style="/* display: none; */">
            <div class="row" id="pdf_template_1">
                <div class="col-sm-12">
                <img src="CSDlogo.png" style="position:relative; top:10px;" width="200" alt="">
                    <div class="row">
                        <div class="col-sm-12 text-center">
                            <h3>Certified Safe Driver Inc.</h3>
                            <h4>Safe Work Practice Evaluation and Coaching</h4>
                        </div>
                    </div>
                    <div class="row">
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
                                <span class="value" id="employeeId">GA_553322</span>
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
                    </div>
                </div>
                <div class="col-md-12 col-sm-12 col-xs-12">
                    <h5 class="text-center">Reason For Safe Work Practice Training: </h5>
                    <div class="col-md-4 col-sm-4 col-xs-4">
                        <div class="col-md-12  col-xs-12 col-sm-12  reason-txt">
                            <label>New Hire:</label>
                            <span id="trainingNewHire">${
                              testInfo?.new_hire === false ? 'no' : 'yes'
                            }</span>
                        </div>
                        <div class="col-md-12  col-xs-12 col-sm-12 reason-txt">
                            <label>Near Miss:</label>
                            <span id="trainingNearMiss">${
                              testInfo?.near_miss === false ? 'no' : 'yes'
                            }</span>
                        </div>
                        <div class="col-md-12  col-xs-12 col-sm-12 reason-txt">
                            <label>Incident Follow-up:</label>
                            <span id="trainingIncidentFollowUp">${
                              testInfo?.incident_follow_up === false
                                ? 'no'
                                : 'yes'
                            }</span>
                        </div>
                        <div class="col-md-12  col-xs-12 col-sm-12 reason-txt">
                            <label>Chnge Job:</label>
                            <span id="trainingChangeJob">${
                              testInfo?.change_job === false ? 'no' : 'yes'
                            }</span>
                        </div>
                        <div class="col-md-12  col-xs-12 col-sm-12 reason-txt">
                            <label>Change of Equipment:</label>
                            <span id="trainingChangeOfEquipment">${
                              testInfo?.change_of_equipment === false
                                ? 'no'
                                : 'yes'
                            }</span>
                        </div>
                        <div class="col-md-12  col-xs-12 col-sm-12 reason-txt">
                            <label>Annual:</label>
                            <span id="trainingAnnual">${
                              testInfo?.annual === false ? 'no' : 'yes'
                            }</span>
                        </div>
                    </div>
    
                    <div class="col-md-4 col-sm-4 col-xs-4">
                        <div class="col-md-12  col-xs-12 reason-date">
                            <label>Injury Date:</label>
                            <span id="trainingInjuryDate">${
                              testInfo?.injury_date
                                ? testInfo?.injury_date
                                : 'N/A'
                            }</span>
                        </div>
                        <div class="col-md-12  col-xs-12 reason-date">
                            <label>Accident Date:</label>
                            <span id="trainingAccidentDate">${
                              testInfo?.accident_date
                                ? testInfo?.accident_date
                                : 'N/A'
                            }</span>
                        </div>
                        <div class="col-md-12  col-xs-12 reason-date">
                            <label>TAW Start Date:</label>
                            <span id="trainingTAWStartDate">${
                              testInfo?.taw_start_date
                                ? testInfo?.taw_start_date
                                : 'N/A'
                            }</span>
                        </div>
                        <div class="col-md-12  col-xs-12 reason-date">
                            <label>TAW End Date:</label>
                            <span id="trainingTAWEndDate">${
                              testInfo?.taw_end_date
                                ? testInfo?.taw_end_date
                                : 'N/A'
                            }</span>
                        </div>
                        <div class="col-md-12  col-xs-12 reason-date">
                            <label>Lost Time Start Date:</label>
                            <span id="trainingLostTimeStartDate">${
                              testInfo?.lost_time_start_date
                                ? testInfo?.lost_time_start_date
                                : 'N/A'
                            }</span>
                        </div>
                        <div class="col-md-12  col-xs-12 reason-date">
                            <label>Return to Work Date:</label>
                            <span id="trainingReturnToWorkDate">${
                              testInfo?.return_work_date
                                ? testInfo?.return_work_date
                                : 'N/A'
                            }</span>
                        </div>
                    </div>
                    <div class="col-md-4 col-sm-4 col-xs-4">
                        <div class="col-md-12  col-xs-12 history-txt">
                            <label>History reviewed:</label>
                            <span class="value" id="driverHistoryReviewed">${
                              testInfo?.history_reviewed === false
                                ? 'no'
                                : 'yes'
                            }</span>
                        </div>
                    </div>
    
                </div>
    
                <div class="col-sm-12 col-xs-12 text-center" style="background-color:rgb(166, 166, 236)  !important">
                    <span>5 = performed correctly-4 = Reinforced - 3 = corrected &amp; reinforced - 2 = Multi corrections &amp;
                        reinforced - 1 = unacceptable</span>
                </div>
                
                <div class="col-sm-12 text-center">
                    <div class="row">
                        <div class="col-sm-6">
                            <span>Start Time:</span>
                            <span class="value" id="startTime">${
                              testInfo?.start_time
                                ? testInfo?.start_time
                                : 'N/A'
                            }</span>
                        </div>
                        <div class="col-sm-6">
                            <span>End Time:</span>
                            <span class="value" id="endTime">${
                              testInfo?.end_time ? testInfo?.end_time : 'N/A'
                            }</span>
                        </div>
                    </div>
                </div>

        ${htmlString}

 </div>
<br>
                <div class="col-sm-12 col-xs-12 signatures">
                    <div class="row">
                        <div class="col-sm-3 col-xs-3">
                            <table border="3&quot;" style="width: 360px;">
                                <tbody><tr>
                                    <td style="border-bottom:3px solid grey;">Possible Points: </td>
                                    <td id="pointsPossible" style="border-bottom:3px solid grey; text-align: center;">${
                                      state.totalPossiblePoints
                                    }</td>
                                    <td rowspan="2" style="border-left:3px solid grey; border-right:3px solid grey; text-align: center;">% Eff
                                    </td>
                                    <td rowspan="2" id="pointsPercentage" style="text-align: center;">${
                                      state.totalEffPercentage
                                    }%</td>
                                </tr>
                                <tr style="border-bottom:3px solid grey">
                                    <td style="border-bottom:3px solid grey">Points Received: </td>
                                    <td style="border-bottom:3px solid grey; text-align: center;" id="pointsReceived">${
                                      state.totalPointsReceived
                                    }</td>
                                </tr>
                            </tbody></table>
                        </div>
                        <div class="col-sm-9 col-xs-9 text-center">
                            <span></span>
                        </div>
                    </div>
                    <br>
                    <div class="row">
                        <div class="col-sm-12 col-xs-12 text-left">
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
                                    <span>Evaluation Location:</span>
                                    <span id="pdf_evaluation_location">${
                                      testInfo?.location
                                        ? testInfo?.location
                                        : 'N/A'
                                    }</span>
                                </div>
                            </div>    
                        </div>
                    </div>
                    <div class="row"  style="margin-top:10px;">
                        <div class="col-sm-12 col-xs-12">
                            <div class="row">
                                ${htmlsignature}
                    </div>
                </div>
                <br>
                <br>
            </div>
            <br>
            <div id="pdf_template_2">
                    <div class="col-sm-12 col-xs-12 pdf-sections-results">
                        <table class="table table-bordered" id="table">
                        <tbody>
                        ${htmltableRow}
                        <tr></tr>
                    </tbody>
                        </table>
                        <div id="container1" style="min-width: 300px; height: 400px; margin: 0 auto"></div>
                        <div id="container2" style="min-width: 300px; height: 400px; margin: 0 auto"></div>
                    </div>
                </div>
        </div>
        <script>
        Highcharts.chart('container1', {
            chart: {
                type: 'column'
            },
            title: {
                text: 'Element Effective Chart'
            },
            xAxis: {
                type: 'category',
                labels: {
                    rotation: -45,
                    style: {
                        fontSize: '13px',
                        fontFamily: 'Verdana, sans-serif'
                    }
                }
            },
            yAxis: {
                min: 0,
                title: {
                    text: ''
                }
            },
            legend: {
                enabled: false
            },
            tooltip: {
                pointFormat: '<b>{point.y:.1f}%</b>'
            },
            series: [{
                name: 'Element Effective Chart',
                data: [${effectiveBarChartData}],
                dataLabels: {
                    enabled: true,
                    rotation: -90,
                    color: '#FFFFFF',
                    align: 'right',
                    format: '{point.y:.1f}', // one decimal
                    y: 10, // 10 pixels down from the top
                    style: {
                        fontSize: '13px',
                        fontFamily: 'Verdana, sans-serif'
                    }
                }
            }]
        });

        Highcharts.chart('container2', {
            chart: {
                type: 'column'
            },
            title: {
                text: 'Injury Probability Graph'
            },
            xAxis: {
                type: 'category',
                labels: {
                    rotation: -45,
                    style: {
                        fontSize: '13px',
                        fontFamily: 'Verdana, sans-serif'
                    }
                }
            },
            yAxis: {
                min: 0,
                title: {
                    text: ''
                }
            },
            legend: {
                enabled: false
            },
            series: [{
                name: 'Probability',
                data: [${charData}],
                dataLabels: {
                    enabled: true,
                    rotation: -90,
                    color: '#FFFFFF',
                    align: 'right',
                    format: '{point.y:.1f}', // one decimal
                    y: 10, // 10 pixels down from the top
                    style: {
                        fontSize: '13px',
                        fontFamily: 'Verdana, sans-serif'
                    }
                }
            }]
        });
</script>
</body>
  </html>
    `;
};
