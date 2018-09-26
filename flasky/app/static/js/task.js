let apiTaskAll = function (callback) {
    let path = '/api/todo/all'
    ajax('GET', path, '', callback)
}

let taskTemplate = function (task) {
    let template = `
        
    `
}

let insertTask = function (task) {
    let taskPanel = taskTemplate(task)
    let taskList = e('#task-list')
    log('task list', taskList)
    taskList.insertAdjacentHTML('beforeend', taskPanel)
}

let loadTasks = function () {
    apiTaskAll(function (tasks) {
        log('redy to load all tasks')
        for (i = 0; i < tasks.length; i++) {
            let task = tasks[i]
            log('task object', task)
            insertTask(todo)
        }
    })
}

let __main = function () {
    loadTasks()
}

__main()