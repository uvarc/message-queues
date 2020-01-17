# moquitto

MQTT protocol

Download the `mosquitto_pub` and `mosquitto_sub` tools from https://mosquitto.org/.

Using the https://test.mosquitto.org/ site:

## Publish / Send

    mosquitto_pub -h test.mosquitto.org -t "channel-name" -m "message goes here"

## Subscribe / Get

    mosquitto_sub -h test.mosquitto.org -t "channel-name" -v
