/* eslint-disable prettier/prettier */
import React from 'react';
import _ from 'lodash';
import moment from 'moment';

export default DestructiveQuizPreview = (
  state,
  studentInfo,
  companyInfo,
  instructorInfo,
) => {
  const wrongChoice = (statement) => `<p style="color:red">${statement}.</p>`;
  const rightChoice = (statement) => `<p style="color:green">${statement}.</p>`;
  const choice = (statement) => `<p">${statement}.</p>`;
  let previewData = '';
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
              ${index + 1}) ${item.title}
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

        <div>
          <span>Date: </span>
          <span>${state?.date ? state?.date : 'N/A'}</span>
        </div>
      </div>

        </div>
        <br />
        <br />
  
        <div class="row table-container">
         

            ${previewData}
          

        </div>

        
      </div>
    </body>
  </html>
  `;
};
