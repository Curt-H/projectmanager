let apiTaskFinish = function (data, callback) {
    let path = '/api/task/finish';
    ajax('POST', path, data, callback)
};

let bindEventFinish = function () {
    let taskList = e('#task-list');

    // Event trusteeship
    taskList.addEventListener('click', function (t) {
        let self = t.target;

        // Get task panel object
        if (self.classList.contains('finish')) {
            log('The object clicked:', self);

            let taskPanel = self.closest('.panel');
            let taskIdTitle = e('.panel-title', taskPanel);
            let taskTitle = e('.panel-content', taskPanel);
            log('The closest object:', taskPanel);
            log('The closest object:', taskTitle);

            let taskId = taskPanel.dataset['id'];
            log('Task ID:', taskId);

            const data = {
                id: taskId,
            };

            let responseMsg = confirm('Really want to mark it as finished?\nYou can not reedit if you click yes');
            if (responseMsg) {
                log('Sending data');
                apiTaskFinish(data, function (response) {
                    log(response);

                    // Change button clickable status
                    let btn_finish = e('.finish', taskPanel);
                    log('FINISH: ', btn_finish);
                    btn_finish.classList.remove('pure-button-primary');
                    btn_finish.classList.add('pure-button-disabled');

                    // Add <s> into text
                    taskIdTitle.classList.add('fin');
                    taskTitle.classList.add('fin')
                })
            }
        }
    })
};

let bindEventRemove = function () {
    let taskList = e('#task-list');

    // Event trusteeship
    taskList.addEventListener('click', function (t) {
        let self = t.target;

        // Get task panel object
        log(self.classList);
        if (self.classList.contains('cancle')) {
            log('The object clicked:', self);

            let taskPanel = self.closest('.panel');
            taskPanel.classList.add('move-out')
            setTimeout(function () {
                taskPanel.remove()
                log('1s')
            },1000)

        }
    })
};

let __main = function () {
    bindEventFinish();
    bindEventRemove();
};

__main();