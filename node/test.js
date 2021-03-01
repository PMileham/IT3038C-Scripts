var path = require("path");

var hello = "Helloe from Node JS Variable!"
console.log(`printing variable ello: ${hello}`)

console.log("Directory name: " + __dirname )
console.log("directory and file name " + __filename)


console.log("Using the PATH module:")
console.log(`Hello from file ${path.basename(__filename)}`);

console.log(`Process args: ${process.argv}`)