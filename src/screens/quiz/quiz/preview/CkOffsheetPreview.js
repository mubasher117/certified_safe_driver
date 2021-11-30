/* eslint-disable prettier/prettier */
import React from 'react';
import _ from 'lodash';
import moment from 'moment';

export default CkOffsheetPreview = (
  dfq_requirements,
  trainee_book_data,
  state,
  studentInfo,
  companyInfo,
  instructorInfo,
  infoicon,
) => {
  var dfqRequirementsDataHTML = '';
  dfq_requirements.map((training, index) => {
    dfqRequirementsDataHTML += `<thead>
      <tr role="row">
        <th
          class="sorting_disabled day"
          rowspan="1"
          colspan="2"
          style="width: 0px;"
        >
          ${training.item.title}
        </th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Department</td>
        <td>${dfq_requirements[
          index
        ].item.department_display_name?.toString() || ''}</td>
      </tr>
      <tr>
        <td>Initials</td>
        <td>${dfq_requirements[index].initials?.toString() || ''}</td>
      </tr>
      <tr>
        <td>Date</td>
        <td>${dfq_requirements[index].date?.toString() || ''}</td>
      </tr>
    </tbody>`;
  });

  var traineeBookDataHTML = '';
  trainee_book_data.map((training, index) => {
    traineeBookDataHTML += `
    
    

    <tbody>
  <tr>
    <td><h3>Trainee Book</h3></td>
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
    ${training.item.title}
    </th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Department</td>
    <td>${trainee_book_data[
      index
    ].item?.department_display_name?.toString() || ''}</td>
  </tr>
  <tr>
    <td>Initials</td>
    <td>${trainee_book_data[index].initials?.toString() || ''}</td>
  </tr>
  <tr>
    <td>Date</td>
    <td>${trainee_book_data[index].date?.toString() || ''}</td>
  </tr>
</tbody>`;
  });

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
            <h3>DQF Requirements</h3>
              ${dfqRequirementsDataHTML}
              ${traineeBookDataHTML}
            </table>
          </div>
        </div>
      </div>
    </body>
  </html>
  `;
};
