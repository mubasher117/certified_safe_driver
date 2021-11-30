export default BTWTest = () =>{
    return(
        `<!DOCTYPE html>
        <html lang="en">
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
                width: 400px;
                margin: 5px;
                overflow: hidden;
                display: inline-block;
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
                <div id="container1" style="min-height: 400px; min-width:300px; margin:0 auto;"></div>
            </div>
            <script>
                Highcharts.chart('container1', {
                    chart: {
                        type: 'column'
                    },
                    title: {
                        text: 'Element effective chart'
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
                            text: 'Population (millions)'
                        }
                    },
                    legend: {
                        enabled: false
                    },
                    tooltip: {
                        pointFormat: 'Population in 2017: <b>{point.y:.1f} millions</b>'
                    },
                    series: [{
                        name: 'Population',
                        data: [
                            ['Shanghai', 24.2],
                            ['Beijing', 20.8],
                            ['Karachi', 14.9],
                            ['Shenzhen', 13.7],
                            ['Guangzhou', 13.1],
                            ['Istanbul', 12.7],
                            ['Mumbai', 12.4],
                            ['Moscow', 12.2],
                            ['São Paulo', 12.0],
                            ['Delhi', 11.7],
                            ['Kinshasa', 11.5],
                            ['Tianjin', 11.2],
                            ['Lahore', 11.1],
                            ['Jakarta', 10.6],
                            ['Dongguan', 10.6],
                            ['Lagos', 10.6],
                            ['Bengaluru', 10.3],
                            ['Seoul', 9.8],
                            ['Foshan', 9.3],
                            ['Tokyo', 9.3]
                        ],
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
        </html>`
        
    )
}
    