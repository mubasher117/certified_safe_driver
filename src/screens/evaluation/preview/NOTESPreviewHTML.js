import React from 'react';
import _ from 'lodash';
import moment from 'moment'

export default NOTES = (studentNotes, state, studentInfo, companyInfo, instructorInfo, infoicon) => {

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
    `
  })

  return (`<!DOCTYPE html>
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
   }

      #pdf_template_1, #pdf_template_2 {
        display: inline-block;
        height: 100%;
        background-color: white !important;
        padding-bottom: 64px;
      }
        #note_print{
          width:1000px;
          margin: auto;
          font-size: 12px;
          background-color: #fff !important;
        }

        #note_table_print{
          background-color: #fff !important;
          height: 100%;
        }

     .note-print-header>div{
        display: inline-block;
      }

    .oneLine{
        width: 45%;
    }

  </style>
</head>

<body>
<div id="note_print" class="printable">
<div class="note-print-header">
    <img src="https://lirp-cdn.multiscreensite.com/da9c67e6/dms3rep/multi/opt/csd+logo-306w.png" style="position:relative; top:10px;" width="150" alt=""> // NEW
     <br>
     <div style="width:100%; text-align: center;">
         <h3>Certified Safe Driver Inc.</h3>
         <h4>Notes</h4>
     </div>
     <br>
     <div class="oneLine">
         <span>Date:</span>
         <span class="value" id="note_date">${state?.date ? state?.date : "N/A"}</span>
     </div>
     <div class="oneLine" style="text-align: right;">
         <span>Student:</span>
         <span class="value" id="driverName">${studentInfo?.first_name + ' ' + studentInfo?.last_name}</span>
     </div>
     <br>
     <div class="oneLine">
         <span>Company:</span>
         <span class="value" id="company">${companyInfo?.name}</span>
     </div>
     <div class="oneLine" style="text-align: right;">
         <span>Instructor:</span>
         <span class="value" id="note_instructor">${instructorInfo?.first_name + ' ' + instructorInfo?.last_name}</span>
     </div>
     <br>
</div>
<br>
<br>
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
</div>
</body>
</html>`)
}