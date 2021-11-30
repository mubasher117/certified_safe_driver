import React from 'react';
import _, {isNumber} from 'lodash';
import {counterToAlpha} from '../../../utils/function';

const classNameMapping = {
  class_a: 'A',
  class_b: 'B',
  class_c: 'C',
  class_p: 'P',
  bus: 'P',
};

export default BTW = (
  dataModal,
  state,
  studentInfo,
  companyInfo,
  testInfo,
  instructorInfo,
  map_screenshot_url,
  mapData,
  charData,
  pdf,
  btwClass,
  map_screenshot_img,
) => {
  let htmlString = '';
  let level1Counter = 0;
  let level2Counter = 0;
  let level2HTML = '';
  let htmlsignature = '';
  let htmltableRow = '';
  let effectiveBarChartData = [];
  const leftOk = mapData?.leftOks?.length;
  const leftShort = mapData?.leftShorts?.length;
  const leftWide = mapData?.leftWides?.length;
  const rightOk = mapData?.rightOks?.length;
  const rightShort = mapData?.rightShorts?.length;
  const rightWide = mapData?.rightWides?.length;
  // let totalPossiblePoints = 0;
  // let totalReceivedPoints = 0;
  // let totalPercentEffective = 0.0;
  let mapDataView = '';
  if (mapData) {
    mapDataView = `<div style="padding: 50px; background:#D3D3D3;">
        <span style="padding-right: 20px;font-size: 20px;">LeftOk:${leftOk}</span>
        <span style="padding-right: 20px;font-size: 20px;">LeftShort:${leftShort}</span>
        <span style="padding-right: 20px;font-size: 20px;">LeftWide:${leftWide}</span>
        <span style="padding-right: 20px;font-size: 20px;">RightOk:${rightOk}</span>
        <span style="padding-right: 20px;font-size: 20px;">RightShort:${rightShort}</span>
        <span style="padding-right: 20px;font-size: 20px;">RightWide:${rightWide}</span>
        </div>`;
  }
  _.forEach(dataModal, (level1) => {
    // console.log('level1', level1)
    ++level1Counter;
    level2Counter = 0;
    level2HTML = '';
    var categoryPointsReceived = 0;
    var categoryPossiblePoints = 0;
    var categoryPercentage = 0;
    _.forEach(level1, (level2, key) => {
      if (level2 && level2.key) {
        if (
          key == 'key' ||
          key == 'title' ||
          level2.key == 'possible_points' ||
          level2.key == 'points_received' ||
          level2.key == 'percent_effective'
        ) {
          // return null;
        }
        if (level2.key != 'notes') {
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
      // console.log('BTWPreviewHTML level1: ', level1);

      htmltableRow += `
                <tr id="01_tr" class="pdf-table-row">
                    <td>${level1Counter}</td>
                    <td>${level1.title}</td>
                    <td id="01_possible_p">Possible Points: ${categoryPossiblePoints}</td>
                    <td id="01_received_p">Points Received: ${categoryPointsReceived}</td>
                    <td id="01_effective_p">Percent Effective: ${categoryPercentage} %</td>
                    <td id="01_note">Note: ${
                      state[level1.key].notes ? state[level1.key].notes : 'N/A'
                    } </td>
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
        if (level2.key != 'notes') {
          ++level2Counter;
          level2HTML += `<div class="row"> 
                <div class="col-sm-10 col-xs-10">${counterToAlpha(
                  level2Counter,
                )})  ${level2.title}</div>
                <div class="col-sm-2 col-xs-2" id="01a">${
                  state[level1.key][level2.key] == 0 ||
                  state[level1.key][level2.key] == null
                    ? 'N/A'
                    : state[level1.key][level2.key]
                }</div>
              </div>`;
              state?.instructions?.map((instruction, idx) => {
                // console.log("Inst: ", instruction.field_name.toLowerCase())
                // console.log(state[level1.key][level2])
                if (
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
        // const instruction = state.instructions.find(instruction=>instruction.field_name==key)
        // console.log('key', key, 'instruction', state.instructions)
        // if(instruction){

        // htmltableRow += `
        //          <tr class="pdf-table-row-white">
        //             <td colspan="6">${level1Counter}${counterToAlpha(level2Counter)}}. ${instruction.instruction}</td>
        //             </tr>`
        // }
        // state.instructions.map((val) => {
        //     if (val.field_name == key){
        //         // console.log('intructions Val: ', key, val);
        //         htmltableRow += `
        //         <tr class="pdf-table-row-white">
        //             <td colspan="6">${val.instruction}</td>
        //             </tr>`
        //     }
        // })
        // console.log('state.instructions[field_name]: ', state.instructions, key);
      });

      htmlString += `<div class="col-sm-1"></div>
                    <div class=${
                      pdf ? 'col-sm-10' : 'col-sm-5'
                    } style="padding-right: 0px !important;margin-right: 15px;">
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

      // totalPossiblePoints += state[level1.key]['possible_points'] ? Number(state[level1.key]['possible_points']) : 0
      // totalReceivedPoints += state[level1.key]['points_received'] ? Number(state[level1.key]['points_received']) : 0
      // totalPercentEffective += state[level1.key]['percent_effective'] ? Number(state[level1.key]['percent_effective']) : 0

      // effectiveBarChartData = [level1.title, level1.percent_effective ? Number(level1.percent_effective.value) : 0.00]
      if (state[level1.key].percent_effective != undefined) {
        effectiveBarChartData.push(
          `["${level1.title}", ${
            state[level1.key].percent_effective
              ? Number(state[level1.key].percent_effective)
              : 5.0
          }]`,
        );
      }
      // effectiveBarChartData.push(
      //     [`'${level1.title}'`, `${state[level1.key]['percent_effective']  ? Number(state[level1.key]['percent_effective']) : 5.00}`]
      // )
      // effectiveBarChartData.concat([level1.title, level1.percent_effective ? Number(level1.percent_effective.value) : 0.00],)
    } else if (level1.title.includes('signature')) {
      // console.log('signature: ', state[level1.key]);
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
                          `${instructorInfo?.first_name} ${instructorInfo?.last_name}`
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
        </div>`; //`<img src=${state[level1.key]}  id="pdf_driver_signature" width="100" height="50"></img>`
    }
  });

  // console.log('effectiveBarChartData: array: ', effectiveBarChartData);
  // console.log('ChartData: array: ', charData);

  return `<!DOCTYPE html>
    <html>
    
    <head>
    <title>iOS CSD BTW </title>
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
    ${!pdf && 'width: 415px;'}
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

.pdf-table-row-white,
.pdf-table-row-white td {
    background: #ffffff !important;
}

.pdf-section-block .row {
    border-bottom: 2px solid grey !important;
}
.map-data-section {
    border: 2px solid grey;
}

@media print {
    body {
        -webkit-print-color-adjust: exact !important;
        float:none !important;
    }

    .pdf-section-block .col-sm-2, .pdf-section-block .col-xs-2 {
        background: rgb(255,165,0) !important;
    }

    .pdf-section-block-content, .pdf-section-block, .signatures, .signatures > div{
        page-break-inside: avoid !important;
    }

     #pdf_template_2, .pdf-sections-results{
         float: none !important;
     }

    #container1, #pdf_template_2 .pdf-sections-results{
        page-break-before: always !important;
    }
    
    #turnsDiv, #pdf_template_2 .pdf-sections-results{
        page-break-before: always !important;
    }
}



</style>
</head>
<body>
<script src="https://code.highcharts.com/highcharts.js"></script>
<div id="pdf_template">
    <div class="row">
        <div class="col-sm-12 col-xs-12">
            <img src={'./CSDlogo.png'} style="position:relative; top:10px;" width="200" alt=""></img>
            <div class="row">
                <div class="col-sm-12 col-xs-12 text-center">
                    <h3>Certified Safe Driver Inc.</h3>
                    <h4>Behind the Wheel Evaluation and Coaching</h4>
                </div>
            </div>
            <div class="row">
                <div class="col-sm-12 col-xs-12">
                    <div class="row">
                        <div class="col-sm-6 col-xs-6"></div>
                        <div class="col-sm-6 col-xs-6">
                            <span>Company Name</span>
                            <span class="value" id="company">${
                              companyInfo?.name
                            }</span>
                        </div>
                    </div>
                </div>

                <div class="col-sm-4 col-xs-4 text-center">
                    <div>
                        <span>Date:</span>
                        <span class="value" id="dateTime">${
                          state?.date ? state?.date : 'N/A'
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
                          studentInfo?.first_name + ' ' + studentInfo?.last_name
                        }</span>
                    </div>
                </div>
                <div class="col-sm-4 text-center">
                    <div class="row">
                        <div class="col-sm-6 col-xs-6">
                            <div>
                                <span>License Exp. date:</span>
                                <span class="value" id="driverLicenseExpirationDate">${
                                  studentInfo?.info.driver_license_expire_date
                                    ? studentInfo?.info
                                        .driver_license_expire_date
                                    : 'N/A'
                                }</span>
                            </div>
                        </div>
                        <div class="col-sm-6 col-xs-6">
                            <div>
                                <span>Class: </span>
                                <span class="value" id="driverLicenseClass">${
                                  btwClass ? classNameMapping[btwClass] : 'N/A'
                                }</span>
                            </div>
                        </div>
                    </div>
                    <div>
                        <span>History reviewed:</span>
                        <span class="value" id="driverHistoryReviewed">${
                          testInfo?.history_reviewed === false ? 'no' : 'yes'
                        }</span>
                    </div>
                </div>
                <div class="col-sm-4 text-center">
                    <div>
                        <span>Endorsements:</span>
                        <span class="value" id="endorsements">${
                          studentInfo?.info.endorsements === false
                            ? 'no'
                            : 'yes'
                        }</span>
                    </div>
                    <div>
                        <span>Dot Exp. date:</span>
                        <span class="value" id="dotExpirationDate">${
                          studentInfo?.info.dot_expiration_date
                            ? studentInfo?.info.dot_expiration_date
                            : 'N/A'
                        }</span>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-md-12 col-xs-12 text-center"><span>Reasons: </span><span class="value" id="reasons">${
          testInfo?.new_hire ? 'Training New Hire,' : ''
        } ${testInfo?.near_miss ? 'Training Near Miss,' : ''} ${
    testInfo?.incident_follow_up ? 'Training Incident FollowUp,' : ''
  } ${testInfo?.change_job ? 'Training Change Job,' : ''} ${
    testInfo?.change_of_equipment ? 'Training Change Of Equipment,' : ''
  } ${testInfo?.annual ? 'Training Annual,' : ''}</span></div>
        <div class="col-sm-12 col-xs-12 text-center" style="background-color:rgb(166, 166, 236) !important; width: 110%;">
            <span>5 = performed correctly-4 = Reinforced - 3 = corrected &amp; reinforced - 2 = Multi corrections &amp;
                reinforced - 1 = unacceptable</span>
        </div>
        <div class="col-sm-12 text-center">
            <div class="row">
                <div class="col-sm-6 col-xs-6">
                    <span>Start Time:</span>
                    <span class="value" id="startTime">${
                      testInfo?.start_time ? testInfo?.start_time : 'N/A'
                    }</span>
                </div>
                <div class="col-sm-6 col-xs-6">
                    <span>End Time:</span>
                    <span class="value" id="endTime">${
                      testInfo?.end_time ? testInfo?.end_time : 'N/A'
                    }</span>
                </div>
            </div>
        </div>
        
        
        
        <div class="row" id="pdf_template_1">
        <div class="col-sm-12 col-xs-12 pdf-sections" style="margin-left: 3%;">
            ${htmlString}
        </div>
            <div class="col-sm-12  col-xs-12 signatures" style="padding-left: 52px;padding-top: 12px;">
                <div class="row">
                    <div class="col-sm-3 col-xs-3">
                        <table border="3&quot;" style="width: 360px;margin-left: 45%;">
                            <tbody>
                                <tr>
                                    <td style="border-bottom:3px solid grey">Possible Points: </td>
                                    <td id="pointsPossible" style="border-bottom:3px solid grey; text-align: center;">${
                                      state.totalPossiblePoints
                                    }</td>
                                    <td rowspan="2" style="border-left:3px solid grey; border-right:3px solid grey; text-align: center;"> % Eff
                                    </td>
                                    <td style="text-align: center;" rowspan="2" id="pointsPercentage">${
                                      state.totalEffPercentage
                                    }%</td>
                                </tr>
                                <tr style="border-bottom:3px solid grey">
                                    <td style="border-bottom:3px solid grey">Points Received: </td>
                                    <td style="border-bottom:3px solid grey; text-align: center;" id="pointsReceived">${
                                      state.totalPointsReceived
                                    }</td>
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
                                  studentInfo?.info.corrective_lense_required
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
                                  studentInfo?.info.driver_license_expire_date
                                    ? studentInfo?.info
                                        .driver_license_expire_date
                                    : 'N/A'
                                }</span>
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
    
        <div id="pdf_template_2" style="padding-left: 30px;">
            <div class="pdf-sections-results">
                <table class="table table-bordered" id ="table">
                <tbody>
                    ${htmltableRow}
                </tbody>
                </table>
            </div>
            <div id="container1" style="min-height: 400px; min-width:300px; margin:0 auto;"></div>
            <div id="container2" style="min-height: 400px; min-width:300px; margin:0 auto;"></div>
            <div id="turnsDiv"> 
            <img src="${map_screenshot_img}" style="width:1000px; height:1200px;" alt="">
            <div/>
        </div>
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
                        name: 'Probability',
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

                Highcharts.chart("container2", {
                  chart: {
                    type: "column",
                  },
                  title: {
                    text: "Accident Probability Chart",
                  },
                  xAxis: {
                    type: "category",
                    labels: {
                      rotation: -45,
                      style: {
                        fontSize: "13px",
                        fontFamily: "Verdana, sans-serif",
                      },
                    },
                  },
                  yAxis: {
                    min: 0,
                    title: {
                      text: "",
                    },
                  },
                  legend: {
                    enabled: false,
                  },
                  
                  series: [
                    {
                      name: "Probability",
                      data: [${charData}],
                      dataLabels: {
                        enabled: true,
                        rotation: -90,
                        color: "#FFFFFF",
                        align: "right",
                        format: "{point.y:.1f}", // one decimal
                        y: 10, // 10 pixels down from the top
                        style: {
                          fontSize: "13px",
                          fontFamily: "Verdana, sans-serif",
                        },
                      },
                    },
                  ],
                });

                


                
            </script>
</div>

</body>
</html>`;
};
