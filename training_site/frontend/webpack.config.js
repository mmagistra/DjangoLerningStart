const path = require('path');

module.exports = {
  entry: {
        index: './src/index.js',
        fetch_courses: './src/fetch_courses.js',
        axios_students: './src/axios_students.js',
    },
  output: {
    path: path.resolve(__dirname, "../static/frontend/"),
    filename: '[name].js',
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      }
    ]
  }
};