import React from 'react';
import _ from 'lodash';
import { counterToAlpha } from '../../../utils/function';


{/* <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css"
integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous"> */}

export default PROD = () => {
    
    return (`<!DOCTYPE html>
    <html lang="en">
    
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
    integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <head>

<style>
.underLined, .bordered{
    width:100%;
    border-bottom: 1px solid #000;
  }

.bordered{
  border:1px solid #000;
  padding: 5px 0px;
}

.mb-0{
  margin-bottom: 0;
}

.p-0{
  padding: 0px;
}

.p-10{
  padding: 5px 0px;
}


.bold>p{
  font-weight: bold;
  min-height: 33px;
}

.underLined{
  min-height: 27px !important;
}

.bold{
  padding-left: 0;
}

.coloredBlue{
  background-color: #bed8ee !important;
  /* margin-top: -24px; */
}

#header_logo{
  padding-left: 32px;
  padding-right: 0px;;
}

#pdf_table{
  border-collapse: collapse;
  border:1px solid;
  overflow: hidden;
}

#pdf_table thead{
  overflow: hidden !important;
  background-color: #d9e1f2 !important;
}

#pdf_table tbody{
  width: 97% !important;
}

#pdf_table tbody tr{
  width: 100%;
  border:1px solid #000 !important;
}

#pdf_table tbody tr td{
  width: 4%;
  border: 1px solid #000;
  vertical-align: middle;
  font-size: 11px;
  background: #fff !important;
  position: relative;
  z-index: 12;
}

#pdf_table tbody tr td:first-child{
  width: 5%;
}

#pdf_table tbody tr td:nth-child(2){
  width: 5%;
  word-break: break-all;
}

#pdf_table tbody tr td:nth-child(3){
  width: 6%;
  word-break: break-all;
}

#pdf_table tbody tr td:last-child{
  width: 6%;
  padding: 0;
}

.pdf_tableHeader{
  position: relative !important;
  height: 118px;
}

.transformed{
  padding: 23px 36px 23px 73px;
  transform: rotate(-55deg);
  border: 1px solid #000 !important;
  width: 245px !important;
  height: 24px !important;
  position: absolute;
  bottom: 24px;
  font-size: 12px !important;
  margin-left: -60px;
}


.on_buttom{
  position: relative;
  bottom: -21px;
}

#table_note{
  background-color: #fff !important;
  position: absolute;
  top: 20px;
  left: 31px;
  padding: 5px;
  width: 170px;
  border: 1px solid #ccc !important;
  font-size: 12px;
}

.small-size{
  font-size: 13px;
}

.odometer-divs{
  display: inline-block;
  border-right: 1px solid #000;
  width: 48%;
  margin: 0;
  padding: 21px 21px 21px 4px;
  min-height: 64px;
  vertical-align: middle;
}

.no-border{
  border:none !important;

}

@media print {

  table { page-break-after:auto; display: block; }
  tr    { page-break-inside:avoid;}
  td    { page-break-inside:avoid;}

  

  .signatures {page-break-before: always;}

  body {
      -webkit-print-color-adjust: exact !important;
      float:none !important;
  }

  #pdf_table tbody tr{
  width: 100%;
  border:1px solid #000 !important;
}

#pdf_table tbody tr td{
  width: 4%;
  border: 3px solid #000 !important;
  vertical-align: middle;
  font-size: 11px;
  background: #fff !important;
  position: relative;
  z-index: 12;
  -webkit-print-color-adjust: exact !important;
}

#pdf_table thead{
  overflow: hidden !important;
  background-color: #d9e1f2 !important;
}

#pdf_table thead th{
  background-color: #d9e1f2 !important;
}

.transformed{
  padding: 23px 36px 23px 73px;
  -ms-transform: rotateY(-55deg);
  -webkit-transform: rotateY(-55deg);
  -moz-transform: rotateY(-55deg);
  -o-transform: rotateY(-55deg);
  transform: rotate(-55deg);
  border: 1px solid #000 !important;
  width: 245px;
  height: 24px;
  position: absolute;
  bottom: 24px;
  font-size: 12px !important;
  margin-left: -60px;
  z-index: 10;
}

.pdf_tableHeader{
  position: relative;
  height: 118px;
}

}
		
      </style>

</head>
   

<body>
  <div id="pdf_template" style="width:1000px; padding-left: 20px;">
    <div class="row" id="pdf_template_1">

        <div class="pdf-sections">
          <div id="new_pdf" class="row">
              <div class="col-sm-2 col-xs-2 small-size">
                  <p class="text-right">Date:</p>
                  <p class="text-right">Employee #:</p>
                  <p class="text-right">Driver Name:</p>
                  <p class="text-right">Observer:</p>
              </div>
              <div class="col-sm-2 col-xs-2 bold small-size">
                  <p class="text-left underLined" id="dateTime">04/02/2020</p>
                  <p class="text-left underLined" id="employeeId">ll3456</p>
                  <p class="text-left underLined" id="driverName">Cola 11F Cola 11L</p>
                  <p class="text-left" id="observer">Instructor1 Instructor1</p>
              </div>
              <div class="col-sm-4 col-xs-4" id="header_logo">
                  <div class="col-sm-12 text-center">
                      <img src="https://lirp-cdn.multiscreensite.com/da9c67e6/dms3rep/multi/opt/csd+logo-306w.png" width="200" alt="CSD">
                  </div>
                  <h3 class="text-center">Certified Safe Driver, Inc.</h3>
              </div>
              <div class="col-sm-2 col-xs-2 small-size">
                  <p class="text-right mb-0 p-10">Company Name:</p>
                  <p class="text-right mb-0 p-10">Department:</p>
                  <p class="text-right mb-0 p-10">Route Number:</p>
              </div>
              <div class="col-sm-2 col-xs-2 bold small-size">
                  <p class="text-center bordered mb-0" id="company">Coca Cola</p>
                  <p class="text-center bordered mb-0" id="department">5346</p>
                  <p class="text-center bordered mb-0" id="routeNumber">345</p>
                  <p class="text-center bordered mb-0" style="padding:12px;"></p>
              </div>
              <div class="col-sm-12 col-xs-12">
                  <div class="col-sm-12 col-xs-12 text-center bordered coloredBlue">
                      5 = performed correctly - 4 = Reinforced - 3 = corrected &amp; reinforced - 2 = Mult corrections &amp; reinforced - 1 = unacceptable
                  </div>
              </div>
              <div class="col-sm-12 col-xs-12" style="position: relative; z-index:14; background: #fff;">
                  <div class="col-sm-1 col-xs-1 p-0 small-size">
                      <p class="text-right mb-0 p-10">Start time:</p>
                      <p class="text-right mb-0 p-10">Finish time:</p>
                  </div>
                  <div class="col-sm-1 col-xs-1 bold" style="padding-left: 2px;">
                      <p class="text-center bordered mb-0" id="startTime" style="min-height: 30px;"></p>
                      <p class="text-center bordered mb-0" id="endTime" style="min-height: 30px;"></p>
                  </div>
                  <div class="col-sm-2 col-xs-2 p-0 small-size">
                      <p class="text-right mb-0 p-10">On Time</p>
                      <p class="text-right mb-0 p-10">Keys Ready</p>
                      <p class="text-right mb-0 p-10">Timecard System Ready</p>
                  </div>
                  <div class="col-sm-1 col-xs-1 bold" style="padding-left: 2px;">
                      <p class="text-center bordered mb-0" id="onTime">Yes</p>
                      <p class="text-center bordered mb-0" id="keysReady">Yes</p>
                      <p class="text-center bordered mb-0" id="timecardSystemReady">Yes</p>
                  </div>
                  <div class="col-sm-2 col-xs-1 p-0 small-size">
                      <p class="text-right mb-0 p-10">Equipment Ready</p>
                      <p class="text-right mb-0 p-10">Equipment Clean</p>
                  </div>
                  <div class="col-sm-1 col-xs-1 bold" style="padding-left: 2px;">
                      <p class="text-center bordered mb-0" id="equipmentReady">Yes</p>
                      <p class="text-center bordered mb-0" id="equipmentClean">Yes</p>
                  </div>
                  <div class="col-sm-2 col-xs-2 p-0 small-size" style="padding-right: 2px;">
                      <p class="text-right mb-0 p-10">Start Odometer</p>
                      <p class="text-right mb-0 p-10">Finish Odometer</p>
                      <p class="text-right mb-0 p-10">Miles</p>
                  </div>
                  <div class="col-sm-2 col-xs-2 p-0" style="border:1px solid #000;">
                      <div class="col-sm-12 col-xs-12 p-0">
                          <div class="col-sm-4 col-xs-4 bold p-0">
                              <p class="text-center bordered mb-0" id="startOdometer">6658</p>
                          </div>
                          <div class="col-sm-4 col-xs-4 bold p-0">
                              <p class="text-center bordered mb-0" style="min-height: 33px; width: 100%;"></p>
                          </div>
                      </div>
                      <div class="col-sm-12 col-xs-12 p-0">
                          <div class="col-sm-4 col-xs-4 bold p-0">
                              <p class="text-center bordered mb-0" id="finishOdometer">324</p>
                          </div>
                          <div class="col-sm-4 col-xs-4 bold p-0">
                              <p class="text-center bordered mb-0" style="min-height: 33px; width: 100%;"></p>
                          </div>
                      </div>
                      <div class="col-sm-12 col-xs-12 p-0">
                          <div class="col-sm-4 col-xs-4 bold p-0">
                              <p class="text-center bordered mb-0" id="miles">mil</p>
                          </div>
                          <div class="col-sm-4 col-xs-4 bold p-0">
                              <p class="text-center bordered mb-0" style="min-height: 33px; width: 100%;"></p>
                          </div>
                          <div class="col-sm-4 col-xs-4 bold p-0">
                              <p class="text-center bordered mb-0" style="min-height: 33px; width: 100%;"></p>
                          </div>
                      </div>
                  </div>
              </div>
      
              <div class="col-sm-12 col-xs-12" style="top:-3px">
                  <p id="table_note">
                      If you change tractors, skip a line and start with new tractor miles
                  </p>
                  <table id="pdf_table" class="table table-striped table-bordered">
                      <thead>
                          
                      
     				<th style="width:3%; vertical-align:bottom;"><p class="on_buttom">Time</p></th>
     				<th style="width:3%; vertical-align:bottom;"><p class="on_buttom">Location</p></th>
    				 <th style="width:3%; vertical-align:bottom;"><p class="on_buttom">Trailer #</p></th><th style="width:3%" class="pdf_tableHeader"><p class="transformed">Start Work</p></th><th style="width:3%" class="pdf_tableHeader"><p class="transformed">Leave building</p></th><th style="width:3%" class="pdf_tableHeader"><p class="transformed">Travel Path</p></th><th style="width:3%" class="pdf_tableHeader"><p class="transformed">Speed</p></th><th style="width:3%" class="pdf_tableHeader"><p class="transformed">Idle Time</p></th><th style="width:3%" class="pdf_tableHeader"><p class="transformed">Plan Ahead</p></th><th style="width:3%" class="pdf_tableHeader"><p class="transformed">Turn Around</p></th><th style="width:3%" class="pdf_tableHeader"><p class="transformed">On Schedule</p></th><th style="width:3%" class="pdf_tableHeader"><p class="transformed">Customer Contact</p></th><th style="width:3%" class="pdf_tableHeader"><p class="transformed">Not Ready Situations</p></th><th style="width:3%" class="pdf_tableHeader"><p class="transformed">Brisk Pace</p></th><th style="width:3%" class="pdf_tableHeader"><p class="transformed">Finish Work</p></th><th style="width:2%; vertical-align:bottom;" class="pdf_tableHeader"><p class="on_buttom">Odometer</p></th></thead>
                <tbody>
                  
                  <tr id ="insert_before_this_div"><td style="border:none !important;"></td><td style="border:none !important;"></td><td style="border:none !important;"></td>
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
                  <td><div class="odometer-divs"></div><div class="odometer-divs" style="border-right:none;" id="totalMiles">133</div></td></tr>
                  <tr><td style="border:none !important;"></td><td style="border:none !important; text-align:right">Percent</td><td style="border:none !important;">Effective</td>
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
                  <td><div class="odometer-divs"><b>Total</b></div><div class="odometer-divs" style="border-right:none;" id="totalPercentage">56%</div></td></tr>
                </tbody>
            </table>
                  
              </div>
              <div class="col-sm-12">
                  
              </div>
          </div>
      </div>
        <br>
        <br>

        <div class="col-sm-12 col-xs-12 signatures"> 
          <br>
          
          <div class="row">
              <div class="col-sm-12 col-xs-12">
                  <div class="row">
                      <div class="col-sm-2 col-xs-2">
                          <span style="line-height: 75px; position: relative; bottom: -27px;">Employee Signature:</span>
                      </div>
                      <div class="col-sm-6 col-xs-6" style="border-bottom:2px solid grey; height:70px;">
                            <img id="pdf_driver_signature" width="100" height="70" alt="">
                            <span id="pdf_driver_signature_name"></span>                      
                      </div>
                      <div class="col-sm-4 col-xs-4">
                          <br>
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
              </div>
              <br>
              <div class="col-sm-12 col-xs-12">
                  <div class="row">
                      <div class="col-sm-2 col-xs-2">
                          <span style="line-height: 75px; position: relative; bottom: -27px;">Trainer Signature:</span>
                      </div>
                      <div class="col-sm-6 col-xs-6" style="border-bottom:2px solid grey; height:70px;">
                            <img id="pdf_evaluators_signature" width="100" height="70" alt="">
                            <span id="pdf_evaluators_signature_name"></span>                     
                      </div>
                      <div class="col-sm-4 col-xs-4">
                          <br>
                          <br>
                          <br>
                          
                          <div class="row">
                              <div class="col-sm-4 col-xs-4">
                                  <span>Date:</span>
                              </div>
                              <div class="col-sm-8 col-xs-8" style="border-bottom:2px solid grey">
                                    <span id="pdf_evaluators_signature_date"></span>
                              </div>
                          </div>
                      </div>
                  </div>
              </div>
              <br>
              <div class="col-sm-12 col-xs-12">
                  <div class="row">
                      <div class="col-sm-2 col-xs-2">
                          <span style="line-height: 75px; position: relative; bottom: -27px;">Company rep.:</span>
                      </div>
                      <div class="col-sm-6 col-xs-6" style="border-bottom:2px solid grey; height:70px;">
                            <img id="pdf_company_rep_signature" width="100" height="70" alt="">
                            <span id="pdf_company_rep_signature_name"></span>                      
                      </div>
                      <div class="col-sm-4 col-xs-4">
                          <br>
                          <br>
                          <br>
                          
                          <div class="row">
                              <div class="col-sm-4 col-xs-4">
                                  <span>Date:</span>
                              </div>
                              <div class="col-sm-8 col-xs-8" style="border-bottom:2px solid grey">
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
    
</body>
  </html>`)
}