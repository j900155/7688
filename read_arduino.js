var SerialPort = require("serialport");
var ser = new SerialPort.SerialPort("/dev/ttyS0", {baudRate : 57600, parser : Se
var mqtt = require("mqtt");
var client = mqtt.connect('mqtt://10.21.20.26')

ser.on('open', function()
{
   console.log("serial open");

   ser.on('data', function(datas)
   {
                console.log(datas.toString());
                s = datas.toString();
                client.publish('arduino/1', s);

   });
});
~
