import React from 'react';
import _ from 'lodash';
import { counterToAlpha } from '../../../utils/function';

export default PAS = (dataModal, state, studentInfo, companyInfo, testInfo, pdf) => {
    let htmlString = ''
    let level1Counter = 0;
    let level2Counter = 0;
    let level2HTML = '';
    let htmlsignature = '';
    _.forEach(dataModal, (level1) => {
        // console.log('level1', level1)
        ++level1Counter;
        level2Counter = 0;
        level2HTML = "";
        if (level1.value === undefined) {
            _.forEach(level1, (level2, key) => {
                if (key == 'key' || key == 'title' || level2.key == "possible_points" || level2.key == "points_received" || level2.key == "percent_effective") {
                    return null;
                }
                if (level2.key != 'notes') {
                    ++level2Counter;
                    level2HTML += `
                <div class="row">
                <div class="col-sm-10 col-xs-10">${counterToAlpha(level2Counter)})  ${level2.title}</div>
                <div class="col-sm-2 col-xs-2" id="01a">${state[level1.key][level2.key] == 0 ? 'N/A' : state[level1.key][level2.key]}</div>
              </div>
                `
                }
            })

            htmlString += `
                <div class=${pdf ? "col-sm-10" : "col-sm-6"}>
                <div class="pdf-section-block">
                <div class="pdf-section-block-number"><span>${level1Counter})</span></div>
                <div class="pdf-section-block-title"><span>${level1.title}</span></div>
                <div class="pdf-section-block-content">
          ${level2HTML}
          </div>
        </div>
      </div>`
        } else if (level1.title.includes('signature')) {
            htmlsignature += `<div class="col-sm-12 col-xs-12">
            <div class="row">
                <div class="col-sm-2 col-xs-2">
                    <span style="line-height: 75px;">${level1.title}:</span>
                </div>
                <div class="col-sm-6 col-xs-6" style="border-bottom:2px solid grey;">
                    <img  src=${state[level1.key]} id="pdf_driver_signature" width="100" height="50">
                    <span id="pdf_driver_signature_name"></span>
                </div>
                <div class="col-sm-4 col-xs-4">
                    <br>
                    <br>
                    <div class="row">
                        <div class="col-sm-4 col-xs-4">
                            <span>Date:</span>
                        </div>
                        <div class="col-sm-8 col-xs-8" style="border-bottom:2px solid grey">
                            <span id="pdf_driver_signature_date"></span>
                        </div>
                    </div>
                </div>
            </div>
        </div>`
        }

    })

    return (`<!DOCTYPE html>
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
            ${!pdf && `width: 400px;`}
            margin: 5px;
            overflow: hidden;
            ${!pdf && `display: inline-block;`}
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
            <div class="col-sm-12">
                <img src="CSDlogo.png" style="position:relative; top:10px;" width="200" alt="">
                <div class="row">
                    <div class="col-sm-12 text-center">
                        <h3>Certified Safe Driver Inc.</h3>
                        <h4>Passenger Vehicle</h4>
                    </div>
                </div>
                <div class="row">
                    <div class="col-sm-12">
                        <div class="row">
                            <div class="col-sm-6"></div>
                            <div class="col-sm-6">
                                <span>Company Name</span>
                                <span class="value" id="company">${companyInfo?.name}</span>
                            </div>
                        </div>
                    </div>
    
                    <div class="col-sm-4 text-center">
                        <div>
                            <span>Date:</span>
                            <span class="value" id="dateTime">${testInfo?.date_of_hire}</span>
                        </div>
                        <div>
                            <span>Employee #:</span>
                            <span class="value" id="employeeId">111</span>
                        </div>
                        <div>
                            <span>Driver Name:</span>
                            <span class="value" id="driverName">${studentInfo?.first_name + ' ' + studentInfo?.last_name}</span>
                        </div>
                    </div>
                    <div class="col-sm-4 text-center">
                        <div class="row">
                            <div class="col-sm-6">
                                <div>
                                    <span>License Exp. date:</span>
                                    <span class="value" id="driverLicenseExpirationDate">${testInfo?.driver_license_expire_date}</span>
                                </div>
                            </div>
                            <div class="col-sm-6">
                                <div>
                                    <span>Class:</span>
                                    <span class="value" id="driverLicenseClass">${testInfo?.driver_license_class}</span>
                                </div>
                            </div>
                        </div>
                        <div>
                            <span>History reviewed:</span>
                            <span class="value" id="driverHistoryReviewed">${testInfo?.history_reviewed === false ? 'no' : 'yes'}</span>
                        </div>
                    </div>
                    <div class="col-sm-4 text-center">
                        <div>
                            <span>Endorsements:</span>
                            <span class="value" id="endorsements">${testInfo?.endorsements === false ? 'no' : 'yes'}</span>
                        </div>
                        <div>
                            <span>Dot Exp. date:</span>
                            <span class="value" id="dotExpirationDate">${testInfo?.dot_expiration_date}</span>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-sm-12 text-center" style="background-color:rgb(166, 166, 236) !important">
                <span>5 = performed correctly-4 = Reinforced - 3 = corrected &amp; reinforced - 2 = Multi corrections &amp;
                    reinforced - 1 = unacceptable</span>
            </div>
            <div class="col-sm-12 text-center">
                <div class="row">
                    <div class="col-sm-6">
                        <span>Start Time:</span>
                        <span class="value" id="startTime">${testInfo?.start_time}</span>
                    </div>
                    <div class="col-sm-6">
                        <span>End Time:</span>
                        <span class="value" id="endTime">${testInfo?.end_time}</span>
                    </div>
                </div>
            </div>
        
            
            <div class="row" id="pdf_template_1" style="padding-left: 30px;">
            ${htmlString}
           </div>
            <div class="col-sm-12  col-xs-12 signatures" style="padding-left: 52px;">
                <div class="row">
                    <div class="col-sm-3 col-xs-3">
                        <table border="3&quot;" style="width: 360px;">
                            <tbody>
                                <tr>
                                    <td style="border-bottom:3px solid grey">Possible Points: </td>
                                    <td id="pointsPossible" style="border-bottom:3px solid grey">595</td>
                                    <td rowspan="2" style="border-left:3px solid grey; border-right:3px solid grey">% Eff
                                    </td>
                                    <td rowspan="2" id="pointsPercentage">0.00 %</td>
                                </tr>
                                <tr style="border-bottom:3px solid grey">
                                    <td style="border-bottom:3px solid grey">Points Received: </td>
                                    <td style="border-bottom:3px solid grey" id="pointsReceived">0</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <div class="col-sm-9 text-center">
                        <span>See supplimental</span>
                    </div>
                </div>
                <br>
                <div class="row">
                    <div class="col-sm-12">
                        <div class="row" style="border:1px solid grey">
                            <div class="col-sm-6" style="border-right:1px solid grey">
                                <span>Corrective lens required:</span>
                                <span id="correctiveLensRequired">No</span>
                            </div>
                            <div class="col-sm-6">
                                <span>Power Unit:</span>
                                <span id="powerUnit">HDT</span>
                            </div>
                        </div>
    
                        <div class="row" style="border:1px solid grey">
                            <div class="col-sm-6" style="border-right:1px solid grey">
                                <span>Evaluation Location:</span>
                                <span id="pdf_evaluation_location">No</span>
                            </div>
                            <div class="col-sm-6">
                                <span>Driver Name:</span>
                                <span id="pdf_driver_name">No</span>
                                </span>
                            </div>
                        </div>
    
                        <div class="row" style="border:1px solid grey">
                            <div class="col-sm-6" style="border-right:1px solid grey">
                                <span></span>
                                <span></span>
                            </div>
                            <div class="col-sm-6">
                                <span>Driver License Expiration Date:</span>
                                <span id="driverLicenseExpirationDateBottom"></span>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-sm-12">
                        <div class="row">
                            ${htmlsignature}
                    </div>
                </div>
                <br>
                <br>
            </div>
            <br>
            <br>
            </div>
            
            <div id="pdf_template_2" style="padding-left: 30px;">
                    <div class="pdf-sections-results">
                        <table class="table table-bordered" id ="table">
                        <tbody>
                        <tr></tr>
                        <tr id="01_tr" class="pdf-table-row">
                            <td>1</td>
                            <td>Cab Safety</td>
                            <td id="01_possible_p">Possible Points: 0</td>
                            <td id="01_received_p">Points Received: 0</td>
                            <td id="01_effective_p">Percent Effective: 0.00 %</td>
                            <td id="01_note">Note: N/A </td>
                        </tr>
                        <tr></tr>
                        <tr id="02_tr" class="pdf-table-row">
                            <td>2</td>
                            <td>Start Engine</td>
                            <td id="02_possible_p">Possible Points: 0</td>
                            <td id="02_received_p">Points Received: 0</td>
                            <td id="02_effective_p">Percent Effective: 0.00 %</td>
                            <td id="02_note">Note: N/A </td>
                        </tr>
                        <tr></tr>
                        <tr id="03_tr" class="pdf-table-row">
                            <td>3</td>
                            <td>Engine Operation</td>
                            <td id="03_possible_p">Possible Points: 0</td>
                            <td id="03_received_p">Points Received: 0</td>
                            <td id="03_effective_p">Percent Effective: 0.00 %</td>
                            <td id="03_note">Note: N/A </td>
                        </tr>
                        <tr></tr>
                        <tr id="04_tr" class="pdf-table-row">
                            <td>4</td>
                            <td>Use of Brakes and Stopping</td>
                            <td id="04_possible_p">Possible Points: 0</td>
                            <td id="04_received_p">Points Received: 0</td>
                            <td id="04_effective_p">Percent Effective: 0.00 %</td>
                            <td id="04_note">Note: N/A </td>
                        </tr>
                        <tr></tr>
                        <tr id="05_tr" class="pdf-table-row">
                            <td>5</td>
                            <td>Passenger Safety</td>
                            <td id="05_possible_p">Possible Points: 0</td>
                            <td id="05_received_p">Points Received: 0</td>
                            <td id="05_effective_p">Percent Effective: 0.00 %</td>
                            <td id="05_note">Note: N/A </td>
                        </tr>
                        <tr></tr>
                        <tr id="06_tr" class="pdf-table-row">
                            <td>6</td>
                            <td>Eye Movement and Mirror Use</td>
                            <td id="06_possible_p">Possible Points: 0</td>
                            <td id="06_received_p">Points Received: 0</td>
                            <td id="06_effective_p">Percent Effective: 0.00 %</td>
                            <td id="06_note">Note: N/A </td>
                        </tr>
                        <tr></tr>
                        <tr id="07_tr" class="pdf-table-row">
                            <td>7</td>
                            <td>Recognizes Hazards</td>
                            <td id="07_possible_p">Possible Points: 0</td>
                            <td id="07_received_p">Points Received: 0</td>
                            <td id="07_effective_p">Percent Effective: 0.00 %</td>
                            <td id="07_note">Note: N/A </td>
                        </tr>
                        <tr></tr>
                        <tr id="08_tr" class="pdf-table-row">
                            <td>8</td>
                            <td>Lights and Signals</td>
                            <td id="08_possible_p">Possible Points: 0</td>
                            <td id="08_received_p">Points Received: 0</td>
                            <td id="08_effective_p">Percent Effective: 0.00 %</td>
                            <td id="08_note">Note: N/A </td>
                        </tr>
                        <tr></tr>
                        <tr id="09_tr" class="pdf-table-row">
                            <td>9</td>
                            <td>Steering</td>
                            <td id="09_possible_p">Possible Points: 0</td>
                            <td id="09_received_p">Points Received: 0</td>
                            <td id="09_effective_p">Percent Effective: 0.00 %</td>
                            <td id="09_note">Note: N/A </td>
                        </tr>
                        <tr></tr>
                        <tr id="10_tr" class="pdf-table-row">
                            <td>10</td>
                            <td>Backing</td>
                            <td id="10_possible_p">Possible Points: 0</td>
                            <td id="10_received_p">Points Received: 0</td>
                            <td id="10_effective_p">Percent Effective: 0.00 %</td>
                            <td id="10_note">Note: N/A </td>
                        </tr>
                        <tr></tr>
                        <tr id="11_tr" class="pdf-table-row">
                            <td>11</td>
                            <td>Speed</td>
                            <td id="11_possible_p">Possible Points: 0</td>
                            <td id="11_received_p">Points Received: 0</td>
                            <td id="11_effective_p">Percent Effective: 0.00 %</td>
                            <td id="11_note">Note: N/A </td>
                        </tr>
                        <tr></tr>
                        <tr id="12_tr" class="pdf-table-row">
                            <td>12</td>
                            <td>Intersections</td>
                            <td id="12_possible_p">Possible Points: 0</td>
                            <td id="12_received_p">Points Received: 0</td>
                            <td id="12_effective_p">Percent Effective: 0.00 %</td>
                            <td id="12_note">Note: N/A </td>
                        </tr>
                        <tr></tr>
                        <tr id="13_tr" class="pdf-table-row">
                            <td>13</td>
                            <td>Turning</td>
                            <td id="13_possible_p">Possible Points: 0</td>
                            <td id="13_received_p">Points Received: 0</td>
                            <td id="13_effective_p">Percent Effective: 0.00 %</td>
                            <td id="13_note">Note: N/A </td>
                        </tr>
                        <tr></tr>
                        <tr id="14_tr" class="pdf-table-row">
                            <td>14</td>
                            <td>Parking</td>
                            <td id="14_possible_p">Possible Points: 0</td>
                            <td id="14_received_p">Points Received: 0</td>
                            <td id="14_effective_p">Percent Effective: 0.00 %</td>
                            <td id="14_note">Note: N/A </td>
                        </tr>
                        <tr></tr>
                        <tr id="15_tr" class="pdf-table-row">
                            <td>15</td>
                            <td>Hills</td>
                            <td id="15_possible_p">Possible Points: 0</td>
                            <td id="15_received_p">Points Received: 0</td>
                            <td id="15_effective_p">Percent Effective: 0.00 %</td>
                            <td id="15_note">Note: N/A </td>
                        </tr>
                        <tr></tr>
                        <tr id="16_tr" class="pdf-table-row">
                            <td>16</td>
                            <td>Passing</td>
                            <td id="16_possible_p">Possible Points: 0</td>
                            <td id="16_received_p">Points Received: 0</td>
                            <td id="16_effective_p">Percent Effective: 0.00 %</td>
                            <td id="16_note">Note: N/A </td>
                        </tr>
                        <tr></tr>
                        <tr id="17_tr" class="pdf-table-row">
                            <td>17</td>
                            <td>Railroad Crossing</td>
                            <td id="17_possible_p">Possible Points: 0</td>
                            <td id="17_received_p">Points Received: 0</td>
                            <td id="17_effective_p">Percent Effective: 0.00 %</td>
                            <td id="17_note">Note: N/A </td>
                        </tr>
                        <tr></tr>
                        <tr id="18_tr" class="pdf-table-row">
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
                <div id="container1" style="min-width: 300px; height: 400px; margin: 0 auto"></div>
                <div id="container2" style="min-width: 300px; height: 400px; margin: 0 auto"></div>
                <div id="turnsDiv"> 
                    <img id="turnsMap" style="width:100%;margin: 0 auto" />
                <div/>
            </div>
        </div>
    </div>
    </body>
    </html>
    `)
}