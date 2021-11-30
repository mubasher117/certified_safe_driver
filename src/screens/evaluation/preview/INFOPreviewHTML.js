/* eslint-disable prettier/prettier */
import React from 'react';
import _, {isNumber} from 'lodash';
import {counterToAlpha} from '../../../utils/function';
import moment from 'moment';

export default INFO = (
  studentNotes,
  state,
  studentInfo,
  companyInfo,
  instructorInfo,
  infoicon,
  dataModal,
  testInfo,
  charData,
  pdf,
  dataModal_btw,
  charData_btw,
  mapData,
  map_screenshot_url,
  dataModal_swp,
  charData_swp,
  dataModalVrt,
  eye_screenshot,
  map_screenshot_img,
) => {
  let htmlString = '';
  let level1Counter = 0;
  let level2Counter = 0;
  let level2HTML = '';
  let htmlsignature = '';
  let htmltableRow = '';
  let totalPossiblePoints = 0;
  let totalPointsReceived = 0;
  let effectiveBarChartData = [];
  // console.log('studentInfo: ', studentInfo, state.medical_card_expire_date, testInfo );
  console.log('state:    ', state);
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
          if (
            key == 'key' ||
            key == 'title' ||
            level2.key == 'possible_points' ||
            level2.key == 'points_received' ||
            level2.key == 'percent_effective'
          ) {
            // return null;
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
            level2HTML += `
                    <div class="row">
                    <div class="col-sm-10 col-xs-10">${counterToAlpha(
                      level2Counter,
                    )})  ${level2.title}</div>
                    <div class="col-sm-2 col-xs-2" id="01a">${
                      state[level1.key][level2.key] == 0 ||
                      state[level1.key][level2.key] == null
                        ? 'N/A'
                        : state[level1.key][level2.key]
                    }</div>
                    </div>
                `;
            
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
        });

        htmlString += `
                    <div class=${pdf ? 'col-sm-10' : 'col-sm-6'}>
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

        if (state[level1.key].percent_effective != undefined) {
          effectiveBarChartData.push(
            `["${level1.title}", ${
              state[level1.key].percent_effective
                ? Number(state[level1.key].percent_effective)
                : 5.0
            }]`,
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

  let tableDataHTML = '';

  _.forEach(studentNotes, (notes) => {
    console.log(';; NOTES ;; ', notes);
    tableDataHTML += `
    <tr id ="endtable" role="row">
             <td>${moment(notes?.updated).format('YYYY-MM-DD hh:mm:ss')}</td>
             <td>${notes?.note}</td>
             <td><img src="${notes.image}" alt="Notes's Image" 
      style="width:200px; height:300px;"></td>
              </tr>
    `;
  });

  // BTW DATA

  let htmlString_btw = '';
  let level1Counter_btw = 0;
  let level2Counter_btw = 0;
  let level2HTML_btw = '';
  let htmlsignature_btw = '';
  let htmltableRow_btw = '';
  let effectiveBarChartData_btw = [];
  const leftOk = mapData?.leftOks?.length;
  const leftShort = mapData?.leftShorts?.length;
  const leftWide = mapData?.leftWides?.length;
  const rightOk = mapData?.rightOks?.length;
  const rightShort = mapData?.rightShorts?.length;
  const rightWide = mapData?.rightWides?.length;

  let totalPossiblePoints_btw = 0;
  let totalPointsReceived_btw = 0;
  let totalEffPercentage_btw = 0;
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
  _.forEach(dataModal_btw, (level1) => {
    // console.log('level1', level1)
    if (state[level1.key]) {
      ++level1Counter_btw;
      level2Counter_btw = 0;
      level2HTML_btw = '';
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
          if (level2.key !== 'notes') {
            if (
              state[level1.key][level2.key] &&
              isNumber(state[level1.key][level2.key]) &&
              state[level1.key][level2.key] !== 0
            ) {
              categoryPointsReceived =
                categoryPointsReceived + state[level1.key][level2.key];
              categoryPossiblePoints = categoryPossiblePoints + 5;
              totalPossiblePoints_btw = totalPossiblePoints_btw + 5;
              totalPointsReceived_btw =
                totalPointsReceived_btw + state[level1.key][level2.key];
            }
          }
        }
      });
      categoryPercentage =
        (categoryPointsReceived / categoryPossiblePoints) * 100;
      categoryPercentage = categoryPercentage.toFixed(2);
      if (level1.value === undefined) {
        // console.log('BTWPreviewHTML level1: ', level1);

        htmltableRow_btw += `
                <tr id="01_tr" class="pdf-table-row">
                    <td>${level1Counter_btw}</td>
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
          if (level2.key !== 'notes') {
            ++level2Counter_btw;
            level2HTML_btw += `<div class="row"> 
                <div class="col-sm-10 col-xs-10">${counterToAlpha(
                  level2Counter_btw,
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
          // const instruction = state.instructions_btw.find(instruction=>instruction.field_name==key)
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

        htmlString_btw += `<div class="col-sm-1"></div>
                    <div class=${
                      pdf ? 'col-sm-10' : 'col-sm-5'
                    } style="padding-right: 0px !important;margin-right: 15px;">
                    <div class="pdf-section-block">
                    <div class="pdf-section-block-number"><span>${level1Counter_btw})</span></div>
                    <div class="pdf-section-block-title"><span>${
                      level1.title
                    }</span></div>
                    <div class="pdf-section-block-content">
                    ${level2HTML_btw}
                    </div>
                    </div>
                </div>`;

        // totalPossiblePoints += state[level1.key]['possible_points'] ? Number(state[level1.key]['possible_points']) : 0
        // totalReceivedPoints += state[level1.key]['points_received'] ? Number(state[level1.key]['points_received']) : 0
        // totalPercentEffective += state[level1.key]['percent_effective'] ? Number(state[level1.key]['percent_effective']) : 0

        // effectiveBarChartData = [level1.title, level1.percent_effective ? Number(level1.percent_effective.value) : 0.00]
        if (state[level1.key].percent_effective !== undefined) {
          effectiveBarChartData_btw.push(
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
        htmlsignature_btw += `<div class="col-sm-12 col-xs-12">
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
    }
  });
  totalEffPercentage_btw =
    (totalPointsReceived_btw / totalPossiblePoints_btw) * 100;
  totalEffPercentage_btw = totalEffPercentage_btw.toFixed(2);

  // SWP data

  let htmlString_swp = '';
  let level1Counter_swp = 0;
  let level2Counter_swp = 0;
  let level2HTML_swp = '';
  let htmlsignature_swp = '';
  let htmltableRow_swp = '';
  let effectiveBarChartData_swp = [];
  let totalPossiblePoints_swp = 0;
  let totalPointsReceived_swp = 0;
  let totalEffPercentage_swp = 0;
  _.forEach(dataModal_swp, (level1) => {
    // console.log('level1', level1)
    if (state[level1.key]) {
      ++level1Counter_swp;
      level2Counter_swp = 0;
      level2HTML_swp = '';

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

              totalPossiblePoints_swp = totalPossiblePoints_swp + 5;
              totalPointsReceived_swp =
                totalPointsReceived_swp + state[level1.key][level2.key];
            }
          }
        }
      });

      categoryPercentage =
        (categoryPointsReceived / categoryPossiblePoints) * 100;
      categoryPercentage = categoryPercentage.toFixed(2);
      if (level1.value === undefined) {
        htmltableRow_swp += `
          <tr id="01_tr" class="pdf-table-row">
              <td>${level1Counter_swp}</td>
              <td>${level1.title}</td>
              <td id="01_possible_p">Possible Points: ${categoryPossiblePoints}</td>
              <td id="01_received_p">Points Received: ${categoryPointsReceived}</td>
              <td id="01_effective_p">Percent Effective: ${categoryPercentage} %</td>
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
            ++level2Counter_swp;
            if (typeof level2.value === 'boolean') {
              level2HTML_swp += `
                      <div class="row">
                      <div class="col-sm-10 col-xs-10"> ${counterToAlpha(
                        level2Counter_swp,
                      )}) ${level2.title}</div>
                      <div class="col-sm-2 col-xs-2" id="01a">${
                        state[level1.key][level2.key] == true ? 'yes' : 'no'
                      }</div>
                    </div>
                      `;
            } else {
              level2HTML_swp += `
                      <div class="row">
                      <div class="col-sm-10 col-xs-10"> ${counterToAlpha(
                        level2Counter_swp,
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
            // else if (
            //   !state.instructionsSwp && !state.instructionsSwp[key] &&
            //   state[level1.key][level2.key] !== 0 &&
            //   state[level1.key][level2.key] !== 5 &&
            //   state[level1.key][level2.key] !== true
            // ) {
            //   htmltableRow_swp += `<tr style="border:3px solid #c4c4c4" class="">
            //                             <td style="border-right:3px solid #c4c4c4">${level1Counter_swp}${counterToAlpha(
            //     level2Counter_swp,
            //   )}</td>
            //                             <td style="border-right:3px solid #c4c4c4" colspan="5">No Instructions</td>
            //                         </tr>`;
            // }
          }
        });

        htmlString_swp += `
                  <div class="col-sm-12">
                  <div class="pdf-section-block">
                  <div class="pdf-section-block-number"><span>${level1Counter_swp})</span></div>
                  <div class="pdf-section-block-title"><span>${level1.title}</span></div>
                  <div class="pdf-section-block-content">
                  ${level2HTML_swp}
                  </div>
                  </div>
              </div>`;

        console.log(state[level1.key]);

        if (state[level1.key].percent_effective != undefined) {
          effectiveBarChartData_swp.push(
            `["${level1.title}", ${state[level1.key].percent_effective}]`,
          );
        }
      } else if (level1.title.includes('signature')) {
        htmlsignature_swp += `<div class="col-sm-12 col-xs-12">
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

  totalEffPercentage_swp =
    (totalPointsReceived_swp / totalPossiblePoints_swp) * 100;
  totalEffPercentage_swp = totalEffPercentage_swp.toFixed(2);

  // VRT Data
  let htmlString_vrt = '';
  let level1Counter_vrt = 0;
  let level2Counter_vrt = 0;
  let level2HTML_vrt = '';
  let htmlsignature_vrt = '';
  let htmltableRow_vrt = '';
  let isQualified_vrt = null;
  let notQualifiedRemarks_vrt = '';

  var totalPossiblePoints_vrt = 0;
  var totalPointsReceived_vrt = 0;
  var totalPercentage_vrt = 0;

  _.forEach(dataModalVrt, (level1) => {
    if (state[level1.key])
    {// console.log('level1', level1)
    ++level1Counter_vrt;
    level2Counter_vrt = 0;
    level2HTML_vrt = '';
    if (level1.title == 'Qualified') {
      isQualified_vrt = state[level1.key];
    } else if (level1.title === 'Remarks') {
      console.log('IS QUALIFIED: ', state.qualified);
      console.log('remarks: ', state[level1.key]);
      if (state.qualified === false) {
        notQualifiedRemarks_vrt = state[level1.key];
      }
      // else  (
      //   level1.title === 'Remarks' &&
      //   state.qualified &&
      //   state.qualified === true
      // ) {
      //   notQualifiedRemarks_vrt = ''
      // }
    } else if (level1.value === undefined) {
      htmltableRow_vrt += `<tr style="border:3px solid #c4c4c4 !important;" class="section-results-pdf">
                                    <td>${level1Counter_vrt}</td>
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
          ++level2Counter_vrt;
          level2HTML_vrt += `
                <div class="row">
                <div class="col-xs-12 col-sm-12 col-md-12"  ${
                  level2.title == 'Notes' && 'style="font-weight:bold"'
                }> ${
            level2.title == 'Notes'
              ? ''
              : `${counterToAlpha(level2Counter_vrt)})`
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
          ++level2Counter_vrt;
          level2HTML_vrt += `
                    <div class="row">
                    <div class="col-sm-10 col-xs-10" ${
                      level2.title == 'Score' && 'style="font-weight:bold"'
                    }> ${
            level2.title == 'Score'
              ? ''
              : `${counterToAlpha(level2Counter_vrt)})`
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
            totalPossiblePoints_vrt = totalPossiblePoints_vrt + 4;
            totalPointsReceived_vrt =
              totalPointsReceived_vrt + state[level1.key][level2.key];
          }
        }
        
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
        // }
      });

      htmlString_vrt += `
                <div class=${pdf ? 'col-sm-10' : 'col-sm-6'}>
                <div class="pdf-section-block">
                <div class="pdf-section-block-number"><span>${level1Counter_vrt})</span></div>
                <div class="pdf-section-block-title"><span>${
                  level1.title
                }</span></div>
                <div class="pdf-section-block-content">
          ${level2HTML_vrt}
          </div>
        </div>
      </div>`;
    } else if (level1.title.includes('signature')) {
      htmlsignature_vrt += `<div class="col-sm-12 col-xs-12">
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
    }}
  });

  totalPercentage_vrt =
    (totalPointsReceived_vrt / totalPossiblePoints_vrt) * 100;
  totalPercentage_vrt = totalPercentage_vrt.toFixed(2);
console.log("EYE:     ", eye_screenshot)
  return `<!DOCTYPE html>
    <html>
    
    <head>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
    integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
<style>
#pdf_template {
    background: white;
    width: 950px;
    font-size: 12px;
}

