import React from 'react';
import Chart from 'react-google-charts';

const data = [
  ['Task', 'Hours per Day'],
  ['Permium', 11],
  ['Starter', 2],
  ['Basic', 2],
  ['Business', 2],
  ['Silver', 7], // CSS-style declaration
];
const options = {
  pieHole: 0.7,
  is3D: true,
};
const PieChart = () => <Chart chartType="PieChart" width="100%" height="400px" data={data} options={options} />;
const BarChart = () => (
  <Chart
    width={'500px'}
    height={'300px'}
    chartType="AreaChart"
    loader={<div>Loading Chart</div>}
    data={[
      ['Year', 'Sales', 'Expenses'],
      ['2013', 1000, 400],
      ['2014', 1170, 460],
      ['2015', 660, 1120],
      ['2016', 1030, 540],
    ]}
    options={{
      hAxis: { title: 'Year', titleTextStyle: { color: '#333' } },
      vAxis: { minValue: 0 },
      // For the legend to fit, we make the chart area smaller
      chartArea: { width: '50%', height: '70%' },
      // lineWidth: 25
    }}
    // For tests
    rootProps={{ 'data-testid': '1' }}
  />
);

const MapsChart = () => (
  <Chart
    width={'500px'}
    height={'300px'}
    chartType="GeoChart"
    data={[
      ['Country', 'Popularity'],
      ['Germany', 200],
      ['United States', 300],
      ['Brazil', 400],
      ['Canada', 500],
      ['France', 600],
      ['RU', 700],
    ]}
    // Note: you will need to get a mapsApiKey for your project.
    // See: https://developers.google.com/chart/interactive/docs/basic_load_libs#load-settings
  />
);

export { PieChart, BarChart, MapsChart };
