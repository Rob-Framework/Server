import unirest from "unirest";

export default class google_scrap {
  static instance;

  constructor() {
    google_scrap.instance = this;
  }

  getData(search) {
    const url = "https://www.google.com/search?q=" + search + "&gl=us&hl=en";
    let header = {
      "User-Agent":
        "Mozilla/5.0 (Windows NT 6.3; Win64; x64)  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 Viewer/96.9.4688.89",
    };
    return unirest
      .get(url)
      .headers(header)
      .then((response) => {
        console.log(response.body);
      });
  }
}
