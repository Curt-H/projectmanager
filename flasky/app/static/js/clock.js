let webClock = function () {
    let clock = new Date();
    let h = clock.getHours();
    let m = clock.getMinutes();
    let s = clock.getSeconds();
    let year = clock.getFullYear();
    let month = clock.getMonth();
    let day = clock.getDate();

    // check if h, m, s less than 10
    h = checktime(h);
    m = checktime(m);
    s = checktime(s);
    month = checktime(month);
    day = checktime(day);

    let date = year + '-' + month + '-' + day;
    let time = h + ':' + m + ':' + s;

    let dateItem = e('#date');
    let clockItem = e('#clock');
    clockItem.innerText = time;
    dateItem.innerText = date;

    setTimeout('webClock()', 800)
};

let checktime = function (num) {
    if (num < 10) {
        return '0' + num
    } else {
        return num
    }
};

webClock();

