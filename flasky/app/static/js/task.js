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

            const taskPanel = self.closest('.panel');
            const taskIdTitle = e('.task-id', taskPanel);
            const taskTitle = e('.task-title', taskPanel);
            const taskContent = e('.task-content', taskPanel);
            log('The closest object:', taskPanel);
            log('The closest object:', taskTitle);
            log('The closest object:', taskContent);

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

                    let btn_cancle = e('.cancle', taskPanel);
                    log('CANCLE:', btn_cancle);
                    btn_cancle.classList.remove('pure-button-disabled');
                    btn_cancle.classList.add('pure-button-primary');

                    // Add <s> into text
                    taskIdTitle.innerHTML = '<s>' + taskIdTitle.innerHTML + '</s>';
                    taskTitle.innerHTML = '<s>' + taskTitle.innerHTML + '</s>';
                    taskContent.innerHTML = '<s>' + taskContent.innerHTML + '</s>';
                })
            }
        }
    })
};

let __main = function () {
    bindEventFinish();
};

__main();