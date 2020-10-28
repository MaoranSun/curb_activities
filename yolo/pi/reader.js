var mqtt = require('mqtt')
var client = mqtt.connect([{host: 'localhost'}])

client.on('connect', function() {
    client.subscribe('RATP', function(err) {})    
})

client.on('message', function(topic, message) {
    console.log("Just received this:", JSON.parse(message.toString()))    
})