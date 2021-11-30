/* eslint-disable prettier/prettier */
import React from 'react';
import _ from 'lodash';
import moment from 'moment';

export default INFOPreview = (
  state,
  studentInfo,
  companyInfo,
  instructorInfo,
  dfq_requirements,
  trainee_book_data,
  truckDrvingSchool,
  timesheet_data,
  calculated_data,
  
) => {
  var dfqRequirementsDataHTML = '';
  dfq_requirements?.map((training, index) => {
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
        <td>${
          dfq_requirements[index].item.department_display_name?.toString() || ''
        }</td>
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
  trainee_book_data?.map((training, index) => {
    traineeBookDataHTML += `
    
    


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
    <td>${
      trainee_book_data[index].item?.department_display_name?.toString() || ''
    }</td>
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

  let tableDataHTML = '';
  let sectionHtml = '';
  console.log(truckDrvingSchool);
  truckDrvingSchool?.days?.map((elem, index) => {
    const drivingSchool = truckDrvingSchool.day_list[elem];
    const dayNumber = elem;
    drivingSchool?.map((entity, mappingIndex) => {
      const title = entity.title;
      const location = entity.location;
      const planned = entity.planned;
      const actual = entity.actual;
      const initials = entity.initials;
      sectionHtml += `
      <tr>
        <td rowspan="1" colspan="2" class="title">${title || ''}</td>
      </tr>
      <tr>
        <td>Location</td>
        <td>${location || ''}</td>
      </tr>
      <tr>
        <td>Planned</td>
        <td>${planned || ''}</td>
      </tr>
      <tr>
        <td>Actual</td>
        <td>${actual || ''}</td>
      </tr>
      <tr>
        <td>Initials</td>
        <td>${initials || ''}</td>
      </tr>`;
    });
    tableDataHTML += `
    <thead>
      <tr role="row">
        <th
          class="sorting_disabled day"
          rowspan="1"
          colspan="2"
          style="width: 0px;"
        >
        <p style="font-size: 20px; margin-bottom: 29px;">Day ${dayNumber || ''}</p>
        <table  class="table-total-days" >
        <tr>
          <th></th>
          <th>Planned</th>
          <th>Actual</th>
        </tr>
        <tr>
          <td>Total</td>
          <td>${truckDrvingSchool?.counters[index]?.total_planned}</td>
          <td>${truckDrvingSchool?.counters[index]?.total_actual}</td>
        </tr>
        <tr>
          <td>Classroom</td>
          <td>${
            truckDrvingSchool?.counters[index]
              .classroom_total_planned
          }</td>
          <td>${
            truckDrvingSchool?.counters[index]
              .classroom_total_actual
          }</td>
        </tr>
        <tr>
          <td>BTW</td>
          <td>${
            truckDrvingSchool?.counters[index]
              .btw_total_planned
          }</td>
          <td>${
            truckDrvingSchool?.counters[index]
              .btw_total_actual
          }</td>
        </tr>
        <tr>
          <td>Yard</td>
          <td>${
            truckDrvingSchool?.counters[index]
              .yard_total_planned
          }</td>
          <td>${
            truckDrvingSchool?.counters[index]
              .yard_total_actual
          }</td>
        </tr>
        <tr>
          <td>On Road</td>
          <td>${
            truckDrvingSchool?.counters[index]
              .on_road_total_planned
          }</td>
          <td>${
            truckDrvingSchool?.counters[index]
              .on_road_total_actual
          }</td>
        </tr>
        </table>
        </th>
      </tr>
    </thead>
    
    <tbody>
    
    ${sectionHtml}
    <tr>
    <td rowspan="1" colspan="2" class="title"><p style="font-size:30px">Comments</p></td>
</tr>
<tr>
    <td rowspan="1" colspan="2"><div style="margin-bottom: 50px;">
    ${state?.comments[dayNumber] || ''}
    </div></td>
</tr>
</tbody`

    
  });

  const wrongChoice = (statement) => `<p style="color:red">${statement}.</p>`;
  const rightChoice = (statement) => `<p style="color:green">${statement}.</p>`;
  const choice = (statement) => `<p">${statement}.</p>`;
  let previewData = '<h2>Defesive Quiz</h2>';
  state?._defenseQuizes?.map((item, index) => {
    let choices = '';
    item?.choices?.map((testChoice, index) => {
      if (testChoice?.isChecked === false) {
        choices = choices + choice(testChoice?.title);
      } else if (testChoice?.isChecked === true) {
        let correctIndex = item?.correct_choices?.findIndex(
          (correctChoice) => correctChoice.title === testChoice?.title,
        );
        if (correctIndex === -1) {
          choices = choices + wrongChoice(testChoice?.title);
        } else {
          choices = choices + rightChoice(testChoice?.title);
        }
      }
    });
    previewData =
      previewData +
      `
    <div class="col-sm-12">
            <div style="background-color: silver; margin: 10px 0px">
              ${index}) ${item.title}
            </div>
            
            ${choices}
          </div>`;
  });





  let distractedPreviewData = '<h2>Distracted Quiz</h2>';
  state?._distractedQuizes?.map((item, index) => {
    let choices = '';
    item?.choices?.map((testChoice, index) => {
      if (testChoice?.isChecked === false) {
        choices = choices + choice(testChoice?.title);
      } else if (testChoice?.isChecked === true) {
        let correctIndex = item?.correct_choices?.findIndex(
          (correctChoice) => correctChoice.title === testChoice?.title,
        );
        if (correctIndex === -1) {
          choices = choices + wrongChoice(testChoice?.title);
        } else {
          choices = choices + rightChoice(testChoice?.title);
        }
      }
    });
    distractedPreviewData =
    distractedPreviewData +
      `
    <div class="col-sm-12">
            <div style="background-color: silver; margin: 10px 0px">
              ${index}) ${item.title}
            </div>
            
            ${choices}
          </div>`;
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
      .table-total-days {
        font-family: arial, sans-serif;
        border-collapse: collapse;
        width: 100%;
      }
      
      .table-total-days td, th {
        border: 1px solid #dddddd;
        text-align: left;
        padding: 8px;
      }
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
            
            </table>

            <table
              id="note_table_print"
              class="table table-bordered dataTable no-footer"
              role="grid"
            >
            
            <h3>Trainee Book</h3>
              ${traineeBookDataHTML}
            </table>
          </div>
        </div>
        <div class="row table-container">
        <h3>Truck Driving School</h3>
        <div class="col-sm-12">
          <table
            id="note_table_print"
            class="table table-bordered dataTable no-footer"
            role="grid"
          >
            ${tableDataHTML}
          </table>
        </div>
      </div>

      <h3>Time Sheet</h3>
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
                  <td>${calculated_data?.totalPlanned}</td>
               </tr>
               <tr>
                  <td>Actual</td>
                  <td>${calculated_data?.totalActual}</td>
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
                  <td>${calculated_data?.classroomPlanned}</td>
               </tr>
               <tr>
                  <td>Actual</td>
                  <td>${calculated_data?.classroomPlanned}</td>
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
                  <td>${calculated_data?.yardPlanned}</td>
               </tr>
               <tr>
                  <td>Actual</td>
                  <td>${calculated_data?.yardActual}</td>
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
                  <td>${calculated_data?.btwPlanned || ''}</td>
               </tr>
               <tr>
                  <td>Actual</td>
                  <td>${calculated_data?.btwActual || ''}</td>
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
                  <td><img src="${
                    state.signature
                  }" alt="Instructor's Signature" 
                     style="width:430px; height:300px;"></td>
               </tr>
            </tbody>
         </table>
         <div class="row table-container">
         

            ${previewData}
          

        </div>


        <div class="row table-container">
         

            ${distractedPreviewData}
          

        </div>

      </div>
   </div>
      </div>
    </body>
  </html>
  `;
};
