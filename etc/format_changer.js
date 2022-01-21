let fs = require("fs");

const WebtoonsArray = [];

const newArray = WebtoonsArray.map((obj) => {
    let genre = obj.genre?.split(",");
    let author = obj.author?.split(",");
    let days = obj.days.split(",");
    let platform = obj.platform.split(",");
    return { ...obj, genre, author, days, platform };
});

const newjson = JSON.stringify(newArray);

let stream = fs.createWriteStream("WebtoonsArrayinJson.txt");
stream.once("open", function () {
    stream.write(newjson);
    stream.end();
});
