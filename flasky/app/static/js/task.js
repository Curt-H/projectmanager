let apiTaskAll = function (callback) {
    let path = '/api/todo/all';
    ajax('GET', path, '', callback)
};

let bindEvenFinish = function () {
    let taskList = e('#task-list');

    // Event trusteeship
    taskList.addEventListener('click', function (t) {
        let self = t.target
        log('The object clicked:', self)

        // Get task panel object
        let taskPanel = self.closest('.panel')
        log('The closest object:', taskPanel)
        let taskId = taskPanel.dataset['Id']
        log('Task ID:', taskId)
    })

};

let __main = function () {
    bindEvenFinish();
};

__main();