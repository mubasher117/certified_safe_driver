/* eslint-disable prettier/prettier */
const path = require('path');

module.exports = {
  outputPath: path.resolve(__dirname, '../../../', 'build'),
  root: path.resolve(__dirname),
  template: './frontend/static/template.html',
  favicon: './frontend/static/favicon.ico',
  imagesFolder: 'static/images',
  fontsFolder: 'static/fonts',
  cssFolder: 'static/css',
  jsFolder: 'static/js',
};
