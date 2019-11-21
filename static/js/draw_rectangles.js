function displayRect(x1, y1, x2, y2) {

    let width = x2 - x1;
    let height = y2 - y1;

    var c = document.getElementById("boardcanvas");
    var ctx = c.getContext("2d");
    console.log("sklsnvnxdfnv")

    console.log(!ctx.getImageData(x1, y1, width, height).data.some(channel => channel !== 0))

    if (!ctx.getImageData(x1, y1, width, height).data.some(channel => channel !== 0)) {
        ctx.beginPath();
        ctx.rect(x1, y1, width, height);
        ctx.fillStyle = "rgba(255, 40, 40, 0.5)";
        ctx.fill();
    } else {
        ctx.clearRect(x1, y1, width, height);
    }
}