.pdf-section-block {
${!pdf && 'width: 461px;'}
margin: 5px;
overflow: hidden;
${!pdf && 'display: inline-block;'}
vertical-align: top;
}
.pdf-section-block-title {
text-align: center;
text-decoration: underline;
}
.pdf-section-block .col-sm-10, .pdf-section-block .col-xs-10 {
border-right: 2px solid grey;
padding-left: 0px;
padding-right: 0px;
}

.pdf-section-block .col-sm-2, .pdf-section-block .col-xs-2 {
background: rgb(255,165,0) !important;
}

.pdf-section-block .col-sm-10, .pdf-section-block .col-xs-10 {
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

.critical-itemtext{
color: red !important;
}

.pdf-table-row,
.pdf-table-row td {
background: #D3D3D3 !important;
}

.pdf-table-row-white,
.pdf-table-row-white td {
    background: #ffffff !important;
}

.p0{
margin-right: 7px !important;
margin-left: 7px !important;
padding:0 !important
}
    
@media print {
body {
-webkit-print-color-adjust: exact !important;
}

.pdf-section-block .col-sm-2, .pdf-section-block .col-xs-2 {
background: rgb(255,165,0) !important;
}

.pdf-section-block-content, .pdf-section-block, .signatures, #table, .signatures > div{
page-break-inside: avoid;
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
<div id="pdf_template">
    <div class="row" id="pdf_template_1">
        <div class="col-sm-12">
    <img src="CSDlogo.png" style="position:relative; top:10px;" width="200" alt="">
            <div class="row">
                <div class="col-sm-12 text-center">
                    <h3>Certified Safe Driver Inc.</h3>
                    <h4>Pre-Trip Evaluation and Coaching</h4>
                </div>
            </div>
            <div class="row">
                <div class="col-sm-12">
                    <div class="row">
                        <div class="col-sm-6 col-xs-6"></div>
                        <div class="col-sm-6 col-xs-6">
                            <span>Company Name</span>
                            <span class="value" id="company">${
                              companyInfo?.name ? companyInfo.name : 'N/A'
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
                        <span class="value" id="employeeId">GA_553322</span>
                    </div>
                    <div>
                        <span>Driver Name:</span>
                        <span class="value" id="driverName">${
                          studentInfo?.first_name + ' ' + studentInfo?.last_name
                        }</span>
                    </div>
                </div>
                <div class="col-sm-4 col-xs-4 text-center">
                    <div class="row">
                        <div class="col-sm-6">
                            <div>
                                <span>License Exp. date:</span>
                                <span class="value" id="driverLicenseExpirationDate">${
                                  studentInfo?.info
                                    ? studentInfo?.info
                                        .driver_license_expire_date
                                    : 'N/A'
                                }</span>
                            </div>
                        </div>
                        <div class="col-sm-6">
                            <div>
                                <span>Class:</span>
                                <span class="value" id="driverLicenseClass">${
                                  studentInfo?.info
                                    ? studentInfo?.info.driver_license_class
                                    : 'N/A'
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
                <div class="col-sm-4 col-xs-4 text-center">
                    <div>
                        <span>Endorsements:</span>
                        <span class="value" id="endorsements">${
                          testInfo?.endorsements === false ? 'no' : 'yes'
                        }</span>
                    </div>
                    <div>
                        <span>Dot Exp. date:</span>
                        <span class="value" id="dotExpirationDate">${
                          studentInfo?.info
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
        <div class="col-sm-12 text-center" style="background-color:rgb(166, 166, 236)  !important">
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


        <div id="print_data_note">
        <div class="dataTable-container">
            <div id="note_table_print_wrapper" class="dataTables_wrapper form-inline dt-bootstrap no-footer"><div class="row"><div class="col-sm-6"></div><div class="col-sm-6"></div></div><div class="row"><div class="col-sm-12">
            <table id="note_table_print" class="table table-striped table-bordered dataTable no-footer" role="grid">
                <thead>
                    <tr role="row"><th class="sorting_disabled" rowspan="1" colspan="1" style="width: 0px;">Date</th><th class="sorting_disabled" rowspan="1" colspan="1" style="width: 0px;">Note</th>
                    <th class="sorting_disabled" rowspan="1" colspan="1" style="width: 0px;">Image</th>
                    </tr></thead>
                <tbody>
                 ${tableDataHTML}
               </tbody>
               </table></div></div><div class="row"><div class="col-sm-5"></div><div class="col-sm-7"></div></div></div>
        </div>
    </div>
        
        ${htmlString}

        <div class="col-md-12 col-sm-12 col-xs-12 signatures">
            <div class="row p0">
                <div class="col-sm-3 col-xs-3">
                    <table border="3&quot;" style="width: 360px;">
                        <tbody><tr>
                            <td style="border-bottom:3px solid grey"> Possible Points: </td>
                            <td id="pointsPossible" style="border-bottom:3px solid grey; text-align: center;">${
                              state.totalPossiblePoints
                            }</td>
                            <td rowspan="2" style="border-left:3px solid grey; border-right:3px solid grey; text-align: center;">  % Eff
                            </td>
                            <td rowspan="2" id="pointsPercentage" style="text-align: center;">${
                              state.totalEffPercentage
                            } %</td>
                        </tr>
                        <tr style="border-bottom:3px solid grey">
                            <td style="border-bottom:3px solid grey; "> Points Received: </td>
                            <td style="border-bottom:3px solid grey; text-align: center;" id="pointsReceived">${
                              state.totalPointsReceived
                            }</td>
                        </tr>
                    </tbody></table>
                </div>
            </div>
            <br>
            <div class="row p0">
                <div class="col-md-12 col-sm-12 col-xs-12 text-left">
                    <div class="row p0" style="border:1px solid grey">
                        <div class="col-sm-6 col-xs-6" style="border-right:1px solid grey">
                            <span>Corrective lens required:</span>
                            <span id="correctiveLensRequired">${
                              studentInfo?.info &&
                              studentInfo?.info.corrective_lense_required
                                ? 'Yes'
                                : 'No'
                            }</span>
                        </div>
                        <div class="col-sm-6 col-xs-6">
                            <span>Evaluation Location:</span>
                            <span id="pdf_evaluation_location">${
                              studentInfo?.info
                                ? studentInfo?.info.location
                                : 'N/A'
                            }</span>
                        </div>
                    </div>

                    <div class="row p0" style="border:1px solid grey">
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
                              studentInfo?.info
                                ? studentInfo?.info.driver_license_expire_date
                                : 'N/A'
                            }</span>
                        </div>
                    </div>
                </div>
            </div>
            <br>
            <div class="row p0">
                <div class="col-sm-12">
                    <div class="row">
                        ${htmlsignature}
            </div>
        </div>
        <br>
        <br>
    </div>
    <!-- <div style="height:800px !important;"></div> -->
    <div id="pdf_template_2">
        <div class="col-sm-12 pdf-sections-results">
            <table class="table table-bordered" id ="table">
                <tbody>
                    ${htmltableRow}
                <tr></tr>
            </tbody>
                </table>
                <div id="container1" style="min-height: 400px; min-width: 300px; margin: 0 auto"></div>
                <div id="container2" style="min-height: 400px; min-width: 300px; margin: 0 auto"></div>
            </div>
        </div>
    </div>








  <div class="col-sm-12 col-xs-12 pdf-sections" style="margin-left: 3%;">
  <h2>Behind the Wheel Evaluation and Coaching</h2>
</div>



  <div class="col-sm-12 col-xs-12 pdf-sections" style="margin-left: 3%;">
  ${htmlString_btw}
</div>


  <div class="col-sm-12  col-xs-12 signatures" style="padding-left: 52px;padding-top: 12px;">
        <div class="row">
            <div class="col-sm-3 col-xs-3">
                <table border="3&quot;" style="width: 360px;margin-left: 45%;">
                    <tbody>
                        <tr>
                            <td style="border-bottom:3px solid grey">Possible Points: </td>
                            <td id="pointsPossible-2" style="border-bottom:3px solid grey; text-align: center;">${totalPossiblePoints_btw}</td>
                            <td rowspan="2"
                                style="border-left:3px solid grey; border-right:3px solid grey; text-align: center;"> %
                                Eff
                            </td>
                            <td style="text-align: center;" rowspan="2" id="pointsPercentage-2">${totalEffPercentage_btw}%</td>
                        </tr>
                        <tr style="border-bottom:3px solid grey">
                            <td style="border-bottom:3px solid grey">Points Received: </td>
                            <td style="border-bottom:3px solid grey; text-align: center;" id="pointsReceived-2">${totalPointsReceived_btw}</td>
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
                        <span id="correctiveLensRequired-3">${
                          studentInfo?.info.corrective_lense_required
                            ? 'Yes'
                            : 'No'
                        }</span>
                    </div>
                    <div class="col-sm-6 col-xs-6">
                        <span>Evaluation Location:</span>
                        <span id="pdf_evaluation_location-2">${
                          testInfo?.location ? testInfo?.location : 'N/A'
                        }</span>
                    </div>
                </div>

                <div class="row" style="border:1px solid grey">
                    <div class="col-sm-6 col-xs-6" style="border-right:1px solid grey">
                        <span>Driver Name:</span>
                        <span id="pdf_driver_name-2">${
                          studentInfo?.first_name + ' ' + studentInfo?.last_name
                        }</span>
                    </div>
                    <div class="col-sm-6 col-xs-6">
                        <span>Driver License Expiration Date:</span>
                        <span id="driverLicenseExpirationDateBottom-2">${
                          studentInfo?.info.driver_license_expire_date
                            ? studentInfo?.info.driver_license_expire_date
                            : 'N/A'
                        }</span>
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            ${htmlsignature_btw}
        </div>
    </div>








<div id="pdf_template_3" style="padding-left: 30px;">
<div class="pdf-sections-results">
    <table class="table table-bordered" id="table-2">
        <tbody>
            ${htmltableRow_btw}
        </tbody>
    </table>
</div>
<div id="container3" style="min-height: 400px; min-width:300px; margin:0 auto;"></div>
<div id="container4" style="min-height: 400px; min-width:300px; margin:0 auto;"></div>
<div id="turnsDiv">
    <img id="turnsMap" style="width:100%;margin: 0 auto" />
    <div />
</div>
</div>












<div class="col-sm-12 col-xs-12 pdf-sections" style="margin-left: 3%;">
<h2>Safe Work Practice Evaluation and Coaching</h2>
</div>




<div class="col-sm-12 col-xs-12 pdf-sections" style="margin-left: 3%;">
${htmlString_swp}
</div>











<div class="col-sm-12 col-xs-12 signatures">
    <div class="row">
        <div class="col-sm-3 col-xs-3">
            <table border="3&quot;" style="width: 360px;">
                <tbody>
                    <tr>
                        <td style="border-bottom:3px solid grey;">Possible Points: </td>
                        <td id="pointsPossible" style="border-bottom:3px solid grey; text-align: center;">${totalPossiblePoints_swp}</td>
                        <td rowspan="2"
                            style="border-left:3px solid grey; border-right:3px solid grey; text-align: center;">% Eff
                        </td>
                        <td rowspan="2" id="pointsPercentage" style="text-align: center;">${totalEffPercentage_swp}%</td>
                    </tr>
                    <tr style="border-bottom:3px solid grey">
                        <td style="border-bottom:3px solid grey">Points Received: </td>
                        <td style="border-bottom:3px solid grey; text-align: center;" id="pointsReceived">${totalPointsReceived_swp}</td>
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
        <div class="col-sm-12 col-xs-12 text-left">
            <div class="row" style="border:1px solid grey">
                <div class="col-sm-6 col-xs-6" style="border-right:1px solid grey">
                    <span>Driver Name:</span>
                    <span id="pdf_driver_name">${
                      studentInfo?.first_name + ' ' + studentInfo?.last_name
                    }</span>
                </div>
                <div class="col-sm-6 col-xs-6">
                    <span>Evaluation Location:</span>
                    <span id="pdf_evaluation_location">${
                      testInfo?.location ? testInfo?.location : 'N/A'
                    }</span>
                </div>
            </div>
        </div>
    </div>
    <div class="row" style="margin-top:10px;">
        <div class="col-sm-12 col-xs-12">
            <div class="row">
                ${htmlsignature_swp}
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
                    ${htmltableRow_swp}
                    <tr></tr>
                </tbody>
            </table>
            <div id="container5" style="min-width: 300px; height: 400px; margin: 0 auto"></div>
            <div id="container6" style="min-width: 300px; height: 400px; margin: 0 auto"></div>
        </div>
    </div>
</div>









<div class="col-sm-12 col-xs-12 pdf-sections" style="margin-left: 3%;">
<h2>Commercial Motor Vehicle Road Test</h2>
</div>




<div class="col-sm-12 col-xs-12 pdf-sections" style="margin-left: 3%;">
${htmlString_vrt}
</div>

<div class="row">
                            <div class="col-sm-3 col-xs-3">
                                <table border="3&quot;" style="width: 360px;">
                                    <tbody>
                                        <tr>
                                            <td style="border-bottom:3px solid grey">Possible Points: </td>
                                            <td id="pointsPossible" style="border-bottom:3px solid grey; text-align: center;">${totalPossiblePoints_vrt}</td>
                                            <td rowspan="2" style="border-left:3px solid grey; border-right:3px solid grey; text-align: center;">
                                                % Eff
                                            </td>
                                            <td style="text-align: center;" rowspan="2" id="pointsPercentage">${totalPercentage_vrt} %</td>
                                        </tr>
                                        <tr style="border-bottom:3px solid grey">
                                            <td style="border-bottom:3px solid grey">Points Received: </td>
                                            <td style="border-bottom:3px solid grey; text-align: center;" id="pointsReceived">${totalPointsReceived_vrt}</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                            <div class="col-sm-9 col-xs-9 text-center">
                                <span></span>
                            </div>
                        </div>





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
                    ${htmlsignature_vrt}
                    </div>








                    <div class="col-sm-12 col-xs-12" id="pdf_template_2" style="width: 100%;padding-top: 20px !important;">
                    <div class="pdf-sections-results">
                        <table class="table table-bordered">
                            <tbody>
                                <tr style="border-bottom:3px solid grey">
                                    <td style="border-bottom:3px solid grey; background-color: #c6c6c6 !important;">Score:
                                    </td>
                                    <td style="border-bottom:3px solid grey;" id="form_scored1">${totalPercentage_vrt} %</td>
                                    <td style="border-bottom:3px solid grey; background-color: #c6c6c6 !important;">
                                        Qualified</td>
                                    <td style="border-bottom:3px solid grey;" id="qualified1">${
                                      isQualified_vrt === true ? 'X' : ''
                                    }</td>
                                    <td style="border-bottom:3px solid grey; background-color: #c6c6c6 !important;">No
                                        Qualified</td>
                                    <td style="border-bottom:3px solid grey;" id="notQualified1">${
                                      isQualified_vrt === false ? 'X' : ''
                                    }</td>
                                </tr>
                                <tr>
                                    <td colspan="6" style="padding: 7px; border: 3px solid #c4c4c4;">If NOT
                                        Qualified(EXPLAIN)</td>
                                </tr>
                                <tr>
                                    <td colspan="6" style="padding: 14px; border: 3px solid #c4c4c4;"
                                        id="disqualifiedRemarks">${notQualifiedRemarks_vrt}</td>
                                </tr>
                                <tr>
                                    <td colspan="6" style="padding: 14px; border: 3px solid #c4c4c4;"></td>
                                </tr>

                                ${htmltableRow_vrt}
    
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


                    <div class="col-sm-12 col-xs-12" style="border:1px solid;">
                        <h6 class="text-center">Company District Office Address</h6>
                        <h6 class="text-center">Certified Safe Driver Inc. 20803 E.Valley Suite 109 Walnut CA 91789</h6>
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




                        <img src="${eye_screenshot}"" style="width:800px; height:1200px;" alt="">
                        <img src="${map_screenshot_img}"" style="width:800px; height:1200px;" alt="">
                        


                    


    <script>
    Highcharts.chart('container1', {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Pre-Trip Percent Effective'
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
                text: 'Pre-Trip Percent Effective'
            }
        },
        legend: {
            enabled: false
        },
        tooltip: {
            pointFormat: '<b>{point.y:.1f}%</b>'
        },
        series: [{
            name: '',
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

    Highcharts.chart('container3', {
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
          data: [${effectiveBarChartData_btw}],
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

  Highcharts.chart("container4", {
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
              data: [${charData_btw}],
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
  Highcharts.chart('container5', {
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
        data: [${effectiveBarChartData_swp}],
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

Highcharts.chart('container6', {
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
        data: [${charData_swp}],
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
    </html>`;
};
