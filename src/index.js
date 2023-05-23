import PyConnect from "./pyconnect.js";
import tcpClient from "./tcpClient.js";
import tcpServer from "./tcpServer.js";
import dotenv from "dotenv";

dotenv.config()
process.stdin.resume();
process.stdin.setEncoding("utf8");

process.stdin.on("data", function (text) {
  const cmd = text.trim();
  console.log("trying to send:", cmd);
  let data = {};
  if (
    cmd == "forward" ||
    cmd == "backward" ||
    cmd == "left" ||
    cmd == "right" ||
    cmd == "stop" ||
    cmd == "break" ||
    cmd == "slow_stop"
  ) {
    data = { command: cmd };
  } else if (cmd.startsWith("move_hand")) {
    split = cmd.split(" ");
    cmdObj = {
      command: "move_hand",
      movement: split[1],
      servo: split[2],
    };
    data = cmdObj;
  } else {
    console.log("got unknow command: ", cmd);
    data = { command: "unknown" };
  }

  const cmdData = { packetId: 0, data: data };
  tcpServer.getInstance.socket.write(JSON.stringify(cmdData));
});

(async function () {
  await PyConnect.invoke(async function () {
    await new tcpClient().init("127.0.0.1", 7781);
    await new tcpServer().init("0.0.0.0", process.env.NODE_SERVER_PORT);
  });
})();

process.on("unhandledRejection", (error) => {
  console.error("Unhandled promise rejection:", error);
});
