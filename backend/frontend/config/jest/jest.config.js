const path = require('path');

console.log(path.join(__dirname, '../../src'));

module.export = {
  roots: ['<rootDir>/src'],
  transform: {
    '\\.(js|jsx)?$': 'babel-jest',
  },
  rootDir: path.join(__dirname, '../..'),
  testMatch: [path.join(__dirname, '../../**/?(*.)+(spec|test).[tj]s?(x)')],
  moduleFileExtensions: ['js', 'jsx', 'json', 'node'],
  moduleNameMapper: {
    '^.*\\.scss$': './src/shared/test/SCSSStub.js',
  },
  testPathIgnorePatterns: ['/node_modules/', '/public/'],
};
