Highcharts.chart('container_name', {
                 chart: {
                 type: 'column'
                 },
                 title: {
                 text: 'chart_title'
                 },
                 subtitle: {
                 text: ''
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
                          data: [
                                 chart_Data
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
