// Tool Function
let log = console.log.bind(console);
let e = function (selector, parent = document) {
    return parent.querySelector(selector)
};

// Ajax function
let ajax = function (method, path, data, responseCallBack) {
    let r = new XMLHttpRequest();
    r.setRequestHeader('Content-Type', 'application/json');
    r.onreadystatechange = function () {
        let json = JSON.parse(r.response);
        if (r.readyState === 4) {
            log('load ajax response type:', typeof(r.response));
            log('load ajax response:', r.response);
            log('load json type:', typeof(json));
        } else (
            responseCallBack(json)
        );
        data = JSON.stringify(data);
        r.send(data)
    }
};