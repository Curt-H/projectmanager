let webClock = function () {
    let clock = new Date()
    let h = clock.getHours()
    let m = clock.getMinutes()
    let s = clock.getSeconds()

    // check if h, m, s less than 10
    h = checktime(h)
    m = checktime(m)
    s = checktime(s)

    time = h + ':' + m + ':' + s

    let clockItem = e('#clock')
    clockItem.innerText = time

    setTimeout('webClock()', 500)
}

let checktime = function (num) {
    if (num < 10) {
        return '0' + num
    } else {
        return num
    }
}

webClock()

