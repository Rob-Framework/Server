import twilio from "twilio";

export default class twillioHandler {
  static instance;
  client;

  constructor() {
    twillioHandler.instance = this;

    const accountSid = process.env.TWILIO_ACCOUNT_SID;
    const authToken = process.env.TWILIO_AUTH_TOKEN;
    this.client = twilio(accountSid, authToken);
  }

  sendSMS(body, to, from) {
    client.messages
      .create({
        body: body,
        to: to,
        from: from,
      })
      .then((message) => console.log(message.sid));
  }
}
