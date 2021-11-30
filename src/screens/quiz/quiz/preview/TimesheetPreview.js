/* eslint-disable prettier/prettier */
import React from 'react';
import _ from 'lodash';
import moment from 'moment';

export default TimesheetPreview = (
  calculated_data,
  timesheet_data,
  state,
  studentInfo,
  companyInfo,
  instructorInfo,
  infoicon,
) => {
  console.log('************************ TIMESHEET PREVIEW *********************');
  console.log(timesheet_data?.completed_statisfactorily_on);
  return `<!DOCTYPE html>
  <html>
    <head>
      <title>iOS CSD BTW</title>
      <link
        rel="stylesheet"
        href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
        integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u"
        crossorigin="anonymous"
      />
      <style>
        #pdf_template {
          background: white;
          width: 1000px;
          font-size: 12px;
        }
  
        #pdf_template_1,
        #pdf_template_2 {
          display: inline-block;
          height: 100%;
          background-color: white !important;
          padding-bottom: 64px;
        }
  
        #note_print {

        display: flex;
        flex-direction: column;
        align-items: center;
          margin: auto;
          font-size: 12px;
          background-color: #fff !important;
        }
  
        #note_table_print {
          background-color: #fff !important;
          height: 100%;
        }
  
        .note-print-header > div {
          display: inline-block;
        }
  
        .oneLine {
          width: 45%;
        }
        .title {
          background-color: #f2f2f2;
        }
        .day {
          background-color: #2fc2df;
        }
        .table-container {
          width: 90%;
        }
      </style>
    </head>
  
    <body>
      <div id="note_print" class="printable">
        <div class="note-print-header">
          <img
            src="https://lirp-cdn.multiscreensite.com/da9c67e6/dms3rep/multi/opt/csd+logo-306w.png"
            style="position: relative; top: 10px;"
            width="150"
            alt=""
          />
          <br />
          <div style="width: 100%; text-align: center;">
            <h3>Certified Safe Driver Inc.</h3>
            <h4>RECORD OF DRIVER TRAINING</h4>
          </div>
          <br />
          
        <div>
        <div>
          <span>Student: </span>
          <span>${studentInfo?.first_name + ' ' + studentInfo?.last_name}</span>
        </div>

        <div>
          <span>Instructor: </span>
          <span>${
            instructorInfo?.first_name + ' ' + instructorInfo?.last_name
          }</span>
        </div>

        <div>
          <span>Company: </span>
          <span>${companyInfo?.name}</span>
        </div>

  
      </div>

        </div>
        <br />
        <br />
  
        <div class="row table-container">
          <div class="col-sm-12">
            <table
              id="note_table_print"
              class="table table-bordered dataTable no-footer"
              role="grid"
            >
            


            <thead>
      <tr role="row">
        <th
          class="sorting_disabled day"
          rowspan="1"
          colspan="2"
          style="width: 0px;"
        >
        Total Training
        </th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Planned</td>
        <td>${calculated_data.totalPlanned}</td>
      </tr>
      <tr>
        <td>Actual</td>
        <td>${calculated_data.totalActual}</td>
      </tr>
    </tbody>



    <thead>
      <tr role="row">
        <th
          class="sorting_disabled day"
          rowspan="1"
          colspan="2"
          style="width: 0px;"
        >
        Classroom
        </th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Planned</td>
        <td>${calculated_data.classroomPlanned}</td>
      </tr>
      <tr>
        <td>Actual</td>
        <td>${calculated_data.classroomPlanned}</td>
      </tr>
    </tbody>




<thead>
      <tr role="row">
        <th
          class="sorting_disabled day"
          rowspan="1"
          colspan="2"
          style="width: 0px;"
        >
        Yard Skills
        </th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Planned</td>
        <td>${calculated_data.yardPlanned }</td>
      </tr>
      <tr>
        <td>Actual</td>
        <td>${calculated_data.yardActual}</td>
      </tr>
    </tbody>


<thead>
      <tr role="row">
        <th
          class="sorting_disabled day"
          rowspan="1"
          colspan="2"
          style="width: 0px;"
        >
        Behind the Wheel
        </th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Planned</td>
        <td>${calculated_data.btwPlanned || ''}</td>
      </tr>
      <tr>
        <td>Actual</td>
        <td>${calculated_data.btwActual || ''}</td>
      </tr>
    </tbody>


    <thead>
      <tr role="row">
        <th
          class="sorting_disabled day"
          rowspan="1"
          colspan="2"
          style="width: 0px;"
        >
        Remarks
        </th>
      </tr>
    </thead>
    <tbody>
      <tr colspan="2">
        <td>${timesheet_data?.remarks || ''}</td>
      </tr>
    </tbody>

    <thead>
      <tr role="row">
        <th
          class="sorting_disabled day"
          rowspan="1"
          colspan="2"
          style="width: 0px;"
        >
        Driver Trainer completed Satisfactorily on
        </th>
      </tr>
    </thead>
    <tbody>
      <tr colspan="2">
        <td>${timesheet_data?.completed_statisfactorily_on || ''}</td>
      </tr>
    </tbody>

    <thead>
    <tr role="row">
      <th
        class="sorting_disabled day"
        rowspan="1"
        colspan="2"
        style="width: 0px;"
      >
      Driver Trainer Signature
      </th>
    </tr>
  </thead>
  <tbody>
    <tr colspan="2">
      <td><img src="${state.signature}" alt="Instructor's Signature" 
      style="width:430px; height:300px;"></td>
    </tr>
  </tbody>



            </table>
          </div>
        </div>
      </div>
    </body>
  </html>
  `;
};
