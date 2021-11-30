/* eslint-disable import/no-extraneous-dependencies */
/* eslint-disable prettier/prettier */
const path = require('path');
const os = require('os');
const CSSNano = require('cssnano');
const PostCSSPresetEnv = require('postcss-preset-env');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const TerserWebpackPlugin = require('terser-webpack-plugin');
// const HardSourceWebpackPlugin = require('hard-source-webpack-plugin');
const DartSass = require('sass');
const WebpackBar = require('webpackbar');
const webpack = require('webpack');
const ThreadLoader = require('thread-loader');
const Dotenv = require('dotenv-webpack');
const commonPaths = require('./common-paths');

ThreadLoader.warmup(
  {
    workers: os.cpus().length - 1,
  },
  ['babel-loader', 'sass-loader'],
);

module.exports = {
  mode: 'production',
  target: 'web',
  stats: 'errors-only',
  entry: path.resolve('frontend', 'index.jsx'),
  output: {
    path: commonPaths.outputPath,
    publicPath: '/',
    filename: 'static/js/[name].[chunkhash].js',
  },
  resolve: {
    extensions: ['.tsx', '.ts', '.js', '.jsx', '.json', '.web.js', '.mjs'],
  },
  optimization: {
    minimizer: [
      new TerserWebpackPlugin({
        cache: true,
        parallel: true,
        sourceMap: true,
        terserOptions: {
          ecma: 5,
        },
      }),
    ],
    splitChunks: {
      cacheGroups: {
        runtimeChunk: 'single',
        vendor: {
          test: /node_modules/,
          chunks: 'initial',
          name: 'vendor',
          priority: 10,
          enforce: true,
        },
      },
    },
  },
  devtool: 'source-map',
  plugins: [
    // new BundleTracker({
    // 	path: './',
    // 	filename: 'webpack-stats.json'
    // }),
    new Dotenv({
      systemvars: true,
    }),

    new WebpackBar(),
    new CleanWebpackPlugin(),
    new HtmlWebpackPlugin({
      template: commonPaths.template,
    }),
    new MiniCssExtractPlugin({
      filename: path.join('static/css', '[name].[chunkhash].css'),
    }),
    new webpack.EnvironmentPlugin(['NODE_ENV', 'DEBUG', 'API_URL']),
    new webpack.HashedModuleIdsPlugin(),
    // new HardSourceWebpackPlugin({
    // 	info: {
    // 		mode: 'none',
    // 		level: 'debug'
    // 	}
    // })
  ],
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
            },
          },
          {
            loader: 'babel-loader',
            options: {
              cacheDirectory: true,
              babelrc: false,
              presets: [
                '@babel/preset-react',
                [
                  '@babel/preset-env',
                  {
                    targets: 'defaults',
                    loose: true,
                    useBuiltIns: 'entry',
                    corejs: {
                      version: 3,
                      proposals: true,
                    },
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
        use: [
          MiniCssExtractPlugin.loader,
          'css-loader',
          {
            loader: 'postcss-loader',
            options: {
              ident: 'postcss',
              plugins: [CSSNano()],
            },
          },
        ],
      },
      {
        test: /\.scss$/i,
        include: path.resolve('frontend/sass'),
        use: [
          {
            loader: MiniCssExtractPlugin.loader,
            options: {
              publicPath: path.join('..', '..', path.sep),
            },
          },
          'css-loader',
          {
            loader: 'postcss-loader',
            options: {
              ident: 'postcss',
              plugins: [
                PostCSSPresetEnv({
                  browsers: 'defaults',
                }),
                CSSNano(),
              ],
              sourceMap: true,
            },
          },
          {
            loader: 'sass-loader',
            options: {
              implementation: DartSass,
              sourceMap: true,
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
