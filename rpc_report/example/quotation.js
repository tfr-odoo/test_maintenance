var rpc = require('node-json-rpc');
const fs = require('fs');
 
var options = {
  // int port of rpc server, default 5080 for http or 5433 for https
  port: 8069,
  // string domain name or ip of rpc server, default '127.0.0.1'
  host: '127.0.0.1',
  // string with default path, default '/'
  path: '/jsonrpc',
  // boolean false to turn rpc checks off, default true
  strict: true
};
 
// Create a server object with options
var client = new rpc.Client(options);

var DB = 'report'
var UID = 2
var PASSWORD  = 'admin'
var regex_test = /'/g
var regex_nope = 4 /3+''+2/ 4
var regex_test = /\*/g
/*   
  Comment
/regx/*/
client.call(
  {"jsonrpc": "2.0", "method": "call", "params": {
      "service": "object", "method": "execute", 
      "args": [DB, UID, PASSWORD, 
              'ir.model.data',  //model 
              'get_object_reference', //method
              'sale', 'action_report_saleorder' //method parameters
              ]
      
    }, 
    "id": 0},
  function (err, res) {
    // Did it all work ?
    if (err) { console.log(err); }
    else { console.log(res); }
  }
);

client.call(
  {"jsonrpc": "2.0", "method": "call", "params": {
      "service": "object", "method": "execute", 
      "args": [DB, UID, PASSWORD, 'ir.model.data', 'get_object_reference', 'sale', 'sale_order_7']
      
    }, 
    "id": 0},
  function (err, res) {
    // Did it all work ?
    if (err) { console.log(err); }
    else { console.log(res); }
  }
);

client.call(
  {"jsonrpc": "2.0", "method": "call", "params": {
      "service": "object", "method": "execute", 
      "args": [DB, UID, PASSWORD, 
         'ir.actions.report', 
         'render_rpc', 
         247, //ID found with the first call 
         7,  //ID found with the second call
         false]
      
    }, 
    "id": 0},
  function (err, res) {
    // Did it all work ?
    if (err) { console.log(err); }
    else { 
        console.log(res["result"]); 
        let writeStream = fs.createWriteStream('report.pdf');

        // write some data with a base64 encoding
        writeStream.write(res["result"][0], 'base64');
    }
  }
);


 
