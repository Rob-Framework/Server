import spawn from "child_process";
import path from "path";

const isWindows = process.platform === "win32";

export default class PyConnect {
  static connected;
  static grpcProcess;
  static grpc;
  static server() {
    return new Promise((resolve, reject) => {
      if (!PyConnect.connected) {
        console.log(
          "PythonConnector – making a new connection to the python layer"
        );
        PyConnect.grpcProcess = spawn.spawn(isWindows ? "python" : "python3", [
          "-u",
          path.join("localServer.py"),
        ]);
        PyConnect.grpcProcess.stdout.on("data", function (data) {
          console.info("python:", data.toString());
          PyConnect.connected = true;
          resolve(PyConnect.grpc);
        });
        PyConnect.grpcProcess.stderr.on("data", function (data) {
          console.error("python:", data.toString());
        });
      } else {
        resolve(PyConnect.grpc);
      }
    });
  }

  static async invoke(method) {
    try {
      return await PyConnect.server().then(async () => {
        method();
      });
    } catch (e) {
      return Promise.reject(e);
    }
  }
}
