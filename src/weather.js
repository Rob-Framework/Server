import weather from "openweather-apis";

const forecast = function (latitude, longitude, callback) {
  const apiKey = "29fad6057a98df8636df25e757835442"; // process.env.OPEN_WEATHER_MAP_API_KEY;
  console.log(apiKey);
  weather.setCoordinate(latitude, longitude);
  weather.setAPPID(apiKey);
  weather.setUnits("metric");
  console.log("api key set");
  weather.setLang("en");

  weather.getAllWeather(function (err, JSONObj) {
    if (err) {
      console.log(err);
    } else {
      callback(JSONObj);
    }
  });
};
