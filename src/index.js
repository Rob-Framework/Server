import PyConnect from "./pyconnect.js";
import tcpClient from "./tcpClient.js";
import tcpServer from "./tcpServer.js";
import readline from "readline";

let input = "";
readline.emitKeypressEvents(process.stdin);
process.stdin.setRawMode(true);
process.stdin.on("keypress", (str, key) => {
  if (key.name === "return") {
    const cmd = input;
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
      data = { command: "unknown" };
    }

    tcpServer.getInstance.socket.write(
      JSON.stringify({ packetId: 0, data: data })
    );
    input = "";
  } else if (key.name === "backspace") {
    input = input.slice(0, -1);
  }
  if (key.ctrl && key.name === "c") {
    process.exit();
  } else {
    input += str;
  }

  console.log(input);
});

(async function () {
  await PyConnect.invoke(async function () {
    await new tcpClient().init("127.0.0.1", 7781);
    await new tcpServer().init("127.0.0.1", 7782);
  });
})();

process.on("unhandledRejection", (error) => {
  console.error("Unhandled promise rejection:", error);
});
