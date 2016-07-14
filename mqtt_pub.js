var mqtt = require("mqtt");

var client = mqtt.connect('matt://10.21.20.26');

client.on('connect', function()
{
        setInterval(function()
        {
                console.log("qwe");
                client.publish('arduino/1', "test");
        }, 1000);
});
