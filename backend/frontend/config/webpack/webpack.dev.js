/* eslint-disable import/no-extraneous-dependencies */
/* eslint-disable prettier/prettier */
const path = require('path');
const os = require('os');
const DartSass = require('sass');
const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const ThreadLoader = require('thread-loader');
const Dotenv = require('dotenv-webpack');
const commonPaths = require('./common-paths');

ThreadLoader.warmup(
  {
    workers: os.cpus().length - 1,
    poolTimeout: Infinity,
  },
  ['babel-loader'],
);

module.exports = {
  mode: 'development',
  entry: ['react-hot-loader/patch', path.resolve('frontend/index.jsx')],
  target: 'web',
  output: {
    filename: '[name].js',
    publicPath: '/',
    path: commonPaths.outputPath,
    chunkFilename: '[name].js',
  },
  plugins: [
    // new BundleTracker({
    // 	path: './',
    // 	filename: 'webpack-stats.json'
    // }),
    new Dotenv({
      systemvars: true,
    }),
    new HtmlWebpackPlugin({
      template: commonPaths.template,
    }),
    new webpack.HotModuleReplacementPlugin(),
    new webpack.EnvironmentPlugin(['NODE_ENV', 'DEBUG', 'API_URL']),
  ],
  devServer: {
    contentBase: commonPaths.outputPath,
    watchContentBase: true,
    port: 3000,
    historyApiFallback: true,
    hot: true,
    open: true,
    inline: true,
    stats: 'errors-only',
  },
  resolve: {
    extensions: ['.tsx', '.ts', '.js', '.jsx', '.json', '.web.js', '.mjs'],
  },
  module: {
    rules: [
      {
        // test: /\.jsx?$/i,
        test: /\.(js|jsx)$/i,
        include: path.resolve('frontend'),
        use: [
          {
            loader: 'thread-loader',
            options: {
              workers: os.cpus().length - 1,
              poolTimeout: Infinity,
            },
          },
          {
            loader: 'babel-loader',
            options: {
              cacheDirectory: true,
              babelrc: false,
              presets: [
                '@babel/preset-env',
                [
                  '@babel/preset-react',
                  {
                    development: true,
                  },
                ],
              ],
              plugins: [
                '@babel/plugin-transform-react-constant-elements',
                '@babel/plugin-transform-runtime',
                '@babel/plugin-transform-react-inline-elements',
                '@babel/plugin-proposal-class-properties',
                'react-hot-loader/babel',
              ],
            },
          },
        ],
      },
      {
        test: /\.css$/i,
        // include: path.resolve('node_modules', 'normalize'),
        use: ['style-loader', 'css-loader'],
      },
      {
        test: /\.(scss|sass)$/i,
        include: path.resolve('frontend/sass'),
        use: [
          'style-loader',
          'css-loader',
          {
            loader: 'sass-loader',
            options: {
              implementation: DartSass,
            },
          },
        ],
      },
      {
        test: /\.mjs$/,
        include: /node_modules/,
        type: 'javascript/auto',
      },
      {
        test: /.(png|jpg|jpeg|gif|svg|woff|woff2|eot|ttf)(\?v=\d+\.\d+\.\d+)?$/,
        use: [
          {
            loader: 'url-loader',
            options: {
              limit: 100000,
              name: '[name].[ext]',
              outputPath: commonPaths.imagesFolder,
            },
          },
        ],
      },
    ],
  },
};
