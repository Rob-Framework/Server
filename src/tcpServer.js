import * as net from "net";
import tcpClient from "./tcpClient.js";

export default class tcpServer {
  static getInstance;
  server;
  socket;

  async init(ip, port) {
    tcpServer.getInstance = this;

    //create a tcp server listening to ip and port
    this.server = net.createServer(function (socket) {
      tcpServer.getInstance.socket = socket;
      console.log("connected");
      socket.on("data", function (data) {
        const json = data.toString().replace(/'/g, '"');
        const resp = JSON.parse(json);
        const packetId = resp["packetId"];
        const _data = resp["data"];

        if (packetId == 1) {
          //console.log("got sensor data: ", _data);

          if (_data["sensor"] == "location") {
            tcpClient.getInstance.sendMessage(2, _data["data"]);
          }
        }
      });
    });
    this.server.listen(port, ip);
  }
}
